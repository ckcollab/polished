import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(description="Generate a screenshot from each commit to convert to video")

    parser.add_argument(
        "url",
        help="URL to capture, can be a local file ~/src/myproj/index.html or remote like http://google.com"
    )
    parser.add_argument(
        '--backend',
        help="Set the polished backend to use, i.e. --backend polished.backends.PelicanBackend",
        default="polished.backends.SimpleBackend"
    )

    args = parser.parse_args()
    # args.backend
    # args.url

    print args.backend

    #backend = importlib.import_module(args.backend)
    backend = __import__(args.backend)

    polished = backend()
    polished.execute(args.url)


if __name__ == "__main__":
    main()
