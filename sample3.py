import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")

i=1 
while i <= 5:
    j.copy_job("hsbc_proj%d"%i,"sample_hsbc%d"%i)
    i = i+1

