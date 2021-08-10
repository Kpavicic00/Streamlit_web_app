from pyngrok import ngrok 
#!ngrok authtoken 1wXf3Exs5GAIItmvzc78opoccae_7bBfKbRjBS69P6njkpdmX
#nohup streamlit run app.py & 

url = ngrok.connect(port = 8501)
url #generates our URL

#!streamlit run --server.port 80 app.py >/dev/null