#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

YELLOW="$(tput setaf 3)"
BLUE="$(tput setaf 4)"
RESET="$(tput sgr0)"

PS1='[${BLUE}\h@\u: ${YELLOW}\W${RESET}]\$ '
