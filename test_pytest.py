import pytest
import pickle
from app import show_recommended_crop
from random import randint

# Importamos el DataFrame
with open('pickle_objects/df.pickle', 'rb') as f:
    df = pickle.load(f)

# Creamos un generador con los nombres de los cultivos y otro con los parámetros de la primera
# instancia de cada cultivo
crop_label = (label for label in df['label'].unique())
parameters = (df[df['label']==label].iloc[randint(0,99)][df.columns[:-1]].to_list() for label in df['label'].unique())

def test_rice():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_maize():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_chickpea():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_kidneybeans():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_pigeonpeas():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_mothbeans():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_mungbean():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_blackgram():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_lentil():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_pomegranate():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_banana():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_mango():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_grapes():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_watermelon():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_muskmelon():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_apple():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_orange():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_papaya():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_coconut():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_cotton():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_jute():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())
def test_coffee():
    assert crop_label.__next__() == show_recommended_crop(*parameters.__next__())

if __name__ == '__main__':
    pytest.main(['test_pytest.py'])