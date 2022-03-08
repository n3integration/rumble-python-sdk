## Rumble Python SDK (unofficial)
Unofficial Rumble Network Discovery Python SDK

### Installation
```bash
pip install rumblesdk
```

### Unauthenticated Usage
```python
from rumblesdk.client import ApiClient


client = ApiClient()
client.releases().get_platform_version()
```

### Organization Key Usage

```python
import os

from rumblesdk.auth import OrgKey
from rumblesdk.client import ApiClient


client = ApiClient(OrgKey(os.getenv("API_KEY")))
win_assets = client.org().get_asset_list("os:windows")
```

### License

Copyright 2022 n3integration

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.