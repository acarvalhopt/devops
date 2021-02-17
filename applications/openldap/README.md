##### To check the current password:
```cat /etc/openldap/slapd.d/cn\=config/olcDatabase\=\{2\}hdb.ldif```

##### To Run the ldif take in consideration the correct hdb.
```ldapmodify -Y EXTERNAL -H ldapi:/// -f /root/tmp/changeReplicationPassword.ldif```

##### Restart slapd