#!/bin/zsh

if [[ -f $HOME/.dir_colors ]]; then
  # enable dircolors for ls and such
  eval `dircolors ~/.dir_colors`
  # idk if this is needed
  zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
fi
