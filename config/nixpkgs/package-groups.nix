{pkgs, ...}: with pkgs;


rec {

	imxx = callPackage "/home/sky/.dotfiles/config/nixpkgs/imhex.nix" { };

	nixpkgs.config.allowUnfree = true;

	pentesting = [
		gobuster
	];

	reverse-engineering = [
		ghidra
		rizin
		jd-gui
		imxx
	];
	
	exploit-dev = [
		one_gadget
	];

	forensics = [
		volatility3
		binwalk
		gocr
	];


	cli-utils = [
		ripgrep
		hyperfine
		lsd
		ouch
		zenith
		bat
		delta
		dust
		duf
		broot
		fd
		jq
		procs
		zoxide
		fzf
		unzip
		asciinema
	];

	gui-utils = [
		sublime3
	];

	build = [
		cmake
		wabt
	];

	system = [
		(nerdfonts.override { fonts = [ "FiraCode" ]; })
	];


	vr = reverse-engineering ++ exploit-dev;
	utils = cli-utils ++ gui-utils;
	security = pentesting ++ vr ++ forensics;
	dev = build;

	apps = utils;

}
