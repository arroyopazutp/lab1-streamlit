
##########################################################
#######[1] PAQUETE
##########################################################
import streamlit as st
from PIL import Image
#@st.cache 
##########################################################
#######[2]FILTROS PRINCIPALES
##########################################################

image = Image.open('covid.jpg')
st.image(image, caption='',use_column_width=True)

st.title("Test de riesgo Covid-19 :sunglasses:")

html_temp = """
<div style="background-color:#26c5de;opacity: 0.80;padding:0.2 px">
<h2 style="color:white;text-align:left;">Datos personales: </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

st.write('**¿Cuál es tu edad?**')
edad= st.slider(label="",min_value=1,max_value=100,value=18,step=1)

st.write('**¿Cuál es tu genero?**')
genero= st.selectbox(label="",options=['Masculino','Femenino'],index=0,)

st.write('**¿En qué region vives?**')
region= st.selectbox(label="",options=['Lima','Lambayeque','Callao'],index=0,)

st.write('**¿En qué distrito vives?**')
distrito= st.selectbox(label="",
		options=['CHICLAYO','SJL','CALLAO','SMP','CERCADO','VILLA EL SALVADOR','ATE','BREÑA',
		         'SJM','VICTORIA','COMAS','SURCO','VMT','AGUSTINO','CHORRILLOS','JESUS MARIA',
		         'MIRAFLORES','SANTA ANITA','RIMAC','LOS OLIVOS','LA MOLINA','CARABAYLLO','PUEBLO LIBRE',
		         'SAN BORJA','SURQUILLO','SAN MIGUEL','INDEPENDENCIA','SAN ISIDRO','PUENTE PIEDRA'],index=0,)


##########################################################
#######[3]CUERPO1
##########################################################
html_temp = """
<div style="background-color:#26c5de;padding:0.2 px">
<h2 style="color:white;text-align:left;">Evaluación del nivel de exposición al Covid19: </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

st.write('**[1] ¿Sales de casa?**')
sales=st.selectbox(label="",options=['Nunca','Algunas veces','Frecuentemente'],index=0,)

st.write('**[2] ¿Has estado últimamente en una zona de riesgo como: trasporte publico,supermercados,tiendas u bancos?**')
publico=st.selectbox(label="",options=['Si','No'],index=0,)

st.write('**[3]¿Cual de estas medidas tomas al salir?**')
medidas=st.multiselect(label="Puedes seleccionar más de una:",options=['Nunca salgo','Mascarilla','Guantes','Lentes','Mameluco','Ducha al regresar'])

st.write('**[4]¿Has estado o crees haber estado en contacto directo con algún contagiado de COVID-19?**')
contacto=st.selectbox(label=" ",options=['Si','No'],index=0,)

st.write('**[5]¿Tienes algún familiar policia, militar, medico, enfermero?**')
familiar=st.selectbox(label="  ",options=['Si','No'],index=0,)

##########################################################
#######[4]CUERPO2
##########################################################

