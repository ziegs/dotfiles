# Xsession config

export ALTERNATE_EDITOR=""
export EDITOR="nvim"
export VISUAL="nvim"
export TERMINAL="urxvt"
export DESKTOP_SESSION=gnome # Makes Chrome pick up proxy settings correctly from gconf

# Disable bell
xset -b

# grey background color
xsetroot -solid "#333333"

[[ -f $HOME/.Xresources ]] && xrdb -merge $HOME/.Xresources

xrandr --output eDP1 --primary 

# start urxvt daemon
#urxvtd -q -f -o

xkbcomp -w0 -I$HOME/.xkb -R$HOME/.xkb keymap/mykbd $DISPLAY

exec i3
