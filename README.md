# rAnPriv (Lite) ~ Privacy-Preserving Online Social Network Information Disclosure Scheme

## Introduction

This is the experimental code for privacy-preserving online social network information disclosure scheme, which is my
undergoing Master's project.

## Dataset

The datasets used in this project are from [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/).

Currently, we support the following two datasets.

- Google+

- Facebook

## Get Started

### Installation

**Note**: The code is written in Python 2.7.x. Currently, it is not compatible with Python 3. 

```bash
	$ git clone https://github.com/rAnYKM/rAnPrivGP.git
	$ cd rAnPrivGP
	$ pip install -r requirements.txt
```
Configure the directory of the SNAP datasets.

```bash
	$ python ranfig.py -g $GOOGLE_PLUS_DIR$ -f $FACEBOOK_DIR$ -d data -o out
```

### A Test Case

```python
	>>> from snap_facebook import FacebookEgoNet
	>>> facebook = FacebookEgoNet('0')
	>>> facebook.ran.soc_net.number_of_nodes()
	348
```
