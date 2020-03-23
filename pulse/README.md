# Pulse Module

## David Abadi

### Start Server

To start the server run:

```bash
python pulse.py
```

### Get Data

Make a get request to "http://127.0.0.1:5000/" to get a JSON with the current pulse. The JSON looks like:

```JSON
{
    "name": "pulse",
    "values": [60]
}
```
