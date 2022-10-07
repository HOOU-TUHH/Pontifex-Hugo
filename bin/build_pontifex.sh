#!/bin/bash
############################################################################
# MIT License
# 
# Copyright (c) 2022 Fabian Gabel and Julian Großmann
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#############################################################################
# run this from the basedir of the hugo folder

PONTIFEX_BASEDIR=`pwd`
# use local bin folder 
if [ ! -n "${PONTIFEX_BIN}" ]; then
    PONTIFEX_BIN=`pwd`/bin
fi
echo "Using Preprocessing routines from PONTIFEX_BIN=${PONTIFEX_BIN}"

BUILD_DIR=${PONTIFEX_BASEDIR}/content/en/docs
INPUT_JSON="${PONTIFEX_BASEDIR}/nodes/graph.json"
jsonconverter="python3 ${PONTIFEX_BIN}/build_json.py"
hugoconverter="python3 ${PONTIFEX_BIN}/build_md.py"

# Preprocessing
echo "Creating files for nodes..."
cd ${PONTIFEX_BASEDIR}/nodes
for i in ???
do 
    ## Pandoc
    mkdir -p $i
    touch $i/$i.tex #delete this line once all nodes have texfiles
    cp -f packs.tex $i/. #needed for pandoc processing
    pandoc -f latex -t html $i/$i.tex -o $i/$i-snippet.html --mathjax 
    rm -f $i/packs.tex #cleanup
    sed -i -e 's/{{&lt; baseurl &gt;}}/{{< baseurl >}}/g' $i/$i-snippet.html #needed if using HUGO Shortcodes in TeX

    ## JSON Files and HUGO
    $jsonconverter $INPUT_JSON $i > $i/$i.json
    $hugoconverter $i
done

# Copy to destination
echo "Copying files to HUGO..."
cd ${PONTIFEX_BASEDIR}/nodes
for i in ???
do
  first=${i:0:1}
  mkdir -p ${BUILD_DIR}/chapter$first/$i
  cp $i.md ${BUILD_DIR}/chapter$first/
  # copy everything but tex and html to destination
  for f in `find $i -not -name "*.tex" -not -name "*-snippet.html" -type f`
  do
    cp -f $f  ${BUILD_DIR}/chapter$first/$i
  done
done

# Run Hugo
echo "Running HUGO..."
cd ${PONTIFEX_BASEDIR}

npm install 
./node_modules/.bin/hugo/hugo

echo "Done!"
echo "Run 

docker run -it --rm --name apache-server -p 8080:80 -v \`pwd\`/public:/usr/local/apache2/htdocs/ httpd:2.4-alpine

and open up 

http://localhost:8080/

in order to view the webpage.
"
