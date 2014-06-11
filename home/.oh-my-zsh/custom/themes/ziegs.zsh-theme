# Based on oh-my-zsh's alanpeabody theme. Assumes vi-mode plugin is enabled.

local user="%{$fg[red]%}%n@%{$fg[red]%}%m%{$reset_color%}"
local pwd="%{$fg[cyan]%}%~%{$reset_color%}"
local return_code="%(?..%{$fg[red]%}%? ↵%{$reset_color%})"

# Change the prompt bracket to magenta in NORMAL mode

_CHAR=">"
_COLOR_CHAR="%{$fg[red]%}$_CHAR%{$reset_color%}"
function prompt_mode_indicator {
  echo "${${KEYMAP/vicmd/$_COLOR_CHAR}/(main|viins)/$_CHAR}"
}

# Mode-colored prompt bracket + git/hg info for current directory
function prompt_char {
#local CHAR="$(prompt_mode_indicator)"
  local CHAR="$_CHAR"
  git branch >/dev/null 2>/dev/null && echo "%{$fg[green]%}±%{$reset_color%} $CHAR" && return
  hg root >/dev/null 2>/dev/null && echo "%{$fg[blue]%}☿%{$reset_color%} $CHAR" && return
  echo "$CHAR"
}

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[green]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY=""
ZSH_THEME_GIT_PROMPT_CLEAN=""

ZSH_THEME_GIT_PROMPT_ADDED="%{$fg[green]%} ✚"
ZSH_THEME_GIT_PROMPT_MODIFIED="%{$fg[blue]%} ✹"
ZSH_THEME_GIT_PROMPT_DELETED="%{$fg[red]%} ✖"
ZSH_THEME_GIT_PROMPT_RENAMED="%{$fg[magenta]%} ➜"
ZSH_THEME_GIT_PROMPT_UNMERGED="%{$fg[green]%} ═"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$fg[cyan]%} ✭"

PROMPT='${user} ${pwd} $(prompt_char) '
#RPS1='$(vi_mode_prompt_info) ${return_code} $(git_prompt_status)%{$reset_color%}$(git_prompt_info)%{$reset_color%}'
RPS1='${return_code} $(git_prompt_status)%{$reset_color%}$(git_prompt_info)%{$reset_color%}'

MODE_INDICATOR="%{$fg_bold[magenta]%}<%{$reset_color%}%{$fg[magenta]%}<<%{$reset_color%}"
