# directory resource to ensure the existence of /var/www/html
file { '/var/www/html':
  ensure  => 'directory',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
}

# Define file resources for specific files in /var/www/html
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => '<title>Holberton &#8211; Just another WordPress site</title>
              <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
              <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
              <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>
              </div>
              <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
              <p>Yet another bug by a Holberton student</p>',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Define file resources for other files if needed
file { '/var/www/html/index.cgi':
  ensure  => 'file',
  # Similar attributes as above (content, owner, group, mode)
}

file { '/var/www/html/index.pl':
  ensure  => 'file',
  # Similar attributes as above (content, owner, group, mode)
}

# Restart Apache after managing files
exec { 'restart_apache':
  command     => '/usr/sbin/service apache2 restart',
  refreshonly => true,
  subscribe   => [File['/var/www/html'], File['/var/www/html/index.html']], # Restart when files change
}
