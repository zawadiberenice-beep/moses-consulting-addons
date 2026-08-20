from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    sharepoint_url = fields.Char(
        string="SharePoint URL"
    )