Configure Grafana datasources and dashboards
============================================

A simple role for loading dashboards and datasources for
Grafana. It follows the rule that if a dashboard or datasource
with the same name already exists, then it is not updated. 

It currently works at the organisation level.

Usage
-----

An example of how to use the role is included in ```example/```.

Requires Ansible >=2.2. If your distro doesn't provide this
you can run Ansible from a venv:

1. Create venv: ```$ virtualenv ansible```
2. Activate venv: ```$ source ansible/bin/activate```
3. Update pip (optional): ```$ pip install -U pip```
4. Install Ansible: ```$ pip install ansible```

Creating dashboards
-------------------

To prevent Grafana stripping out datasource names dashboards
should be downloaded via the API. This can be done via [curl](http://docs.grafana.org/tutorials/api_org_token_howto/#api-tutorial-how-to-create-api-tokens-and-dashboards-for-a-specific-organization),
or via a browser. In this case an example is given for a
browser.

In Grafana switch to the organisation in which the dashboard you
wish to save is located. Then in the same browser access the
dashboard via the API:

http://10.1.2.3:3000/api/dashboards/db/tenant-logs

This will return the dashboard as a JSON string. To allow the
dashboard to load successfully it is required to nullify the
dashboard id. For example:

```
<snip>
"dashboard":{
  "annotations":{"list":[]},
  "editable":true",
  "gnetId":null,
  "hideControls":false,
  "id":null,                               <-- Must be null
  "links":[],
  "rows": </snip>
```
