import os
import csv
import sys
import time

if len(sys.argv) < 3 or "-h" in sys.argv:
    print(f'\nusage:  ping.py <inputFile> <outputFile')
    print(f' \t\tinputFile:  \tName of csv file for input.')
    print(f' \t\toutputFile:  \tName of csv file to save output results.')
    raise SystemExit

startTime = time.time()

def ping_host(ipHost):
    # PING cmd based on my OS syntax: Linux 5.4.0-113-generic #127-Ubuntu SMP, iputils s20190709
    # Preload pings, to account for any arp/other timeouts.
    os.popen(f"ping {ipHost} -l 2 -c 2")
    # Begin ping test
    response = os.popen(f"ping {ipHost} -W 1 -c 2").read()
    if "2 packets transmitted, 2 received" in response:
        pingResult = "success"
    elif "2 packets transmitted, 0 received" in response:
        pingResult = "FAIL-noResponse"
    elif "failure in name resolution" in response:
        pingResult = "FAIL-nameResolution"
    elif "Name or service not known" in response:
        pingResult = "FAIL-nameSrvcUnknown"
    else:
        pingResult = "PktLOSS"
    return pingResult

def input2List(inputFile):
    # Convert csv input file to list
    inList = list()
    with open(inputFile) as data:
        csv_list = csv.reader(data)
        for row in csv_list:
            ipAddr = row[0]
            inList.append(ipAddr)
    return inList

inFile = sys.argv[1]
outFile = sys.argv[2]
ipList = input2List(inFile)

try:
    with open(outFile, "x") as rdata:
        csv_writer = csv.writer(rdata, delimiter=',')
        x = 1 
        for ip in ipList:
            result = ping_host(ip)
            csv_writer.writerow([ip,result])
            print(f'test {x:>3}:\t{ip:<6}\t{result}')
            x += 1
except KeyboardInterrupt:
    print(f'-----------------------\nSTOPPED by User')
    endTime = time.time()
    runTime = round((endTime - startTime),2)
    tests = x - 1
    testsLen = len(ipList)
    print(f'-----------------------')
    print(f'Tests incomplete. {tests} of {testsLen} tests completed.\n Output saved to {outFile}.\n  runTime: {runTime:<3} sec\n')
except FileExistsError:
    print(f'\nERROR: Output file with name {outFile} already exists\n')
else:
    endTime = time.time()
    runTime = round((endTime - startTime),2)
    print(f'-----------------------')
    print(f'All tests complete.\n Output saved to {outFile}.\n  runTime: {runTime:<3} sec\n')

