
import sys
import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2,sequence=4,offset=2)
yaml.compact_seq_map = False

_IP = input('Input your IP：')

myDict = {
    'thingsboard': {
        'host': _IP,
        'port': 1883,
        'remoteConfiguration': False,
        'security': {
            'accessToken': 'MYTOKEN'
        },
    },
    'storage': 
    {
        'type': 'memory',
        'read_records_count': 10,
        'max_records_count': 100000,
    }
}
with open("tb_gateway_1.yaml", "w") as f:
    #yaml.dump(myDict, f,default_flow_style = False,sort_keys=False)
    yaml.dump(myDict,f)

list_connector = []
for i in range(1,11):

    data = {'name': 'OPCUA-'+str(i)+'-TEST Connector',
            'type': 'opcua',
            'configuration': 'opcua-'+str(i)+'-test.json'}
            
    list_connector.append(data)


Data = {
    'connectors': list_connector
}

with open("tb_gateway_1.yaml", "a") as f:
    #yaml.safe_dump(Data, f, default_flow_style = False,sort_keys=False)
    yaml.dump(Data,f)
