#### 上傳隨便一週作業到pythonanywhere

我傳[**第九週**](http://station4178.pythonanywhere.com/)的

作法：
1. 把要上傳的該週作業壓縮成.zip
2. 上傳到pythonanywhere的檔案上傳區
3. 去pythonanywhere的bash輸入 `unzip file_name.zip` 解壓縮檔案
4. pythonanywhere的web app 設定中的wsgi configure檔案改成
``` python
import os
import sys

path = '/home/帳號名稱/專案名稱'

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '專案名稱.settings'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())
```

5. 自己專案的settings.py裡面的`ALLOWED_HOSTS`要改成
```python
ALLOWED_HOSTS = ['pythonanywhere web的連結']
```

6. 設定 Virtual Environment位置
   > 虛擬環境Python版本要跟Web的一樣
7. Reload 連結
   
FINISH