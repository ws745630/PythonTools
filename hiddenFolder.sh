#!/bin/bash
#toggle AppleShowAllFiles

current_value=$(defaults read com.apple.finder AppleShowAllFiles)
echo $current_value
if [ "$current_value" = TRUE ]
then
  defaults write com.apple.finder AppleShowAllFiles FALSE
else
  defaults write com.apple.finder AppleShowAllFiles TRUE
fi

killall Finder
