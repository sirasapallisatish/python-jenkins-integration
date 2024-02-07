import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")

x = j.get_jobs()
print(x)
