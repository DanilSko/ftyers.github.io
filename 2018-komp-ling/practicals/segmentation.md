# Sentence segmentation

## Step one: get a some random wikipedia paragraphs. 

Used this bash command (suggested by Fran) to get first 10000 par, sort them randomly and pick first 50:

`head -n 50000 WikiExtractor/wiki.txt | sort -R | head -n 50 >  input_for_segmentation/50random.txt`

## Step two: segment it with pragmatic segmenter

`ruby -I . segmenter.rb < ../../input_for_segmentation/50random.txt > ../../segmentation_results/prag_segm_result.txt`


