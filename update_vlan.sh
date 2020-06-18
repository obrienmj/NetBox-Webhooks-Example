#!/usr/bin/env bash

switch=$1
interface=$2
vlan=$3
python3 updatevlan.py -s $switch -i $interface -v $vlan  > output.log
