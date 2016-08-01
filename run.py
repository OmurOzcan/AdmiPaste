from admipaste import AdmiPaste, app
import yaml


def main():
    with open("config.yml", "r") as f:
        cfg = yaml.load(f.read())

    apaste = AdmiPaste(cfg["mysql"]["host"],
                    cfg["mysql"]["user"],
                    cfg["mysql"]["pass"],
                    cfg["mysql"]["name"])
    apaste.run(cfg["host"], cfg["port"])

    return 0

if __name__ == "__main__":
    exit(main())
