import logging


def logfile(message):
    """
    Hàm ghi log vào file, kèm theo mốc thời gian.

    Args:
      message: Nội dung cần ghi vào log.
    """

    # Tên file log
    log_file = "logs.log"

    # Cấu hình logger, thêm định dạng mốc thời gian
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        encoding="utf-8",
    )

    # Ghi log
    logging.info(message)