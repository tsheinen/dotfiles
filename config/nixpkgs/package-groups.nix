{pkgs, ...}: with pkgs;
rec {
	pentesting = [
		gobuster
	];

	reverse-engineering = [
		ghidra
	];

	vr = reverse-engineering;


	cli-utils = [
		ripgrep
		hyperfine
		exa
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
	];
	gui-utils = [
		sublime3
	];

	utils = cli-utils ++ gui-utils;
	security = pentesting ++ vr;
}