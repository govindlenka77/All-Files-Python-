import re
f = open("C:\\Users\\glenka\\OneDrive - Cisco\\Documents\\Python Scripts\\delete\\693110730-show_tech_Malathi.txt","r")
data = f.read()

object_group_service = re.findall(r'object-group\sservice\s([\w-]+)',data)
object_group_network = re.findall(r'object-group\snetwork\s([\w-]+)',data)
network_object = re.findall(r'network-object\sobject\s([\w-]+)',data)
object_group_service_count = 0
object_group_network_count = 0
network_object_count = 0
for i in object_group_service:
    if i:
        object_group_service_count+=1

for j in network_object:
    if j:
        # print(j)
        network_object_count+=1
for k in object_group_network:
    # print(k)
    if k:
        # print(k)
        object_group_network_count+=1
print("Network Object -",len(network_object), network_object_count)
print("object_group_service",len(object_group_service), object_group_service_count)
print("object_group_network",len(object_group_network), object_group_network_count)