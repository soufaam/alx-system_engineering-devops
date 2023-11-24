# Using Puppet, create a manifest that kills a process named killmenow

exec{ 'kill_process_killmenow':
command =>  'pkill -f killmenow',
path    => '/usr/local/bin:/usr/bin',
onlyif  => 'pgrep -f killmenow',
}
