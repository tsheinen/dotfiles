{pkgs, ...}: with pkgs;

pkgs.iosevka.override {
  set = "etoile";
}