/**
 * @file sensor_manager.h
 * @brief Multi-channel sensor acquisition manager (AERO-SENTINEL)
 * @author Nicolas Lecomte — ECE Bordeaux
 */

#ifndef AERO_SENSOR_MANAGER_H
#define AERO_SENSOR_MANAGER_H

#include <stdint.h>
#include <stdbool.h>

#define AERO_MAX_CHANNELS 8

typedef enum {
    AERO_SENSOR_OK = 0,
    AERO_SENSOR_TIMEOUT,
    AERO_SENSOR_CRC_ERROR,
    AERO_SENSOR_OFFLINE
} aero_sensor_status_t;

typedef struct {
    uint8_t  channel_id;
    float    value;
    uint32_t timestamp_ms;
    aero_sensor_status_t status;
} aero_sample_t;

typedef struct {
    aero_sample_t samples[AERO_MAX_CHANNELS];
    uint8_t       active_channels;
    bool          degraded_mode;
} aero_frame_t;

void aero_sensor_init(void);
bool aero_sensor_read_frame(aero_frame_t *frame);
void aero_sensor_set_degraded(uint8_t channel_id, bool offline);

#endif /* AERO_SENSOR_MANAGER_H */
