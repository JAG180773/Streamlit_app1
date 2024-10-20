# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import streamlit as st
import pandas as pd
import numpy as np
from datetime import time
import datetime
import streamlit as st

st.title('Mi Primer Proyecto')
st.write('Hola **como** estas')
appointment = st.slider(label = 'Programe Horario de asesoria',
                        value= (time(11,30), time(12,45)))
st.write('Usted a agendado para :', appointment)
d = st.date_input( 'Fecha de cumpleaños',datetime.date(1973, 7, 6))
st.write('Tu cumpleños es:', d)
option = st.selectbox( '¿Cómo desearía ser contactado/a?', 
                      ('Email', 'Teléfono', 'Whatsapp'))
st.write('usted selecciono', option)
n = st.slider("n", 5,100, step=1)
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(chart_data)
df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)
