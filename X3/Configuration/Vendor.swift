//
//  Vendor.swift
//  X3
//
//  Created by 王小涛 on 2020/2/12.
//  Copyright © 2020 王小涛. All rights reserved.
//

import Foundation

enum Wechat {
    static var appKey: String {
        try! Configuration.value(for: "WechatId")
    }
    static var appSecret: String {
        try! Configuration.value(for: "WechatSecret")
    }
}
