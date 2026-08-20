from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    sharepoint_url = fields.Char(
        string="Lien SharePoint"
    )

    def action_open_sharepoint(self):
        self.ensure_one()

        if not self.sharepoint_url:
            return False

        return {
            "type": "ir.actions.act_url",
            "url": self.sharepoint_url,
            "target": "new",
        }