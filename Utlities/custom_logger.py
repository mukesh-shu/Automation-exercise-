import logging
import os
class Log_maker:
    @staticmethod
    def log_gen():
      log_dir = os.path.join(os.getcwd(), "logs")
      os.makedirs(log_dir, exist_ok=True)

      log_file = os.path.join(log_dir, "automation.log")
      logging.basicConfig(
            filename=log_file,
            filemode="a",
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
        )
      logger = logging.getLogger()
      logger.setLevel(logging.INFO)
      return logger   