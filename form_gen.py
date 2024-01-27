import random
class Form_Gen: 

    
    possible_sentence_forms = []

    def find_possible_sentence_forms():
        return

    def ret_possible_sentence_forms(self):
        return self.possible_sentence_forms
    
    def satisfies_parameters(self, parameters, form):
        return
    
    def get_random_form(self, parameters):
        valid_forms = []
        for form in self.possible_sentence_forms:
            if(self.satisfies_parameters(parameters, form)):
                valid_forms.add(form)
        
        return valid_forms[random.randint(valid_forms.len)]

