# Sentence segmentation

## Step one: get a some random wikipedia paragraphs. 

Used this bash command (suggested by Fran) to get first 10000 par, sort them randomly and pick first 50:

`head -n 50000 WikiExtractor/wiki.txt | sort -R | head -n 50 >  input_for_segmentation/50random.txt`

## Step two: segment it with pragmatic segmenter

`ruby -I . segmenter.rb < ../../input_for_segmentation/50random.txt > ../../segmentation_results/prag_segm_result.txt`


## Setp three: segment it with nltk tokenize

My most basic Python code that does sent tokenize to stdin is [here](/segmentation/python_code/nltk_tokenize_from_stdin.py)

And this bash command that launches it on sample file and outputs segmentation results to results folder:

`/media/sf_share_ubuntu/github/ftyers.github.io/2018-komp-ling/practicals/segmentation$ python3 python_code/nltk_tokenize_from_stdin.py < input_for_segmentation/50random.txt > segmentation_results/nltk_punkt_results.txt`


