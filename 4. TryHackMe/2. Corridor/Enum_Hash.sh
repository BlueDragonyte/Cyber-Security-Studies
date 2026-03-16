#!/bin/bash

for i in {0..20}
do
hash=$(echo -n $i | md5sum | awk '{print $1}')
echo "Test room $i !"
curl -s http://10.65.179.249/$hash
echo ""
done

