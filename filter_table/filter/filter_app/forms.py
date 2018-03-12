from django import forms

# Forms for filters


class users_filter(forms.Form):

    type_filter = forms.ChoiceField(widget = forms.Select(), choices = ([(None,''),('ppt','ppt'), ('pdf','pdf'),('doc','doc'),]) , initial=None , required = False)
    objective_filter = forms.ChoiceField(widget = forms.Select(), choices = ([(None,''),('Awareness','Awareness'), ('Engagement','Engagement'),('Trials','Trials')]), initial=None , required = False)
    sentiment_filter = forms.ChoiceField(widget = forms.Select(), choices = ([(None,''), ('Youth','Youth'), ('Action','Action'), ('Happiness','Happiness'),('Motherhood','Motherhood'),('Care','Care')]), initial=None , required = False)
    segment_filter = forms.ChoiceField(widget = forms.Select(), choices = ([(None,''),('AA','AA'), ('BB','BB'), ('AB','AB'),('CC','CC'),('AC','AC'),('BC','BC')]), initial = None , required=False)
