from openerp import models, fields, api


# https://www.odoo.com/forum/help-1/question/create-custom-fields-and-set-alerts-on-it-97466
class product_template_inherit(models.Model):
    _inherit = 'product.template'

    threshold = fields.Integer('Threshold')

    def check_product_qty(self, cr, uid, context=None):
        ids = self.search(cr, uid, [], context)
        products = self.browse(cr, uid, ids, context)
        for product in products:
            if product.qty_available < product.threshold:
                print '\n', product.name, '***', True



                # https://www.odoo.com/forum/help-1/question/concatenate-firstname-and-lastname-and-fill-into-name-field-97505
                # name = fields.Char(compute='_compute_name', store="True")
                # firstname = fields.Char()
                # lastname = fields.Char()

                # @api.depends('firstname', 'lastname')
                # def _compute_name(self):
                #     for record in self:
                #         record.name = record.firstname + record.lastname


                # https://www.odoo.com/forum/help-1/question/how-to-call-onchane-from-xmlrpc-in-odoo-97452
                # import xmlrpclib
                # url = 'http://localhost:8050'
                # db = 'b2b_quick_order_list_view'
                # username = 'admin'
                # password = 'admin'

                # models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
                # sss = models.execute_kw(db, 1, password,'sale.order', 'onchange_partner_id',[[],[1]])
                # print sss

                # https://www.odoo.com/forum/help-1/question/add-current-user-to-a-session-97459
                # self.env['res.users'].browse(self._uid).partner_id
