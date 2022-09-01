from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
import pymysql
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/caijing')
def caijing():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    #sql = "select count(title) from caijing"
    sql = "select channelName,title,content from caijing"
    cur.execute(sql)
    a = cur.fetchall()
    conn.close()
    return render_template('caijing.html',a=a)

@app.route('/fangchan')
def fangchan():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from fangchan"
    cur.execute(sql)
    b = cur.fetchall()
    conn.close()
    return render_template('fangchan.html',b=b)

@app.route('/jiaoyu')
def jiaoyu():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from jiaoyu"
    cur.execute(sql)
    c = cur.fetchall()
    conn.close()
    return render_template('jiaoyu.html',c=c)

@app.route('/keji')
def keji():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from keji"
    cur.execute(sql)
    d = cur.fetchall()
    conn.close()
    return render_template('keji.html',d=d)

@app.route('/junshi')
def junshi():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from junshi"
    cur.execute(sql)
    e = cur.fetchall()
    conn.close()
    return render_template('junshi.html',e=e)

@app.route('/qiche')
def qiche():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from qiche"
    cur.execute(sql)
    f = cur.fetchall()
    conn.close()
    return render_template('qiche.html',f=f)

@app.route('/tiyu')
def tiyu():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from tiyu"
    cur.execute(sql)
    g = cur.fetchall()
    conn.close()
    return render_template('tiyu.html',g=g)

@app.route('/youxi')
def youxi():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from youxi"
    cur.execute(sql)
    h = cur.fetchall()
    conn.close()
    return render_template('youxi.html',h=h)

@app.route('/yule')
def yule():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='news', charset='utf8')
    cur = conn.cursor()
    sql = "select channelName,title,content from yule"
    cur.execute(sql)
    i = cur.fetchall()
    conn.close()
    return render_template('yule.html',i=i)

@app.route('/keshihua')
def keshihua():
    return render_template('keshihua.html')

@app.route('/ciyuntu')
def ciyuntu():
    return render_template('ciyuntu.html')

@app.route('/caijingtu')
def caijingtu():
    return render_template('caijingtu.html')

@app.route('/fangchantu')
def fangchantu():
    return render_template('fangchantu.html')

@app.route('/jiaoyutu')
def jiaoyutu():
    return render_template('jiaoyutu.html')

@app.route('/kejitu')
def kejitu():
    return render_template('kejitu.html')

@app.route('/junshitu')
def junshitu():
    return render_template('junshitu.html')

@app.route('/qichetu')
def qichetu():
    return render_template('qichetu.html')

@app.route('/tiyutu')
def tiyutu():
    return render_template('tiyutu.html')

@app.route('/youxitu')
def youxitu():
    return render_template('youxitu.html')

@app.route('/yuletu')
def yuletu():
    return render_template('yuletu.html')

@app.route('/look')
def look():
    return render_template('look.html')

if __name__ == '__main__':
    app.run(debug=True)

