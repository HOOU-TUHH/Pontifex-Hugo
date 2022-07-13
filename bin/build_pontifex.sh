#!/bin/bash
# run this from the basedir of the hugo folder

PONTIFEX_BASEDIR=`pwd`
# docker container will provide PONTIFEX_BIN
if [ ! -n "${PONTIFEX_BIN}" ]; then
    PONTIFEX_BIN=`pwd`/bin
fi

BUILD_DIR=${PONTIFEX_BASEDIR}/content/en/docs
INPUT_JSON="${PONTIFEX_BASEDIR}/nodes/cyto.json"
jsonconverter="python3 ${PONTIFEX_BIN}/makejson.py"
hugoconverter="python3 ${PONTIFEX_BIN}/makehugo.py"

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
  cp $i/$i.json ${BUILD_DIR}/chapter$first/$i
  cp $i.md ${BUILD_DIR}/chapter$first/
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
