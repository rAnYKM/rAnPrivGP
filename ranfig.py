#!/usr/bin/env python
# Project Name: rAnPrivGP
# Author: rAnYKM (Jiayi Chen)
#
#          ___          ____       _
#    _____/   |  ____  / __ \_____(_)   __
#   / ___/ /| | / __ \/ /_/ / ___/ / | / /
#  / /  / ___ |/ / / / ____/ /  / /| |/ /
# /_/  /_/  |_/_/ /_/_/   /_/  /_/ |___/
#
# Script Name: ranfig.py
# Date: May. 9, 2016


import os
import platform
import sys
import getopt
import ConfigParser as cp


DEFAULT_GPLUS_DIR = ''
DEFAULT_FBOOK_DIR = ''
DEFAULT_DATA_DIR = 'data'
DEFAULT_OUT_DIR = 'out'
DEFAULT_NETKIT_DIR = ''


def make_ranfig(gplus_dir=DEFAULT_GPLUS_DIR, fbook_dir=DEFAULT_FBOOK_DIR, 
                data_dir=DEFAULT_DATA_DIR, out_dir=DEFAULT_OUT_DIR,
                netkit_dir=DEFAULT_NETKIT_DIR):
    computer_name = platform.node()
    config = cp.RawConfigParser()
    config.add_section('FILE_DIR')
    config.set('FILE_DIR', 'GPLUS_DIR', gplus_dir)
    config.set('FILE_DIR', 'FBOOK_DIR', fbook_dir)
    config.set('FILE_DIR', 'DATA_DIR', data_dir)
    config.set('FILE_DIR', 'OUT_DIR', out_dir)
    config.set('NETKIT', 'NETKIT_DIR', netkit_dir)
    # Writing our configuration file to 'example.cfg'
    with open(computer_name + '.rfg', 'wb') as configfile:
        config.write(configfile)


def load_ranfig():
    computer_name = platform.node()
    config = cp.RawConfigParser()
    config.read(computer_name + '.rfg')
    gplus_dir = config.get('FILE_DIR', 'GPLUS_DIR')
    fbook_dir = config.get('FILE_DIR', 'FBOOK_DIR')
    data_dir = config.get('FILE_DIR', 'DATA_DIR')
    out_dir = config.get('FILE_DIR', 'OUT_DIR')
    netkit_dir = config.get('NETKIT', 'NETKIT_DIR')
    custom_dir = {'GPLUS': gplus_dir, 'FBOOK': fbook_dir, 'DATA': data_dir, 'OUT': out_dir, 'NETKIT': netkit_dir}
    return custom_dir


def main(argv):
    gplus_dir = DEFAULT_GPLUS_DIR
    fbook_dir = DEFAULT_FBOOK_DIR
    data_dir = DEFAULT_DATA_DIR
    out_dir = DEFAULT_OUT_DIR
    netkit_dir = DEFAULT_NETKIT_DIR
    try:
        opts, args = getopt.getopt(argv, "hg:f:d:o:n:", ["gfile=", "ffile=", "dfile=", "ofile=", "netkit="])
    except getopt.GetoptError:
        print('ERROR: ranfig.py -g <gplus_dir> -f <fbook_dir> -d <data_dir> -o <out_dir> -n <netkit_dir>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('ranfig.py -g <gplus_dir> -f <fbook_dir> -d <data_dir> -o <out_dir> -n <netkit_dir>')
            sys.exit()
        elif opt in ("-g", "--gfile"):
            gplus_dir = arg
        elif opt in ("-f", "--ffile"):
            fbook_dir = arg
        elif opt in ("-d", "--dfile"):
            data_dir = arg
        elif opt in ("-o", "--ofile"):
            out_dir = arg
        elif opt in ("-n", "--netkit"):
            netkit_dir = arg
    make_ranfig(gplus_dir, fbook_dir, data_dir, out_dir, netkit_dir)
    print('Fin. By rAnYKM')


if __name__ == '__main__':
    main(sys.argv[1:])
