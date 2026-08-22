{
  description = "Python + Pygame development environment";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixos-unstable";
  };
  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.${system}.default = pkgs.mkShell {
        packages = with pkgs; [
          python3
          pyright
          ruff
          python3Packages.python-lsp-server
          python3Packages.pygame
          SDL2
          SDL2_image
          SDL2_mixer
          SDL2_ttf
          freetype
          libpng
          alsa-lib
          pipewire
          libxkbcommon
          wayland
          wayland-protocols
          wayland-scanner
          xorg.libX11
          xorg.libXext
          xorg.libXrandr
          xorg.libXcursor
          xorg.libXi
          xorg.libXfixes
          mesa
          libGL
          libglvnd
        ];
        env = {
          SDL_VIDEODRIVER = "wayland,x11";
          SDL_AUDIODRIVER = "pipewire,pulse,alsa";
        };
      };
    };
}
