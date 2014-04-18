import argparse
import importlib
import sys


def load_class(full_class_string):
    """
    dynamically load a class from a string

    http://thomassileo.com/blog/2012/12/21/dynamically-load-python-modules-or-classes/
    """
    class_parts = full_class_string.split(".")
    module_path = ".".join(class_parts[:-1])
    class_name = class_parts[-1]

    module = importlib.import_module(module_path)

    return getattr(module, class_name)


def main():
    parser = argparse.ArgumentParser(description="Generate a screenshot from each commit to convert to video")

    parser.add_argument(
        "url",
        help="URL to capture, can be a local file ~/src/myproj/index.html or remote like http://google.com"
    )
    parser.add_argument(
        '--backend',
        help="Set the polished backend to use, i.e. --backend polished.backends.PelicanBackend",
        default="backends.SimpleBackend"
    )

    args = parser.parse_args()

    sys.path.append("../")

    backend = load_class(args.backend)

    polished = backend()
    polished.execute(args.url)


if __name__ == "__main__":
    main()
