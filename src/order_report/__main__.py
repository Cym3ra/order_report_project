import logging

from .config import configure_logging



def main() -> None:
    configure_logging()


if __name__ == "__main__":
    main()