html_temp = """
<div style="background-color:#26c5de;padding:0.2 px">
<h2 style="color:white;text-align:left;">Evaluación de los síntomas </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

st.write('**[6]¿Presentas algunos de estos sintomas?**')
sintomas=st.radio(label="",options=['Ninguno','Tos seca/dolor garganta/dolor muscular','Tos con flema/dolor garganta/dolor muscular','Estornudo/mocosidad nasal/malestar corporal'],index=0,)

st.write('**[7]¿Sensación de falta de aire o dificultad para respirar aún estando en reposo?**')
aire=st.selectbox(label="     ",options=['Si','No'],index=0,)

st.write('**[8]¿Coloración azul en los labios(cianosis)?**')
labio=st.selectbox(label="      ",options=['Si','No'],index=0,)

st.write('**[9]¿Fiebre mayor a 38° persistente por más de dos días?**')
fiebre=st.selectbox(label="       ",options=['Si','No'],index=0,)

st.write('**[10]¿Desorientación y confusión?**')
confusion=st.selectbox(label="        ",options=['Si','No'],index=0,)


##########################################################
#######[5]FUNCIONES
##########################################################

##################edad
if edad < 30:
	edad = 0.01
elif edad > 29 and edad < 51:
    edad = 0.12
if edad > 50:
    edad= 0.87

##################genero
if genero == 'Masculino':
    genero = 0.7
if genero =='Femenino':
    genero= 0.3

##################region
if region == 'Lima':
	region = 0.6
if region =='Callao':
	region= 0.2
if region =='Lambayeque':
	region= 0.2
    
###################distrito

if distrito == 'SJL':
	distrito = 0.08
if distrito =='CALLAO':
	region=0.07
if distrito =='SMP':
	distrito=0.07
if distrito == 'CERCADO':
	distrito = 0.07
if distrito =='VILLA EL SALVADOR':
	region= 0.06
if distrito =='ATE':
	distrito= 0.06
if distrito == 'SJM':
	distrito = 0.05
if distrito =='VICTORIA':
	region= 0.05
if distrito =='COMAS':
	distrito= 0.04        
if distrito == 'SURCO':
	distrito = 0.04
if distrito =='VMT':
	region= 0.04
if distrito =='AGUSTINO':
	distrito= 0.04
if distrito == 'CHORRILLOS':
	distrito = 0.04
if distrito =='JESUS MARIA':
	region= 0.03
if distrito =='MIRAFLORES':
	distrito= 0.03
if distrito == 'SANTA ANITA':
	distrito = 0.03
if distrito =='RIMAC':
	region= 0.03
if distrito =='LOS OLIVOS':
	distrito= 0.02
if distrito == 'LA MOLINA':
	distrito = 0.02
if distrito =='CARABAYLLO':
	region= 0.02
if distrito =='SAN BORJA':
	distrito= 0.02
if distrito =='SURQUILLO':
	region= 0.02
if distrito =='SAN MIGUEL':
	distrito= 0.02
if distrito =='INDEPENDENCIA':
	region= 0.02
if distrito =='SAN ISIDRO':
	distrito= 0.02
if distrito =='PUENTE PIEDRA':
	region= 0.02
if distrito =='BREÑA':
	distrito= 0.01
if distrito =='PUEBLO LIBRE':
	region= 0.01
if distrito =='CHICLAYO':
	distrito= 0.08

###################sales
if sales =='Nunca':
	sales= 0.2
if sales =='Algunas veces':
	sales= 0.5
if sales =='Frecuentemente':
	sales= 0.8

###################publico
if publico =='Si':
	publico= 0.7
if publico =='No':
	publico= 0.3

###################medidas	          
medidas=1-(len(medidas)*0.2)

###################contacto
if contacto =='Si':
	contacto= 0.7
if contacto =='No':
	contacto= 0.3

###################familiar
if familiar =='Si':
	familiar= 0.6
if familiar =='No':
	familiar= 0.4

###################sintomas
if sintomas =='Ninguno':
	sintomas= 0.2      
if sintomas =='Tos seca/dolor garganta/dolor muscular':
	sintomas= 0.9
if sintomas =='Tos con flema/dolor garganta/dolor muscular':
	sintomas= 0.7
if sintomas =='Estornudo/mocosidad nasal/malestar corporal':
	sintomas= 0.5

###################aire
if aire =='Si':
	aire= 0.8
if aire =='No':
	aire= 0.2

###################labio
if labio =='Si':
	labio= 0.8
if labio =='No':
	labio= 0.2

###################fiebre
if fiebre =='Si':
	fiebre= 0.8
if fiebre =='No':
	fiebre= 0.2

###################confusion
if confusion =='Si':
	confusion= 0.8	        
if confusion =='No':
	confusion= 0.2


###################calculo contagio:
contagio=(1000000*sintomas*aire*labio*fiebre*confusion)
si=(1000000*0.9*0.8*0.8*0.8*0.8)
no=(1000000*0.2*0.2*0.2*0.2*0.2)
valor1=(contagio/si)*100

if valor1 < 30:
	contagio2 = 'Es **poco probable** que tengas Covid-19'
elif valor1 > 29 and edad < 60:
   	contagio2 ='Es **medianamente probable** que tegas Covid-19'
if valor1 >= 60:
    contagio2= 'Es **muy probable** que tengas covid-19'


###################calculo riesgo:
riesgo=(1000000*edad*genero*region*distrito*publico*medidas*contacto*familiar)
alto=(1000000*0.01*0.7*0.6*0.06*0.7*1*0.7*0.6)
bajo=(1000000*0.01*0.3*0.06*0.01*0.3*0.1*0.3*0.4)
valor2=(riesgo/alto)*100

if valor2 < 30:
	riesgo2 = 'Tienes **bajo riesgo** de contraer Covid-19'
elif valor1 > 29 and edad < 60:
   	riesgo2 ='Tienes **mediano riesgo** de contraer Covid-19'
if valor2 >= 60:
     riesgo2= 'Tienes **alto riesgo** de contraer Covid-19'

def contagio():
    return(contagio2)

def riesgo():
    return(riesgo2)

html_temp = """
<div style="background-color:#26c5de;padding:0.2px">
<h2 style="color:white;text-align:left;">Ejecuta para ver tus resultados </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

def main():
	if st.button("**EJECUTAR**"):
		result1 = contagio()
		result2 = riesgo()
		result1
		result2




st.text("-------------------------------------------------------------------------")
st.text("Laboratorio de ciencia de datos")
st.text("Konecta_Perú")


if __name__ == '__main__':
	main()
