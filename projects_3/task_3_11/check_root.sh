#!/bin/bash
check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "У вас нет прав"
        return 1
     fi
         echo "Запущен от имени суперпользователя"
}
check_root

