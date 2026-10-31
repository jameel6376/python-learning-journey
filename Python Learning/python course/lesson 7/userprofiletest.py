user_profiles = {
    101: {'username': "coder15", 'role': 'developer', 'status': 'active'},
    102: {'username': 'admin_dave', 'role': 'admin', 'status': 'suspended'}
}

banned_ips = {'192.168.1.5', '192.168.1.1', '192.168.1.1'}

user_id = int(input('user ID: \n'))
i_d = user_profiles.get(101)
print(i_d)
user_ip = '10.0.0.99'
if user_ip in banned_ips:
    print ("connection secure")
else:
    print ('access denied: ip banned')

user_profiles[101]["status"] = 'offline'

user_profiles.pop(102)
print(user_profiles)