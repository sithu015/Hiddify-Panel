#!/usr/bin/env bash
#previous_release=$(curl --silent "https://api.github.com/repos/hiddify/HiddifyPanel/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")')
pip install lastversion
previous_release=$(lastversion --at pip hiddifypanel)
current=$(cat hiddifypanel/VERSION)
gitchangelog "${previous_release}..$current"