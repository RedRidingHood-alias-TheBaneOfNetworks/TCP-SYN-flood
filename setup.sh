#! /bin/bash

echo ""
echo "installing dependencies :"
echo "-------------------------"
echo ""

sudo pip install colorama && sudo pip install scapy

echo ""
echo "updating your system :"
echo "----------------------"
echo ""

v=sudo apt-get update && sudo apt-get dist-upgrade
$v
