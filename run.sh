
usage ()
{
     echo " Usage: $0 input_path output_path"
}

if [ $# -lt 2 ]; then
        usage
        exit;
fi


docker exec extractor python entrypoint.py --tmx-file $1 --output $2
