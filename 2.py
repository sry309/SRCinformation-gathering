#coding:utf8
import sys

log = open("result.gnmap","r")
xls = open("output.csv","a")
xls.write("IP,port,status,protocol,service,version\n")
for line in log.readlines():
		if line.startswith("#") or line.endswith("Status: Up\n"):
				continue
		result = line.split("	")
		#print result
		host = result[0].split(" ")[1]
		#print host
		port_info = result[1].split("/, ")
		#print port_info
		port_info[0] = port_info[0].strip("Ports: ")
		#print port_info[0]
		for i in port_info:
				j = i.split("/")
				#print j
				output = host + "," + j[0] + "," + j[1] + "," + j[2] + ","+ j[4] + "," + j[6] + "\n"
				xls.write(output)