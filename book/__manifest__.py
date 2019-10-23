# -*- coding: utf-8 -*-
{
    'name': "book",

    'summary': """
        图书管理系统""",

    'description': """
        用户能够查看系统中的图书，kanban显示图片和名称等信息
        若没有用户想要的图书，用户可以填写申购单
        管理员可以查看所有申购，并将申购单转化为系统书籍
    """,

    'author': "andy",
    'website': "http://www.wffeitas.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    'demo': [
        # 'demo/demo.xml',
    ],
}