#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import argparse
import logging

from wechat.parser import WeChatDBParser
from wechat.res import Resource
from wechat.common.textutil import ensure_unicode
from wechat.render import HTMLRender
import json

logger = logging.getLogger("wechat")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='name of contact')
    parser.add_argument('--db', default='EnMicroMsg.db.decrypted', help='path to decrypted database')
    parser.add_argument('--avt', default='avatar.index', help='path to avatar.index file')
    parser.add_argument('--res', default='resource', help='reseource directory')
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = get_args()

    name = ensure_unicode(args.name)

    parser = WeChatDBParser(args.db)

    try:
        chatid = parser.get_chat_id(args.name)
    except KeyError:
        sys.stderr.write(u"Valid Contacts: {}\n".format(
            u'\n'.join(parser.all_chat_nicknames)))
        sys.stderr.write(u"Couldn't find the chat {}.".format(name));
        sys.exit(1)

    res = Resource(parser, args.res, args.avt)
    msgs = parser.msgs_by_chat[chatid]
    logger.info(f"Number of Messages for chatid {chatid}: {len(msgs)}")
    assert len(msgs) > 0

    render = HTMLRender(parser, res)
    htmls = render.render_msgs(msgs)

    all_date_strs = []
    
    for idx, pair in enumerate(htmls):
        html,date = pair
        date_str = date.strftime("%Y_%m_%d")
        all_date_strs.append(date_str)
        with open("pages/dates/" + date_str+'.html', 'w') as f:
            f.write(html)
    res.emoji_cache.flush()

    # write a file contianing all the dates found
    all_date_strs_json = json.dumps(all_date_strs,indent=2)
    with open("pages/home/home-app/src/all_dates.js","w") as f:
        f.write("const allDates = \n"+all_date_strs_json+"\nexport default allDates;")