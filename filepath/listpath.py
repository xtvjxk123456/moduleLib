# coding:utf-8
import os
import sys


def folders_in_dir(dirpath):
    all = os.listdir(dirpath)
    result = []
    for x in all:
        if os.path.isdir(os.path.join(dirpath, x)):
            result.append(os.path.join(dirpath, x))
    return result


def files_in_dir(dirpath):
    all = os.listdir(dirpath)
    result = []
    for x in all:
        if os.path.isfile(os.path.join(dirpath, x)):
            result.append(os.path.join(dirpath, x))
    return result


def all_folders_in_dir(dirpath):
    tempdir = []
    for root, dirs, files in os.walk(dirpath):
        for x in dirs:
            dirname = os.path.join(root, x)
            tempdir.append(dirname)
    return tempdir


def all_files_in_dir(dirpath):
    tempfile = []
    for root, dirs, files in os.walk(dirpath):
        for x in files:
            dirname = os.path.join(root, x)
            tempfile.append(dirname)
    return tempfile
