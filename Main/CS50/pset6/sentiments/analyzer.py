import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positives = set()
        self.negatives = set()

        pFile = open(positives, 'r')

        for i in pFile:
        	if not i.startswith(';'):
          		self.positives.add(i.strip())
        pFile.close()

        nFile = open(negatives, 'r')
        
        for s in nFile:
        	if not i.startswith(';'):
        		self.negatives.add(s.strip())
        nFile.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        score = 0

        for s in tokens:
        	if s.lower() in self.positives:
        		score += 1
        	elif s.lower() in self.negatives:
        		score -= 1

        return score
