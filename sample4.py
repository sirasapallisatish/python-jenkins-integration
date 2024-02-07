import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")

i =1
while i<= 5:
    j.delete_job("hsbc_proj%d"%i)
    i =i+1
      
