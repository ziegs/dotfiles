ZSH=$HOME/.oh-my-zsh
ZSH_CUSTOM=$HOME/.zsh
ZSH_THEME="ziegs"

if [[ -d $HOME/.zshrc.pre ]]; then
  source $HOME/.zshrc.pre
fi

# Set to this to use case-sensitive completion
# CASE_SENSITIVE="true"

COMPLETION_WAITING_DOTS="true"

# Uncomment following line if you want to disable marking untracked files under
# VCS as dirty. This makes repository status check for large repositories much,
# much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

fpath=(/usr/local/share/zsh-completions $fpath)

plugins=(git brew tmux osx lol golang node npm bower grunt maven zsh-syntax-highlighting $plugins) #vi-mode?

source $ZSH/oh-my-zsh.sh

export GOPATH="$HOME/go"
export PATH="$PATH:/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin::/usr/local/go/bin"
# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='gvim'
fi

bindkey -M viins 'jj' vi-cmd-mode
bindkey -M viins '^R' history-incremental-pattern-search-backward
bindkey -M viins '^F' history-incremental-pattern-search-forward

source ~/.zsh_aliases

## ZSH options
setopt correct

## Autocomplete options
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache

## Some Bash autocompletions
autoload bashcompinit
bashcompinit
source $ZSH_CUSTOM/homesick_bash_completion.sh

if [[ -d $HOME/.zshrc.post ]]; then
  source $HOME/.zshrc.post
fi

