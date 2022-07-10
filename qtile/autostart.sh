#!/bin/sh

# resolution setter
# xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
# xrandr --addmode eDP-1 "1920x1080_60.00"
# xrandr -s 1920x1080

picom --experimental-backend &
sh ~/.config/polybar/launch.sh --${POLYBAR_THEME}
wal -R

export QT_QPA_PLATFORMTHEME=qt5ct
