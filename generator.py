from form_gen import Form_Gen as fg
class Generator:
    parts_of_speech = []
    noun_dict = {}
    verb_dict = {}
    adj_dict = {}
    pronoun_dict = {}
    prepositions_dict = {}
    articles_dict = {}
    adverbs_dict = {}
    numerals_dict = {}

    def add_word(self, word):
        forms = self.get_forms(word)

    def get_forms(self, word):
        return "str"
    
    def classify_words(self, words):
        parts = []
        parts.add(nouns = [], verbs = [], adjs = [],
        pronouns = [], preps = [], articles = [], adverbs = [], numerals = [])
        for word in words:
            if(word in self.noun_dict.values):
                parts.nouns.add(word)
            if(word in self.verb_dict.values):
                parts.verbs.add(word)
            if(word in self.pronoun_dict.values):
                parts.pronouns.add(word)
            if(word in self.prepositions_dict.values):
                parts.preps.add(word)
            if(word in self.articles_dict.values):
                parts.articles.add(word)
            if(word in self.adverbs_dict.values):
                parts.adverbs.add(word)
            if(word in self.numerals_dict.values):
                parts.numerals.add(word)
            if(word in self.adj_dict.values):
                parts.adjs.add(word)
        return parts
    
    def get_sentence_params(self, words_by_parts):
        return
    
    def words_in_form(self, words_by_parts, form):
        return ""
    
    def proper_grammar(self, basic_sentence):
        proper_sentence = ""
        return proper_sentence
    
    def gen_sentence(self, words):
        words_by_parts = self.classify_words(words)
        params = self.get_sentence_params(words_by_parts)
        form = fg.get_random_form(params)
        basic_sentence = self.words_in_form(words_by_parts, form)
        return self.proper_grammar(basic_sentence)




        

        
            
            
            
            




    





