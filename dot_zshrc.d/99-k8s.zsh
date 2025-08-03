#!/usr/bin/zsh

export SOPS_AGE_KEY_FILE=~/.config/sops/age/keys.txt

if type kubectl > /dev/null; then
  alias k='kubectl'
  source <(kubectl completion zsh)
fi

if type flux > /dev/null; then
  source <(flux completion zsh)
fi

if type helm > /dev/null; then
  source <(helm completion zsh)
fi

if type kubectl-cnpg > /dev/null; then
  source <(kubectl cnpg completion zsh)
fi
