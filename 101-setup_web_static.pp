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

file { '/data/web_static/current':
  ensure => link,
  links  => manage,
  source => '/data/web_static/releases/test/'
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

exec { 'change-permission':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
}

file { 'data/web_static/releases/test/index.html':
  ensure  => 'present',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => 'Sample text',
}


file { '/etc/nginx/sites-available/default':
  ensure => 'present',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file_line { 'update-default-serve-web-static':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => "\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}",
  after  => 'root /var/www/html;',
}

exec { 'restart':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx'],
}
