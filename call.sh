read -p $'[?]  \033[31m\033[1mEnter The \033[37mMobile📱 Number : \n                  \033[32m' numb
termux-telephony-call $numb
sleep 3
python caller.py
