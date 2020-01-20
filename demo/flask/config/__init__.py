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


def company_db():
    host = get_config("config.yml", "data-sources.company.host")
    port = get_config("config.yml", "data-sources.company.port")
    user = get_config("config.yml", "data-sources.company.username")
    password = str(get_config("config.yml", "data-sources.company.password"))
    db_name = get_config("config.yml", "data-sources.company.db-name")
    charset = get_config("config.yml", "data-sources.company.charset")
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=db_name, charset=charset)
    return db.cursor()


def scf_db():
    host = get_config("config.yml", "data-sources.scf.host")
    port = get_config("config.yml", "data-sources.scf.port")
    user = get_config("config.yml", "data-sources.scf.username")
    password = str(get_config("config.yml", "data-sources.scf.password"))
    db_name = get_config("config.yml", "data-sources.scf.db-name")
    charset = get_config("config.yml", "data-sources.scf.charset")
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=db_name, charset=charset)
    return db.cursor()
