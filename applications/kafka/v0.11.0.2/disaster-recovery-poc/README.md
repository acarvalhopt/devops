# Mirror Maker PoC for Kafka 0.11.0.2 for Disaster Recovery Purposes

# Configuration
- create 2 machines in different regions
- the test was done with one machine in Frankfurt and another in London.
- Run the scripts for installation in both machines
- After the installation you should be able to produce messages in instance-developer-kafka1 and receive them in instance-developer-kafka2.

# Testing the mirror maker

## In the instance-developer-kafka2

#### create a new topic
```/opt/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic1```

#### start the mirror maker on a new console terminal
```/opt/kafka/bin/kafka-mirror-maker.sh --consumer.config /opt/kafka/config/consumer.properties --num.streams 1 --producer.config /opt/kafka/config/producer.properties --whitelist topic1 ```

#### start the consumer on a new console terminal
```/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topic1 --from-beginning```

## In the instance-developer-kafka1 

#### create a new topic
```/opt/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic topic1```

#### start the producer
```/opt/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic topic1```

##### produce some messages and they should appear on instance-developer-kafka2.

![MirrorMakerTest](<Screenshot 2023-10-20 at 16.10.21.png>)