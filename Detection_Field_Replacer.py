# This script finds and replaces field names in a text file. Used for Elasticsearch mapping changes and ultimate
# update to Watchers.

import os
import json

with open("C:\\Users\\<user_id>\\Desktop\\Windows_Clear_Audit_logs.json", "r") as f:
    watcherUpdateFields=f.read()

    while "microsoft_windows" in watcherUpdateFields:
        watcherUpdateFields=watcherUpdateFields.replace("microsoft_windows", "enterprise-winlogbeats")

    while "Control" in watcherUpdateFields:
        watcherUpdateFields=watcherUpdateFields.replace("Control", "user-account-control")

    while "NT-Domain" in watcherUpdateFields:
        watcherUpdateFields=watcherUpdateFields.replace("NT-Domain", "user-domain")

    while "destinationUserName" in watcherUpdateFields:
        watcherUpdateFields=watcherUpdateFields.replace("destinationUserName", "user-name")

with open("C:\\Users\\<user_id>\\Desktop\\Windows_Clear_Audit_logs.json", "w") as f:
    f.write(watcherUpdateFields)

f.close()