import frappe

@frappe.whitelist()
def get_vendor_for_current_user():
    user = frappe.session.user
    if user == "Guest":
        return None

    vendor = frappe.db.get_value(
        "HRSN Vendor Contact",
        {"user": user, "portal_enabled": 1},
        "vendor"
    )
    return vendor
