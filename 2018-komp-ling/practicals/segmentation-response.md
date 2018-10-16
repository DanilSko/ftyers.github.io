# Sentence segmentation

## Step one: get a some random wikipedia paragraphs. 

Used this bash command (suggested by Fran) to get first 10000 par, sort them randomly and pick first 50:

`head -n 50000 WikiExtractor/wiki.txt | sort -R | head -n 50 >  input_for_segmentation/50random.txt`

## Step two: segment it with pragmatic segmenter

`ruby -I . segmenter.rb < ../../input_for_segmentation/50random.txt > ../../segmentation_results/prag_segm_result.txt`


## Step three: segment it with nltk tokenize

My most basic Python code that does sent tokenize to stdin is [here](segmentation/python_code/nltk_tokenize_from_stdin.py)

And this bash command that launches it on sample file and outputs segmentation results to results folder:

`/media/sf_share_ubuntu/github/ftyers.github.io/2018-komp-ling/practicals/segmentation$ python3 python_code/nltk_tokenize_from_stdin.py < input_for_segmentation/50random.txt > segmentation_results/nltk_punkt_results.txt`

## Step four: look at the results and compare

So, both files are here: 

[Ruby results](segmentation/segmentation_results/prag_segm_result.txt)

[Python results](segmentation/segmentation_results/nltk_punkt_results.txt)

### Pragmatic segmenter issues:
Splits intitials:

*При закладке завода присутствовал В.
 Н.
 Татищев.*

*В рукописи «Описание Уральских и Сибирских заводов. 1735 г.» В.
И.
де Геннин писал:*

Splits  н. э., т.п. and many other common short forms:

*В 107 году н.
 э.
японцы привезли в Китай 160 подданных китайского императора, которые ранее были захвачены разбойниками и проданы в Японию.*

*Прочерк (-) означает невозможность участия страны в данном межгосударственном объединении вследствие причин, не зависящих от её воли (географические, политические и т.
п.).*

### Pragmatic segmenter successes:
*Данные по состоянию на 01.01.2010.*


### NLTK issues

also failed at "т.п."

*Прочерк (-) означает невозможность участия страны в данном межгосударственном объединении вследствие причин, не зависящих от её воли (географические, политические и т.
п.).*

### NLTK successes

Handles intitials:
*При закладке завода присутствовал В. Н. Татищев.*

*В. И. де Геннин писал*

Handles some common abbreviations:

*В 107 году н. э. японцы привезли в Китай 160 подданных китайского императора, которые ранее были захвачены разбойниками и проданы в Японию.*


## Step five: calculate accuracy

TBD

# Tokenisation

Here is my implementation of maxmatch algorightm:

[dsmaxmatch](segmentation/python_code/ds_maxmatch.py)

And here is the full code that parses train file for dictionary and then applies maxmatch to the sentences from train file:

[maxmatch tokenizer] (segmentation/python_code/ds_maxmatch_tokenizer.py)


It inputs paths to three files:

1. the file to extract dictionary from
2. the file with text to tokenize
3. the output file

Example:

`$ python3 python_code/ds_maxmatch_tokenizer.py input_for_tokenisation/ja_gsd-ud-train.conllu input_for_tokenisation/ja_gsd-ud-test.conllu word_tokenisation_results/maxmatch_output.txt`

