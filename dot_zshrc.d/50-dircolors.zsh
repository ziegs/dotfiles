#!/bin/zsh

if [[ -f $HOME/.dir_colors ]]; then
  # enable dircolors for ls and such
  eval `dircolors ~/.dir_colors`
fi
