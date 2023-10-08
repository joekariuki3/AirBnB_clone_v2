# puppet manifest to prepare new server for deployment
exec { 'Update lists':
  command => '/usr/bin/apt update'
}
package { 'nginx':
  ensure => 'installed'
  }

exec { 'make-file':
  command => 'sudo /usr/bin/mkdir -p /data/web_static/shared/',
}

exec { 'make-more-file':
  command => 'sudo /usr/bin/mkdir -p /data/web_static/releases/test/',
}

exec { 'make-symbolic-link':
  command => 'sudo /usr/bin/ln -f -s /data/web_static/releases/test/ /data/web_static/current',
}
exec { 'change-permission':
  command => 'sudo usr/bin/chown -R ubuntu:ubuntu /data/',
}

exec { 'add-index':
  command => '/usr/bin/echo "Sample text" > /data/web_static/releases/test/index.html',
}

exec { 'change-permission-index':
  command => 'sudo /usr/bin/chown ubuntu:ubuntu /data/web_static/releases/test/index.html',
}

exec { 'change-permission-nginx-default':
  command => 'sudo /usr/bin/chown -R ubuntu:ubuntu /etc/nginx/sites-available/default',
}

exec { 'update-nginx-default':
  command => "sudo /usr/bin/sed -i 's#root /var/www/html;#root /var/www/html;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}#1' /etc/nginx/sites-available/default",
}

exec { 'restart':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx'],
}
