# mparse

Simple URL parser for bug bounty hunting. Extracts unique URLs from a file or stdin, prepares GET parameters for other pentesting tools.


```
usage: mparse.py [-f <FILE>] [-p <PARAM>] [-g] [-u] [-h]

Simple URL parser for bug bounty hunting.

optional arguments:
  -f <FILE>      Specify file with URLs.
  -p <PARAM>     Specify placeholder parameter value.
  -g, --getvals  Print all unique GET parameters.
  -u, --unique   Print only unique URLs.
  -h, --help     Print this help menu.

```
