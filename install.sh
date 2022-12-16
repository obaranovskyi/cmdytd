echo 'Installing cmdytd...'
mkdir -p ~/.config
cd ~/.config
python3 -m pip install -e git+https://github.com/obaranovskyi/cmdytd.git#egg=cmdytd
cd ~/.config/src/cmdytd
pip install -r requirements.txt
echo 'cmdytd installed'
