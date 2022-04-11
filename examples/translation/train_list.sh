export WORKDIR=$HOME/psen_workdir;
mkdir $WORKDIR;
python3 main.py --workdir=$WORKDIR --config.reverse_translation=True > psen_30000.out;
export WORKDIR=$HOME/enps_workdir;
mkdir $WORKDIR;
python3 main.py --workdir=$WORKDIR  > enps_30000.out;
