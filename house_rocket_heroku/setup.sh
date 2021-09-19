mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"igor_queiroz17@yahoo.com.br\"\n\
               " > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml