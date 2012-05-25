object_definitions = {}
object_definitions["host"] = {
	"host_name": {
		"name":"host_name",
		"required":"required",
		"value":"host_name",
		"tip": "eg web01.example.com",
		"type": "string", 
	},
	"alias": { 
		"name":"alias", 
		"required":"required", 
		"value":"alias",
		"tip": "Textual description of host", 
		"type": "string"
	},
	
	"display_name": {
		"name":"display_name", 
		"required":"optional", 
		"value":"display_name",
		"tip": "Alternate hostname displayed in nagios",
		"type": "string",
	},
	"address": {
		"name":"address", 
		"required":"required", 
		"value":"address",
		"tip": "Usually IP address but can also be hostname",
		"type": [ "hostname", "ip" ],
	},
	"parents": { 
		"name":"parents", 
		"required":"optional", 
		"value":"host_names",
		"tip": "Logical device your host is connected to",
		"type": "ext",
		"exttype": [ "host", "host_name" ],
	},
}
object_definitions["host"]["hostgroups"] = { "name":"hostgroups", "required":"optional", "value":"hostgroup_names" }
object_definitions["host"]["check_command"] = { "name":"check_command", "required":"optional", "value":"command_name" }
object_definitions["host"]["initial_state"] = { "name":"initial_state", "required":"optional", "value":"[o,d,u]" }
object_definitions["host"]["max_check_attempts"] = { "name":"max_check_attempts", "required":"required", "value":"#" }
object_definitions["host"]["check_interval"] = { "name":"check_interval", "required":"optional", "value":"#" }
object_definitions["host"]["retry_interval"] = { "name":"retry_interval", "required":"optional", "value":"#" }
object_definitions["host"]["active_checks_enabled"] = { "name":"active_checks_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["passive_checks_enabled"] = { "name":"passive_checks_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["check_period"] = { "name":"check_period", "required":"required", "value":"timeperiod_name" }
object_definitions["host"]["obsess_over_host"] = { "name":"obsess_over_host", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["check_freshness"] = { "name":"check_freshness", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["freshness_threshold"] = { "name":"freshness_threshold", "required":"optional", "value":"#" }
object_definitions["host"]["event_handler"] = { "name":"event_handler", "required":"optional", "value":"command_name" }
object_definitions["host"]["event_handler_enabled"] = { "name":"event_handler_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["low_flap_threshold"] = { "name":"low_flap_threshold", "required":"optional", "value":"#" }
object_definitions["host"]["high_flap_threshold"] = { "name":"high_flap_threshold", "required":"optional", "value":"#" }
object_definitions["host"]["flap_detection_enabled"] = { "name":"flap_detection_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["flap_detection_options"] = { "name":"flap_detection_options", "required":"optional", "value":"[o,d,u]" }
object_definitions["host"]["process_perf_data"] = { "name":"process_perf_data", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["retain_status_information"] = { "name":"retain_status_information", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["retain_nonstatus_information"] = { "name":"retain_nonstatus_information", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["contacts"] = { "name":"contacts", "required":"required", "value":"contacts" }
object_definitions["host"]["contact_groups"] = { "name":"contact_groups", "required":"required", "value":"contact_groups" }
object_definitions["host"]["notification_interval"] = { "name":"notification_interval", "required":"required", "value":"#" }
object_definitions["host"]["first_notification_delay"] = { "name":"first_notification_delay", "required":"optional", "value":"#" }
object_definitions["host"]["notification_period"] = { "name":"notification_period", "required":"required", "value":"timeperiod_name" }
object_definitions["host"]["notification_options"] = { "name":"notification_options", "required":"optional", "value":"[d,u,r,f,s]" }
object_definitions["host"]["notifications_enabled"] = { "name":"notifications_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["host"]["stalking_options"] = { "name":"stalking_options", "required":"optional", "value":"[o,d,u]" }
object_definitions["host"]["notes"] = { "name":"notes", "required":"optional", "value":"note_string" }
object_definitions["host"]["notes_url"] = { "name":"notes_url", "required":"optional", "value":"url" }
object_definitions["host"]["action_url"] = { "name":"action_url", "required":"optional", "value":"url" }
object_definitions["host"]["icon_image"] = { "name":"icon_image", "required":"optional", "value":"image_file" }
object_definitions["host"]["icon_image_alt"] = { "name":"icon_image_alt", "required":"optional", "value":"alt_string" }
object_definitions["host"]["vrml_image"] = { "name":"vrml_image", "required":"optional", "value":"image_file" }
object_definitions["host"]["statusmap_image"] = { "name":"statusmap_image", "required":"optional", "value":"image_file" }
object_definitions["host"]["2d_coords"] = { "name":"2d_coords", "required":"optional", "value":"x_coord,y_coord" }
object_definitions["host"]["3d_coords"] = { "name":"3d_coords", "required":"optional", "value":"x_coord,y_coord,z_coord" }
object_definitions["hostgroup"] = {}
object_definitions["hostgroup"]["hostgroup_name"] = { "name":"hostgroup_name", "required":"required", "value":"hostgroup_name" }
object_definitions["hostgroup"]["alias"] = { "name":"alias", "required":"required", "value":"alias" }
object_definitions["hostgroup"]["members"] = { "name":"members", "required":"optional", "value":"hosts" }
object_definitions["hostgroup"]["hostgroup_members"] = { "name":"hostgroup_members", "required":"optional", "value":"hostgroups" }
object_definitions["hostgroup"]["notes"] = { "name":"notes", "required":"optional", "value":"note_string" }
object_definitions["hostgroup"]["notes_url"] = { "name":"notes_url", "required":"optional", "value":"url" }
object_definitions["hostgroup"]["action_url"] = { "name":"action_url", "required":"optional", "value":"url" }
object_definitions["service"] = {}
object_definitions["service"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["service"]["hostgroup_name"] = { "name":"hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["service"]["service_description"] = { "name":"service_description", "required":"required", "value":"service_description" }
object_definitions["service"]["display_name"] = { "name":"display_name", "required":"optional", "value":"display_name" }
object_definitions["service"]["servicegroups"] = { "name":"servicegroups", "required":"optional", "value":"servicegroup_names" }
object_definitions["service"]["is_volatile"] = { "name":"is_volatile", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["check_command"] = { "name":"check_command", "required":"required", "value":"command_name" }
object_definitions["service"]["initial_state"] = { "name":"initial_state", "required":"optional", "value":"[o,w,u,c]" }
object_definitions["service"]["max_check_attempts"] = { "name":"max_check_attempts", "required":"required", "value":"#" }
object_definitions["service"]["check_interval"] = { "name":"check_interval", "required":"required", "value":"#" }
object_definitions["service"]["retry_interval"] = { "name":"retry_interval", "required":"required", "value":"#" }
object_definitions["service"]["active_checks_enabled"] = { "name":"active_checks_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["passive_checks_enabled"] = { "name":"passive_checks_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["check_period"] = { "name":"check_period", "required":"required", "value":"timeperiod_name" }
object_definitions["service"]["obsess_over_service"] = { "name":"obsess_over_service", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["check_freshness"] = { "name":"check_freshness", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["freshness_threshold"] = { "name":"freshness_threshold", "required":"optional", "value":"#" }
object_definitions["service"]["event_handler"] = { "name":"event_handler", "required":"optional", "value":"command_name" }
object_definitions["service"]["event_handler_enabled"] = { "name":"event_handler_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["low_flap_threshold"] = { "name":"low_flap_threshold", "required":"optional", "value":"#" }
object_definitions["service"]["high_flap_threshold"] = { "name":"high_flap_threshold", "required":"optional", "value":"#" }
object_definitions["service"]["flap_detection_enabled"] = { "name":"flap_detection_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["flap_detection_options"] = { "name":"flap_detection_options", "required":"optional", "value":"[o,w,c,u]" }
object_definitions["service"]["process_perf_data"] = { "name":"process_perf_data", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["retain_status_information"] = { "name":"retain_status_information", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["retain_nonstatus_information"] = { "name":"retain_nonstatus_information", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["notification_interval"] = { "name":"notification_interval", "required":"required", "value":"#" }
object_definitions["service"]["first_notification_delay"] = { "name":"first_notification_delay", "required":"optional", "value":"#" }
object_definitions["service"]["notification_period"] = { "name":"notification_period", "required":"required", "value":"timeperiod_name" }
object_definitions["service"]["notification_options"] = { "name":"notification_options", "required":"optional", "value":"[w,u,c,r,f,s]" }
object_definitions["service"]["notifications_enabled"] = { "name":"notifications_enabled", "required":"optional", "value":"[0/1]" }
object_definitions["service"]["contacts"] = { "name":"contacts", "required":"required", "value":"contacts" }
object_definitions["service"]["contact_groups"] = { "name":"contact_groups", "required":"required", "value":"contact_groups" }
object_definitions["service"]["stalking_options"] = { "name":"stalking_options", "required":"optional", "value":"[o,w,u,c]" }
object_definitions["service"]["notes"] = { "name":"notes", "required":"optional", "value":"note_string" }
object_definitions["service"]["notes_url"] = { "name":"notes_url", "required":"optional", "value":"url" }
object_definitions["service"]["action_url"] = { "name":"action_url", "required":"optional", "value":"url" }
object_definitions["service"]["icon_image"] = { "name":"icon_image", "required":"optional", "value":"image_file" }
object_definitions["service"]["icon_image_alt"] = { "name":"icon_image_alt", "required":"optional", "value":"alt_string" }
object_definitions["servicegroup"] = {}
object_definitions["servicegroup"]["servicegroup_name"] = { "name":"servicegroup_name", "required":"required", "value":"servicegroup_name" }
object_definitions["servicegroup"]["alias"] = { "name":"alias", "required":"required", "value":"alias" }
object_definitions["servicegroup"]["members"] = { "name":"members", "required":"optional", "value":"services" }
object_definitions["servicegroup"]["servicegroup_members"] = { "name":"servicegroup_members", "required":"optional", "value":"servicegroups" }
object_definitions["servicegroup"]["notes"] = { "name":"notes", "required":"optional", "value":"note_string" }
object_definitions["servicegroup"]["notes_url"] = { "name":"notes_url", "required":"optional", "value":"url" }
object_definitions["servicegroup"]["action_url"] = { "name":"action_url", "required":"optional", "value":"url" }
object_definitions["contact"] = {}
object_definitions["contact"]["contact_name"] = { "name":"contact_name", "required":"required", "value":"contact_name" }
object_definitions["contact"]["alias"] = { "name":"alias", "required":"optional", "value":"alias" }
object_definitions["contact"]["contactgroups"] = { "name":"contactgroups", "required":"optional", "value":"contactgroup_names" }
object_definitions["contact"]["host_notifications_enabled"] = { "name":"host_notifications_enabled", "required":"required", "value":"[0/1]" }
object_definitions["contact"]["service_notifications_enabled"] = { "name":"service_notifications_enabled", "required":"required", "value":"[0/1]" }
object_definitions["contact"]["host_notification_period"] = { "name":"host_notification_period", "required":"required", "value":"timeperiod_name" }
object_definitions["contact"]["service_notification_period"] = { "name":"service_notification_period", "required":"required", "value":"timeperiod_name" }
object_definitions["contact"]["host_notification_options"] = { "name":"host_notification_options", "required":"required", "value":"[d,u,r,f,s,n]" }
object_definitions["contact"]["service_notification_options"] = { "name":"service_notification_options", "required":"required", "value":"[w,u,c,r,f,s,n]" }
object_definitions["contact"]["host_notification_commands"] = { "name":"host_notification_commands", "required":"required", "value":"command_name" }
object_definitions["contact"]["service_notification_commands"] = { "name":"service_notification_commands", "required":"required", "value":"command_name" }
object_definitions["contact"]["email"] = { "name":"email", "required":"optional", "value":"email_address" }
object_definitions["contact"]["pager"] = { "name":"pager", "required":"optional", "value":"pager_number or pager_email_gateway" }
object_definitions["contact"]["address"] = { "name":"address", "required":"optional", "value":"additional_contact_address" }
object_definitions["contact"]["can_submit_commands"] = { "name":"can_submit_commands", "required":"optional", "value":"[0/1]" }
object_definitions["contact"]["retain_status_information"] = { "name":"retain_status_information", "required":"optional", "value":"[0/1]" }
object_definitions["contact"]["retain_nonstatus_information"] = { "name":"retain_nonstatus_information", "required":"optional", "value":"[0/1]" }
object_definitions["contactgroup"] = {}
object_definitions["contactgroup"]["contactgroup_name"] = { "name":"contactgroup_name", "required":"required", "value":"contactgroup_name" }
object_definitions["contactgroup"]["alias"] = { "name":"alias", "required":"required", "value":"alias" }
object_definitions["contactgroup"]["members"] = { "name":"members", "required":"optional", "value":"contacts" }
object_definitions["contactgroup"]["contactgroup_members"] = { "name":"contactgroup_members", "required":"optional", "value":"contactgroups" }
object_definitions["timeperiod"] = {}
object_definitions["timeperiod"]["timeperiod_name"] = { "name":"timeperiod_name", "required":"required", "value":"timeperiod_name" }
object_definitions["timeperiod"]["alias"] = { "name":"alias", "required":"required", "value":"alias" }
object_definitions["timeperiod"]["[weekday]"] = { "name":"[weekday]", "required":"optional", "value":"timeranges" }
object_definitions["timeperiod"]["[exception]"] = { "name":"[exception]", "required":"optional", "value":"timeranges" }
object_definitions["timeperiod"]["exclude"] = { "name":"exclude", "required":"optional", "value":"]" }
object_definitions["command"] = {}
object_definitions["command"]["command_name"] = { "name":"command_name", "required":"required", "value":"command_name" }
object_definitions["command"]["command_line"] = { "name":"command_line", "required":"required", "value":"command_line" }
object_definitions["servicedependency"] = {}
object_definitions["servicedependency"]["dependent_host_name"] = { "name":"dependent_host_name", "required":"required", "value":"host_name" }
object_definitions["servicedependency"]["dependent_hostgroup_name"] = { "name":"dependent_hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["servicedependency"]["dependent_service_description"] = { "name":"dependent_service_description", "required":"required", "value":"service_description" }
object_definitions["servicedependency"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["servicedependency"]["hostgroup_name"] = { "name":"hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["servicedependency"]["service_description"] = { "name":"service_description", "required":"required", "value":"service_description" }
object_definitions["servicedependency"]["inherits_parent"] = { "name":"inherits_parent", "required":"optional", "value":"[0/1]" }
object_definitions["servicedependency"]["execution_failure_criteria"] = { "name":"execution_failure_criteria", "required":"optional", "value":"[o,w,u,c,p,n]" }
object_definitions["servicedependency"]["notification_failure_criteria"] = { "name":"notification_failure_criteria", "required":"optional", "value":"[o,w,u,c,p,n]" }
object_definitions["servicedependency"]["dependency_period"] = { "name":"dependency_period", "required":"optional", "value":"timeperiod_name" }
object_definitions["serviceescalation"] = {}
object_definitions["serviceescalation"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["serviceescalation"]["hostgroup_name"] = { "name":"hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["serviceescalation"]["service_description"] = { "name":"service_description", "required":"required", "value":"service_description" }
object_definitions["serviceescalation"]["contacts"] = { "name":"contacts", "required":"required", "value":"contacts" }
object_definitions["serviceescalation"]["contact_groups"] = { "name":"contact_groups", "required":"required", "value":"contactgroup_name" }
object_definitions["serviceescalation"]["first_notification"] = { "name":"first_notification", "required":"required", "value":"#" }
object_definitions["serviceescalation"]["last_notification"] = { "name":"last_notification", "required":"required", "value":"#" }
object_definitions["serviceescalation"]["notification_interval"] = { "name":"notification_interval", "required":"required", "value":"#" }
object_definitions["serviceescalation"]["escalation_period"] = { "name":"escalation_period", "required":"optional", "value":"timeperiod_name" }
object_definitions["serviceescalation"]["escalation_options"] = { "name":"escalation_options", "required":"optional", "value":"[w,u,c,r]" }
object_definitions["hostdependency"] = {}
object_definitions["hostdependency"]["dependent_host_name"] = { "name":"dependent_host_name", "required":"required", "value":"host_name" }
object_definitions["hostdependency"]["dependent_hostgroup_name"] = { "name":"dependent_hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["hostdependency"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["hostdependency"]["hostgroup_name"] = { "name":"hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["hostdependency"]["inherits_parent"] = { "name":"inherits_parent", "required":"optional", "value":"[0/1]" }
object_definitions["hostdependency"]["execution_failure_criteria"] = { "name":"execution_failure_criteria", "required":"optional", "value":"[o,d,u,p,n]" }
object_definitions["hostdependency"]["notification_failure_criteria"] = { "name":"notification_failure_criteria", "required":"optional", "value":"[o,d,u,p,n]" }
object_definitions["hostdependency"]["dependency_period"] = { "name":"dependency_period", "required":"optional", "value":"timeperiod_name" }
object_definitions["hostescalation"] = {}
object_definitions["hostescalation"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["hostescalation"]["hostgroup_name"] = { "name":"hostgroup_name", "required":"optional", "value":"hostgroup_name" }
object_definitions["hostescalation"]["contacts"] = { "name":"contacts", "required":"required", "value":"contacts" }
object_definitions["hostescalation"]["contact_groups"] = { "name":"contact_groups", "required":"required", "value":"contactgroup_name" }
object_definitions["hostescalation"]["first_notification"] = { "name":"first_notification", "required":"required", "value":"#" }
object_definitions["hostescalation"]["last_notification"] = { "name":"last_notification", "required":"required", "value":"#" }
object_definitions["hostescalation"]["notification_interval"] = { "name":"notification_interval", "required":"required", "value":"#" }
object_definitions["hostescalation"]["escalation_period"] = { "name":"escalation_period", "required":"optional", "value":"timeperiod_name" }
object_definitions["hostescalation"]["escalation_options"] = { "name":"escalation_options", "required":"optional", "value":"[d,u,r]" }
object_definitions["hostextinfo"] = {}
object_definitions["hostextinfo"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["hostextinfo"]["notes"] = { "name":"notes", "required":"optional", "value":"note_string" }
object_definitions["hostextinfo"]["notes_url"] = { "name":"notes_url", "required":"optional", "value":"url" }
object_definitions["hostextinfo"]["action_url"] = { "name":"action_url", "required":"optional", "value":"url" }
object_definitions["hostextinfo"]["icon_image"] = { "name":"icon_image", "required":"optional", "value":"image_file" }
object_definitions["hostextinfo"]["icon_image_alt"] = { "name":"icon_image_alt", "required":"optional", "value":"alt_string" }
object_definitions["hostextinfo"]["vrml_image"] = { "name":"vrml_image", "required":"optional", "value":"image_file" }
object_definitions["hostextinfo"]["statusmap_image"] = { "name":"statusmap_image", "required":"optional", "value":"image_file" }
object_definitions["hostextinfo"]["2d_coords"] = { "name":"2d_coords", "required":"optional", "value":"x_coord,y_coord" }
object_definitions["hostextinfo"]["3d_coords"] = { "name":"3d_coords", "required":"optional", "value":"x_coord,y_coord,z_coord" }
object_definitions["serviceextinfo"] = {}
object_definitions["serviceextinfo"]["host_name"] = { "name":"host_name", "required":"required", "value":"host_name" }
object_definitions["serviceextinfo"]["service_description"] = { "name":"service_description", "required":"required", "value":"service_description" }
object_definitions["serviceextinfo"]["notes"] = { "name":"notes", "required":"optional", "value":"note_string" }
object_definitions["serviceextinfo"]["notes_url"] = { "name":"notes_url", "required":"optional", "value":"url" }
object_definitions["serviceextinfo"]["action_url"] = { "name":"action_url", "required":"optional", "value":"url" }
object_definitions["serviceextinfo"]["icon_image"] = { "name":"icon_image", "required":"optional", "value":"image_file" }
object_definitions["serviceextinfo"]["icon_image_alt"] = { "name":"icon_image_alt", "required":"optional", "value":"alt_string" }
