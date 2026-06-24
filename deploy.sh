#!/bin/bash
cp ~/Downloads/index.html ~/Developer/index.html
cd ~/Developer
git commit -am "update demo" && git push
echo "✅ Deployed — live in ~1 min"