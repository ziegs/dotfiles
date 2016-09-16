# Xsession config

export ALTERNATE_EDITOR=""
export EDITOR="vim"
export TERMINAL="urxvtcd"
export DESKTOP_SESSION=gnome # Makes Chrome pick up proxy settings correctly from gconf

# Disable bell
xset -b

# grey background color
xsetroot -solid "#333333"

# set dpi to something reasonable
xrandr --dpi 96
[[ -f $HOME/.Xresources ]] && xrdb -merge $HOME/.Xresources

# start urxvt daemon
urxvtd -q -f -o

xkbcomp -w0 -I$HOME/.xkb -R$HOME/.xkb keymap/mykbd $DISPLAY

exec i3
