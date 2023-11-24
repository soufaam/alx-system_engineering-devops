# File:Using Puppet, install flask from pip3
package {'python3-pip':
ensure  => 'installed',
}
exec { 'install_werkzeug':
command => '/usr/bin/pip3 install Werkzeug==2.1.1',
path    => '/usr/local/bin:/usr/bin',
creates => '/usr/local/lib/python3.8/dist-packages/Werkzeug-2.1.1.dist-info',
require => Package['python3-pip'],
}

exec{ 'install_flask':
command =>  '/usr/bin/pip3 install flask==2.1.0',
path    => '/usr/local/bin:/usr/bin',
creates => '/usr/local/lib/python3.8/dist-packages/Flask-2.1.0.dist-info',
require => Exec['install_werkzeug'],
}
