sudo apt-get -y update
sudo apt-get -y install python3.8-venv
python3 -m venv venv
source venv/bin/activate
pip install --yes --upgrade pip

pip install --yes "jax[tpu]>=0.2.21" \
    -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
pip install --yes clu
pip install --yes tensorflow_text
pip install --yes sentencepiece

git clone --depth=1 --branch=main https://github.com/google/flax
cd flax
pip install --yes -e .
cd examples/wmt
pip install --yes -r requirements.txt
