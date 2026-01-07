app_name = "portalis_app"
app_title = "Portalis"
app_publisher = "Jennifer Croft"
app_description = "HRSN Platform Just Compassion"
app_email = "jcroft@justcompassionewc.com"
app_license = "mit"


# Fixtures
# --------
# These control what gets exported by:
#   bench --site <site> export-fixtures --app portalis_app
#

PORTALIS_DOCTYPES = [
    "Client",
    "Client Bill and Ledger Submission",
    "Client Document Submission",
    "Client Intake Form - About Me",
    "Client Intake Form - Housing and Utilities",
    "Client Intake Form - Income",
    "Client Intake Form - ROI Attestations and Certifications",
    "Client Vendor Accounts",
    "Client Management",
    "Household Income Entry",
    "Household Member",
    "Housing Service Option",
    "HRSN Activity Log",
    "HRSN Billing Month",
    "HRSN Case",
    "HRSN Client Bill",
    "HRSN Client Vendor Payment",
    "HRSN Month Payment",
    "HRSN Referrals",
    "HRSN Service Authorization",
    "HRSN Staff Coverage",
    "HRSN Vendor",
    "HRSN Vendor Contact Property",
    "HRSN Vendor Document",
    "HRSN Vendor Property",
    "HRSN Vendor W9",
]

PORTALIS_WEB_FORMS = [
    "client-intake-packet-about-me",
    "client-intake-packet-housing-and-utilities",
    "client-intake-packet-income",
    "client-intake-packet-roi-attestations-certifications",
    "vendor-contact-my-profile",
    "vendor-document-upload",
]

PORTALIS_WORKSPACES = [
    "hrsn-billing",
    # Add more workspace names here...
]

PORTALIS_PRINT_FORMATS = [
    "Trillium ROI",
    "YCCO HRSN Housing Service Plan",
    "YCCO ROI",
    "Zero Income Affidavit",
]

PORTALIS_ROLES = [
    "Case Manager",
    "Intake Specialist",
    "Billing Specialist",
    "Data and Compliance Specialist",
    "Program Manager",
    "Court Liaison",
    "Administrative Assistant",
]

PORTALIS_ROLE_PROFILES = [
    "Case Manager",
    "Intake Specialist",
    "Billing Specialist",
    "Data and Compliance Specialist",
    "Program Manager",
    "Court Liaison",
    "Administrative Assistant",
]

fixtures = [
    # 1) DocTypes (DB-defined DocTypes; bench export-fixtures will write JSON fixtures)
    {"dt": "DocType", "filters": [["name", "in", PORTALIS_DOCTYPES]]},

    # 2) Customize Form artifacts
    # Exclude workflow_state Custom Fields (Workflow creates it; importing again causes duplicates)
    {"dt": "Custom Field", "filters": [["dt", "in", PORTALIS_DOCTYPES], ["fieldname", "not in", ["workflow_state"]]]},
    {"dt": "Property Setter", "filters": [["doc_type", "in", PORTALIS_DOCTYPES]]},

    # 3) Scripts
    {"dt": "Client Script", "filters": [["dt", "in", PORTALIS_DOCTYPES]]},
    {"dt": "Server Script", "filters": [["reference_doctype", "in", PORTALIS_DOCTYPES]]},

    # 4) Workflows
    {"dt": "Workflow", "filters": [["document_type", "in", PORTALIS_DOCTYPES]]},

    # 5) Web Forms / UI artifacts (explicit by name is safest)
    {"dt": "Web Form", "filters": [["name", "in", PORTALIS_WEB_FORMS]]},
    {"dt": "Workspace", "filters": [["name", "in", PORTALIS_WORKSPACES]]},
    {"dt": "Print Format", "filters": [["name", "in", PORTALIS_PRINT_FORMATS]]},

    # 6) Permissions (Role Permission Manager / Custom DocPerm changes)
    {"dt": "Custom DocPerm", "filters": [["parent", "in", PORTALIS_DOCTYPES]]},

    # 7) Roles / Role Profiles
    {"dt": "Role", "filters": [["name", "in", PORTALIS_ROLES]]},
    {"dt": "Role Profile", "filters": [["name", "in", PORTALIS_ROLE_PROFILES]]},
]


# Apps
# ------------------

# Each item in the list will be shown as an app in the apps page
# NOTE: Keep route on something known-good unless you have a Workspace route you want to land on.
#       If you later add a "Portalis" workspace with route "portalis", change route to "/app/portalis".
add_to_apps_screen = [
    {
        "name": "portalis_app",
        # If you add an icon at portalis_app/public/images/portalis-logo.svg (or .png), update this path:
        # "logo": "/assets/portalis_app/images/portalis-logo.svg",
        "logo": "/assets/portalis_app/images/portalis-logo.svg",
        "title": "Portalis",
        "route": "/app/home",
        # Optional: only if you create this method in your app
        # "has_permission": "portalis_app.api.permission.has_app_permission",
    }
]

# required_apps = []


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/portalis_app/css/portalis_app.css"
# app_include_js = "/assets/portalis_app/js/portalis_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/portalis_app/css/portalis_app.css"
# web_include_js = "/assets/portalis_app/js/portalis_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "portalis_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "portalis_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#       "Role": "home_page"
# }

# Generators
# ----------

# website_generators = ["Web Page"]

# importable_doctypes = [doctype_1]

# Jinja
# ----------
# jinja = {
#       "methods": "portalis_app.utils.jinja_methods",
#       "filters": "portalis_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "portalis_app.install.before_install"
# after_install = "portalis_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "portalis_app.uninstall.before_uninstall"
# after_uninstall = "portalis_app.uninstall.after_uninstall"

# Integration Setup
# ------------------

# before_app_install = "portalis_app.utils.before_app_install"
# after_app_install = "portalis_app.utils.after_app_install"

# Integration Cleanup
# -------------------

# before_app_uninstall = "portalis_app.utils.before_app_uninstall"
# after_app_uninstall = "portalis_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------

# notification_config = "portalis_app.notifications.get_notification_config"

# Permissions
# -----------

# permission_query_conditions = {
#       "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#       "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------

# doc_events = {
#       "*": {
#               "on_update": "method",
#               "on_cancel": "method",
#               "on_trash": "method"
#       }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#       "all": [
#               "portalis_app.tasks.all"
#       ],
#       "daily": [
#               "portalis_app.tasks.daily"
#       ],
#       "hourly": [
#               "portalis_app.tasks.hourly"
#       ],
#       "weekly": [
#               "portalis_app.tasks.weekly"
#       ],
#       "monthly": [
#               "portalis_app.tasks.monthly"
#       ],
# }

# Testing
# -------

# before_tests = "portalis_app.install.before_tests"

# Extend DocType Class
# ------------------------------

# extend_doctype_class = {
#       "Task": "portalis_app.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------

# override_whitelisted_methods = {
#       "frappe.desk.doctype.event.event.get_events": "portalis_app.event.get_events"
# }
#
# override_doctype_dashboards = {
#       "Task": "portalis_app.task.get_dashboard_data"
# }

# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["portalis_app.utils.before_request"]
# after_request = ["portalis_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["portalis_app.utils.before_job"]
# after_job = ["portalis_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#       {
#               "doctype": "{doctype_1}",
#               "filter_by": "{filter_by}",
#               "redact_fields": ["{field_1}", "{field_2}"],
#               "partial": 1,
#       },
#       {
#               "doctype": "{doctype_4}"
#       }
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#       "portalis_app.auth.validate"
# ]

# export_python_type_annotations = True

# default_log_clearing_doctypes = {
#       "Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# ignore_translatable_strings_from = []
