from flask import Flask
app = Flask(__name__) #__name__ 目前執行的模組 模組?

@app.route("/") #函式的裝飾(Decorator):函式為基礎,提供附加功能 #http:127.0.0.1:5000/ 根目錄,到根目錄要回應Hello Flask,否則not found(如http:127.0.0.1:5000/test)
def home():
    return "Hello Flask"

@app.route("/test")  #http:127.0.0.1:5000/test
def test():
    return "kore wa shirenda!"

if __name__ == "__main__": #如以主程式執行(不是被import)
    app.run()  #啟動伺服器
    
#這個只是在自己網站做測試