#!/usr/bin/python3 

print('content-type: text/html')
print()

import cgi 
import subprocess
#print('python file from rhel vm')
#time.sleep(10)

f=cgi.FieldStorage()
cmd=f.getvalue('x') 

print(x)
print()
#image=None
#name=None
#port=None
#replicas=None
"""
if "directory" in cmd:
    cmd="pwd"


#print('after directory')

if "describe" in cmd:
    if 'pod' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            #print(b[i])
            if b[i]=='pod':
                name=b[i+1]
                print(name)
        cmd='kubectl describe pod '+name
    if 'deploy' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            #print(b[i])
            if b[i]=='deployment':
                name=b[i+1]
                print(name)
        cmd='kubectl describe pod '+name
    if 'svc' in cmd or 'service' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            #print(b[i])
            if b[i]=='service' or b[i]=='svc':
                name=b[i+1]
                print(name)
        cmd='kubectl describe pod '+name

if 'show' in cmd or 'see' in cmd or 'get' in cmd:
    if 'pod' in cmd:
        cmd='kubectl get pods'
    if 'svc' in cmd or 'service' in cmd:
        cmd='kubectl get svc'
    if 'deploy' in cmd:
        cmd='kubectl get deploy'




if "launch" in cmd or 'run' in cmd or 'create' in cmd  :
    if "pod" in cmd:
        b=cmd.split()
        for i in range(len(b)):
            if b[i]=="image":
                image=b[i+1]
            if b[i]=="name":
                name=b[i+1]
        cmd='kubectl run '+name+' '+' --image='+image
    if 'deploy' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            if b[i]=="name":
                name=b[i+1]
                #print('name:',name)
            if b[i]=="image":
                image=b[i+1]
            if b[i]=='replicas':
                replicas=b[i+1]
        #print(cmd)
        if replicas==None:
            #print('replica is none')
            cmd='kubectl create deployment '+ name + ' ' + ' --image=' + image
            #print(cmd)
        else:
            #print('inside else')
            cmd='kubectl create deployment '+name+' '+' --image='+image+' --replicas='+replicas
            


if 'expose' in cmd:
    b=cmd.split()
    for i in range(len(b)):
        if b[i]=='deployment':
            name=b[i+1]
        if b[i]=='port':
            port=b[i+1]
    cmd='kubectl expose deployment '+name+' --port='+port+' --type=NodePort'
    #print(cmd)


if 'replicate' in cmd or 'increase' in cmd or 'scale' in cmd        :
    b=cmd.split()
    for i in range(len(b)):
        #print(b[i])
        if b[i]=='deployment':
            name=b[i+1]
            #print('name: ', name)
        if b[i]=='to':
            replicas=(b[i+1])
            #print('replica : ', replicas)
    #print('out of for loop')
    cmd='kubectl scale deployment '+name + ' --replicas='+replicas
    #print(cmd)

#print('before delete')
if 'delete' in cmd or 'remove' in cmd:
    if 'all' in cmd or 'everything' in cmd:
        cmd='sudo kubectl delete all --all'
        print(cmd)
    if 'pod' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            if b[i]=="pod":
                name=b[i+1]
        cmd="kubectl delete pod "+name
    if 'deploy' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            if b[i]=='deploy' or b[i]=='deployment':
                name=b[i+1]
        cmd='kubectl delete deployment '+name
    if 'svc' in cmd or 'service' in cmd:
        b=cmd.split()
        for i in range(len(b)):
            if b[i]=='service' or b[i]=='svc':
                name=b[i+1]
        cmd='kubectl delete svc '+name


print('your command: ', cmd+" --kubeconfig admin.conf")  
print() 
o=subprocess.getoutput("sudo "cmd+' --kubeconfig admin.conf')
print('Ouput >_')
print()
print(o)"""

