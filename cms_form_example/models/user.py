# Copyright 2017 Simone Orsi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models
from odoo import fields
from odoo import tools

testing = tools.config.get('test_enable')


if not testing:
    # prevent these forms to be registered when running tests

    class ExampleUsersForm(models.AbstractModel):
        """A test model form."""

        _name = 'cms.form.res.users'
        _inherit = 'cms.form'
        _description = __doc__
        _form_model = 'res.users'
        _form_model_fields = ('name', 'login')
        _form_required_fields = ('name', )
        _form_fields_order = ('name', 'login')

        custom = fields.Char()

        def _form_load_custom(
                self, form, main_object, fname, value, **req_values):
            """Load a custom default for the field 'custom'."""
            return req_values.get('custom', 'oh yeah!')

    class UsersSearchForm(models.AbstractModel):
        """users model search form."""

        _name = 'cms.form.search.res.users'
        _inherit = 'cms.form.search'
        _description = __doc__
        _form_model = 'res.users'
        _form_model_fields = ('name', 'login', )

    class UsersSearchFormAjax(models.AbstractModel):
        """users model search form with ajax."""
        _inherit = 'cms.form.search.res.users'
        _name = 'cms.form.search.res.users.ajax'
        _description = __doc__
        _form_ajax = True
        _form_ajax_onchange = True

    class ExampleusersFormWithFieldsets(models.AbstractModel):
        _name = 'cms.form.res.users.fset'
        _inherit = 'cms.form.res.users'
        _description = __doc__

        _form_fieldsets = [
            {
                'id': 'main',
                'title': 'Main',
                'fields': [
                    'name',
                ],
            },
            {
                'id': 'secondary',
                'title': 'Secondary',
                'fields': [
                    'login',
                ],
            },
        ]

    class ExampleusersFormWithTabbedFieldsets(models.AbstractModel):
        _name = 'cms.form.res.users.fset.tabbed'
        _inherit = 'cms.form.res.users.fset'
        _form_fieldsets_display = 'tabs'
