# NLP_visualization
A python based visualization tool for Natural Language Processing and Machine Translation

## Word Alignment Viewer 
usage: 

import alignment_view from AlignmentView

Call alignment_view with following args:

1. list of words in the source sentence (e0 ... en)

2. list of words in the target sentence (f0 ... fm)

3. dictionary of rules with this format :  "e0 ||| f0" = p(f | e)

You can also run the AlignmentView to run a unit test
