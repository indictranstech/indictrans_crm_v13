from __future__ import unicode_literals
import frappe
from frappe import _

settings = frappe.get_doc("CRM Settings")
global_settings = frappe.get_doc("Global Defaults")


def set_image(self, method):
	
	self.sign = settings.signature
	self._address = settings.address
	

def set_address(self,method):
	self._address = settings.address
	self.dododododo = global_settings.current_fiscal_year

def get_user_permission(user):
	pass
