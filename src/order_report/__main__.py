import logging


def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(name)s | %(message)s"
    )


def main() -> None:
    configure_logging()


if __name__ == "__main__":
    main()