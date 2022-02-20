{pkgs, ...}: with pkgs;

let
  discord-patched = import ./discord-patched.nix {inherit pkgs;};
  in with discord-patched;

rec {

	nixpkgs.config.allowUnfree = true;

	pentesting = [
		gobuster
	];

	reverse-engineering = [
		ghidra
		rizin
	];

	vr = reverse-engineering;


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
	];
	gui-utils = [
		sublime3
	];

	build = [
		cmake
	];

	chat = [
	];

	utils = cli-utils ++ gui-utils;
	security = pentesting ++ vr;
	dev = build;

	apps = chat;

}
