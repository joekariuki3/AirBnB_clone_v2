# puppet manifest to prepare new server for deployment
# Update package lists
exec { 'Update lists':
  command => 'sudo /bin/apt update'
}

# Install Nginx
package { 'nginx':
  ensure  => 'present',
  require => Exec['Update lists']
}

# Create the directory tree
exec { 'Create Directory Tree':
  command => 'sudo /bin/mkdir -p /data/web_static/releases/test /data/web_static/shared',
  require => Package['nginx']
}

# Create a fake HTML file with simple content,
# to test Nginx configuration
file { 'Create Fake HTML':
  ensure  => 'present',
  path    => '/data/web_static/releases/test/index.html',
  content => 'Sample Text',
  require => Exec['Create Directory Tree']
}

# Create a symbolic link '/data/web_static/current' linked to the
# '/data/web_static/releases/test/' folder.
file { 'Create Symbolic Link':
  ensure  => 'link',
  path    => '/data/web_static/current',
  force   => true,
  target  => '/data/web_static/releases/test',
  require => File['Create Fake HTML']
}

# Ensures that Nginx is running
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}

# Set permissions for 'ubuntu' user
exec { 'Set permissions':
  command => 'sudo /bin/chown -R ubuntu:ubuntu /data',
  require => File['Create Symbolic Link']
}

# Set a new location for a Nginx VHost 
$loc_header='location /hbnb_static/ {'
$loc_content='alias /data/web_static/current/;'
$new_location="\n\t${loc_header}\n\t\t${loc_content}\n\t}\n"

# Write the new location to the default Nginx VHost
file_line { 'Set Nginx Location':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'root /var/www/html;',
  line    => $new_location,
  notify  => Service['nginx'],
  require => Exec['Set permissions']
}
exec { 'restart-nginx':
  command => '/bin/service nginx restart',
}
