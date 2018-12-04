# Xsession config

export ALTERNATE_EDITOR=""
export EDITOR="nvim"
export VISUAL="nvim"
export TERMINAL="x-terminal-emulator"
export DESKTOP_SESSION="gnome" # Makes Chrome pick up proxy settings correctly from gconf

export GTK_IM_MODULE=xim

# Disable bell
xset -b

[[ -f $HOME/.Xresources ]] && xrdb -merge $HOME/.Xresources

xrandr --output eDP1 --primary 

# start urxvt daemon
#urxvtd -q -f -o

xkbcomp -w0 -I$HOME/.xkb -R$HOME/.xkb keymap/mykbd $DISPLAY

if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin":$PATH
fi

exec i3
