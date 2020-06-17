# python_metis
Just a modified package from official "METIS for Python" to support lastest networkx.
Should support all features.

## Installation
You need to install **metis** first for this wrapper.
1. Download and extract metis-5.1.0.tar.gz from [METIS - Serial Graph Partitioning and Fill-reducing Matrix Ordering](http://glaros.dtc.umn.edu/gkhome/metis/metis/download)
2. `cd metis-5.1.0`
3. `make config shared=1 prefix=~/.local/`
4. `make install`
5. `export METIS_DLL=~/.local/lib/libmetis.so`

You are ready to use this wrapper
```
pip3 install metis-python
```

## Test
```
python3 metis.py  # Official Test
python3 test.py  # A Simple Test
```