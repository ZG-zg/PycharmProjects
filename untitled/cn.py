
import ldap,ldif
import ldap.modlist,ldap.dn
from ldap import MOD_ADD


baseDN="dc=mypaas,dc=com"
username="Manager"
password="123456"
def _connect(baseDN, username, password):
    conn = None
    try:
        _userDN = "cn=" + username + "," + baseDN
        # 连接ldap
        conn = ldap.initialize('ldap://10.20.2.24:389')
        conn.set_option(ldap.OPT_REFERRALS, 0)
        conn.set_option(ldap.OPT_TIMEOUT, 7)
        conn.set_option(ldap.OPT_NETWORK_TIMEOUT, 7)  # 网络原因连接异常 7s 超时
        conn.protocol_version = ldap.VERSION3
        # 登录
        print(conn.simple_bind_s(_userDN, password))
        return conn
    except Exception as e:
        invalid = {'desc': 'Invalid credentials'}
        if str(invalid) == str(e):
            print('连接LDAP，密码错误（一般是用户登录密码错误）')
            print(conn.simple_bind_s(_userDN, password))
        else:
            print("连接LDAP异常，异常信息：" + str(e))
        conn = None  # 连接异常，初始化conn

    def addStructural(conn, stoogeDN, stoogeInfo):
        try:
            stooge_attrib = [(k, v) for (k, v) in stoogeInfo.items()]
            if conn is None:
                _connect(baseDN, username, password)
            conn.add_s(stoogeDN, stooge_attrib)
            return True
        except Exception as e:
            print("新建结构失败，原因：" + str(e))
            return False
        finally:
            if conn:
                conn.unbind_s()
                conn = None


def create_ad_user(conn):
    user = {}
    user['objectclass'] = [b'inetOrgPerson']
    user['cn'] = b'Manager3'
    user['sn'] = b'zg'
    user['userpassword'] = b"123456"
    user_dn = 'cn=%s,%s' % ("Manager3", "ou=Tester,o=swust,dc=mypaas,dc=com")
    user['objectclass'] = [b'inetOrgPerson']
    stooge_attrib = ldap.modlist.addModlist(user)
    print(stooge_attrib)
    ret = conn.add_s(user_dn, stooge_attrib)
    print(ret)
def create_ad(conn):
    user = {}
    user['objectclass'] = [b'organizationalUnit']
    user['ou'] = b'Zg11'
    #user['sn'] = b'zg'
    #user['userpassword'] = b"123456"
    user_dn = 'ou=%s,%s' % ("Zg11", "o=swust,dc=mypaas,dc=com")
    modlist = ldap.modlist.addModlist(user)
    #user['objectclass'] = [b'organizationalUnit']

    #stooge_attrib = [(k, v) for (k, v) in user.items()]
    #print(stooge_attrib)
    ret= conn.add_s(user_dn, modlist)
    print(ret)

def create_mod_user(conn):
    attr_list =[(ldap.MOD_REPLACE, 'ou', b'Zg1')

                ]

    user_dn = 'cn=%s,%s' % ("Manager1","ou=Developer,o=swust,dc=mypaas,dc=com")
    ret= conn.modify_s(user_dn, attr_list)
    print(ret)

# 用户校验
    # :returns: True 验证成功
    # :returns: False 验证出错
    # :returns: None 验证失败
def vertify(conn):
    try:
        _connect("ou=Tester,o=swust,dc=mypaas,dc=com", "Manager3", '123456')
        if conn:
            return True
        else:
            return None
    except Exception as e:
        print("用户校验失败，原因: "+ str(e))
        return False
    finally:
        if conn:
            conn.unbind_s()
            conn = None
conn = _connect("dc=mypaas,dc=com", "Manager", "123456")

#create_mod_user(conn)
#create_ad(conn)
#conn.modify_s(conn)
#ldap.modlist.addModlist()
#conn.delete_s("cn=Manager1,ou=Tester,o=swust,dc=mypaas,dc=com")
#conn = _connect("cn=Manager2,ou=Developer,o=swust,dc=mypaas,dc=com", "Manager2", "")
'''results1 = ldap.dn.str2dn('cn=Manager12+ou=Developer.swust@mypaas.com,dc=mypaas,dc=com')
print(results1)
print(len(results1))

oldpwd = b'123456'
newpwd = b'1234'
conn.passwd_s("cn=Manager1,ou=Developer,o=swust,dc=mypaas,dc=com", oldpwd, newpwd)'''
conn.delete_s("cn=Manager1,ou=Tester,o=swust,dc=mypaas,dc=com")
'''ldap_result_id = conn.search(u'dc=mypaas,dc=com', ldap.SCOPE_SUBTREE, 'cn=Manager12',None)
result_type, result_data = conn.result(ldap_result_id, 0)
if result_type == ldap.RES_SEARCH_ENTRY:

    print(result_data[0][1])
else:
    print(result_type)
print(ldap.RES_SEARCH_ENTRY)'''
print(conn.whoami_s())
pg_ctrl =  ldap.controls.libldap.SimplePagedResultsControl(True, size=4, cookie="")
results = conn.search_ext_s(u'dc=mypaas,dc=com', ldap.SCOPE_SUBTREE, '(objectClass=person)',serverctrls=[pg_ctrl])

print(results)
#print(len(results))
#create_ad_user(conn)
#print(vertify(conn))

