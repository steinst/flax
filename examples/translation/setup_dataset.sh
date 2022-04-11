my_dataset=$1
mkdir -p ~/tensorflow_datasets/
mkdir -p ~/tensorflow_datasets/${my_dataset}
cd ~/tensorflow_datasets/${my_dataset}
tfds new $my_dataset