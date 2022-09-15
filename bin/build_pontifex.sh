#!/bin/bash
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
  for f in `find $i -not -name "*.tex" -not -name "*.html" -type f`
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
