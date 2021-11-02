from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.product'

    available_in_pos_company = fields.Boolean(string="Available in POS (by Company)", company_dependent=True, default=True)

    @api.onchange('available_in_pos_company')
    def _onchange_available_in_pos(self):
        if self.available_in_pos_company:
            self.available_in_pos = True


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    available_in_pos_company = fields.Boolean(string="Available in POS (by Company)", compute='_compute_available_in_pos', inverse='_set_available_in_pos', search='_search_available_in_pos')

    @api.depends_context('force_company')
    @api.depends('product_variant_ids', 'product_variant_ids.available_in_pos_company')
    def _compute_available_in_pos(self):
        for template in self:
            template.available_in_pos_company = any(template.product_variant_ids.mapped('available_in_pos_company'))

    def _set_available_in_pos(self):
        for template in self:
            template.product_variant_ids.available_in_pos_company = template.available_in_pos_company

    def _search_available_in_pos(self, operator, value):
        products = self.env['product.product'].search([('available_in_pos_company', operator, value)], limit=None)
        return [('id', 'in', products.mapped('product_tmpl_id').ids)]

    @api.onchange('available_in_pos_company')
    def _onchange_available_in_pos(self):
        if self.available_in_pos_company:
            self.available_in_pos = True
