# autostart when log-in
if [[ "$(tty)" = "/dev/tty1" ]] && [[ "$(whoami)" = "josema" ]]; then
    echo "\n\033[1;33mStarting qtile...\033[0m"
    pgrep qtile || startx
fi

# Enable colors
autoload -U colors && colors

# path-completion, case insensitive, selection theme and hidden files
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]} l:|=* r:|=*'
zstyle ':completion:*' menu select
_comp_options+=(globdots)

# Enable history
HISTSIZE=5000
SAVEHIST=5000
HISTFILE=~/.zsh_history

# prompt ========================================================
PS1="%F{magenta}(%~) %F{blue}%n%f %(?.%F{green}.%F{red})%f "

# highlight config
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets)       # enables main and brackets highlight

# Sources -------------------------------------------------------------
for f in /home/josema/.zsh_config/*; do source $f; done         # load all data from /home/josema/.zsh_config

source ~/zsh-autosuggestions/zsh-autosuggestions.zsh
source /home/josema/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh     # this must be the last one