#!/bin/bash

convertgif() {
    convert -dispose 2 -delay 20 -loop 0  ${1}.png -crop 32x32 +repage -depth 4 ${1}.tmp.gif
    convert ${1}.tmp.gif[0-3] ${1}.gif
    rm -f ${1}.tmp.gif
}

for i in $(find ./ -maxdepth 1 -name "*.png" | sed s/\.png//g); do
    while [ $(jobs | wc -l) -ge 12 ]; do
        sleep 1
    done
    convertgif ${i} &
done
