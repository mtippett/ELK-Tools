#!/usr/bin/python

import sys
import json

json_input = json.load(sys.stdin)

hosts = json_input['sysstat']['hosts']

#host = hosts[0]
#stat = host['statistics'][0]      
for host in hosts:
  for stat in host['statistics']:
    stat['host'] = host['nodename']
    stat['time'] = stat['timestamp']['date']+'T'+stat['timestamp']['time']
    stat['docid'] = stat['host']+'-'+stat['time']
    for dev in stat['network']['net-dev']:
        dev['rxkB'] = - dev['rxkB'] 
        dev['rxpck'] = - dev['rxpck'] 
    for dev in stat['disk']:
        dev['rd_sec'] = - dev['rd_sec'] 


    print json.dumps(stat)
   

