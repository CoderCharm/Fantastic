# -*- coding:utf-8 -*-
# @Author: wg
# @Time: 2019/1/7 11:11
# @Desc: 
"""

"""
from flask import request, jsonify
from app.libs.redprint import RedPrint
from app.models import db, FanTask, FanTaskDetail
from sqlalchemy import exc   # 捕获异常

from app import swagger

# from flask_restful import Resource 准备使用flask_restful的 但是不是很好加载 route 暂时不考虑
api = RedPrint('article')


@api.route('/get/list', methods=["GET"])
def get_article_list():
    """ 查询文章接口每次返回10条数据
        ---
        tags:
          - Articles API
        parameters:
          - name: page
            in: path
            type: string
            enum: 1
            required: true
            default: 1
            description: 数据起页坐标
          - name: size
            in: path
            type: string
            enum: 10
            required: true
            default: 10
            description: 每次数据长度
        responses:
          200:
            description: 返回新闻数据信息
            examples:
              data: {"code":200,"count":564,"data":[{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/80d729b556b64b8e61dce4f0ab69766a80c0782f.jpg","description":"\n\u8ffd\u8e2a\u4eba\u5de5\u667a\u80fd\u65b0\u8d8b\u52bf\uff0c\u62a5\u9053\u79d1\u6280\u884c\u4e1a\u65b0\u7a81\u7834","id":72,"nickname":"\u91cf\u5b50\u4f4d","qrcode":null},"author":"\u5173\u6ce8\u524d\u6cbf\u79d1\u6280","content_url":"http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247512013&idx=1&sn=fd0dde1e1c7aabc5ee659eb77a8d3da1&chksm=e8d018bfdfa791a9bf1deee6db4b775e5f9eb6cfd27912cca5670eb04812f79477385402ac00&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/31e31e8d140c6b8f7593c60690b7be84e5be3ecd.jpg","digest":"\u8fd9\u4e0d\u8bef\u4eba\u7ec8\u8eab\u5417\uff1f","id":11312,"md5_url":"0a777a259617d75d2aa8b884cdb01a4d","published_at":"2019-01-07T12:59:20","title":"\u62a5\u540d\u5173\u53e3\u5b95\u673a\uff01\u5784\u65ad\u6027App\u60f9\u601270\u4e07\u827a\u8003\u751f\uff0c\u4e70589\u5143VIP\u901a\u9053\u4e5f\u5f92\u52b3","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/ee078da8c0faf3a4a045eae1e2d248bf69ef40bc.jpg","description":"\n\u4e13\u4e1a\u7684\u4e2d\u6587\u00a0IT\u00a0\u6280\u672f\u793e\u533a\uff0c\u4e0e\u5343\u4e07\u6280\u672f\u4eba\u5171\u6210\u957f\u3002","id":204,"nickname":"CSDN","qrcode":null},"author":"\u80e1\u5dcd\u5dcd\u00a0\u6574\u7406","content_url":"http://mp.weixin.qq.com/s?__biz=MjM5MjAwODM4MA==&mid=2650711874&idx=1&sn=86f2e9aeac90fcede2d9060e94868f27&chksm=bea6d69189d15f873df1cba501fb8f70947afb7a77d44a92c51f3ef2d3b727a36af945e60ec2&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/c8d9a39e75bfe3344ad183bf6b1cd955948b8ea5.jpg","digest":"\u585e\u7fc1\u5931\u9a6c\uff0c\u7109\u77e5\u975e\u798f\u3002","id":11249,"md5_url":"48c6c23da14db5570e190a62f5902e34","published_at":"2019-01-07T11:49:52","title":"Java\u00a0JDK\u00a0\u6536\u8d39\uff0cAndroid\u00a0\u4e5f\u5750\u4e0d\u4f4f\u4e86\uff0c\u7a0b\u5e8f\u5458\u4eec\u8be5\u548b\u529e\uff1f","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/d2e2486790660c00f13b844652c10b06b0848407.jpg","description":"\u9762\u5411AI\u7231\u597d\u8005\u3001\u5f00\u53d1\u8005\u548c\u79d1\u5b66\u5bb6\uff0c\u63d0\u4f9bAI\u9886\u57df\u6280\u672f\u8d44\u8baf\u3001\u4e00\u7ebf\u4e1a\u754c\u5b9e\u8df5\u6848\u4f8b\u3001\u641c\u7f57\u6574\u7406\u4e1a\u754c\u6280\u672f\u5206\u4eab\u5e72\u8d27\u3001AI\u8bba\u6587\u89e3\u8bfb\u3002\u6bcf\u5468\u4e00\u8282\u6280\u672f\u5206\u4eab\u516c\u5f00\u8bfe\uff0c\u52a9\u529b\u4f60\u5168\u9762\u62e5\u62b1\u4eba\u5de5\u667a\u80fd\u6280\u672f\u3002","id":2308,"nickname":"AI\u524d\u7ebf","qrcode":"https://open.weixin.qq.com/qr/code?username=gh_b7682654f4a3"},"author":"AI\u524d\u7ebf\u5c0f\u7ec4","content_url":"http://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA==&mid=2247494684&idx=1&sn=3ae6cb7bbf0e829148580fda0b318d60&chksm=fbea55d3cc9ddcc57d256c880ce95e5384fe2f9bdeb99572059c6bd931269e3ce4159932f7cf&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/9f4e3a7e884029f39ab7d481b000360eddc5a8e9.jpg","digest":"\u591a\u79cd\u8ba1\u7b97\u67b6\u6784\u7684\u7ec4\u5408\u662f\u5b9e\u73b0\u6700\u4f18\u6027\u80fd\u8ba1\u7b97\u7684\u5fc5\u7136\u9009\u62e9","id":12064,"md5_url":"d72d94652a1d117e285445e0a08b12a4","published_at":"2019-01-07T11:22:20","title":"\u534e\u4e3a\u53d1\u5e03\u5168\u65b0\u9cb2\u9e4f920\u82af\u7247\uff0c\u6027\u80fd\u6253\u7834\u65b0\u7eaa\u5f55\uff01","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/d326c855f597c70608c0675aedfc589cc85d982e.jpg","description":"\n\u7528\u6781\u5ba2\u89c6\u89d2\uff0c\u8ffd\u8e2a\u4f60\u6700\u4e0d\u53ef\u9519\u8fc7\u7684\u79d1\u6280\u5708\u3002\u6709\u5feb\u95fb\u3001\u4e5f\u6709\u6d1e\u89c1\uff1b\u6709\u8111\u6d1e\u3001\u4e5f\u6709\u601d\u8003\u3002","id":60,"nickname":"\u6781\u5ba2\u516c\u56ed","qrcode":null},"author":"\u5b8b\u5fb7\u80dc","content_url":"http://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2652859797&idx=1&sn=3fe2ca5317149df52ea2922f79f33113&chksm=7e6a1023491d9935c985c18921469d44b7259fd0ba25a95953045650207813f9b9bd98d11588&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/ee3020b362f0885b32000311929457c59b9b897c.jpg","digest":"\u4eca\u5929\u7684\u521b\u4e1a\u8005\u8be5\u5982\u4f55\u4ece\u4e92\u8054\u7f51\u9769\u547d\u7684\u65f6\u4ee3\u6c72\u53d6\u7ecf\u9a8c\uff1f","id":11323,"md5_url":"54b44585f1c9589d60fbe9cc371ca398","published_at":"2019-01-06T21:30:00","title":"\u8bb0\u5f55\u4e92\u8054\u7f51\u9769\u547d\u7684\u300a\u8fde\u7ebf\u300b\uff0c\u548c\u5439\u54cd\u53f7\u89d2\u7684\u7f57\u585e\u6258\u3021IF19\u00a0\u5c01\u9762\u6545\u4e8b","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/c97921f07fee5fd285adc8947ae61176e0a1e1f2.jpg","description":"\n\u6da8\u7c89\u3001\u53d8\u73b0\u3001\u8fd0\u8425\u3001\u89c2\u5bdf\uff0c\u65b0\u699c\u7ed9\u4f60\u4e0d\u4e00\u6837\u7684\u65b0\u601d\u8def\u3002\u65b0\u699c\u2014\u2014\u5185\u5bb9\u521b\u4e1a\u670d\u52a1\u5e73\u53f0\uff0cwww.newrank.cn","id":110,"nickname":"\u65b0\u699c","qrcode":null},"author":"newrank","content_url":"http://mp.weixin.qq.com/s?__biz=MzAwMjE1NjcxMg==&mid=2654672316&idx=1&sn=8b8350b793a3f8e288b7f55ddd614362&chksm=8101047bb6768d6d229c3c604372cd0467d479f3bbbe33664442aa5483ba361b99a626b3c26b&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/228bda8506c3ebadfb389c313eb7c202ab296d86.jpg","digest":"\u8fd9\u4efd\u62a5\u544a\u4ee52018\u5e74\u4f20\u64ad\u529b\u6700\u5f3a\u7684500\u4e2a\u5fae\u4fe1\u516c\u4f17\u53f7\u4e3a\u7740\u773c\u70b9\uff0c\u89c2\u5bdf\u6574\u4e2a\u5fae\u4fe1\u516c\u4f17\u5e73\u53f0\u7684\u53d8\u5316\u3002\u6211\u4eec\u5c06\u4ece\u5e73\u53f0\u53d8\u8fc1\u3001\u5185","id":11872,"md5_url":"24440ac44649b3c8c2e62173ab750764","published_at":"2019-01-06T21:04:07","title":"2018\u5e74\u4e2d\u56fd\u5fae\u4fe1500\u5f3a\u5e74\u62a5\u00a0|\u00a0\u65b0\u699c\u51fa\u54c1","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/81d96bd0079afa419b210174cdc7526b823b43db.jpg","description":"\nInfoQ\u5927\u524d\u7aef\u6280\u672f\u793e\u7fa4\uff1a\u56ca\u62ec\u524d\u7aef\u3001\u79fb\u52a8\u3001Node\u5168\u6808\u4e00\u7ebf\u6280\u672f\uff0c\u7d27\u8ddf\u4e1a\u754c\u53d1\u5c55\u6b65\u4f10\u3002","id":154,"nickname":"\u524d\u7aef\u4e4b\u5dc5","qrcode":null},"author":"\u524d\u7aef\u4e4b\u5dc5","content_url":"http://mp.weixin.qq.com/s?__biz=MzUxMzcxMzE5Ng==&mid=2247490230&idx=1&sn=7c407256e1d144631ea143f593311153&chksm=f951aff5ce2626e3c362361ac5473dcc231ffee12c8e5e9e34fd5b9b664b2cce3122b517e992&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/ef56328dc79ee3835ed186b79a00295b05d44a97.jpg","digest":"\u4f60\u4e0d\u77e5\u9053\u7684\u6027\u80fd\u4f18\u5316","id":10854,"md5_url":"857a0ddd10fe8b9e29aae59ee55ca76d","published_at":"2019-01-06T19:03:55","title":"JavaScript\u6027\u80fd\u4f18\u5316\u4e4b\u6447\u6811","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/0d97ef1829a3765911c3fc7383c4102ced268ade.jpg","description":"\n\u521b\u4e1a\u90a6\u6210\u7acb\u4e8e2007\u5e74\uff0c\u662f\u5168\u7ef4\u5ea6\u521b\u4e1a\u8005\u670d\u52a1\u5e73\u53f0\uff0c\u516c\u53f8\u53ca\u76f8\u5173\u57fa\u91d1\u5148\u540e\u83b7\u5f97IDG\u3001\u7ea2\u6749\u3001\u5317\u6781\u5149\u3001\u8d5b\u5bcc\u3001\u542f\u8d4b\u7b49\u56fd\u5185\u5916\u6295\u8d44\u673a\u6784\u6295\u8d44\uff0c\u4e3a\u521b\u4e1a\u8005\u63d0\u4f9b\u8de8\u5e73\u53f0\u5a92\u4f53\u3001\u4f1a\u5c55\u3001\u57f9\u8bad\u3001\u5b75\u5316\u7a7a\u95f4\u3001\u5929\u4f7f\u57fa\u91d1\u5168\u65b9\u4f4d\u670d\u52a1\u3002","id":227,"nickname":"\u521b\u4e1a\u90a6","qrcode":null},"author":"\u5927\u6e7f\u5144Felix","content_url":"http://mp.weixin.qq.com/s?__biz=MjM5OTAzMjc4MA==&mid=2650090241&idx=1&sn=e820264bcb9d9b957b50a99a942b64e4&chksm=bec029a289b7a0b47626d3d2f79b00e74982cba1b4568008aceb9eb2100a3af8beb8e9a7671b&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/2ab8ce7f6e7ee39d00f93a3c8c5e25bedbfa0e99.jpg","digest":"\u6709\u94b1\u4eba\u7684\u70e6\u607c","id":11930,"md5_url":"91fa3eca0f12e6d5b96a0427d094e60e","published_at":"2019-01-06T16:14:46","title":"\u300a\u5927\u9ec4\u8702\u300b\u80cc\u540e\u7684\u7537\u4eba\uff1a\u201c\u7f8e\u7248\u738b\u601d\u806a\u201d\uff0c\u5931\u8d25\u4e86\u5c31\u56de\u53bb\u7ee7\u627f\u5343\u4ebf\u5bb6\u4ea7","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/7bb257ee9e619a53239893d765814d3a68e1adb9.jpg","description":"\n\u805a\u5408\u4f18\u8d28\u7684\u521b\u65b0\u4fe1\u606f\u548c\u4eba\u7fa4","id":201,"nickname":"\u864e\u55c5APP","qrcode":null},"author":"\u5218\u7136","content_url":"http://mp.weixin.qq.com/s?__biz=MTQzMjE1NjQwMQ==&mid=2655553509&idx=1&sn=b57fdc07c78ae25b019f2a1bcc6050b8&chksm=66df287b51a8a16d462160bcd9adb9c743147b18e908e4283e76a85e67ba6932ceaa3fdd5ac1&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/754a7219ca9d48ae47c23fd82f2fcc6ff94c147b.jpg","digest":"\u70ed\u95f9\u4e14\u5148\u77a7\u7740\uff0c\u4e1c\u5357\u4e9a\u8fd9\u7247\u571f\u5730\u5230\u5e95\u4f1a\u4e0d\u4f1a\u7ed9\u8db3\u4e2d\u56fd\u5de8\u5934\u4eec\u9762\u5b50\uff0c\u5c31\u518d\u8bf4\u4e86","id":10887,"md5_url":"ef8f48893f7b039196412fba2b67840f","published_at":"2019-01-06T13:16:15","title":"\u963f\u91cc\u817e\u8baf\u4eec\u5728\u4e1c\u5357\u4e9a\u7684\u590d\u5236\u7c98\u8d34\u6e38\u620f","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/80d729b556b64b8e61dce4f0ab69766a80c0782f.jpg","description":"\n\u8ffd\u8e2a\u4eba\u5de5\u667a\u80fd\u65b0\u8d8b\u52bf\uff0c\u62a5\u9053\u79d1\u6280\u884c\u4e1a\u65b0\u7a81\u7834","id":72,"nickname":"\u91cf\u5b50\u4f4d","qrcode":null},"author":"\u5173\u6ce8\u524d\u6cbf\u79d1\u6280","content_url":"http://mp.weixin.qq.com/s?__biz=MzIzNjc1NzUzMw==&mid=2247511922&idx=1&sn=cdeb0fe33e4ffd364cd8c274571ef8e3&chksm=e8d01800dfa791167a64229d6fa38586acbc664a1b01d0c670ba09f0df1cf2a4559c6a6dc6f6&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/0722cf494fdc26dfe8bd159b908f2f11b5075528.jpg","digest":"\u5f00\u4e1a8\u5e74\uff0c0\u5dee\u8bc4~","id":11313,"md5_url":"c4400da1f1b399f790ea3391c0e275dc","published_at":"2019-01-06T12:17:20","title":"\u7f8e\u56fd\u7f51\u763e\u6212\u9664\u4e2d\u5fc3\uff1a\u6ca1\u6709\u7535\u51fb\u3001\u9694\u7eddWiFi\uff0c\u6cbb\u4e00\u6b2118\u4e07\u5143","top":0},{"account":{"avatar":"http://duweixin.oss-cn-beijing.aliyuncs.com/e22dbb9947d65f1e80d0774dac042eaf6df2a651.jpg","description":"\n\u6709\u5185\u5bb9\u7684\u6280\u672f\u793e\u533a\u5a92\u4f53","id":89,"nickname":"InfoQ","qrcode":null},"author":"\u671b\u4eac\u4e00\u54e5\u5c0f\u667a","content_url":"http://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651012453&idx=1&sn=5aa8355f1ba86ab346c3d7910c91791b&chksm=bdbec5368ac94c20544c7258e0fc64e9ace4943e0182a6224cbe5b0dd03966b4307778b351a2&scene=27#wechat_redirect","copyright_stat":11,"cover":"http://duweixin.oss-cn-beijing.aliyuncs.com/46401ac95baad5d9d291b2008f35b2302d4c7d39.jpg","digest":"\u5982\u679c\u7528\u4e00\u53e5\u8bdd\u5f62\u5bb9\u4f60\u7684\u00a02018\uff0c\u4f1a\u662f\u4ec0\u4e48\uff1f\u5982\u679c\u7528\u4e00\u53e5\u8bdd\u9884\u6d4b\u4f60\u7684\u00a02019\uff0c\u53c8\u4f1a\u662f\u4ec0\u4e48\uff1f","id":10723,"md5_url":"de1d512dc11c8ccb21362d2c33540e54","published_at":"2019-01-06T10:31:55","title":"\u7a0b\u5e8f\u54582018\u5e74\u5ea6\u4ee3\u7801\u62a5\u544a\uff0c\u53e5\u53e5\u6233\u5fc3","top":0}],"msg":"success","page":2,"size":10}
        """
    return jsonify({"param": request.args.get("time_stamp")})


