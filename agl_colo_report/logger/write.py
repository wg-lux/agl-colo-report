import logging
import os
from datetime import datetime

def get_custom_logger(log_type, log_name, log_dir, include_date=True, overwrite=False):
    """
    Returns a logger with customized settings.

    Parameters:
    - log_type (str): The type of the log (e.g., 'error', 'info').
    - log_name (str): The name of the log file.
    - include_date (bool): Whether to include the current date in the filename.
    - overwrite (bool): Whether to overwrite the existing log file.

    Returns:
    - logger: A logging.Logger object with customized settings.
    """
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Generate the log filename
    date_str = datetime.now().strftime('%Y-%m-%d') if include_date else ''
    filename = f"{date_str}_{log_type}_{log_name}.md" if include_date else f"{log_type}_{log_name}.md"
    filepath = os.path.join(log_dir, filename)

    

    # Define the file mode ('w' for overwrite, 'a' for append)
    if overwrite:
        file_mode = 'w'
    else:
        file_mode = 'a'

    # Create a logger object
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)  # You can set this to any level

    # Create a file handler and set the level to debug
    fh = logging.FileHandler(filepath, mode=file_mode)
    fh.setLevel(logging.DEBUG)  # You can set this to any level

    # Create a Markdown-friendly formatter and set it for the file handler
    formatter = logging.Formatter(
        '## Log Entry\n'
        '**Timestamp**: `%(asctime)s`\n'
        '**Logger Name**: `%(name)s`\n'
        '**Level**: `%(levelname)s`\n'
        '**Message**:\n'
        '```markdown\n'
        '%(message)s\n'
        '```\n'
    )
    fh.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(fh)

    return logger

# Usage example
# logger = get_custom_logger('error', 'my_log', include_date=True, overwrite=True)
# logger.error('This is an error message.')

