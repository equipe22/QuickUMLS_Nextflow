basedir=`pwd`
echo $basedir
docker run -it -v $basedir/data/:/home/quickumls/tmp \
    -v $basedir/src:/home/quickumls/src \
 --network annotations quickumls-democlient-hegp bash
