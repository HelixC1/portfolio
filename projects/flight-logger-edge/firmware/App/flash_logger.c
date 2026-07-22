/**
 * @file flash_logger.c
 * @brief In-memory ring buffer demo (flash backend on target)
 */

#include "flash_logger.h"

#define FLIGHT_MAX_RECORDS 1024

static flight_record_t buffer[FLIGHT_MAX_RECORDS];
static uint32_t write_index;
static uint32_t record_count;

bool flight_logger_init(void) {
    write_index = 0;
    record_count = 0;
    return true;
}

bool flight_logger_append(const flight_record_t *record) {
    if (!record) return false;
    buffer[write_index] = *record;
    write_index = (write_index + 1) % FLIGHT_MAX_RECORDS;
    if (record_count < FLIGHT_MAX_RECORDS) record_count++;
    return true;
}

uint32_t flight_logger_count(void) {
    return record_count;
}
