from odoo import fields, models, tools

class PosOrderReportWithAnalytic(models.Model):
    _inherit = "report.pos.order"

    analytic_account_id = fields.Many2one(
        'account.analytic.account', string='Analytic Account', readonly=True)
    
    region = fields.Integer(string='Region', readonly=True)

    def _select(self):
        return super(PosOrderReportWithAnalytic, self)._select() + """
            , ps.sh_analytic_account AS analytic_account_id
            , pc.region AS region
        """

    def _from(self):
        return super(PosOrderReportWithAnalytic, self)._from() + """
            LEFT JOIN pos_config pc ON pc.id = ps.config_id
        """

    def _group_by(self):
        return super(PosOrderReportWithAnalytic, self)._group_by() + """
            , ps.sh_analytic_account
            , pc.region
        """

    def init(self):
        # Recreate the SQL view
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (%s %s %s)
        """ % (self._table, self._select(), self._from(), self._group_by()))
