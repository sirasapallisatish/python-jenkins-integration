import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")

j.copy_job("Development1","sampledevelopment")
