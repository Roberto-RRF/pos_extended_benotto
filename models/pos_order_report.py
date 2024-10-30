from odoo import fields, models, tools

class PosOrderReportWithAnalytic(models.Model):
    _inherit = "report.pos.order"

    # Assuming sh_analytic_account is a Many2one field
    analytic_account_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account', readonly=True)

    def _select(self):
        # Call the super method to get the original select statement
        return super(PosOrderReportWithAnalytic, self)._select() + ", ps.sh_analytic_account AS analytic_account_id"


    def _group_by(self):
        # Call the super method to get the original group by statement
        return super(PosOrderReportWithAnalytic, self)._group_by() + """
            , ps.sh_analytic_account
        """

    def init(self):
        # Call the super method to create the original view
        super(PosOrderReportWithAnalytic, self).init()