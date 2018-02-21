#!/bin/bash
#clear
source ~/user_id.conf
echo -n "Ingrese nombre de usuario: "
read USER_ID
echo -n "Ingrese contraseña: "
read USER_PASS
let USER_NUMBER=$LAST_NUMBER+1
LDIF=ldapuser.ldif
echo "dn: uid=$USER_ID,ou=People,dc=hpm,dc=cl" > $LDIF
echo "objectClass: inetOrgPerson" >> $LDIF
echo "objectClass: posixAccount" >> $LDIF
echo "objectClass: shadowAccount" >> $LDIF
echo "cn: $USER_ID" >> $LDIF
echo "sn: $USER_ID" >> $LDIF
echo "userPassword: $USER_PASS" >> $LDIF
echo "loginShell: /bin/bash" >> $LDIF
echo "uidNumber: $USER_NUMBER" >> $LDIF
echo "gidNumber: $USER_NUMBER" >> $LDIF
echo "homeDirectory: /home/$USER_ID" >> $LDIF
echo "" >> $LDIF
echo "dn: cn=$USER_ID,ou=Group,dc=hpm,dc=cl" >> $LDIF
echo "objectClass: posixGroup" >> $LDIF
echo "cn: $USER_ID" >> $LDIF
echo "gidNumber: $USER_NUMBER" >> $LDIF
echo "memberUid: $USER_ID" >> $LDIF
ldapadd -x -D "cn=Manager,dc=hpm,dc=cl" -w hpm -f ldapuser.ldif
id $USER_ID
mkhomedir_helper $USER_ID
echo "LAST_NUMBER=$USER_NUMBER" > user_id.conf
