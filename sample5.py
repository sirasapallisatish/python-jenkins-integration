import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")

j.build_job("Development1")
j.build_job("Testing1")

