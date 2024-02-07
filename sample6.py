import jenkins
j = jenkins.Jenkins("http://localhost:8080","karthik","satish")
j.build_job("sample_hsbc1")
j.build_job("sample_hsbc2")
