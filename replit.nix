{pkgs}: {
  deps = [
    pkgs.libopus
    pkgs.ffmpeg
    pkgs.libsodium
    pkgs.postgresql
    pkgs.openssl
  ];
}
