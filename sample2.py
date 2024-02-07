import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")

j.delete_job("sampledevelopment")
