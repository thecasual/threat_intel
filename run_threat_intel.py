import threat_intel.threat_intel
import json
import os

def main():

    #print("Threat Intel Feed")
    my_path = os.path.dirname(os.path.abspath(__file__))

    with open(my_path + '\\threat_intel.json', 'r') as f:
        config = json.load(f)

    out = threat_intel.threat_intel.query(config, '148.251.45.170')

    print(out)

if __name__ == "__main__":
    main()