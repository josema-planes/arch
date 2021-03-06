#
# ~/.bashrc
#

# autostart when log-in
if [[ "$(tty)" = "/dev/tty1" ]] && [[ "$(whoami)" = "josema" ]]; then
    echo -e "\n\033[1;33mStarting qtile...\033[0m"
    pgrep qtile || startx
fi

# load all aliases from ~/.zsh_config/aliases
source ~/.zsh_config/aliases

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1="\[\033[01;35m\][\d]\[\033[00m\] \[\033[01;32m\]\u@\h\[\033[00m\]: \[\033[01;34m\]{ \w }\[\033[33m\] \[\033[1;37m\]\$\[\033[00m\] "
