#!/usr/bin/zsh

if type direnv > /dev/null; then
  eval "$(direnv hook zsh)"
fi