@api.route('/get/detail', methods=["GET"])
def get_article_detail():
    """
    获取文章详情
    :return:
    """
    return jsonify({"param": request.args.get("article_id")})


@api.route('/del', methods=["DELETE"])
def del_article():
    """
    删除文章
    :return:
    """
    return "success"


@api.route('/add', methods=["POST"])
def add_article():
    """
    添加文章
    :return:
    """
    t_author = request.form.get("t_author")
    t_title = request.form.get("t_title")
    t_desc = request.form.get("t_desc")
    t_image = request.form.get("t_image")
    t_url = request.form.get("t_url")
    t_key = request.form.get("t_key")
    article_type = request.form.get("article_type")
    task_content = request.form.get("t_content")

    article_list = FanTask(
        t_author=t_author,
        t_title=t_title,
        t_desc=t_desc,
        t_image=t_image,
        t_url=t_url,
        t_key=t_key,
        article_type=article_type
    )

    try:
        db.session.add(article_list)
        db.session.commit()
        article_detail = FanTaskDetail(task_id=article_list.task_id, task_content=task_content)
        db.session.add(article_detail)
        db.session.commit()
        return jsonify({"res": 1, "msg": "Success"})
    except exc.SQLAlchemyError:
        db.session.rollback()
        return jsonify({"res": -1, "msg": "Error"})


