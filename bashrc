#
# ~/.bashrc
#

[[ $- != *i* ]] && return

colors() {
	local fgc bgc vals seq0

	printf "Color escapes are %s\n" '\e[${value};...;${value}m'
	printf "Values 30..37 are \e[33mforeground colors\e[m\n"
	printf "Values 40..47 are \e[43mbackground colors\e[m\n"
	printf "Value  1 gives a  \e[1mbold-faced look\e[m\n\n"

	# foreground colors
	for fgc in {30..37}; do
		# background colors
		for bgc in {40..47}; do
			fgc=${fgc#37} # white
			bgc=${bgc#40} # black

			vals="${fgc:+$fgc;}${bgc}"
			vals=${vals%%;}

			seq0="${vals:+\e[${vals}m}"
			printf "  %-9s" "${seq0:-(default)}"
			printf " ${seq0}TEXT\e[m"
			printf " \e[${vals:+${vals+$vals;}}1mBOLD\e[m"
		done
		echo; echo
	done
}


alias grep='grep --colour=auto'
alias egrep='egrep --colour=auto'
alias cp="cp -i"                          # confirm before overwriting something
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
alias vp='vim PKGBUILD'
alias more=less
alias cat='bat'
alias ucat='/usr/bin/cat'
alias icat='kitty +kitten icat'
alias sums='paste -s -d+ - | bc'
alias top='zenith'
alias ls="lsd"
alias vim="nvim"
alias pwninit='pwninit --template-path ~/.config/pwninit-template.py --template-bin-name exe'
alias cb=clipboard
alias kdiff='kitty +kitten diff'

alias connect_br20.04='ssh -L 127.0.0.1:63222:127.0.0.1:63222 -fNqC teddy@hulkcybr1.dlh.tamu.edu'
alias connect_br16.04='ssh -L 127.0.0.1:61222:127.0.0.1:61222 -fNqC teddy@hulkcybr1.dlh.tamu.edu'

xhost +local:root > /dev/null 2>&1


#
# # ex - archive extractor
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1     ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}


up ()
{
	if [ -z ${1+x} ]; then cd ..; return 0; fi
	if [ $1 -ge 0 ]; then
		cmd="cd "
		for i in {1..$1}; do
			cmd="${cmd}../"
		done
		eval $cmd
	else
		echo "Argument must be a positive integer"
	fi
}


venv(){
	local SEL=$(ls ~/venvs | fzf)
	source ~/venvs/$SEL/bin/activate;

}



if ! pgrep -u "$USER" ssh-agent > /dev/null; then
    ssh-agent > "$XDG_RUNTIME_DIR/ssh-agent.env"
fi
if [[ ! "$SSH_AUTH_SOCK" ]]; then
    eval "$(<"$XDG_RUNTIME_DIR/ssh-agent.env")"
fi

export LIBVIRT_DEFAULT_URI="qemu:///system"

#. /home/sky/.local/bin/virtualenvwrapper.sh

# BEGIN_KITTY_SHELL_INTEGRATION
if test -n "$KITTY_INSTALLATION_DIR" -a -e "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; then source "$KITTY_INSTALLATION_DIR/shell-integration/bash/kitty.bash"; fi
# END_KITTY_SHELL_INTEGRATION
. "$HOME/.cargo/env"
