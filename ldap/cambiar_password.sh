#!/bin/bash
#clear
source ~/user_id.conf

echo -n "Ingrese nombre de usuario: "
read USER_ID
echo -n "Ingrese nueva contraseña: "
read USER_PASS


LDIF=ldapuser.ldif


echo "dn: uid=$USER_ID,ou=People,dc=hpm,dc=cl" > $LDIF
echo "changetype: modify" >> $LDIF
echo "replace: userPassword" >> $LDIF
echo "userPassword: $USER_PASS" >>$LDIF


ldapmodify -x -D "cn=Manager,dc=hpm,dc=cl" -w hpm -f ldapuser.ldif
id $USER_ID

