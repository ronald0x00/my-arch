#!/bin/sh

# Verifica se o processo openvpn está em execução
if pgrep -x "openvpn" > /dev/null; then
    echo -n  "󰄸 Connected"
else
    echo -n "󰅛 Disconnected"
fi

