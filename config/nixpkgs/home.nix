{ config, pkgs, ... }:
let
  packageGroups = import ./package-groups.nix {
    inherit pkgs;
  };
  in with packageGroups;


{
  nixpkgs.config.allowUnfree = true;
  home.username = "sky";
  home.homeDirectory = "/home/sky";

  home.stateVersion = "22.05";
  home.packages = with packageGroups; [
  ] ++ security ++ utils ++ dev ++ apps;

  # Let Home Manager install and manage itself.
  programs.home-manager.enable = true;
  
  targets.genericLinux.enable = true;
}
