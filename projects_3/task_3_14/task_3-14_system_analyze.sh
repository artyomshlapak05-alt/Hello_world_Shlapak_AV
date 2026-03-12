#!/bin/bash

df -h | awk 'NR>1 {
    sub(/%/,"",$5)
    if ($5+0 > 90) {
        print $1, $5"%" "Диск почти заполнен"
    } else {
        print $1, $5"%"
    }
}'
