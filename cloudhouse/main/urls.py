from django.urls import path
from . import views

urlpatterns = [
    path('ajaxbd/', views.ajaxbd, name='ajaxbd'),
    path('', views.index, name='home'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('admins/', views.admin_panel, name='admin_panel'),
    path('about', views.about, name='about'),
    path('support', views.support, name='support'),
    path('account', views.index, name='account'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pay/', views.send_email_view, name='pay'),
    path('clear_notification/', views.clear_notif, name='clear_notification'),
    path('clear_notification_all/', views.clear_notif_all, name='clear_notification_all'),
    path('accept_settings/', views.settings_acc, name='accept_settings'),
    path('accept_settings_upd/', views.accept_settings_upd, name='accept_settings_upd'),
    path('favorite_add/', views.favorite_add, name='favorite_add'),
    path('report_sens/', views.report_sens, name='report_sens'),
    path('report_sens_all/', views.report_sens_all, name='report_sens_all'),
    path('button_on/', views.device_button_on, name='button_on'),
    path('button_off/', views.device_button_off, name='button_off'),
    path('light_onoff/', views.light_onoff, name='light_onoff'),
    path('activate/', views.active_device, name='activate'),
    path('notification_send/', views.notification_send, name='notification_send'),
    path('search_contracts/', views.search_admin, name='search_contracts'),
    path('search_clients/', views.search_admin2, name='search_clients'),
    path('search_devices/', views.search_admin3, name='search_devices'),
    path('search_temp/', views.search_admin4, name='search_temp'),
    path('search_energy/', views.search_admin5, name='search_energy'),
    path('search_voice/', views.search_admin6, name='search_voice'),
    path('search_light/', views.search_admin7, name='search_light'),
    path('search_notifications/', views.search_admin8, name='search_notifications'),
    path('search_settings/', views.search_admin9, name='search_settings'),
    path('search_favorites/', views.search_admin10, name='search_favorites'),
    path('search_reports/', views.search_admin11, name='search_reports'),
    path('delete_temp/', views.delete_admin_temp, name='delete_temp'),
    path('delete_voice/', views.delete_admin_voice, name='delete_voice'),
    path('delete_energy/', views.delete_admin_energy, name='delete_energy'),
    path('delete_light/', views.delete_admin_light, name='delete_light'),
    path('delete_notif/', views.delete_admin_notif, name='delete_notif'),
    path('delete_report/', views.delete_admin_report, name='delete_report'),
    path('updatetemp/', views.update_admin_temp, name='updatetemp'),
    path('updatevoice/', views.update_admin_voice, name='updatevoice'),
    path('updateenergy/', views.update_admin_energy, name='updateenergy'),
    path('updatelight/', views.update_admin_light, name='updatelight'),
    path('updateclient/', views.update_admin_client, name='updateclient'),
    path('addtemp/', views.add_admin_temp, name='addtempetarure'),
    path('addvoice/', views.add_admin_voice, name='addvoice'),
    path('addlight/', views.add_admin_light, name='addlight'),
    path('addenergy/', views.add_admin_energy, name='addenergy'),
    path('createcontract/', views.create_admin_contract, name='createcontract'),
    path('deletecontract/', views.delete_admin_contract, name='deletecontract'),
    path('loadcontract/', views.load_admin_contract, name='loadcontract'),
    path('add_contract_device/', views.add_contract_admin_device, name='add_contract_device'),
    path('editaddr/', views.editaddr, name='editaddr'),
    path('morecontract/', views.morecontract, name='morecontract'),
    path('arch_admin_contract/', views.arch_admin_contract, name='arch_admin_contract'),
    path('unarch_admin_contract/', views.unarch_admin_contract, name='unarch_admin_contract'),
]
