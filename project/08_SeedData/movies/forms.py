from django import forms
from .models import Genre, Movie, Score

class MovieModelForm(forms.ModelForm):
    
    class Meta:
        model = Movie
        fields = ['title', 'audience', 'poster_url', 'description', 'genre']
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': "영화 제목을 입력하세요",
                }    
            ),
            'audience': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': "누적 관객수를 입력하세요",
                    'min': '0',
                }    
            ),
            'genre': forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
            'poster_url': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': "URL을 입력하세요",
                }    
            ),
            'description': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': "영화를 소개해주세요",
                }    
            ),
        }
        
class ScoreModelForm(forms.ModelForm):
    
    class Meta:
        model = Score
        fields = ['content', 'score']
        widgets = {
            'content': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': "한줄평을 써주세요",
                }    
            ),
            'score': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'type':'number',
                    'min': "0",
                    'max': '5',
                    'step': 'any',
                }    
            ),
        }