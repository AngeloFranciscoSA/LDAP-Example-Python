import ldap
import getpass
# definindo variaveis de conexao
 
HOST1 = "x.x.x.x"
HOST2 = "x.x.x.x"
HOST3 = "x.x.x.x"

username = input("\nUsername: ")
user = "uid="+username+",ou=someou,dc=somedc,dc=local"
password = getpass.getpass()
base = "dc=somedc,dc=local"
 
# Try all host to connect
# If you more host, you can add more try and except! :D
try:
    connection = ldap.initialize("ldap://%s"%HOST1)
except:
    try:
        connection = ldap.initialize("ldap://%s"%HOST2)
    except:
            connection = ldap.initialize("ldap://%s"%HOST3)

try:
    connection.protocol_version = ldap.VERSION3  #Version 3 is most recommend
    connection.set_option(ldap.OPT_REFERRALS,0)
    connection.bind_s(user,password) 
    
    #Define a filter to search
    ldap_filter = "uid="+username
    
    #will search based on filter
    result = connection.search_s(base,ldap.SCOPE_SUBTREE,ldap_filter) 

    if len(result) != 0:
        #.decode is import, because all data will be come like bytes! 
        print(result[0][1].decode("utf-8"))

#if something going wrong, will say it for us! (most Credential Invalid, you create more except for whatever error you want see)
except ldap.INVALID_CREDENTIALS:
    raise("Error!")