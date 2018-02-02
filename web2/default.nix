with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "mywebpage";
  src = ./.;
  installPhase = "mkdir $out; cp index.html $out/; cp image.jpg $out/";
}