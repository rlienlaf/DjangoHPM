#!/bin/bash
echo -n "Ingrese IP del equipo: "
read IP

CONF_FILE=/etc/ansible/hosts

#contraseña root de los equipos esclavos
PASS='10.7.164.22'

sshpass -p $PASS ssh-copy-id root@$IP

echo "$IP" >> $CONF_FILE
