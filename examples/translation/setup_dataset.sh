my_dataset=$1
mkdir -p ~/tensorflow_datasets/
mkdir -p ~/tensorflow_datasets/${my_dataset}
cd ~/tensorflow_datasets/${my_dataset}
tfds new $my_dataset

#skipta út skriftu

tfds build

export WORKDIR=$HOME/pc_initialfilter_workdir
mkdir $WORKDIR

#stilla config skrá
nohup python3 main.py --workdir=$WORKDIR > nohup_10000.out &
