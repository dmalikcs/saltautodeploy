#!/usr/bin/env python
import os
import sys
import dotenv
dotenv.read_dotenv()

JENKINS_SERVER = 'ind198lc001.krunksystems.com'

if __name__ == "__main__":
    if os.uname()[1] == JENKINS_SERVER:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saltautodeploy.settings_jenkins")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saltautodeploy.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
