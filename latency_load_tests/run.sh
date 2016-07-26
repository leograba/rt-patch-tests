#!/bin/sh

CORES="$(grep -c ^processor /proc/cpuinfo)"
MEM="$(grep MemTotal /proc/meminfo | awk '{print $2}')"

echo "CPU cores detected: ${CORES}"

set -x # echo on

bash hd_script &
bash rtcr_script &
bash rtcw_script &
bash find_script &
bash du_script &
bash ping_script &
stress --cpu ${CORES} --io ${CORES} --vm $((CORES > 1 ? CORES / 2 : 1)) --vm-bytes $(((MEM / (CORES > 1 ? CORES / 2 : 1)) / 16))k
