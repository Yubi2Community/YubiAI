__version__ = "01.23"

### FTP Server constants
FTPPORT = "8989"
FTPHOST = "13.235.92.51"

### Cernunnos base path constant
import pathlib
#BASE_PATH = pathlib.Path(__file__).parent.absolute()
BASE_PATH = pathlib.Path.home().joinpath(".cache", "yubiai").absolute()



