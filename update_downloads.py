#!/usr/bin/env python
"""
Uses sftp to get a directory listing from matplotlib's sourceforge
files and then generates a page of direct download links to those
files.
"""
from __future__ import print_function

import paramiko

import base64
import getpass
import io
import os
import socket
import sys
import traceback

import cPickle

# CONSTANTS
hostname = 'frs.sourceforge.net'
port = 22
project_name = 'matplotlib'
dir_template = '/home/frs/project/{0}/{0}/{0}-{{0}}'.format(project_name)


def get_versions():
    with open('downloads.txt', 'r') as fd:
        versions = [
            x.strip() for x in fd.readlines()]
    versions = [
        x for x in versions if len(x) and not x.startswith('#')]
    versions = [
        x.split(' ', 1) for x in versions]
    return versions


def get_username_and_password(hostname):
    # get username
    default_username = getpass.getuser()
    username = raw_input(
        '{0} username [{1}]: '.format(hostname, default_username))
    if len(username) == 0:
        username = default_username
    password = getpass.getpass(
        'Password for {0}@{1}: '.format(username, hostname))
    return username, password


def get_hostkey_and_type(hostname):
    # get host key, if we know one
    hostkeytype = None
    hostkey = None
    host_keys = paramiko.util.load_host_keys(
        os.path.expanduser('~/.ssh/known_hosts'))

    if hostname in host_keys:
        hostkeytype = host_keys[hostname].keys()[0]
        hostkey = host_keys[hostname][hostkeytype]

    return hostkey, hostkeytype


def get_files_for_version(sftp, version):
    sftp.chdir(dir_template.format(version))
    base_files = set(sftp.listdir())
    for folder in ('mac', 'windows'):
        try:
            base_files.remove(folder)
            sftp.chdir(dir_template.format(version) + '/' + folder)
            base_files |= set(folder + '/' + _ for _ in sftp.listdir())

        except KeyError:
            continue
    return list(base_files)


def get_file_listings(hostname, username, password, hostkey, versions):

    files = []

    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username=username, password=password, hostkey=hostkey)
        sftp = paramiko.SFTPClient.from_transport(t)

        for version, description in versions:
            version_files = get_files_for_version(sftp, version)
            version_files.sort()
            files.append((version, description, version_files))
    finally:
        t.close()

    return files


def generate_download_page(files):
    from jinja2 import Template
    with io.open("downloads.tpl.html", "r", encoding='utf-8') as fd:
        t = Template(fd.read())
    stream = t.stream(files=files)
    with io.open("downloads.html", "w", encoding='utf-8') as fd:
        stream.dump(fd)


def split_file_listing(input_list):
    source = [(_, _) for _ in input_list if 'tar' in _]
    mac = [(_, _.split('/', 1)[-1]) for _ in input_list if 'mac' in _]
    win = [(_, _.split('/', 1)[-1]) for _ in input_list if 'win' in _]
    return ('Source', source), ('Windows', win), ('OSX', mac)


def main():
    versions = get_versions()

    username, password = get_username_and_password(hostname)
    hostkey, hostkeytype = get_hostkey_and_type(hostname)

    files = get_file_listings(hostname, username,
                              password, hostkey, versions)

    files = [(a, b, split_file_listing(c)) for a, b, c in files]

    generate_download_page(files)


if __name__ == '__main__':
    main()
