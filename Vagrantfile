# Vagrantfile
Vagrant.configure("2") do |config|
  
    # Configuración de la VM
    config.vm.box = "ubuntu/bionic64"  
    config.vm.hostname = "devops-server"  
    config.vm.network "private_network", ip: "192.168.56.101"  # 
  
    # Provisión con Ansible
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "playbook.yml"
    end
  end
  