
import os
import yaml

def getConFigYaml_data(fname):
    config_dir = os.path.join(fname)
    stream = open(config_dir, "r")
    yaml_data = yaml.safe_load(stream)
    return yaml_data
    # try:
    #
    # except OSError as e:
    #     print(f"OSError {e}")
    #     f = open(config_dir, "w")
    #     f.write("ServerDomainName : 192.168.3.11\n"
    #             "ServerPort : 5000")
    #     f.close()
    #     stream = open(config_dir, "r")
    #     yaml_data = yaml.safe_load(stream)
    #     errorMessageText.insert(1.0,"ReadConfigError")
    # except Exception as e:
    #     errorMessageText.insert(1.0,"ReadConfigError")
    #     print(f"ReadConfigError {e}")

# def writeLog(fname):

