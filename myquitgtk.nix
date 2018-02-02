with import <nixpkgs> {};
stdenv.mkDerivation rec {
  version = "0.2";
  name = "myquitgtk-${version}";
  src = fetchurl {
    url = "https://github.com/juliendehos/myquitgtk/archive/v${version}.tar.gz";
    sha256 = "1zjvxlbi04shy70w5ad2k8z43gyaqq9hcnlrdj4fahw4y812z8xh";
  };
  buildInputs = [ pkgs.cmake pkgs.gnome3.gtkmm pkgs.pkgconfig ];
}
