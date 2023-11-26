# puppet configuration
file { '/etc/ssh/ssh_config':
  ensure  => 'file',
  content => "
Host 389038-web-01
    HostName 54.152.81.82
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
  ",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
