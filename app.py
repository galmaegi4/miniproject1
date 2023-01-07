from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://DoyeonKim:rlaehdus33,,@cluster0.ccp0ukt.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.miniproject1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/member')
def getmember():
    return render_template('member.html')

@app.route('/page1/<id>')
def getpage1(id):
    return render_template('page1.html')


@app.route("/page1/comment", methods=["POST"])
def comment_post():
    comment_receive = request.form['comment_give']
    id_receive = request.form['id_give']
    doc = {
        'id_num' :id_receive,
        'comment':comment_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/page1/comment/<id>", methods=["GET"])
def comment_get(id):
    data_list = list(db.comment.find({'id_num':id},{'_id':False}))
    return jsonify({'data':data_list})

@app.route("/member_list", methods=["POST"])
def member_post():
    name_receive = request.form['name_give']
    mbti_receive = request.form['mbti_give']
    blog_url_receive = request.form['blog_url_give']
    myadvantage_receive = request.form['myadvantage_give']
    mystyle_receive = request.form['mystyle_give']
    introduction_receive = request.form['introduction_give']

    member_list = list(db.member.find({},{'_id':False}))
    count = len(member_list) + 1

    doc = {
        'num': count,
        'name':name_receive,
        'mbti': mbti_receive,
        'blog_url': blog_url_receive,
        'myadvantage': myadvantage_receive,
        'mystyle': mystyle_receive,
        'introduction': introduction_receive
    }
    db.member.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})

@app.route("/page1/id", methods=["GET"])
def id_get():
    member_list = list(db.member.find({},{'_id':False}))
    return jsonify({'member':member_list})

@app.route("/page1/persnal/<id>", methods=["GET"])
def page_go(id):
    member_list = list(db.member.find({'num':int(id)},{'_id':False}))
    return jsonify({'member':member_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)