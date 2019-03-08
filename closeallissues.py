import os
import yaml
import githubapimock as api 


config_path = os.path.expanduser("~/repo.yml")

settings = yaml.load(open(config_path))


user = settings["user"]
org =  settings["org"]
repo = settings["repo"]
token =  settings["token"]
"""
title = "My first client issue"
body = "This was created from the client"
labels = ['todo', 'helpwanted', 'autogenerated']
issue_id = api.create_issue(org, repo, user, token, title, body)
print ( "Created issue: " + str (issue_id ))
api.set_labels(org, repo, user, token, issue_id, labels)

print ("Added labels " + str(labels) + " to  issue " + str(issue_id ))


title = ""
while title != "q":
    title = input("Title: ")
    body = input("Body: ")
    label = input("Label: ")
    labels = [label]
    issue_id = api.create_issue(org, repo, user, token, title, body)
    print ( "Created issue: " + str (issue_id ) + " in " + org + "/" + repo)
    api.set_labels(org, repo, user, token, issue_id, labels)
    print ( "Added labels " + str(labels) + " to issue " + str(issue_id) )
"""

all_issues = api.get_issues(org, repo, user, token)


for issue in all_issues:
    print("Closing " + str(issue["number"]))
    api.close_issue(org, repo, user, token,issue["number"])


    







