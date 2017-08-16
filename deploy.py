from subprocess import call
cmd = []
cmd.append('ansible-playbook')
cmd.append('-i')
cmd.append('inventories/inventory')
cmd.append('deploy.yml')
call(cmd)
