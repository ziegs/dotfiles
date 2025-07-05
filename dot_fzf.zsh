# Setup fzf
# ---------
if [[ ! "$PATH" == */home/ziegs/.fzf/bin* ]]; then
  PATH="${PATH:+${PATH}:}/home/ziegs/.fzf/bin"
fi

source <(fzf --zsh)
