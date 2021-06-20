```bash
# Install env
$ python -m venv venv

# Active virtual environment(Windows)
$ venv\Scripts\activate

# Install lib requirements
$ pip install -r requirements.txt

# Run
$ python -m flask run --host=0.0.0.0
```

```bash
# Build
$ docker build --tag spellio .

# Run in Windows
$ docker run -d -v %cd%:/app -p 5000:5000 --name spellio spellio

# Run in mac or linux
$ docker run -d -v ${PWD}:/app -p 5000:5000 --name spellio spellio

# Stop and Remove
$ docker container rm -f spellio
```