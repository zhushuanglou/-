# -*- coding: utf-8 -*-

#导入包
from odoo import models, fields, api

# 创建一个叫book_manage的类
# 创建一个叫book.manage的模型
class book_manage(models.Model):
    _name = 'book.manage'

#创建四个字段，name与author是必填字段
    name = fields.Char(string='名称',required=True)
    author = fields.Char(string='作者',required=True)
    price = fields.Float(string='价格')
    picture = fields.Binary(string='上传图片')

# 创建一个叫book_manage的类
# class book_manage(models.Model):
#     # 创建一个叫book.manage的模型
#     _name = 'book.manage'
#
#     name = fields.Char(string='名称',required=True)
#     author = fields.Char(string='作者',require=True)
#
#     price = fields.Float(string='价格')
#     picture = fields.Binary(string='上传图片')
#
# #创建一个叫book_sub的类
# #创建一个叫book.sub的模型
# class book_sub(models.Model):
#     _name = 'book.sub'
#
# #创建5个字段，name与author是必填字段
#     name = fields.Char(string='名称',required=True)
#     author = fields.Char(string='作者',required=True)
#     price = fields.Float(string='价格')
#     picture = fields.Binary(string='上传图片')
#     state = fields.Selection([('draft','草稿'),('done','完成')],string="状态",default="draft")
#
# #定义btn_submit方法，方法的作用是将当前的state的状态变成done
#     @api.one
#     def btn_submit(self):
#         self.state='done'
#
# #定义btn_ver方法
#     @api.multi
#     def btn_ver(self):
# #创建vals，将当前页面的数据传递给vals
#         vals={
#             'name': self.name,
#             'author':self.author,
#             'price':self.price,
#             'picture':self.picture,
#         }
# #在模型book.manage里创建vals
#         self.env['book.manage'].create(vals)
# #把当前页面的数据删除
#         self.unlink()

# 名称 作者 价格 上传图品    [('draft','草稿'),('done','完成')],string="状态",default="draft"
# class book_manage(models.Model):
#
#     name = fields.Char(string='名称',required=True)
#
#     author = fields.Char(string='作者',required=True)
#
#     price = fields.Char(string='价格')
#
#     picture = fields.Binary(string='上传图片')
#
#     state = fields.Selection([('draft','草稿'),('done','完成')],string='状态',default='draft')


class book_sub(models.Model):
    _name = 'book.sub'
    name = fields.Char(string='名称',required = True)
    author = fields.Char(string='作者',required = True)
    price = fields.Float(string='价格')
    picture = fields.Binary(string='上传图片')
    '''state的Selection为多选字段，后面的string和name  author一样都有string属性，default = “draft”  默认选中的为draft'''
    state = fields.Selection([('draft','草稿'),('done','完成')],string='状态',default = "draft")
#     该方法将state的状态改为done
    @api.one
    def btn_sumit(self):
        self.state = "done"

    @api.multi
    def btn_ver(self):
#         创建vals，将当前页面的数据传递给vals
        vals = {'name':self.name,
                'author':self.author,
                'price':self.price,
                'picture':self.picture,
                }
  # 环境储存了模型的缓存记录集，因此我们可以通过环境来获取、增加、修改、删除记录，而触发数据库更改，从而达到操作数据库的目的。
  #   例如：新增一条记录
  #      '''self.env['模型'].create(vals)'''
        self.evn['book.manage'].create(vals)
#把当前页面的数据删除          删除在当前book_sub创建的 vals,这个vals是属于book.manage模型的对象
        self.unlink()

    # @api.multi
    # def btn_ver(self):
    #     vals = {'name':self.name,
    #             'author':self.auth,
    #             'price':self.price,
    #             'picture':self.picture
    #             }
    #     self.env['book.manage'] = vals

# # -*- coding: utf-8 -*-
#
# # 导入包
# from odoo import models, fields, api
#
#
# # 创建一个叫book_manage的类
# # 创建一个叫book.manage的模型
# class book_manage(models.Model):
#     _name = 'book.manage'
#
#     # 创建四个字段，name与author是必填字段
#     name = fields.Char(string='名称', required=True)
#     author = fields.Char(string='作者', required=True)
#     price = fields.Float(string='价格')
#     picture = fields.Binary(string='上传图片')
#
#
# # 创建一个叫book_sub的类
# # 创建一个叫book.sub的模型
# class book_sub(models.Model):
#     _name = 'book.sub'
#
#     # 创建5个字段，name与author是必填字段
#     name = fields.Char(string='名称', required=True)
#     author = fields.Char(string='作者', required=True)
#     price = fields.Float(string='价格')
#     picture = fields.Binary(string='上传图片')
#     state = fields.Selection([('draft', '草稿'), ('done', '完成')], string="状态", default="draft")
#
#     # 定义btn_submit方法，方法的作用是将当前的state的状态变成done
#     @api.one
#     def btn_submit(self):
#         self.state = 'done'
#
#     # 定义btn_ver方法
#     @api.multi
#     def btn_ver(self):
#         # 创建vals，将当前页面的数据传递给vals
#         vals = {
#             'name': self.name,
#             'author': self.author,
#             'price': self.price,
#             'picture': self.picture,
#         }
#         # 在模型book.manage里创建vals
#         self.env['book.manage'].create(vals)
#         # 把当前页面的数据删除
#         self.unlink()

# class book_sub(models.Model):
#     _name = 'book.sub'
#     name = fields.Char(string='名称',required = True)
#     auth = fields.Char(string='作者',required = True)
#     price = fields.Float(string='价格')
#     picture = fields.Binary(string='上传图片')
#     '''state的Selection为多选字段，后面的string和name  author一样都有string属性，default = “draft”  默认选中的为draft'''
#     state = fields.Selection([('draft','草稿'),('done','完成')],string='状态',default = "draft")
# #     该方法将state的状态改为done
#     @api.one
#     def btn_sumit(self):
#         self.state = "done"
#
#     @api.multi
#     def btn_ver(self):
# #         创建vals，将当前页面的数据传递给vals
#         vals = {'name':self.name,
#                 'author':self.author,
#                 'price':self.price,
#                 'picture':self.picture,
#                 }
#   # 环境储存了模型的缓存记录集，因此我们可以通过环境来获取、增加、修改、删除记录，而触发数据库更改，从而达到操作数据库的目的。
#   #   例如：新增一条记录
#   #      '''self.env['模型'].create(vals)'''
#         self.evn['book.manage'].create(vals)
# #把当前页面的数据删除          删除在当前book_sub创建的 vals,这个vals是属于book.manage模型的对象
#         self.unlink()