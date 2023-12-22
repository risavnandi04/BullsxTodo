#!/bin/bash

# Name of the file to convert
export filename="manage.py"

# Use python to run your Python code
python << END
import os
filename = os.getenv('filename')
with open(filename, 'r') as f:
    content = f.read()
content = content.replace('\r\n', '\n')
with open(filename, 'w') as f:
    f.write(content)
END
