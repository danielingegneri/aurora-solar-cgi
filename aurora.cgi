#!/usr/bin/env bash
AURORA=/usr/bin/aurora
DEV=/dev/ttyUSB0
echo "input1_voltage,input1_amps,input1_power,input2_voltage,input2_amps,input2_power,grid_voltage,grid_amps,grid_power,freq,efficiency,temp_inverter,temp_booster"
$AURORA -cd 0 -a 2 $DEV | sed 's/\s\+/,/g' | cut -c 2-


