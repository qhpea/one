# An example package with dependencies defined via pyproject.toml
{ config
, lib
, dream2nix
, ...
}:
let
  pyproject = lib.importTOML (config.mkDerivation.src + /pyproject.toml);
in
{
  imports = [
    dream2nix.modules.dream2nix.buildPythonPackage
  ];

  inherit (pyproject.project) name version;

  deps = { nixpkgs, ... }: {
    build-system = [ config.deps.python.pkgs.setuptools ];
    dependencies = map (name: config.deps.python.pkgs.${name}) (pyproject.project.dependencies or [ ]);
    inherit (nixpkgs) mkShell;
  };

  mkDerivation = {
    src = lib.cleanSourceWith {
      src = lib.cleanSource ./.;
      filter = name: type:
        !(builtins.any (x: x) [
          (lib.hasSuffix ".nix" name)
          (lib.hasPrefix "." (builtins.baseNameOf name))
          (lib.hasSuffix "flake.lock" name)
        ]);
    };
    propagatedBuildInputs = [
      # isso implicitly assumes that pkg_resources, which is
      # part of setuptools.
      config.deps.python.pkgs.setuptools
    ];
  };

  buildPythonPackage = {
    dependencies = config.deps.dependencies;
    build-system = config.deps.build-system;
    pyproject = true;
    pythonImportsCheck = [
      config.name
    ];
  };
}
