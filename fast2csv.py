import re


def line2csv(line):
    print(line)
    a = re.compile(r"([0-9]{2}\/[0-9]{2}\/20[0-9]{2})-([0-9]+\:[0-9]+\:[0-9]+\.[0-9]+)\s+\[\*\*\]\s+\[([0-9]+)\:(["
                   r"0-9]+)\:([0-9]+)\]\s+(.*)\[\*\*\]\s+\[Classification\:\s+([aA-zZ 0-9]+)\]\s+\[Priority\:\s+(["
                   r"0-9]+)\]\s+\{([aA-zZ 0-9]+)\}\s+(.*)\s+->\s(.*)")
    results = a.match(line)
    return results.groups(0)
with open('wrccdc_alerts_converted.csv', 'w') as outFile:
    outFile.write('date,time,group,sid,sev,rule_name,classification,priority,protocol,from_addr,to_addr\n')
    with open('fast.log', 'r') as inFile:
        for line in inFile:
            outFile.write(','.join(str(i) for i in line2csv(line))+'\n')
