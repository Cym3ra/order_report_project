import logging

from .config import configure_logging, ReportConfig
from .loading import load_orders
from .processing import (
    calculate_order_values,
    clean_order_data,
)
from .reporting import create_reports
from .validation import validate_orders

logger = logging.getLogger(__name__)

def main(config: ReportConfig) -> None:
    configure_logging()

    logger.info("Startar orderrapport")

    try:
        raw_data = load_orders(config.input_path)

        errors = validate_orders(raw_data)
        if errors:
            for error in errors:
                logger.error(error)
            return

        raw_data = clean_order_data(raw_data)
        raw_data = calculate_order_values(raw_data)

        create_reports(raw_data, config.output_path)
        logger.info("Orderrapport klar")

    except FileNotFoundError as error:
        logger.error("Kunde inte hitta datafilen: %s", error)

    except OSError as error:
        logger.error("Kunde inte läsa eller skriva fil: %s", error,)

if __name__ == "__main__":
    main(ReportConfig()) 