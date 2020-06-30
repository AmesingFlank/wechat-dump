#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import logging
from wechat.parser import WeChatDBParser
from wechat.common.textutil import safe_filename  #generate a safe name for contacts with weird names. not used
import sys, os

logger = logging.getLogger("wechat")

if __name__ == '__main__':
    
    db_file = "EnMicroMsg.db.decrypted"
    target_name = sys.argv[1]
    output_file = sys.argv[2]
    
    
    parser = WeChatDBParser(db_file)

    for chatid, msgs in parser.msgs_by_chat.items():
        name = parser.contacts[chatid]
        if name != target_name:
            continue
        if len(name) == 0:
            logger.info(f"Chat {chatid} doesn't have a valid display name.")
            name = str(id(chatid))
        logger.info(f"Writing msgs for {name}")
        
        
        with open(output_file, 'w') as f:
            for m in msgs:
                f.write(str(m))
                f.write("\n")

        print("Done writing")
        break