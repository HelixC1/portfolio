/**
 * @file flash_logger.h
 * @brief Ring buffer flash logger with CRC integrity (FLIGHT-LOGGER EDGE)
 */

#ifndef FLIGHT_FLASH_LOGGER_H
#define FLIGHT_FLASH_LOGGER_H

#include <stdint.h>
#include <stdbool.h>

typedef struct {
    uint32_t timestamp_ms;
    float    latitude;
    float    longitude;
    float    altitude_m;
    float    roll_deg;
    float    pitch_deg;
    uint32_t crc32;
} flight_record_t;

bool flight_logger_init(void);
bool flight_logger_append(const flight_record_t *record);
uint32_t flight_logger_count(void);

#endif /* FLIGHT_FLASH_LOGGER_H */
