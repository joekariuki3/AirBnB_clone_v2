# puppet manifest to prepare new server for deployment

package { 'nginx':
  ensure => 'installed'
  }

exec { 'make-file':
  command => 'sudo mkdir -p /data/web_static/shared/',
}

exec { 'make-more-file':
  command => 'sudo mkdir -p /data/web_static/releases/test/',
}

exec { 'make-symbolic-link':
  command => 'sudo ln -f -s /data/web_static/releases/test/ /data/web_static/current',
}
exec { 'change-permission':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
}

exec { 'add-index':
  command => 'echo "Sample text" > /data/web_static/releases/test/index.html',
}

exec { 'change-permission-index':
  command => 'sudo chown ubuntu:ubuntu /data/web_static/releases/test/index.html',
}

exec { 'change-permission-nginx-default':
  command => 'sudo chown -R ubuntu:ubuntu /etc/nginx/sites-available/default',
}

exec { 'update-nginx-default':
  command => "sudo sed -i 's#root /var/www/html;#root /var/www/html;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}#1' /etc/nginx/sites-available/default",
}

exec { 'restart':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx'],
}
