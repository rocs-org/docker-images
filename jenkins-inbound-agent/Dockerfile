FROM jenkins/inbound-agent:latest-alpine-jdk17

# Copy custom certificates
RUN mkdir -p /tmp/certs
COPY root.crt sub04.crt /tmp/certs/

USER root

# Add custom certificates to ca-certificates.crt
RUN cat /tmp/certs/root.crt /tmp/certs/sub04.crt >> /etc/ssl/certs/ca-certificates.crt

# Add custom certificates to java keystore
RUN ${JAVA_HOME}/bin/keytool -import -trustcacerts -alias custom-root -keystore ${JAVA_HOME}/lib/security/cacerts -storepass changeit -noprompt -file /tmp/certs/root.crt \
    && ${JAVA_HOME}/bin/keytool -import -trustcacerts -alias custom-sub04 -keystore ${JAVA_HOME}/lib/security/cacerts -storepass changeit -noprompt -file /tmp/certs/sub04.crt

RUN awk -v cmd='openssl x509 -noout -subject' '/BEGIN/{close(cmd)};{print | cmd}' < /etc/ssl/certs/ca-certificates.crt > /tmp/ca.txt

USER jenkins