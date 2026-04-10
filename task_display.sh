#!/bin/bash

echo "" >> $LOG_FILE

# 2. Memory Usage
echo "--- Memory Usage (MB) ---" >> $LOG_FILE
free -m >> $LOG_FILE
echo "" >> $LOG_FILE

# 3. Disk Usage
echo "--- Disk Space Usage ---" >> $LOG_FILE
df -h | grep '^/dev/' >> $LOG_FILE
echo "" >> $LOG_FILE

echo "Stats saved to $LOG_FILE"







