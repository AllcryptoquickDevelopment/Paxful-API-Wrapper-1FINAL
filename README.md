
# General
This package contains a python wrapper for the Paxful Cryptocurrency Exchange APIv1. It utilizes the requests python 
package to communicate with the API. A Paxful account is required and must be authenticated using your own  API key.

Please visit https://paxful.readthedocs.io/ for more details on the API. 

# Install
This package can be installed from the PyPi repository.

`pip install paxful-api`

You can also download the zip and and place it into a Virtual Environment created using virtualenv (recommended).

# Setup
In the main client, you must define your API key and API secret.
Example:

`api_key=cinow2P4gwP8hCD_MTe6p-YlnhQIeRrtiQswcxx 
api_secret=F8Rt6xuKwertRpLVs7vowoDwertX79O_39RK1kLdxx`

The _main client_ is used for general operations such as opening a trade, creating offers, fetching available payment 
methods, and getting transaction information.

The _trade client_ is used for specific trade operations such as chatting, releasing funds, sending pictures and giving
feedback. **Each trade client object represents an individual trade.** 

## Examples


