# Xsession config

export ALTERNATE_EDITOR=""
export EDITOR="vim"
export VISUAL="vim"
export TERMINAL="x-terminal-emulator"
export DESKTOP_SESSION="cinnamon" # Makes Chrome pick up proxy settings correctly from gconf

export GTK_IM_MODULE=xim

# Disable bell
xset -b

[[ -f $HOME/.Xresources ]] && xrdb -merge $HOME/.Xresources

xrandr --output eDP1 --primary

## Turn monitor off 30 seconds after locking
export XSECURELOCK_BLANK_DPMS_STATE=off
export XSECURELOCK_BLANK_TIMEOUT=30

if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin":$PATH
fi

exec i3
