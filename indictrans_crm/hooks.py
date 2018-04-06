# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "indictrans_crm"
app_title = "Indictrans CRM"
app_publisher = "khushal"
app_description = "new flow control for crm"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "khushal.t@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/indictrans_crm/css/indictrans_crm.css"
# app_include_js = "/assets/indictrans_crm/js/indictrans_crm.js"

# include js, css files in header of web template
# web_include_css = "/assets/indictrans_crm/css/indictrans_crm.css"
# web_include_js = "/assets/indictrans_crm/js/indictrans_crm.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "indictrans_crm.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "indictrans_crm.install.before_install"
# after_install = "indictrans_crm.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "indictrans_crm.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Lead": "indictrans_crm.customisation.get_user_permission",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"indictrans_crm.tasks.all"
# 	],
# 	"daily": [
# 		"indictrans_crm.tasks.daily"
# 	],
# 	"hourly": [
# 		"indictrans_crm.tasks.hourly"
# 	],
# 	"weekly": [
# 		"indictrans_crm.tasks.weekly"
# 	]
# 	"monthly": [
# 		"indictrans_crm.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "indictrans_crm.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "indictrans_crm.event.get_events"
# }

doc_events = {
	"Sales Invoice":{
		"before_submit": "indictrans_crm.customisation.set_image",
		"before_insert" : "indictrans_crm.customisation.set_address",
		"autoname":"indictrans_crm.customisation.autoname"
	} 
}

fixtures= ['Custom Script','Property Setter','Custom Field','Print Format']