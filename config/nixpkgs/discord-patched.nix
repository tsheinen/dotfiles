{pkgs, ...}: with pkgs;

# pkgs.discord.override {
#     nss = pkgs.nss_3_73;
# }

(pkgs.discord.overrideAttrs (oldAttrs: rec {
  desktopItem = oldAttrs.desktopItem.overrideAttrs (desktopAttrs: {
    buildCommand =
      let
        oldExec = builtins.match ".*(\nExec=[^\n]+\n).*" desktopAttrs.buildCommand;
        matches = oldExec;
        replacements = [ "\nExec=discord --ignore-gpu-blocklist --disable-features=UseOzonePlatform --enable-features=VaapiVideoDecoder --use-gl=desktop --enable-gpu-rasterization --enable-zero-copy\n" ];
      in
        assert oldExec != null;
        builtins.replaceStrings matches replacements desktopAttrs.buildCommand;
  });
  postInstall = builtins.replaceStrings [ "${oldAttrs.desktopItem}" ] [ "${desktopItem}" ] "";
}))