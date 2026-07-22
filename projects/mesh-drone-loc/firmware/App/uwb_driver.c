/**
 * @file uwb_driver.c
 * @brief Stub UWB driver (DW1000 backend on target)
 */

#include "uwb_driver.h"

static bool initialized;

bool uwb_init(void) {
    initialized = true;
    return true;
}

bool uwb_poll_range(uint8_t target_id, uwb_range_t *out) {
    if (!initialized || !out) return false;
    out->node_id = target_id;
    out->distance_m = 0.0f;
    out->timestamp_ms = 0;
    out->valid = false;
    return true;
}
