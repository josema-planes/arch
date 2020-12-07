#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias grep='grep --color=auto'
alias ls='exa --group-directories-first --header'
alias cat='ccat -G Plaintext="blink" -G Keyword="purple" -G String="darkgreen" -G Punctuation="brown" -G Comment="faint"'

alias yay='yay --nodiffmenu'

PS1="\[\033[01;35m\][\d]\[\033[00m\] \[\033[01;32m\]\u@\h\[\033[00m\]: \[\033[01;34m\]{ \w }\[\033[33m\] \[\033[1;37m\]\$\[\033[00m\] "
