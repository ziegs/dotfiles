##
# Sets an variable with a file for tmux to source for machine-specific configurations. Sets to /dev/null if the file is not found.
##

if [[ -d $HOME/.tmux.conf.local ]]; then
  export TMUX_LOCAL_CONFIG="$HOME/.tmux.conf.local"
else
  export TMUX_LOCAL_CONFIG="/dev/null"
fi
