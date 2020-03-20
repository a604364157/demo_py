import MySQLdb
import yaml


def get_config(file: str, key=None):
    with open("config/" + file, 'r', encoding="utf-8") as f:
        yml_data = f.read()
        data = yaml.load(yml_data, Loader=yaml.FullLoader)
        if None is not key:
            if not key.__contains__('.') and key in data:
                return data[key]
            elif not key.__contains__('.') and key not in data:
                return None
            else:
                lists = key.split('.')
                result = data
                for item in lists:
                    if item in result:
                        result = result[item]
                        if result is None:
                            return
                    else:
                        result = None
                        return
                if None is not result:
                    return result
                else:
                    return None
        else:
            return None


def scf_db():
    db = MySQLdb.connect(host="192.168.138.233", port=33306, user="root", passwd="123456", db="scf_w", charset="utf8")
    return db.cursor()
