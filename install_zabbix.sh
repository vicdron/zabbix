#!/bin/bash


################################################################## #

Script Name: install_zabbix.sh
Description: Faz instalação do Zabbix 6.0 ou 6.2 na Ubuntu 20.04 ou 22.04

Written by: Victor Lins
----------------------------------------------------------------
Version 1.0.0
##################################################################-#

echo "Informe a versão do Ubuntu, 20.04 ou 22.04:  "
read versao_ubuntu

HEIGHT=10
WIDTH=60
CHOICE_HEIGHT=4
TITLE="Instalação Zabbix"
MENU="Escolha a versão:"
OPTIONS=(1 "Zabbix 6.0"
2 "Zabbix 6.2")

CHOICE=(dialog --clear \ --title "TITLE" 
--menu "$MENU" 
$HEIGHT $WIDTH CHOICE_HEIGHT \ "{OPTIONS[@]}" 
2>&1 >/dev/tty)
clear

case CHOICE in 1) 
	wget https://repo.zabbix.com/zabbix/6.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.0-4+ubuntu/$versao_ubuntu/_all.deb
	sudo dpkg -i zabbix-release_6.0-4+ubuntu$(lsb_release -rs)_all.deb
	sudo apt update
	sudo apt -y install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent;;

2)      wget https://repo.zabbix.com/zabbix/6.2/ubuntu/pool/main/z/zabbix-release/zabbix-release_6.2-2+ubuntu/$versao_ubuntu/_all.deb
        sudo dpkg -i zabbix-release_6.2-2+ubuntu$(lsb_release -rs)_all.deb
        sudo apt update
        sudo apt -y install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent	;;


esac


#Instalação da bando de dados

sudo apt install software-properties-common -y
curl -LsS -O https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
sudo bash mariadb_repo_setup --mariadb-server-version=10.6
sudo apt update
sudo apt -y install mariadb-common mariadb-server-10.6 mariadb-client-10.6

#Habilitando e iniciando o serviço após instalação

sudo systemctl start mariadb
sudo systemctl enable mariadb


#alterando senha root do banco

sudo mysql_secure_installation

#Enter current password for root (enter for none): Press Enter
#Switch to unix_socket authentication [Y/n] y
#Change the root password? [Y/n] y
#New password: <Enter root DB password>
#Re-enter new password: <Repeat root DB password>
#Remove anonymous users? [Y/n]: Y
#Disallow root login remotely? [Y/n]: Y
#Remove test database and access to it? [Y/n]:  Y
#Reload privilege tables now? [Y/n]:  Y

#Criando o banco de dados

sudo mysql -uroot -p'SenhaRootdoBanco' -e "create database zabbix character set utf8mb4 collate utf8mb4_bin;"
sudo mysql -uroot -p'SenhaRootdoBanco' -e "grant all privileges on zabbix.* to zabbix@localhost identified by 'zabbixsenha';"

sudo zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql --default-character-set=utf8mb4 -uzabbix -p'zabbixsenha' zabbix


# sudo nano /etc/zabbix/zabbix_server.conf
#  incluir senha do banco 
# DBPassword=zabbixsenha
sudo sed -i "s/# DBPassword=/DBPassword=zabbixsenha/" /etc/zabbix/zabbix_server.conf


#configuração do php
sed -i "s/php_value\[date.timezone\] = #{PHP_TIMEZONE}/php_value\[date.timezone\] = America\/Sao_Paulo/" /etc/zabbix/apache.conf

sudo systemctl restart apache2
sudo systemctl enable apache2

#configurando o firewall

ufw allow 10050/tcp
ufw allow 10051/tcp
ufw allow 80/tcp
ufw reload

# iniciando serviços

sudo systemctl restart zabbix-server zabbix-agent
sudo systemctl enable zabbix-server zabbix-agent
