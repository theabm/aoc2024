let
  pkgs =
    import
    (
      fetchTarball "https://github.com/NixOS/nixpkgs/archive/nixpkgs-unstable.tar.gz"
    ) {};

  myPython = pkgs.python3;

in
  pkgs.mkShell {
    packages = [
      # need the python packages
      (myPython.withPackages (pp: [
        pp.numpy
      ]))
    ];
  }
