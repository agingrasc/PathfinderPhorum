import yaml


def main():
    with open('phorum/data/default_players.yml') as f:
        lines = f.readlines()

    lines = "".join(lines)
    print(yaml.load(lines))

if __name__ == "__main__":
    main()
