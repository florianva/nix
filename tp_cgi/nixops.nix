{
  network.description = "Simple scipts";
  webserver = { config, pkgs, ... }: {
    networking.firewall.allowedTCPPorts = [ 80 ];
    services.lighttpd = {
      enable = true;
      document-root = import ./default.nix;
      enableModules = [ "mod_cgi" ];
      extraConfig = ''
      		  cgi.assign = ( ".py"  => "${pkgs.python3}/bin/python" )
    		  '';
    };
    deployment = {
      targetEnv = "virtualbox";
      virtualbox = {
        memorySize = 512;
        vcpu = 1;
        headless = true;
      };
    };
  };
}