from IPy import IP

ip_s=input('请输入IP或网段地址:')
ips=IP(ip_s)
if len(ips)>1:#判断是否为1个ip
    print('网络地址:%s'%ips.net())
    print('网络掩码地址:%s'%ips.netmask())
    print('网络广播地址:%s'%ips.broadcast())
    print('网络地址反向解析:%s'%ips.reverseNames()[0])
    print('网络子网数:%s'%len(ips))
else:
    print('IP反向解析:%s'%ips.reverseNames()[0])
    print('网络掩码地址:%s' % ips.netmask())
    print('网络广播地址:%s' % ips.broadcast())

print('十六进制:%s'%ips.strHex())
print('二进制:%s'%ips.strBin())
print('地址类型:%s'%ips.iptype())


