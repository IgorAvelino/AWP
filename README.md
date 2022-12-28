
# AWP
<h3 align="center"> Fast, Powerful and Nondiscrete Pentest toolkit </h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/77363934/209717836-04a785f7-9719-47ed-8b42-cd814d351e37.png">
</p>

##
<h3><p align="center">Disclaimer</p></h3>

<i>Any actions and or activities related to <b>AWP</b> is solely your responsibility. The misuse of this toolkit can result in <b>criminal charges</b> brought against the persons in question. <b>The contributors will not be held responsible</b> in the event any criminal charges be brought against any individuals misusing this toolkit to break the law.
##


## Instalation
- First of all, you need [Python3](https://www.python.org/downloads/)

- After this, clone the repository:

```bash
  git clone --- LINK ---
  cd .\AWP
```

- Install the requirements.txt for use the python3 external libraries:
```bash
    pip install -r requirements.txt
```
- And that's it, just read the how_to_use.py file and have fun tests :)
```bash
    python how_to_use.py
```
## Documentation of Python Scripts

### Port Scanning a Host

```bash
  python port_scan.py [ HOST ] [ Optional: TIMEOUT ]
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `HOST` | `string` | **Required**. The target domain |
| `TIMEOUT` | `INT` | Optional. The time to wait to close the connection if the port does not respond, in milliseconds |


