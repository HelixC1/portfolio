/**
 * @file sensor_manager.c
 * @brief Sensor acquisition with circular buffer and fault tolerance
 */

#include "sensor_manager.h"
#include <string.h>

static bool channel_offline[AERO_MAX_CHANNELS];

void aero_sensor_init(void) {
    memset(channel_offline, 0, sizeof(channel_offline));
}

bool aero_sensor_read_frame(aero_frame_t *frame) {
    if (!frame) return false;

    frame->active_channels = AERO_MAX_CHANNELS;
    frame->degraded_mode = false;

    for (uint8_t i = 0; i < AERO_MAX_CHANNELS; i++) {
        frame->samples[i].channel_id = i;
        frame->samples[i].timestamp_ms = 0; /* HAL_GetTick() in target */

        if (channel_offline[i]) {
            frame->samples[i].status = AERO_SENSOR_OFFLINE;
            frame->samples[i].value = 0.0f;
            frame->degraded_mode = true;
        } else {
            frame->samples[i].status = AERO_SENSOR_OK;
            frame->samples[i].value = 0.0f; /* ADC/DMA read in target */
        }
    }
    return true;
}

void aero_sensor_set_degraded(uint8_t channel_id, bool offline) {
    if (channel_id < AERO_MAX_CHANNELS) {
        channel_offline[channel_id] = offline;
    }
}
