# essencial packages
yum install java-1.8.0-openjdk-devel telnet-server telnet -y
systemctl start telnet.socket
systemctl enable telnet.socket

# get kafka and configure it
wget https://archive.apache.org/dist/kafka/0.11.0.2/kafka_2.11-0.11.0.2.tgz
mv /home/opc/kafka_2.11-0.11.0.2.tgz /opt/
cd /opt/
tar -xvf kafka_2.11-0.11.0.2.tgz 
ln -s /opt/kafka_2.11-0.11.0.2 /opt/kafka
useradd kafka
chown -R kafka:kafka /opt/kafka*

# allow the zookeeper and kafka on the firewall
firewall-cmd --zone=public --permanent --add-port 23/tcp
firewall-cmd --zone=public --permanent --add-port 9092/tcp
firewall-cmd --zone=public --permanent --add-port 2181/tcp
firewall-cmd --reload

# get the ip from the instance-developer-kafka1 and add it to the /etc/hosts
vim /etc/hosts

# start zookeeper
kafka/bin/zookeeper-server-start.sh kafka/config/zookeeper.properties &

# start kafka
kafka/bin/kafka-server-start.sh kafka/config/server.properties &
telnet instance-developer-kafka1 9092
telnet instance-developer-kafka1 2181

# create a new topic
/opt/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic1

# Mirror Maker should be on the destination node or the closest possible to the destination node.
# check the configurations on this repository.
vim /opt/kafka/config/producer.properties
vim /opt/kafka/config/consumer.properties
