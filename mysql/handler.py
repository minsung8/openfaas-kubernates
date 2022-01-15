import pymysql


def handle(req):

    ret = []
    db = pymysql.connect(host='localhost', user='local', db='storelink_vaccumator', password='local1234', charset='utf8')
    curs = db.cursor()

    return 'success'
    # sql = "select * from community_ppomppu_board;"
    # curs.execute(sql)
    #
    # rows = curs.fetchall()
    # for e in rows:
    #     temp = {'id': e[0],
    #             'created_at': e[1],
    #             'updated_at': e[2],
    #             'board_id': e[3]}
    #     ret.append(temp)
    #
    # db.commit()
    # db.close()
    # return ret
