import logging
import sys
import os

class LogSystem():
    def __init__(self,test_name):
        self.test_name = test_name
        self.logger = self.setup_logging()
    
    def setup_logging(self):
        logger = logging.getLogger(self.test_name)
        
        if not logger.handlers:
            log_folder = os.path.join(os.getcwd(),'selenium_', 'logs')
            os.makedirs(log_folder, exist_ok=True)
            formatter = logging.Formatter('%(asctime)s-%(levelname)%-%(message)s')
            
            
            file_handler = logging.FileHandler(os.path.join(log_folder,f'{self.test_name}_log.txt'))
            file_handler.setFormatter(formatter)
            
            
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.INF0)
            console_handler.setFormatter(formatter)
            
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            logger.setLevel(logging.INFO)
        
        return logger
    
    
    
    
    def clear_log_folder(self):
        log_folder = os.path.join(os.getcwd(),'selenium_', 'logs')
        log_file_path=os.path.join(log_folder, log_folder,f'{self.test_name}_log.txt')
        
        try:
            with open(log_file_path, 'w'):
                pass
        except FileNotFoundError:
            print(f'Log file not found: {log_file_path}')
        
        
        
        