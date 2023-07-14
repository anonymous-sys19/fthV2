from ipaddress import ip_address
import ipinfo
import pprint
import os
import time
from ipinfo.details import Details
from ipinfo.handler import Handler
from requests import get
import socket

def Locate_ip():
    try:

        TokenAccess = 'e346a48b2e9c41'
        def Ipublic():
            def Ips():
                #  YOUR IP PRIV
                socker = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                socker.connect(('8.8.8.8', 80))
                
    # Ottrer
                IpPublic = get('https://api.ipify.org').text

                print ('\nYours Ip is: {} '.format(IpPublic)+' Yours ip priv Is: '+socker.getsockname()[0])
                print('\nYour Informatons personal is:'+'https://ipinfo.io/'+str(IpPublic)+'/json?token=e346a48b2e9c41')

            # SEGUNDA FACE  IS location ;
            
            Ips()
            AccessAlTOken = TokenAccess
            
            handler = ipinfo.getHandler(AccessAlTOken)
            ip_address = input('\n\nEnter la Ip:> \n\n')
            details = handler.getDetails(ip_address)
            
            print('\nYour Details is: \n')
            pprint.pprint(details.all)

        Ipublic()    
    except KeyboardInterrupt:
        print('Error Programa cerrado OH Mal dato de Codigo')
        pass
Locate_ip()