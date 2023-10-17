
#Sonar-scanner manually installed on python image.

FROM python:3.7

COPY my_python_project /

ENV PYTHON_PROJECT=my_project
ENV SONAR_URL=my_sonar_url
ENV SONAR_AUTH_TOKEN=my_token
ENV COV_PATH=my_coverage_path

RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472.zip \
    && unzip sonar-scanner-cli-4.6.2.2472.zip \
    && mv sonar-scanner-4.6.2.2472/ /opt/sonar/ \
    && echo "PATH=/opt/sonar/bin" >> /etc/environment \
    && apt-get update && apt-get install default-jre -y \
    && export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/ \
    && /opt/sonar/bin/sonar-scanner -Dsonar.projectKey=${PYTHON_PROJECT} -Dsonar.host.url=${SONAR_URL} -Dsonar.login=${SONAR_AUTH_TOKEN} -Dsonar.qualitygate.wait -Dsonar.python.coverage.reportPaths=${COV_PATH}/coverage.xml