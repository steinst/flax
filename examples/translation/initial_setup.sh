sudo apt-get -y update
sudo apt-get -y install python3.8-venv
python3 -m venv venv
source venv/bin/activate
/usr/bin/python3 -m pip install --upgrade pip
export PATH=/home/steinst/.local/bin:$PATH

pip install --no-input "jax[tpu]>=0.2.21" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
pip install --no-input clu
pip install --no-input tensorflow_text
pip install --no-input sentencepiece

cd ~/flax
pip install --no-input -e .
cd examples/translation

##Ath með requirements og setja hvert um sig bara upp einu sinni, merkja við útgáfunúmer