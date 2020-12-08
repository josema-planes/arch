# Enable colors
autoload -U colors && colors

# path-completion, case insensitive, selection theme and hidden files
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*'
zstyle ':completion:*' menu select
_comp_options+=(globdots)

# Enable history
HISTSIZE=500
SAVEHIST=500
HISTFILE=~/.zsh_history

# prompt
PS1="%F{magenta}(%~) %F{blue}%n %F{white}$%f "

# load all data from /home/josema/.zsh_config
for f in /home/josema/.zsh_config/*; do source $f; done

# source for zsh syntax highlighting (this must be the last one)
source /home/josema/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
