#!/bin/bash
#
# Copyright (c) 2023 @weigefenxiang
#

NUM=0
GITHUB_ENV=$1
#1.0	stock（非108M 原厂Uboot）
export VanillaFILENAME=$SERIAL'.'$NUM'-360T7-'$NAME
export VanillaBIN=$VanillaFILENAME'-BIN'
export VanillaFACTORY=$VanillaFILENAME'-factory'
export VanillaSYSUPGRADE=$VanillaFILENAME'-sysupgrade'

echo "VanillaBIN=$VanillaBIN" >> $GITHUB_ENV
echo "VanillaFACTORY=$VanillaFACTORY" >> $GITHUB_ENV
echo "VanillaSYSUPGRADE=$VanillaSYSUPGRADE" >> $GITHUB_ENV

export NUM=$((NUM+1))

#1.1	108M
export FILENAME=$SERIAL'.'$NUM'-360T7-108M-'$NAME
export BIN=$FILENAME'-BIN'
export FACTORY=$FILENAME'-factory'
export SYSUPGRADE=$FILENAME'-sysupgrade'

#echo "FILENAME=$FILENAME" >> $GITHUB_ENV
echo "BIN=$BIN" >> $GITHUB_ENV
echo "FACTORY=$FACTORY" >> $GITHUB_ENV
echo "SYSUPGRADE=$SYSUPGRADE" >> $GITHUB_ENV
export NUM=$((NUM+1))

#1.2	ttyd+filetransfer
export mini_NAME=$SERIAL'.'$NUM'-360T7-108M-'$NAME'-mini'
export mini_BIN=$mini_NAME'-BIN'
export mini_FACTORY=$mini_NAME'-factory'
export mini_SYSUPGRADE=$mini_NAME'-sysupgrade'

# echo "mini_NAME=${mini_NAME}" >> $GITHUB_ENV	
echo "mini_BIN=${mini_BIN}" >> $GITHUB_ENV
echo "mini_FACTORY=${mini_FACTORY}" >> $GITHUB_ENV
echo "mini_SYSUPGRADE=${mini_SYSUPGRADE}" >> $GITHUB_ENV
export NUM=$((NUM+1))

#1.3	 ssrplus
export ssrplus_NAME=$SERIAL'.'$NUM'-360T7-108M-'$NAME'-ssrplus'
export ssrplus_BIN=$ssrplus_NAME'-BIN'
export ssrplus_FACTORY=$ssrplus_NAME'-factory'
export ssrplus_SYSUPGRADE=$ssrplus_NAME'-sysupgrade'

echo "ssrplus_BIN=${ssrplus_BIN}" >> $GITHUB_ENV
echo "ssrplus_FACTORY=${ssrplus_FACTORY}" >> $GITHUB_ENV
echo "ssrplus_SYSUPGRADE=${ssrplus_SYSUPGRADE}" >> $GITHUB_ENV
export NUM=$((NUM+1))

#1.4	passwall
export passwall_NAME=$SERIAL'.'$NUM'-360T7-108M-'$NAME'-passwall'
export passwall_BIN=$passwall_NAME'-BIN'
export passwall_FACTORY=$passwall_NAME'-factory'
export passwall_SYSUPGRADE=$passwall_NAME'-sysupgrade'

echo "passwall_BIN=${passwall_BIN}" >> $GITHUB_ENV
echo "passwall_FACTORY=${passwall_FACTORY}" >> $GITHUB_ENV
echo "passwall_SYSUPGRADE=${passwall_SYSUPGRADE}" >> $GITHUB_ENV
export NUM=$((NUM+1))

#1.5	openclash
export openclash_NAME=$SERIAL'.'$NUM'-360T7-108M-'$NAME'-openclash'
export openclash_BIN=$openclash_NAME'-BIN'
export openclash_FACTORY=$openclash_NAME'-factory'
export openclash_SYSUPGRADE=$openclash_NAME'-sysupgrade'

echo "openclash_BIN=${openclash_BIN}" >> $GITHUB_ENV
echo "openclash_FACTORY=${openclash_FACTORY}" >> $GITHUB_ENV
echo "openclash_SYSUPGRADE=${openclash_SYSUPGRADE}" >> $GITHUB_ENV
export NUM=$((NUM+1))

#1.6	openclash_ssrplus_passwall
export openclash_ssrplus_passwall_NAME=$SERIAL'.'$NUM'-360T7-108M-'$NAME'-openclash-ssrplus-passwall'
export openclash_ssrplus_passwall_BIN=$openclash_ssrplus_passwall_NAME'-BIN'
export openclash_ssrplus_passwall_FACTORY=$openclash_ssrplus_passwall_NAME'-factory'
export openclash_ssrplus_passwall_SYSUPGRADE=$openclash_ssrplus_passwall_NAME'-sysupgrade'

echo "openclash_ssrplus_passwall_BIN=${openclash_ssrplus_passwall_BIN}" >> $GITHUB_ENV
echo "openclash_ssrplus_passwall_FACTORY=${openclash_ssrplus_passwall_FACTORY}" >> $GITHUB_ENV
echo "openclash_ssrplus_passwall_SYSUPGRADE=${openclash_ssrplus_passwall_SYSUPGRADE}" >> $GITHUB_ENV
export NUM=$((NUM+1))
		  
echo "FILENAME： $FILENAME" 
echo "BIN： $BIN" 
echo "FACTORY： $FACTORY" 
echo "SYSUPGRADE： $SYSUPGRADE"
echo "VanillaFILENAME： $VanillaFILENAME"
echo "VanillaBIN： $VanillaBIN"
echo "VanillaFACTORY： $VanillaFACTORY" 
echo "VanillaSYSUPGRADE： $VanillaSYSUPGRADE" 

echo "NUM=$NUM" >> $GITHUB_ENV
export GITHUB_ENV
