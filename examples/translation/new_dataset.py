"""enps dataset."""

import csv
import os
import six

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

# TODO(enps): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(enps): BibTeX citation
_CITATION = """
"""

_LANGUAGES = ('en', 'is')
_DATA_URL = 'http://malfong.is/data/pc_initialfilter.tar.gz'

class Enps(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for enps dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(enps): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.Translation(languages=_LANGUAGES),
        supervised_keys=_LANGUAGES,
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    dl_dir = dl_manager.download_and_extract(_DATA_URL)

    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs={
                'data_file': os.path.join(dl_dir, 'enis_train.tsv')
            }),
        tfds.core.SplitGenerator(
            name=tfds.Split.VALIDATION,
            gen_kwargs={'data_file': os.path.join(dl_dir,
                                                  'enis_dev.tsv')}),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs={
                'data_file': os.path.join(dl_dir, 'enis_test.tsv')
            }),
    ]

  def _generate_examples(self, data_file):
    with tf.io.gfile.GFile(data_file) as f:
      reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
      for idx, row in enumerate(reader):
        # Everything in the row except for 'talk_name' will be a translation.
        # Missing/incomplete translations will contain the string "__NULL__" or
        # "_ _ NULL _ _".
        yield idx, {
            lang: row[lang]
            for lang in _LANGUAGES
        }

def _is_translation_complete(text):
  return text and '__NULL__' not in text and '_ _ NULL _ _' not in text
