# Path to your oh-my-zsh configuration.
source ~/.bin/iTerm2Colors.sh

ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
# Optionally, if you set this to "random", it'll load a random theme each
# time that oh-my-zsh is loaded.
ZSH_THEME="ziegs"

# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Set to this to use case-sensitive completion
# CASE_SENSITIVE="true"

# Uncomment following line if you want red dots to be displayed while waiting for completion
# COMPLETION_WAITING_DOTS="true"

# Uncomment following line if you want to disable marking untracked files under
# VCS as dirty. This makes repository status check for large repositories much,
# much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

HOMESHICK_COMPLETION="$HOME/.homesick/repos/homeshick/completions"
if [ -d $HOMESHICK_COMPLETION ]; then
  fpath=($HOMESHICK_COMPLETION $fpath)
fi
fpath=(/usr/local/share/zsh-completions $fpath)

plugins=(git brew tmux osx lol golang node npm bower grunt maven) #vi-mode?

source $ZSH/oh-my-zsh.sh

export GOPATH="$HOME/go"
export PATH=":/Users/ziegs/.bin:$GOPATH/bin:/Users/ziegs/android-sdks/platform-tools:/Users/ziegs/android-sdks/tools:/usr/local/bin:/usr/local/sbin:/Users/ziegs/Library/Python/2.7/bin:/usr/bin:/bin:/usr/sbin:/sbin::/usr/local/go/bin:/Users/ziegs/.go_appengine"
# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='vim'
else
  export EDITOR='mvim'
fi

bindkey -M viins 'jj' vi-cmd-mode
bindkey -M viins '^R' history-incremental-pattern-search-backward
bindkey -M viins '^F' history-incremental-pattern-search-forward

source "$HOME/.homesick/repos/homeshick/homeshick.sh"

export ANDROID_HOME=/Applications/Android\ Studio.app/sdk

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_51.jdk/Contents/Home

source ~/.zsh_aliases
