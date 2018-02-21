with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "myscripts";
  src = ./.;
  installPhase = "mkdir $out; cp index.html $out/; cp hello.py $out/; cp captain.txt $out/; cp captain.py $out/; cp print_envs.py $out/; cp hello_name.py $out/; cp cgi_field.py $out/; cp -r tmp/ $out/; cp utils.py $out/; cp make_img.py $out/; cp image.py $out/";
}
