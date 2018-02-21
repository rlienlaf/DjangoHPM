#!/bin/bash
unalias cp
shopt -s dotglob
cp -vrf skel /etc/
