Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 4, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/report_creator/models/__init__.py", line 3, in <module>
    from . import models
  File "/home/t12016074307/odoo12/odoo/addons_tusas/report_creator/models/models.py", line 10, in <module>
    import pdfkit
ModuleNotFoundError: No module named 'pdfkit'
2026-03-10 05:14:35,996 7390 INFO odoodb werkzeug: 127.0.0.1 - - [10/Mar/2026 05:14:35] "GET /web?debug HTTP/1.1" 500 - 9 0.006 0.618
2026-03-10 05:14:36,002 7390 ERROR odoodb werkzeug: Error on request:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 205, in run_wsgi
    execute(self.server.app)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 193, in execute
    application_iter = app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/server.py", line 436, in app
    return self.app(e, s)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 141, in application
    return application_unproxied(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 116, in application_unproxied
    result = odoo.http.root(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1329, in __call__
    return self.dispatch(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1302, in __call__
    return self.app(environ, start_wrapped)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/wsgi.py", line 599, in __call__
    return self.app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1480, in dispatch
    odoo.registry(db).check_signaling()
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 4, in <module>
    
  File "/home/t12016074307/odoo12/odoo/addons_tusas/report_creator/models/__init__.py", line 3, in <module>
    from . import models
  File "/home/t12016074307/odoo12/odoo/addons_tusas/report_creator/models/models.py", line 10, in <module>
    import pdfkit
ModuleNotFoundError: No module named 'pdfkit' - - -
2026-03-10 05:14:39,500 7390 INFO odoodb odoo.modules.loading: loading 1 modules... 
2026-03-10 05:14:39,518 7390 INFO odoodb odoo.modules.loading: 1 modules loaded in 0.02s, 0 queries 
2026-03-10 05:14:39,596 7390 INFO odoodb odoo.modules.loading: loading 67 modules... 
2026-03-10 05:14:39,687 7390 CRITICAL odoodb odoo.modules.module: Couldn't load module facility_management 
2026-03-10 05:14:39,688 7390 CRITICAL odoodb odoo.modules.module: No module named 'unicode_tr' 
2026-03-10 05:14:39,689 7390 WARNING odoodb odoo.modules.loading: Transient module states were reset 
2026-03-10 05:14:39,690 7390 ERROR odoodb odoo.modules.registry: Failed to load registry 
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 2, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/facility_management/models/__init__.py", line 3, in <module>
    from . import fm_function
  File "/home/t12016074307/odoo12/odoo/addons_tusas/facility_management/models/fm_function.py", line 1, in <module>
    from unicode_tr import unicode_tr
ModuleNotFoundError: No module named 'unicode_tr'
2026-03-10 05:14:39,707 7390 INFO odoodb werkzeug: 127.0.0.1 - - [10/Mar/2026 05:14:39] "GET /web?debug HTTP/1.1" 500 - 9 0.004 0.209
2026-03-10 05:14:39,711 7390 ERROR odoodb werkzeug: Error on request:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 205, in run_wsgi
    execute(self.server.app)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 193, in execute
    application_iter = app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/server.py", line 436, in app
    return self.app(e, s)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 141, in application
    return application_unproxied(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 116, in application_unproxied
    result = odoo.http.root(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1329, in __call__
    return self.dispatch(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1302, in __call__
    return self.app(environ, start_wrapped)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/wsgi.py", line 599, in __call__
    return self.app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1480, in dispatch
    odoo.registry(db).check_signaling()
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 2, in <module>
    
  File "/home/t12016074307/odoo12/odoo/addons_tusas/facility_management/models/__init__.py", line 3, in <module>
    from . import fm_function
  File "/home/t12016074307/odoo12/odoo/addons_tusas/facility_management/models/fm_function.py", line 1, in <module>
    from unicode_tr import unicode_tr
ModuleNotFoundError: No module named 'unicode_tr' - - -
2026-03-10 05:14:43,572 7390 INFO odoodb odoo.modules.loading: loading 1 modules... 
2026-03-10 05:14:43,598 7390 INFO odoodb odoo.modules.loading: 1 modules loaded in 0.03s, 0 queries 
2026-03-10 05:14:43,676 7390 INFO odoodb odoo.modules.loading: loading 67 modules... 
2026-03-10 05:14:43,808 7390 INFO odoodb odoo.addons.sms.wizard.send_sms: The `phonenumbers` Python module is not available. Phone number validation will be skipped. Try `pip3 install phonenumbers` to install it. 
2026-03-10 05:14:43,911 7390 CRITICAL odoodb odoo.modules.module: Couldn't load module hr_environment 
2026-03-10 05:14:43,911 7390 CRITICAL odoodb odoo.modules.module: No module named 'unicode_tr' 
2026-03-10 05:14:43,912 7390 WARNING odoodb odoo.modules.loading: Transient module states were reset 
2026-03-10 05:14:43,912 7390 ERROR odoodb odoo.modules.registry: Failed to load registry 
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 2, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_environment/models/__init__.py", line 4, in <module>
    from . import hr_job
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_environment/models/hr_job.py", line 12, in <module>
    from unicode_tr import unicode_tr
ModuleNotFoundError: No module named 'unicode_tr'
2026-03-10 05:14:43,951 7390 INFO odoodb werkzeug: 127.0.0.1 - - [10/Mar/2026 05:14:43] "GET /web?debug HTTP/1.1" 500 - 9 0.006 0.387
2026-03-10 05:14:43,956 7390 ERROR odoodb werkzeug: Error on request:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 205, in run_wsgi
    execute(self.server.app)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 193, in execute
    application_iter = app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/server.py", line 436, in app
    return self.app(e, s)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 141, in application
    return application_unproxied(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 116, in application_unproxied
    result = odoo.http.root(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1329, in __call__
    return self.dispatch(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1302, in __call__
    return self.app(environ, start_wrapped)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/wsgi.py", line 599, in __call__
    return self.app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1480, in dispatch
    odoo.registry(db).check_signaling()
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 2, in <module>
    
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_environment/models/__init__.py", line 4, in <module>
    from . import hr_job
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_environment/models/hr_job.py", line 12, in <module>
    from unicode_tr import unicode_tr
ModuleNotFoundError: No module named 'unicode_tr' - - -
2026-03-10 05:14:47,096 7390 INFO odoodb odoo.modules.loading: loading 1 modules... 
2026-03-10 05:14:47,128 7390 INFO odoodb odoo.modules.loading: 1 modules loaded in 0.03s, 0 queries 
2026-03-10 05:14:47,208 7390 INFO odoodb odoo.modules.loading: loading 67 modules... 
2026-03-10 05:14:47,412 7390 CRITICAL odoodb odoo.modules.module: Couldn't load module hr_employee_ext 
2026-03-10 05:14:47,412 7390 CRITICAL odoodb odoo.modules.module: No module named 'unicode_tr' 
2026-03-10 05:14:47,413 7390 WARNING odoodb odoo.modules.loading: Transient module states were reset 
2026-03-10 05:14:47,414 7390 ERROR odoodb odoo.modules.registry: Failed to load registry 
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 4, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_employee_ext/models/__init__.py", line 5, in <module>
    from . import res_partner
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_employee_ext/models/res_partner.py", line 14, in <module>
    from unicode_tr import unicode_tr
ModuleNotFoundError: No module named 'unicode_tr'
2026-03-10 05:14:47,422 7390 INFO odoodb odoo.modules.loading: loading 1 modules... 
2026-03-10 05:14:47,439 7390 INFO odoodb odoo.modules.loading: 1 modules loaded in 0.02s, 0 queries 
2026-03-10 05:14:47,520 7390 INFO odoodb odoo.modules.loading: loading 67 modules... 
2026-03-10 05:14:47,617 7390 CRITICAL odoodb odoo.modules.module: Couldn't load module approval_dashboard 
2026-03-10 05:14:47,618 7390 CRITICAL odoodb odoo.modules.module: No module named 'zeep' 
2026-03-10 05:14:47,619 7390 WARNING odoodb odoo.modules.loading: Transient module states were reset 
2026-03-10 05:14:47,619 7390 ERROR odoodb odoo.modules.registry: Failed to load registry 
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1480, in dispatch
    odoo.registry(db).check_signaling()
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 4, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_employee_ext/models/__init__.py", line 5, in <module>
    from . import res_partner
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_employee_ext/models/res_partner.py", line 14, in <module>
    from unicode_tr import unicode_tr
ModuleNotFoundError: No module named 'unicode_tr'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 1, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/approval_dashboard/models/__init__.py", line 1, in <module>
    from . import res_users
  File "/home/t12016074307/odoo12/odoo/addons_tusas/approval_dashboard/models/res_users.py", line 10, in <module>
    from zeep import Client, Settings
ModuleNotFoundError: No module named 'zeep'
2026-03-10 05:14:47,658 7390 INFO odoodb werkzeug: 127.0.0.1 - - [10/Mar/2026 05:14:47] "GET /web?debug HTTP/1.1" 500 - 23 0.014 0.565
2026-03-10 05:14:47,664 7390 ERROR odoodb werkzeug: Error on request:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 205, in run_wsgi
    execute(self.server.app)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 193, in execute
    application_iter = app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/server.py", line 436, in app
    return self.app(e, s)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 141, in application
    return application_unproxied(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 116, in application_unproxied
    result = odoo.http.root(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1329, in __call__
    return self.dispatch(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1302, in __call__
    return self.app(environ, start_wrapped)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/wsgi.py", line 599, in __call__
    return self.app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1501, in dispatch
    response = self.get_response(httprequest, result, explicit_session)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 295, in __exit__
    elif self.registry:
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 387, in registry
    return odoo.registry(self.db)
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 1, in <module>
    
  File "/home/t12016074307/odoo12/odoo/addons_tusas/approval_dashboard/models/__init__.py", line 1, in <module>
    from . import res_users
  File "/home/t12016074307/odoo12/odoo/addons_tusas/approval_dashboard/models/res_users.py", line 10, in <module>
    from zeep import Client, Settings
ModuleNotFoundError: No module named 'zeep' - - -
2026-03-10 05:14:51,909 7390 INFO odoodb odoo.modules.loading: loading 1 modules... 
2026-03-10 05:14:51,936 7390 INFO odoodb odoo.modules.loading: 1 modules loaded in 0.03s, 0 queries 
2026-03-10 05:14:52,016 7390 INFO odoodb odoo.modules.loading: loading 67 modules... 
2026-03-10 05:14:52,123 7390 CRITICAL odoodb odoo.modules.module: Couldn't load module hr_delegation 
2026-03-10 05:14:52,123 7390 CRITICAL odoodb odoo.modules.module: No module named 'ibm_db' 
2026-03-10 05:14:52,125 7390 WARNING odoodb odoo.modules.loading: Transient module states were reset 
2026-03-10 05:14:52,125 7390 ERROR odoodb odoo.modules.registry: Failed to load registry 
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 4, in <module>
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_delegation/models/__init__.py", line 3, in <module>
    from . import models
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_delegation/models/models.py", line 9, in <module>
    import ibm_db
ModuleNotFoundError: No module named 'ibm_db'
2026-03-10 05:14:52,136 7390 INFO odoodb werkzeug: 127.0.0.1 - - [10/Mar/2026 05:14:52] "GET /web?debug HTTP/1.1" 500 - 9 0.014 0.241
2026-03-10 05:14:52,141 7390 ERROR odoodb werkzeug: Error on request:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 205, in run_wsgi
    execute(self.server.app)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 193, in execute
    application_iter = app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/server.py", line 436, in app
    return self.app(e, s)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 141, in application
    return application_unproxied(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 116, in application_unproxied
    result = odoo.http.root(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1329, in __call__
    return self.dispatch(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1302, in __call__
    return self.app(environ, start_wrapped)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/wsgi.py", line 599, in __call__
    return self.app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1480, in dispatch
    odoo.registry(db).check_signaling()
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 179, in load_module_graph
    load_openerp_module(package.name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 368, in load_openerp_module
    __import__('odoo.addons.' + module_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/module.py", line 82, in load_module
    exec(open(modfile, 'rb').read(), new_mod.__dict__)
  File "<string>", line 4, in <module>
    
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_delegation/models/__init__.py", line 3, in <module>
    from . import models
  File "/home/t12016074307/odoo12/odoo/addons_tusas/hr_delegation/models/models.py", line 9, in <module>
    import ibm_db
ModuleNotFoundError: No module named 'ibm_db' - - -
2026-03-10 05:14:56,319 7390 INFO odoodb odoo.modules.loading: loading 1 modules... 
2026-03-10 05:14:56,346 7390 INFO odoodb odoo.modules.loading: 1 modules loaded in 0.03s, 0 queries 
2026-03-10 05:14:56,422 7390 INFO odoodb odoo.modules.loading: loading 67 modules... 
2026-03-10 05:14:56,548 7390 WARNING odoodb odoo.modules.loading: Transient module states were reset 
2026-03-10 05:14:56,549 7390 ERROR odoodb odoo.modules.registry: Failed to load registry 
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 61, in __new__
    return cls.registries[db_name]
  File "/home/t12016074307/odoo12/odoo/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/home/t12016074307/odoo12/odoo/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: 'odoodb'
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 188, in load_module_graph
    model_names = registry.load(cr, package)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 241, in load
    model = cls._build_model(self, cr)
  File "/home/t12016074307/odoo12/odoo/odoo/models.py", line 440, in _build_model
    raise TypeError("Model %r does not exist in registry." % name)
TypeError: Model 'hr.delegation' does not exist in registry.
2026-03-10 05:14:56,554 7390 INFO odoodb werkzeug: 127.0.0.1 - - [10/Mar/2026 05:14:56] "GET /web?debug HTTP/1.1" 500 - 9 0.007 0.246
2026-03-10 05:14:56,559 7390 ERROR odoodb werkzeug: Error on request:
Traceback (most recent call last):
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 205, in run_wsgi
    execute(self.server.app)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/serving.py", line 193, in execute
    application_iter = app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/server.py", line 436, in app
    return self.app(e, s)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 141, in application
    return application_unproxied(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/service/wsgi_server.py", line 116, in application_unproxied
    result = odoo.http.root(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1329, in __call__
    return self.dispatch(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1302, in __call__
    return self.app(environ, start_wrapped)
  File "/home/t12016074307/odoo12/venv/lib/python3.7/site-packages/werkzeug/wsgi.py", line 599, in __call__
    return self.app(environ, start_response)
  File "/home/t12016074307/odoo12/odoo/odoo/http.py", line 1480, in dispatch
    odoo.registry(db).check_signaling()
  File "/home/t12016074307/odoo12/odoo/odoo/__init__.py", line 117, in registry
    return modules.registry.Registry(database_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 63, in __new__
    return cls.new(db_name)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 87, in new
    odoo.modules.load_modules(registry._db, force_demo, status, update_module)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 417, in load_modules
    force, status, report, loaded_modules, update_module, models_to_check)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 313, in load_marked_modules
    perform_checks=perform_checks, models_to_check=models_to_check
  File "/home/t12016074307/odoo12/odoo/odoo/modules/loading.py", line 188, in load_module_graph
    model_names = registry.load(cr, package)
  File "/home/t12016074307/odoo12/odoo/odoo/modules/registry.py", line 241, in load
    model = cls._build_model(self, cr)
  File "/home/t12016074307/odoo12/odoo/odoo/models.py", line 440, in _build_model
    raise TypeError("Model %r does not exist in registry." % name)
TypeError: Model 'hr.delegation' does not exist in registry. - - -
