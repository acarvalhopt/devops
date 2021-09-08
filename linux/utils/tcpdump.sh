# To make the tcpDump end to end we need to do the following command on each machine and after that check on wireshark the "Arrival time" of the packets.
tcpdump -A -s 0 'tcp port <port> and (((ip[2:2] - ((ip[0]&0xf)<<2)) - ((tcp[12]&0xf0)>>2)) != 0)' -w /tmp/output.pcap