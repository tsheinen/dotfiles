# list plugins
#
# Produce an HTML report showing how to use a sortable HTML table to make a slightly more useful UI. Appologies for the awful intermixing of code and HTMl, think it's actually more readable this way.

from binaryninjaui import getThemeColor, ThemeColor
r=RepositoryManager()
repos = ["community", "official"]

html = '''<html>
<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/bs4/jq-3.3.1/dt-1.10.22/datatables.min.css"/>
<script type="text/javascript" src="https://cdn.datatables.net/v/bs4/jq-3.3.1/dt-1.10.22/datatables.min.js"></script>
 <script>'''

for repo in repos:
  html += f'''$(document).ready( function () {{
 $('#{repo}').DataTable({{
	"paging": false,
    "info": false,
    "searching": false,
    "order": [[2, "desc"], [0, "asc"]]
}});
 }} );
'''

html += f''' </script>
<style>
tr[data-state="Update Available"]{{
  color: {getThemeColor(ThemeColor.CyanStandardHighlightColor).name()};
}}
tr[data-state="Disabled"]{{
  color: {getThemeColor(ThemeColor.FalseBranchColor).name()};
}}
tr[data-state="Enabled"]{{
  color: {getThemeColor(ThemeColor.TrueBranchColor).name()};
}}
</style>
</head>
<body>

<div style="margin: 50px">
'''

for repo in ["community", "official"]:
  html += f'''<h3>{repo.capitalize()} Plugins</h3>
<table id="{repo}" class="sortable" cellspacing="0" width="100%">
  <thead>
    <tr>
      <th>Plugin Name</th>
      <th>Version</th>
      <th>Status</th>
      <th>Short Description</th>
    </tr>
  </thead>
  <tbody>
'''
  for plugin in r.plugins[repo]:
    if plugin.update_available:
      status = "Update Available"
    elif plugin.installed and not plugin.enabled:
      status = "Disabled"
    elif plugin.installed:
      status = "Enabled"
    else:
      continue
    html += f'<tr data-state="{status}"><td>{plugin.name}</td><td>{plugin.version}</td><td>{status}</td><td>{plugin.description}</td></tr>'
  html += f'''</tbody>
</table>
<hr />
'''  

html += '''
</div>
</body>
</html>
'''

show_html_report('Plugin List', html)