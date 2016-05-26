#!/bin/bash

#/usr/local/bin/pocketsphinx_continuous -logfn /dev/null -samprate 8000 -hmm /home/asterisk/speech/cmusphinx-en-us-ptm-8khz-5.2 #-infile "$1"

phrases="test.phrases"
options="-logfn /dev/null -agc max -doublebw yes -samprate 8000 -hmm /home/asterisk/speech/en-us-8khz -kws $phrases"
/usr/local/bin/pocketsphinx_continuous $options -infile "$1"
