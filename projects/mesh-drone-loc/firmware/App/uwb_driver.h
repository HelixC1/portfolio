/**
 * @file uwb_driver.h
 * @brief UWB time-of-flight ranging (MESH-DRONE LOC)
 */

#ifndef MESH_UWB_DRIVER_H
#define MESH_UWB_DRIVER_H

#include <stdint.h>
#include <stdbool.h>

typedef struct {
    uint8_t  node_id;
    float    distance_m;
    uint32_t timestamp_ms;
    bool     valid;
} uwb_range_t;

bool uwb_init(void);
bool uwb_poll_range(uint8_t target_id, uwb_range_t *out);

#endif /* MESH_UWB_DRIVER_H */
