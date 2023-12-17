API usage  
Assuming port 5000

`curl http://127.0.0.1:5000/tmp |jq .`

    {
      "FirstBootAfterUpdate": {
        "file": {
          "name": "FirstBootAfterUpdate",
          "owner": "root",
          "size": 36,
          "type": "Unknown File Type"
        }
      },
      "FirstBootCleanupHandled": {
        "file": {
          "name": "FirstBootCleanupHandled",
          "owner": "root",
          "size": 12,
          "type": "Unknown File Type"
        }
      },
      "com.apple.launchd.r7wtH1CabJ": {
        "file": {
          "name": "com.apple.launchd.r7wtH1CabJ",
          "owner": "patrick",
          "size": 96,
          "type": "Directory"
        }
      },
      "powerlog": {
        "file": {
          "name": "powerlog",
          "owner": "root",
          "size": 64,
          "type": "Directory"
        }
      }
    }

["file"]["type"] is based on mimetypes, with 'Unknown File Type' for unassociated mimetype

`curl http://127.0.0.1:5000/tmp/FirstBootAfterUpdate|jq .`

    {
      "file": {
        "name": "FirstBootAfterUpdate",
        "text": "4732D5A4-8AB5-4811-92DD-282714D27874"
      }
    }

To run locally:  
git clone  
(in fs-api directory) python -m venv venv  
source venv/bin/activate  
pip install -r requirements  
ROOT_PATH='/path/to/root' flask run  
(e.g., ROOT_PATH='/' flask run)  
This will run with the defaults of binding to 127.0.0.1 on port 5000

To run from docker:  
`docker build -t local:fs-api .`  
`docker run -e ROOT_PATH='/' -v /path/locally/:/path/in/container -p 5500:5500 local:fs-api`  
(Note that port 5500 is used because of conflicts with mac control center run running port 5000 on other than localhost)
`curl http://127.0.0.1:5500/tmp |jq .`

    {
      ".dockerenv": {
        "file": {
          "name": ".dockerenv",
          "owner": "root",
          "size": 0,
          "type": "Unknown File Type"
        }
      },
      "bin": {
        "file": {
          "name": "bin",
          "owner": "root",
          "size": 4096,
          "type": "Directory"
        }
      },
      "boot": {
        "file": {
          "name": "boot",
          "owner": "root",
          "size": 4096,
          "type": "Directory"
        }
      },
      "dev": {
        "file": {
          "name": "dev",
          "owner": "root",
          "size": 340,
          "type": "Directory"
        }
      },
      "etc": {
        "file": {
          "name": "etc",
          "owner": "root",
          "size": 4096,
          "type": "Directory"
        }
      },
    ...
    ..
    }