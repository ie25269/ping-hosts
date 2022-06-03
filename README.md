# ping-hosts

Simple python3 script to quickly ICMP ping a list of hosts by ip and determine if they are alive.  Runs preload pings to account for any possible arp/misc timeouts prior to ping tests. Created for a specific purpose, not compatibility...
Uses os.popen to call PING cmd based on my OS syntax at time of creation: Linux 5.4.0-113-generic #127-Ubuntu SMP, iputils s20190709
May need to change ping result conditions and ping cmd syntax in ping_host func for your system.  

Input: single column csv/txt/list of ip's.  
Output: csv file containing "ip,result"

Could use hostnames for input but lookup = DNS = takes longer & dns problems not accounted for.
