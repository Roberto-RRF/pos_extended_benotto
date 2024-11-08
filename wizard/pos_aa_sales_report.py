from odoo import fields, models, api


class PosAASalesReport(models.TransientModel):
    _name = 'pos.aa.sales.reports.wizard'
    _description = 'Point of Sale Analitic Account Report'


    date_start = fields.Datetime(string='Start Date', required=True)
    date_stop = fields.Datetime(string='End Date', required=True)
    analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', required=True)
    config_ids = fields.Many2many('pos.config', string='Point of Sale Configurations', readonly=True)

    @api.onchange('date_start', 'date_stop', 'analytic_account_id')
    def _onchange_date_and_analytic_account(self):
        if self.date_start and self.date_stop and self.analytic_account_id:
            # Fetch the configurations based on the selected dates and analytic account
            config_ids = self.env['pos.config'].search([
                ('sh_analytic_account', '=', self.analytic_account_id.id)
            ])

            self.config_ids = [(6, 0, config_ids.ids)]

        else:
            self.config_ids = [(5, 0, 0)]

    def generate_report(self):
        data = {
            'date_start': self.date_start,
            'date_stop': self.date_stop,
            'analytic_account_id': self.analytic_account_id.id,
            'config_ids': self.config_ids.ids,
        }
        return self.env.ref('point_of_sale.sale_details_report').report_action([], data=data)


