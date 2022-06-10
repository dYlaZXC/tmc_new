# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgentActivity(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.AutoField(primary_key=True)
    activity_id = models.CharField(max_length=16)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255)
    agent_country = models.CharField(max_length=255, blank=True, null=True)
    agent_city = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    agg_run_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    activity = models.CharField(max_length=13)
    duration = models.BigIntegerField()
    detail = models.CharField(max_length=255, blank=True, null=True)
    pending_time = models.BigIntegerField(blank=True, null=True)
    talk_time = models.BigIntegerField(blank=True, null=True)
    hold_time = models.BigIntegerField(blank=True, null=True)
    held = models.BigIntegerField()
    max_hold = models.BigIntegerField()
    acw_time = models.BigIntegerField(blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    origination_number = models.CharField(max_length=255, blank=True, null=True)
    destination_number = models.CharField(max_length=255, blank=True, null=True)
    external_number = models.CharField(max_length=255, blank=True, null=True)
    other_party_phone_type = models.CharField(max_length=8, blank=True, null=True)
    disposition = models.CharField(max_length=27, blank=True, null=True)
    agent_disposition_name = models.CharField(max_length=255, blank=True, null=True)
    agent_disposition_code = models.IntegerField(blank=True, null=True)
    agent_disposition_notes = models.TextField(blank=True, null=True)
    session_id = models.CharField(max_length=16, blank=True, null=True)
    media_type = models.CharField(max_length=8, blank=True, null=True)
    case_number = models.CharField(max_length=48, blank=True, null=True)
    email_completion_time = models.BigIntegerField(blank=True, null=True)
    workitem_id = models.CharField(max_length=255, blank=True, null=True)
    call_detail_id = models.CharField(max_length=16, blank=True, null=True)
    has_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    cobrowsing = models.TextField(blank=True, null=True)  # This field type is a guess.
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_activity'


class AgentDispositions(models.Model):
    disposition_name = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agent_dispositions'


class AgentPerformance(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255)
    agent_country = models.CharField(max_length=255, blank=True, null=True)
    agent_city = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    no_service = models.TextField()  # This field type is a guess.
    service_name = models.CharField(max_length=255)
    is_internal = models.TextField()  # This field type is a guess.
    is_campaign = models.TextField()  # This field type is a guess.
    media_type = models.CharField(max_length=8, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    total_num_calls = models.BigIntegerField()
    num_calls_in = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_out = models.BigIntegerField()
    num_calls_answered_outbound = models.BigIntegerField()
    num_calls_agent_abandoned = models.BigIntegerField(blank=True, null=True)
    num_calls_rejected = models.BigIntegerField()
    num_calls_no_answer = models.BigIntegerField()
    num_calls_held = models.BigIntegerField()
    num_calls_graded = models.BigIntegerField()
    num_calls_in_cobrowsing = models.BigIntegerField(blank=True, null=True)
    num_calls_out_cobrowsing = models.BigIntegerField(blank=True, null=True)
    num_initiated_transfers = models.BigIntegerField()
    total_login_time = models.BigIntegerField()
    total_working_time = models.BigIntegerField()
    total_ready_time = models.BigIntegerField()
    total_handling_time = models.BigIntegerField()
    total_handling_call_time = models.BigIntegerField()
    total_handling_call_time_in = models.BigIntegerField()
    total_handling_call_time_out = models.BigIntegerField()
    total_handling_acw_time = models.BigIntegerField()
    total_handling_acw_time_in = models.BigIntegerField()
    total_handling_acw_time_out = models.BigIntegerField()
    total_busy_time_in = models.BigIntegerField()
    total_busy_time_out = models.BigIntegerField()
    total_ringing_time_in = models.BigIntegerField()
    total_ringing_time_out = models.BigIntegerField()
    total_acw_time_in = models.BigIntegerField()
    total_acw_time_out = models.BigIntegerField()
    total_hold_time_in = models.BigIntegerField()
    total_hold_time_out = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    num_surveys_with_cs = models.BigIntegerField()
    num_surveys_with_nps = models.BigIntegerField()
    num_surveys_with_fcr = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()
    grade_name = models.CharField(max_length=255, blank=True, null=True)
    grade_count = models.BigIntegerField()
    grade_total_value = models.BigIntegerField()
    grade_order_num = models.IntegerField(blank=True, null=True)
    not_ready_reason = models.CharField(max_length=255, blank=True, null=True)
    not_ready_time = models.BigIntegerField(blank=True, null=True)
    num_emails_pulled = models.BigIntegerField()
    num_emails_received_as_transfers = models.BigIntegerField()
    num_emails_received_as_assignments = models.BigIntegerField()
    num_emails_replied_by_agent = models.BigIntegerField()
    num_emails_closed_without_reply = models.BigIntegerField()
    num_emails_discarded = models.BigIntegerField()
    email_answer_time = models.BigIntegerField()
    email_personal_queue_time = models.BigIntegerField()
    num_emails_in_carried_over = models.BigIntegerField()
    num_emails_in_waiting_in_personal_queues = models.BigIntegerField()
    num_emails_in_waiting_in_personal_queues_breached_sla = models.BigIntegerField()
    num_emails_out_waiting_in_personal_queues = models.BigIntegerField()
    num_emails_in_service_changed = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'agent_performance'


class AgentSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    agent_state_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    proficiency = models.IntegerField()
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_skills'


class AgentStates(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.AutoField(primary_key=True)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255)
    agent_country = models.CharField(max_length=255, blank=True, null=True)
    agent_city = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.CharField(max_length=8, blank=True, null=True)
    direction = models.CharField(max_length=8, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    workitem_id = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    agent_capacity = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=15)
    is_connected = models.TextField(blank=True, null=True)  # This field type is a guess.
    was_connected = models.TextField(blank=True, null=True)  # This field type is a guess.
    not_ready_reason = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    session_id = models.CharField(max_length=16, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    has_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    ip_address = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agent_states'


class Agents(models.Model):
    login_id = models.CharField(primary_key=True, max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    agent_country = models.CharField(max_length=255, blank=True, null=True)
    agent_city = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'agents'


class AggregatorRuns(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    period_start_time = models.DateTimeField()
    period_end_time = models.DateTimeField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    num_records_aggregated = models.BigIntegerField(blank=True, null=True)
    status = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aggregator_runs'


class CallDetail(models.Model):
    id = models.CharField(unique=True, max_length=16, blank=True, null=True)
    pkid = models.AutoField(primary_key=True)
    agg_run_id = models.CharField(max_length=16)
    media_type = models.CharField(max_length=8, blank=True, null=True)
    start_time = models.DateTimeField()
    ivr_time = models.BigIntegerField()
    queue_time = models.BigIntegerField()
    pending_time = models.BigIntegerField()
    talk_time = models.BigIntegerField()
    hold_time = models.BigIntegerField()
    held = models.BigIntegerField()
    max_hold = models.BigIntegerField()
    acw_time = models.BigIntegerField()
    duration = models.BigIntegerField()
    service_name = models.CharField(max_length=255, blank=True, null=True)
    scenario_name = models.CharField(max_length=255, blank=True, null=True)
    trunk_description = models.CharField(max_length=255, blank=True, null=True)
    caller_login_id = models.CharField(max_length=255, blank=True, null=True)
    callee_login_id = models.CharField(max_length=255, blank=True, null=True)
    caller_phone_type = models.CharField(max_length=8, blank=True, null=True)
    callee_phone_type = models.CharField(max_length=8, blank=True, null=True)
    caller_rank = models.CharField(max_length=255, blank=True, null=True)
    callee_rank = models.CharField(max_length=255, blank=True, null=True)
    from_phone = models.CharField(max_length=255, blank=True, null=True)
    original_destination_phone = models.CharField(max_length=255, blank=True, null=True)
    connected_to_phone = models.CharField(max_length=255, blank=True, null=True)
    transferred_from_phone = models.CharField(max_length=255, blank=True, null=True)
    disposition = models.CharField(max_length=27, blank=True, null=True)
    agent_disposition_name = models.CharField(max_length=255, blank=True, null=True)
    agent_disposition_code = models.IntegerField(blank=True, null=True)
    agent_disposition_notes = models.TextField(blank=True, null=True)
    reported_problem = models.CharField(max_length=18, blank=True, null=True)
    global_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    initial_call_id = models.CharField(max_length=16, blank=True, null=True)
    initial_start_time = models.DateTimeField(blank=True, null=True)
    initial_service_name = models.CharField(max_length=255, blank=True, null=True)
    initial_caller_phone_type = models.CharField(max_length=8, blank=True, null=True)
    initial_callee_phone_type = models.CharField(max_length=8, blank=True, null=True)
    initial_from_phone = models.CharField(max_length=255, blank=True, null=True)
    initial_original_destination_phone = models.CharField(max_length=255, blank=True, null=True)
    initial_connected_to_phone = models.CharField(max_length=255, blank=True, null=True)
    flagged = models.TextField(blank=True, null=True)  # This field type is a guess.
    voice_signature = models.TextField(blank=True, null=True)  # This field type is a guess.
    account_number = models.CharField(max_length=255, blank=True, null=True)
    caller_first_name = models.CharField(max_length=255, blank=True, null=True)
    callee_first_name = models.CharField(max_length=255, blank=True, null=True)
    caller_last_name = models.CharField(max_length=255, blank=True, null=True)
    callee_last_name = models.CharField(max_length=255, blank=True, null=True)
    caller_city = models.CharField(max_length=255, blank=True, null=True)
    callee_city = models.CharField(max_length=255, blank=True, null=True)
    caller_country = models.CharField(max_length=255, blank=True, null=True)
    callee_country = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=48, blank=True, null=True)
    email_subject = models.CharField(max_length=1024, blank=True, null=True)
    email_language = models.CharField(max_length=255, blank=True, null=True)
    case_id = models.CharField(max_length=48, blank=True, null=True)
    thread_id = models.CharField(max_length=48, blank=True, null=True)
    case_number = models.CharField(max_length=48, blank=True, null=True)
    case_search_result = models.CharField(max_length=48, blank=True, null=True)
    response_email_id = models.CharField(max_length=48, blank=True, null=True)
    caller_monitored = models.TextField(blank=True, null=True)  # This field type is a guess.
    callee_monitored = models.TextField(blank=True, null=True)  # This field type is a guess.
    caller_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    callee_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    caller_cpa_rtp_server_id = models.CharField(max_length=16, blank=True, null=True)
    caller_cpa_recording_url = models.CharField(max_length=255, blank=True, null=True)
    caller_encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    callee_cpa_rtp_server_id = models.CharField(max_length=16, blank=True, null=True)
    callee_cpa_recording_url = models.CharField(max_length=255, blank=True, null=True)
    callee_encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    caller_has_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    callee_has_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    caller_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    callee_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    caller_has_voice_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    callee_has_voice_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    voice_recording_banned = models.TextField(blank=True, null=True)  # This field type is a guess.
    monitoring_banned = models.TextField(blank=True, null=True)  # This field type is a guess.
    email_detail_id = models.CharField(unique=True, max_length=48, blank=True, null=True)
    email_completion_time = models.BigIntegerField()
    email_kb_article_id = models.CharField(max_length=48, blank=True, null=True)
    caller_team_name = models.CharField(max_length=255, blank=True, null=True)
    callee_team_name = models.CharField(max_length=255, blank=True, null=True)
    detail_record_count = models.IntegerField(blank=True, null=True)
    in_service_level = models.CharField(max_length=10, blank=True, null=True)
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    sentiment = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    erased_voice_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    erased_voice_signature = models.TextField(blank=True, null=True)  # This field type is a guess.
    erased_chat_transcript = models.TextField(blank=True, null=True)  # This field type is a guess.
    erased_email = models.TextField(blank=True, null=True)  # This field type is a guess.
    erased_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    ewt = models.BigIntegerField(blank=True, null=True)
    cobrowsing = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'call_detail'


class CallbackCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    num_calls_queued = models.BigIntegerField(blank=True, null=True)
    num_callbacks_requested = models.BigIntegerField(blank=True, null=True)
    num_callbacks_attempted = models.BigIntegerField(blank=True, null=True)
    num_callbacks_busy = models.BigIntegerField(blank=True, null=True)
    num_callbacks_no_answer = models.BigIntegerField(blank=True, null=True)
    num_callbacks_answered = models.BigIntegerField(blank=True, null=True)
    num_callbacks_requeued = models.BigIntegerField(blank=True, null=True)
    num_callbacks_abandoned = models.BigIntegerField(blank=True, null=True)
    num_callbacks_handled = models.BigIntegerField(blank=True, null=True)
    callback_wait_time = models.BigIntegerField(blank=True, null=True)
    callback_customer_answer_time = models.BigIntegerField(blank=True, null=True)
    callback_agent_answer_time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'callback_counters'


class ChatMessageRecipients(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    chat_message_id = models.CharField(max_length=16)
    user_id = models.CharField(max_length=16)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_message_recipients'


class ChatMessages(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    user_id = models.CharField(max_length=16)
    login_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField()
    send_time = models.DateTimeField()
    is_urgent = models.TextField()  # This field type is a guess.
    dest_team_id = models.CharField(max_length=16, blank=True, null=True)
    dest_team_name = models.CharField(max_length=255, blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    ext_message_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chat_messages'


class ConcurrentUsers(models.Model):
    pkid = models.AutoField(primary_key=True)
    num_users = models.IntegerField(blank=True, null=True)
    users = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    agg_run_id = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'concurrent_users'


class CustomFieldNames(models.Model):
    category = models.CharField(primary_key=True, max_length=16)
    custom_field = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'custom_field_names'
        unique_together = (('category', 'name'),)


class Databasechangelog(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=63)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=63)  # Field name made lowercase.
    filename = models.CharField(db_column='FILENAME', max_length=200)  # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DATEEXECUTED')  # Field name made lowercase.
    orderexecuted = models.IntegerField(db_column='ORDEREXECUTED')  # Field name made lowercase.
    exectype = models.CharField(db_column='EXECTYPE', max_length=10)  # Field name made lowercase.
    md5sum = models.CharField(db_column='MD5SUM', max_length=35, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='COMMENTS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    liquibase = models.CharField(db_column='LIQUIBASE', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasechangelog'
        unique_together = (('id', 'author', 'filename'),)


class Databasechangeloglock(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    locked = models.IntegerField(db_column='LOCKED')  # Field name made lowercase.
    lockgranted = models.DateTimeField(db_column='LOCKGRANTED', blank=True, null=True)  # Field name made lowercase.
    lockedby = models.CharField(db_column='LOCKEDBY', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'databasechangeloglock'


class DeferredAggregatedInteractions(models.Model):
    interaction_id = models.CharField(primary_key=True, max_length=16)

    class Meta:
        managed = False
        db_table = 'deferred_aggregated_interactions'


class DeferredInteractionStepSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_step_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    service_level = models.IntegerField(blank=True, null=True)
    service_level_threshold = models.IntegerField(blank=True, null=True)
    short_abandonment_threshold = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deferred_interaction_step_skills'


class DeferredInteractionSteps(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    prev_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    next_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    interaction_id = models.CharField(max_length=16)
    scenario_id = models.CharField(max_length=16)
    scenario_name = models.CharField(max_length=255)
    direction = models.CharField(max_length=8)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    agent_country = models.CharField(max_length=255, blank=True, null=True)
    agent_city = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    agent_capacity = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ivr_start_time = models.DateTimeField(blank=True, null=True)
    ivr_end_time = models.DateTimeField(blank=True, null=True)
    queue_start_time = models.DateTimeField(blank=True, null=True)
    queue_end_time = models.DateTimeField(blank=True, null=True)
    pending_start_time = models.DateTimeField(blank=True, null=True)
    pending_end_time = models.DateTimeField(blank=True, null=True)
    delivered_start_time = models.DateTimeField(blank=True, null=True)
    delivered_end_time = models.DateTimeField(blank=True, null=True)
    delivered_duration = models.BigIntegerField(blank=True, null=True)
    hold_duration = models.BigIntegerField(blank=True, null=True)
    num_holds = models.BigIntegerField(blank=True, null=True)
    max_hold_duration = models.BigIntegerField(blank=True, null=True)
    wrap_up_start_time = models.DateTimeField(blank=True, null=True)
    wrap_up_end_time = models.DateTimeField(blank=True, null=True)
    wrap_up_duration = models.BigIntegerField(blank=True, null=True)
    total_duration = models.BigIntegerField(blank=True, null=True)
    route_result = models.CharField(max_length=19, blank=True, null=True)
    priority = models.IntegerField()
    overflow = models.TextField()  # This field type is a guess.
    monitored = models.TextField()  # This field type is a guess.
    direct = models.TextField()  # This field type is a guess.
    result = models.CharField(max_length=27, blank=True, null=True)
    cpa_rtp_server_id = models.CharField(max_length=16, blank=True, null=True)
    cpa_recording_url = models.CharField(max_length=255, blank=True, null=True)
    cpa_result = models.CharField(max_length=17, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    workitem_id = models.CharField(max_length=255, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone_type = models.CharField(max_length=16, blank=True, null=True)
    external_number = models.CharField(max_length=255, blank=True, null=True)
    bridge_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    linked_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    qm_mode = models.CharField(max_length=11, blank=True, null=True)
    monitored_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    trunk_description = models.CharField(max_length=255, blank=True, null=True)
    disposition_name = models.CharField(max_length=255, blank=True, null=True)
    disposition_code = models.IntegerField(blank=True, null=True)
    disposition_notes = models.TextField(blank=True, null=True)
    voice_signature = models.TextField(blank=True, null=True)  # This field type is a guess.
    self_service = models.TextField(blank=True, null=True)  # This field type is a guess.
    reported_problem = models.CharField(max_length=18, blank=True, null=True)
    has_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    matched_first_interval = models.TextField(blank=True, null=True)  # This field type is a guess.
    case_id = models.CharField(max_length=48, blank=True, null=True)
    case_number = models.CharField(max_length=48, blank=True, null=True)
    training_class = models.CharField(max_length=255, blank=True, null=True)
    trainer_login_id = models.CharField(max_length=255, blank=True, null=True)
    trainer_first_name = models.CharField(max_length=255, blank=True, null=True)
    trainer_last_name = models.CharField(max_length=255, blank=True, null=True)
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=48, blank=True, null=True)
    ewt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deferred_interaction_steps'


class DeferredInteractions(models.Model):
    record_id = models.CharField(primary_key=True, max_length=16)
    id = models.CharField(max_length=16, blank=True, null=True)
    waiting_for_initiator_id = models.CharField(max_length=16, blank=True, null=True)
    waiting_for_initiated_by_id = models.CharField(max_length=16, blank=True, null=True)
    waiting_for_initiated_by_reason = models.CharField(max_length=28, blank=True, null=True)
    global_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    scenario_context_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    media_type = models.CharField(max_length=8)
    duration = models.BigIntegerField(blank=True, null=True)
    origination = models.CharField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    initiated_by_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    flagged = models.TextField(blank=True, null=True)  # This field type is a guess.
    account_number = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=8)
    unattended = models.TextField(blank=True, null=True)  # This field type is a guess.
    has_voice_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    voice_recording_banned = models.IntegerField(blank=True, null=True)
    monitoring_banned = models.IntegerField(blank=True, null=True)
    sentiment = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    cobrowsing = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'deferred_interactions'


class DeferredSurveys(models.Model):
    interaction_id = models.CharField(primary_key=True, max_length=16)
    global_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    created_time = models.DateTimeField()
    fcr = models.TextField(blank=True, null=True)  # This field type is a guess.
    nps = models.IntegerField(blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    custom1 = models.IntegerField(blank=True, null=True)
    custom2 = models.IntegerField(blank=True, null=True)
    custom3 = models.IntegerField(blank=True, null=True)
    custom4 = models.IntegerField(blank=True, null=True)
    custom5 = models.IntegerField(blank=True, null=True)
    custom6 = models.IntegerField(blank=True, null=True)
    custom7 = models.IntegerField(blank=True, null=True)
    custom8 = models.IntegerField(blank=True, null=True)
    custom9 = models.IntegerField(blank=True, null=True)
    comment_sentiment = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    comment_url = models.TextField(blank=True, null=True)
    comment_transcript = models.TextField(blank=True, null=True)
    survey_id = models.CharField(max_length=255, blank=True, null=True)
    layout = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    late_survey = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'deferred_surveys'


class DispositionCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    disposition_name = models.CharField(max_length=255, blank=True, null=True)
    disposition_code = models.CharField(max_length=255, blank=True, null=True)
    is_campaign = models.TextField()  # This field type is a guess.
    media_type = models.CharField(max_length=8, blank=True, null=True)
    num_records_completed = models.BigIntegerField()
    num_calls_received = models.BigIntegerField()
    num_calls_outbound = models.BigIntegerField()
    num_preview_items = models.BigIntegerField()
    num_campaign_calls = models.BigIntegerField()
    num_non_campaign_calls_inbound = models.BigIntegerField()
    num_non_campaign_calls_outbound = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'disposition_counters'


class EvaluationResultDetails(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=64)  # Field name made lowercase.
    result = models.ForeignKey('EvaluationResults', models.DO_NOTHING, db_column='RESULT_ID')  # Field name made lowercase.
    area_name = models.CharField(db_column='AREA_NAME', max_length=1023, blank=True, null=True)  # Field name made lowercase.
    question_name = models.CharField(db_column='QUESTION_NAME', max_length=1023, blank=True, null=True)  # Field name made lowercase.
    option_name = models.TextField(db_column='OPTION_NAME', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase.
    order_in_form = models.IntegerField(db_column='ORDER_IN_FORM', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase.
    score_percent = models.DecimalField(db_column='SCORE_PERCENT', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    failed = models.TextField(db_column='FAILED')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'evaluation_result_details'


class EvaluationResults(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=16)  # Field name made lowercase.
    form_id = models.CharField(db_column='FORM_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    form_name = models.CharField(db_column='FORM_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    layout = models.TextField(db_column='LAYOUT', blank=True, null=True)  # Field name made lowercase.
    login_id = models.CharField(db_column='LOGIN_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    form_score = models.IntegerField(db_column='FORM_SCORE', blank=True, null=True)  # Field name made lowercase.
    evaluation_time = models.DateTimeField(db_column='EVALUATION_TIME', blank=True, null=True)  # Field name made lowercase.
    review_time = models.DateTimeField(db_column='REVIEW_TIME', blank=True, null=True)  # Field name made lowercase.
    cdr_id = models.CharField(db_column='CDR_ID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    media_type = models.CharField(db_column='MEDIA_TYPE', max_length=9, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=9, blank=True, null=True)  # Field name made lowercase.
    team_id = models.CharField(db_column='TEAM_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    team_name = models.CharField(db_column='TEAM_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_id = models.CharField(db_column='AGENT_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    confirmed_on = models.DateTimeField(db_column='CONFIRMED_ON', blank=True, null=True)  # Field name made lowercase.
    confirmed_by = models.CharField(db_column='CONFIRMED_BY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bookmark = models.TextField(db_column='BOOKMARK')  # Field name made lowercase. This field type is a guess.
    global_interaction_id = models.CharField(db_column='GLOBAL_INTERACTION_ID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    interaction_id = models.CharField(db_column='INTERACTION_ID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    form_failed = models.TextField(db_column='FORM_FAILED')  # Field name made lowercase. This field type is a guess.
    service_name = models.CharField(db_column='SERVICE_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    evaluator_first_name = models.CharField(db_column='EVALUATOR_FIRST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    evaluator_last_name = models.CharField(db_column='EVALUATOR_LAST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_first_name = models.CharField(db_column='AGENT_FIRST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_last_name = models.CharField(db_column='AGENT_LAST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supervisor_first_name = models.CharField(db_column='SUPERVISOR_FIRST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supervisor_last_name = models.CharField(db_column='SUPERVISOR_LAST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_comment = models.TextField(db_column='AGENT_COMMENT', blank=True, null=True)  # Field name made lowercase.
    evaluator_comment = models.TextField(db_column='EVALUATOR_COMMENT', blank=True, null=True)  # Field name made lowercase.
    cd_start_time = models.DateTimeField(db_column='CD_START_TIME', blank=True, null=True)  # Field name made lowercase.
    cd_duration = models.BigIntegerField(db_column='CD_DURATION', blank=True, null=True)  # Field name made lowercase.
    agent_training_class = models.CharField(db_column='AGENT_TRAINING_CLASS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_rank = models.CharField(db_column='AGENT_RANK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_trainer_login_id = models.CharField(db_column='AGENT_TRAINER_LOGIN_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cd_custom1 = models.CharField(db_column='CD_CUSTOM1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cd_custom2 = models.CharField(db_column='CD_CUSTOM2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cd_custom3 = models.CharField(db_column='CD_CUSTOM3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cd_custom4 = models.CharField(db_column='CD_CUSTOM4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cd_custom5 = models.CharField(db_column='CD_CUSTOM5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_trainer_first_name = models.CharField(db_column='AGENT_TRAINER_FIRST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    agent_trainer_last_name = models.CharField(db_column='AGENT_TRAINER_LAST_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evaluation_results'


class InteractionQualityMonitoring(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    response_email_id = models.CharField(max_length=48, blank=True, null=True)
    review_time = models.DateTimeField()
    review_agent_login_id = models.CharField(max_length=255)
    review_agent_first_name = models.CharField(max_length=255)
    review_agent_last_name = models.CharField(max_length=255)
    review_notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interaction_quality_monitoring'


class InteractionQualityMonitoringGrades(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    iqm_id = models.CharField(max_length=16)
    grade_name = models.CharField(max_length=255, blank=True, null=True)
    grade_value = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interaction_quality_monitoring_grades'


class InteractionStepSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_step_id = models.CharField(max_length=16)
    name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    service_level = models.IntegerField(blank=True, null=True)
    service_level_threshold = models.IntegerField(blank=True, null=True)
    short_abandonment_threshold = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interaction_step_skills'


class InteractionSteps(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.AutoField(primary_key=True)
    prev_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    next_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    interaction_id = models.CharField(max_length=16)
    scenario_id = models.CharField(max_length=16)
    scenario_name = models.CharField(max_length=255)
    direction = models.CharField(max_length=8)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    agent_country = models.CharField(max_length=255, blank=True, null=True)
    agent_city = models.CharField(max_length=255, blank=True, null=True)
    rank = models.CharField(max_length=255, blank=True, null=True)
    agent_capacity = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    ivr_start_time = models.DateTimeField(blank=True, null=True)
    ivr_end_time = models.DateTimeField(blank=True, null=True)
    queue_start_time = models.DateTimeField(blank=True, null=True)
    queue_end_time = models.DateTimeField(blank=True, null=True)
    pending_start_time = models.DateTimeField(blank=True, null=True)
    pending_end_time = models.DateTimeField(blank=True, null=True)
    delivered_start_time = models.DateTimeField(blank=True, null=True)
    delivered_end_time = models.DateTimeField(blank=True, null=True)
    delivered_duration = models.BigIntegerField(blank=True, null=True)
    hold_duration = models.BigIntegerField(blank=True, null=True)
    num_holds = models.BigIntegerField(blank=True, null=True)
    max_hold_duration = models.BigIntegerField(blank=True, null=True)
    wrap_up_start_time = models.DateTimeField(blank=True, null=True)
    wrap_up_end_time = models.DateTimeField(blank=True, null=True)
    wrap_up_duration = models.BigIntegerField(blank=True, null=True)
    total_duration = models.BigIntegerField(blank=True, null=True)
    route_result = models.CharField(max_length=19, blank=True, null=True)
    priority = models.IntegerField()
    overflow = models.TextField()  # This field type is a guess.
    monitored = models.TextField()  # This field type is a guess.
    direct = models.TextField()  # This field type is a guess.
    result = models.CharField(max_length=27, blank=True, null=True)
    cpa_rtp_server_id = models.CharField(max_length=16, blank=True, null=True)
    cpa_recording_url = models.CharField(max_length=255, blank=True, null=True)
    cpa_result = models.CharField(max_length=17, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    workitem_id = models.CharField(max_length=255, blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    phone_type = models.CharField(max_length=16, blank=True, null=True)
    external_number = models.CharField(max_length=255, blank=True, null=True)
    bridge_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    linked_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    qm_mode = models.CharField(max_length=11, blank=True, null=True)
    monitored_interaction_step_id = models.CharField(max_length=16, blank=True, null=True)
    trunk_description = models.CharField(max_length=255, blank=True, null=True)
    disposition_name = models.CharField(max_length=255, blank=True, null=True)
    disposition_code = models.IntegerField(blank=True, null=True)
    disposition_notes = models.TextField(blank=True, null=True)
    voice_signature = models.TextField(blank=True, null=True)  # This field type is a guess.
    self_service = models.TextField(blank=True, null=True)  # This field type is a guess.
    reported_problem = models.CharField(max_length=18, blank=True, null=True)
    has_screen_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    matched_first_interval = models.TextField(blank=True, null=True)  # This field type is a guess.
    case_id = models.CharField(max_length=48, blank=True, null=True)
    case_number = models.CharField(max_length=48, blank=True, null=True)
    training_class = models.CharField(max_length=255, blank=True, null=True)
    trainer_login_id = models.CharField(max_length=255, blank=True, null=True)
    trainer_first_name = models.CharField(max_length=255, blank=True, null=True)
    trainer_last_name = models.CharField(max_length=255, blank=True, null=True)
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    email_id = models.CharField(max_length=48, blank=True, null=True)
    ewt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interaction_steps'


class Interactions(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.AutoField(primary_key=True)
    global_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    scenario_context_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    media_type = models.CharField(max_length=8)
    duration = models.BigIntegerField(blank=True, null=True)
    origination = models.CharField(max_length=255, blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    initiated_by_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    flagged = models.TextField(blank=True, null=True)  # This field type is a guess.
    account_number = models.CharField(max_length=255, blank=True, null=True)
    direction = models.CharField(max_length=8)
    unattended = models.TextField(blank=True, null=True)  # This field type is a guess.
    has_voice_recording = models.TextField(blank=True, null=True)  # This field type is a guess.
    voice_recording_banned = models.IntegerField(blank=True, null=True)
    monitoring_banned = models.IntegerField(blank=True, null=True)
    sentiment = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    cobrowsing = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'interactions'


class OverflowCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    destination_phone = models.CharField(max_length=255, blank=True, null=True)
    routed_to = models.CharField(max_length=255)
    is_overflow = models.TextField()  # This field type is a guess.
    no_team = models.TextField()  # This field type is a guess.
    media_type = models.CharField(max_length=8, blank=True, null=True)
    num_calls_received = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_abandoned_after_threshold = models.BigIntegerField()
    handling_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'overflow_counters'


class Ranks(models.Model):
    rank = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ranks'


class RequestedSkills(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    media_type = models.CharField(max_length=8, blank=True, null=True)
    skill_name = models.CharField(max_length=255)
    skill_group_name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=8)
    total_answer_time = models.BigIntegerField()
    num_calls_received = models.BigIntegerField()
    num_calls_queued = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_overflow = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'requested_skills'


class ScenarioContexts(models.Model):
    id = models.CharField(unique=True, max_length=16)
    pkid = models.AutoField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    interaction_end_time = models.DateTimeField()
    steps = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scenario_contexts'


class ScenarioStepsCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    agg_run_id = models.CharField(max_length=16)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    scenario_name = models.CharField(max_length=255, blank=True, null=True)
    block_type = models.CharField(max_length=50)
    block_title = models.CharField(max_length=255)
    exit_id = models.CharField(max_length=255)
    caller_disconnect = models.TextField()  # This field type is a guess.
    num_steps = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'scenario_steps_counters'


class Scenarios(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scenarios'


class ScreenRecordings(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    login_id = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    rec_url = models.CharField(max_length=255, blank=True, null=True)
    rec_server_id = models.CharField(max_length=16, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    erase_time = models.DateTimeField(blank=True, null=True)
    erase_login_id = models.CharField(max_length=255, blank=True, null=True)
    erase_reason = models.TextField(blank=True, null=True)
    s3_rec_url = models.CharField(max_length=255, blank=True, null=True)
    s3_bucket = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'screen_recordings'


class ServiceInTimeCounters(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    destination_phone = models.CharField(max_length=255, blank=True, null=True)
    team_name = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.CharField(max_length=8, blank=True, null=True)
    custom1 = models.CharField(max_length=255, blank=True, null=True)
    custom2 = models.CharField(max_length=255, blank=True, null=True)
    custom3 = models.CharField(max_length=255, blank=True, null=True)
    custom4 = models.CharField(max_length=255, blank=True, null=True)
    custom5 = models.CharField(max_length=255, blank=True, null=True)
    num_calls_received = models.BigIntegerField()
    num_calls_received_as_transfers = models.BigIntegerField()
    num_calls_received_as_transfers_from_same_service = models.BigIntegerField()
    num_calls_received_as_transfers_from_other_service = models.BigIntegerField()
    num_calls_received_cobrowsing = models.BigIntegerField()
    num_calls_queued = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    num_calls_transferred_internally = models.BigIntegerField()
    num_calls_transferred_externally = models.BigIntegerField()
    answer_time = models.BigIntegerField()
    num_calls_abandoned = models.BigIntegerField()
    num_calls_abandoned_after_threshold = models.BigIntegerField()
    num_calls_abandoned_in_ivr = models.BigIntegerField()
    num_calls_self_service = models.BigIntegerField()
    num_calls_in_service_level = models.BigIntegerField()
    num_overflow_calls = models.BigIntegerField()
    num_calls_held = models.BigIntegerField()
    num_calls_recv_as_transfers_answered = models.BigIntegerField()
    num_calls_recv_as_transfers_in_service_level = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_in_ivr = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_after_threshold = models.BigIntegerField()
    num_calls_recv_as_transfers_queued = models.BigIntegerField()
    num_calls_recv_as_transfers_held = models.BigIntegerField()
    num_calls_queued_answered = models.BigIntegerField()
    answer_time_queued = models.BigIntegerField()
    num_calls_queued_abandoned = models.BigIntegerField()
    num_calls_queued_abandoned_after_threshold = models.BigIntegerField()
    num_calls_queued_in_service_level = models.BigIntegerField()
    num_calls_queued_held = models.BigIntegerField()
    abandonment_time_queued = models.BigIntegerField()
    abandonment_time_after_threshold_queued = models.BigIntegerField()
    abandonment_time = models.BigIntegerField()
    abandonment_time_after_threshold = models.BigIntegerField()
    total_duration_in = models.BigIntegerField()
    busy_time_in = models.BigIntegerField()
    busy_time_out = models.BigIntegerField()
    acw_time = models.BigIntegerField()
    acw_time_in = models.BigIntegerField()
    acw_time_out = models.BigIntegerField()
    hold_time_in = models.BigIntegerField()
    hold_time_out = models.BigIntegerField()
    ringing_time_in = models.BigIntegerField()
    ringing_time_out = models.BigIntegerField()
    num_calls_outbound = models.BigIntegerField()
    num_calls_answered_outbound = models.BigIntegerField()
    num_calls_held_outbound = models.BigIntegerField()
    num_calls_outbound_cobrowsing = models.BigIntegerField()
    ready_time = models.BigIntegerField()
    not_ready_time = models.BigIntegerField()
    login_time = models.BigIntegerField()
    handling_time = models.BigIntegerField()
    handling_call_time = models.BigIntegerField()
    handling_acw_time = models.BigIntegerField()
    assigned_handling_call_time = models.BigIntegerField()
    assigned_handling_acw_time = models.BigIntegerField()
    min_agents = models.BigIntegerField(blank=True, null=True)
    max_agents = models.BigIntegerField(blank=True, null=True)
    campaign_calls_attempted = models.BigIntegerField()
    campaign_dialer_calls_queued = models.BigIntegerField()
    campaign_dialer_calls_handled = models.BigIntegerField()
    campaign_calls_ivr = models.BigIntegerField()
    campaign_calls_live_answered = models.BigIntegerField()
    campaign_calls_queued = models.BigIntegerField()
    campaign_calls_abandoned = models.BigIntegerField()
    campaign_calls_handled = models.BigIntegerField()
    campaign_calls_held = models.BigIntegerField()
    campaign_calls_rpc = models.BigIntegerField()
    campaign_calls_unattended = models.BigIntegerField()
    campaign_calls_cobrowsing = models.BigIntegerField()
    campaign_records_completed = models.BigIntegerField()
    campaign_records_valid = models.BigIntegerField()
    campaign_records_dialed = models.BigIntegerField()
    campaign_records_queued = models.BigIntegerField()
    campaign_records_handled = models.BigIntegerField()
    campaign_records_excluded = models.BigIntegerField()
    campaign_records_rpc = models.BigIntegerField()
    campaign_ivr_time = models.BigIntegerField()
    campaign_queue_time = models.BigIntegerField()
    campaign_abandonment_time = models.BigIntegerField()
    campaign_answer_time = models.BigIntegerField()
    campaign_talk_time = models.BigIntegerField()
    campaign_hold_time = models.BigIntegerField()
    campaign_acw_time = models.BigIntegerField()
    campaign_handling_call_time = models.BigIntegerField()
    campaign_handling_acw_time = models.BigIntegerField()
    campaign_assigned_handling_call_time = models.BigIntegerField()
    campaign_assigned_handling_acw_time = models.BigIntegerField()
    campaign_preview_items = models.BigIntegerField()
    campaign_preview_time = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    num_surveys_with_cs = models.BigIntegerField()
    num_surveys_with_nps = models.BigIntegerField()
    num_surveys_with_fcr = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()
    num_emails_replied_by_agent = models.BigIntegerField()
    num_emails_closed_without_reply = models.BigIntegerField()
    email_routing_time = models.BigIntegerField()
    email_reply_time = models.BigIntegerField()
    num_emails_carried_over = models.BigIntegerField()
    num_emails_in_progress = models.BigIntegerField()
    num_emails_remaining_in_personal_queues = models.BigIntegerField()
    num_emails_remaining_in_personal_queues_breached_sla = models.BigIntegerField()
    num_emails_in_service_changed = models.BigIntegerField()
    num_emails_in_service_changed_received = models.BigIntegerField()
    num_emails_received_new = models.BigIntegerField()
    num_emails_carried_over_new = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service_in_time_counters'


class ServicePerformance(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    agg_run_id = models.CharField(max_length=16)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    service_name = models.CharField(max_length=255, blank=True, null=True)
    destination_phone = models.CharField(max_length=255, blank=True, null=True)
    media_type = models.CharField(max_length=8, blank=True, null=True)
    num_calls_received = models.BigIntegerField()
    num_calls_received_as_transfers = models.BigIntegerField()
    num_calls_received_as_transfers_from_same_service = models.BigIntegerField()
    num_calls_received_as_transfers_from_other_service = models.BigIntegerField()
    num_calls_transferred_internally = models.BigIntegerField()
    num_calls_transferred_externally = models.BigIntegerField()
    num_calls_answered = models.BigIntegerField()
    answer_time = models.BigIntegerField()
    num_calls_in_service_level = models.BigIntegerField()
    num_calls_abandoned = models.BigIntegerField()
    num_calls_abandoned_in_ivr = models.BigIntegerField()
    num_calls_abandoned_short = models.BigIntegerField()
    num_calls_abandoned_after_threshold = models.BigIntegerField()
    abandonment_time = models.BigIntegerField()
    abandonment_time_except_short = models.BigIntegerField()
    abandonment_time_after_threshold = models.BigIntegerField()
    num_calls_self_service = models.BigIntegerField()
    num_calls_overflow = models.BigIntegerField()
    num_calls_queued = models.BigIntegerField()
    num_calls_held = models.BigIntegerField()
    handling_time_in = models.BigIntegerField()
    talk_time_in = models.BigIntegerField()
    hold_time_in = models.BigIntegerField()
    wrap_up_time_in = models.BigIntegerField()
    num_calls_recv_as_transfers_answered = models.BigIntegerField()
    num_calls_recv_as_transfers_in_service_level = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_in_ivr = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_short = models.BigIntegerField()
    num_calls_recv_as_transfers_abandoned_after_threshold = models.BigIntegerField()
    num_calls_recv_as_transfers_queued = models.BigIntegerField()
    num_calls_recv_as_transfers_held = models.BigIntegerField()
    num_calls_received_cobrowsing = models.BigIntegerField()
    num_calls_outbound = models.BigIntegerField()
    num_calls_answered_outbound = models.BigIntegerField()
    handling_time_out = models.BigIntegerField()
    talk_time_out = models.BigIntegerField()
    wrap_up_time_out = models.BigIntegerField()
    num_calls_outbound_cobrowsing = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    num_surveys_with_cs = models.BigIntegerField()
    num_surveys_with_nps = models.BigIntegerField()
    num_surveys_with_fcr = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()
    campaign_calls_attempted = models.BigIntegerField()
    campaign_dialer_calls_queued = models.BigIntegerField()
    campaign_dialer_calls_handled = models.BigIntegerField()
    campaign_calls_ivr = models.BigIntegerField()
    campaign_calls_live_answered = models.BigIntegerField()
    campaign_calls_queued = models.BigIntegerField()
    campaign_calls_abandoned = models.BigIntegerField()
    campaign_calls_handled = models.BigIntegerField()
    campaign_calls_held = models.BigIntegerField()
    campaign_calls_rpc = models.BigIntegerField()
    campaign_calls_unattended = models.BigIntegerField()
    campaign_calls_cobrowsing = models.BigIntegerField()
    campaign_records_completed = models.BigIntegerField()
    campaign_records_valid = models.BigIntegerField()
    campaign_records_dialed = models.BigIntegerField()
    campaign_records_queued = models.BigIntegerField()
    campaign_records_handled = models.BigIntegerField()
    campaign_records_excluded = models.BigIntegerField()
    campaign_records_rpc = models.BigIntegerField()
    campaign_ivr_time = models.BigIntegerField()
    campaign_queue_time = models.BigIntegerField()
    campaign_abandonment_time = models.BigIntegerField()
    campaign_answer_time = models.BigIntegerField()
    campaign_talk_time = models.BigIntegerField()
    campaign_hold_time = models.BigIntegerField()
    campaign_acw_time = models.BigIntegerField()
    campaign_handling_call_time = models.BigIntegerField()
    campaign_handling_acw_time = models.BigIntegerField()
    campaign_assigned_handling_call_time = models.BigIntegerField()
    campaign_assigned_handling_acw_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'service_performance'


class Skills(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    group_name = models.CharField(max_length=255)
    type = models.CharField(max_length=8)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'skills'


class SupervisorActivity(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    login_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    activity = models.CharField(max_length=18, blank=True, null=True)
    call_detail_id = models.CharField(max_length=16, blank=True, null=True)
    agent_activity_id = models.CharField(max_length=16, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    disposition_name = models.CharField(max_length=255, blank=True, null=True)
    disposition_code = models.IntegerField(blank=True, null=True)
    disposition_notes = models.TextField(blank=True, null=True)
    old_disposition_name = models.CharField(max_length=255, blank=True, null=True)
    old_disposition_code = models.IntegerField(blank=True, null=True)
    agent_login_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supervisor_activity'


class Surveys(models.Model):
    interaction_id = models.CharField(primary_key=True, max_length=16)
    global_interaction_id = models.CharField(max_length=16, blank=True, null=True)
    created_time = models.DateTimeField()
    fcr = models.TextField(blank=True, null=True)  # This field type is a guess.
    nps = models.IntegerField(blank=True, null=True)
    cs = models.IntegerField(blank=True, null=True)
    ts = models.DateTimeField(blank=True, null=True)
    custom1 = models.IntegerField(blank=True, null=True)
    custom2 = models.IntegerField(blank=True, null=True)
    custom3 = models.IntegerField(blank=True, null=True)
    custom4 = models.IntegerField(blank=True, null=True)
    custom5 = models.IntegerField(blank=True, null=True)
    custom6 = models.IntegerField(blank=True, null=True)
    custom7 = models.IntegerField(blank=True, null=True)
    custom8 = models.IntegerField(blank=True, null=True)
    custom9 = models.IntegerField(blank=True, null=True)
    comment_sentiment = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    comment_url = models.TextField(blank=True, null=True)
    comment_transcript = models.TextField(blank=True, null=True)
    survey_id = models.CharField(max_length=255, blank=True, null=True)
    layout = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    late_survey = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'surveys'


class TeamPerformance(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    team_name = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    agg_run_id = models.CharField(max_length=16)
    total_num_calls = models.BigIntegerField()
    num_calls_in = models.BigIntegerField()
    num_calls_out = models.BigIntegerField()
    num_calls_agent_abandoned = models.BigIntegerField(blank=True, null=True)
    num_calls_rejected = models.BigIntegerField()
    num_initiated_transfers = models.BigIntegerField()
    total_login_time = models.BigIntegerField()
    total_working_time = models.BigIntegerField()
    total_ready_time = models.BigIntegerField()
    total_busy_time_in = models.BigIntegerField()
    total_busy_time_out = models.BigIntegerField()
    total_ringing_time = models.BigIntegerField()
    total_acw_time = models.BigIntegerField()
    num_surveys = models.BigIntegerField()
    cs = models.BigIntegerField()
    nps = models.BigIntegerField()
    num_fcr = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'team_performance'


class Teams(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'teams'


class VoiceRecordings(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rec_url = models.CharField(max_length=255, blank=True, null=True)
    rec_server_id = models.CharField(max_length=16, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    s3_rec_url = models.CharField(max_length=255, blank=True, null=True)
    s3_bucket = models.CharField(max_length=255, blank=True, null=True)
    erase_time = models.DateTimeField(blank=True, null=True)
    erase_login_id = models.CharField(max_length=255, blank=True, null=True)
    erase_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voice_recordings'


class VoiceTranscripts(models.Model):
    id = models.CharField(primary_key=True, max_length=16)
    interaction_id = models.CharField(max_length=16)
    interaction_step_id = models.CharField(max_length=16)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    rec_url = models.CharField(max_length=255, blank=True, null=True)
    rec_server_id = models.CharField(max_length=16, blank=True, null=True)
    encryption_key_id = models.CharField(max_length=16, blank=True, null=True)
    erase_time = models.DateTimeField(blank=True, null=True)
    erase_login_id = models.CharField(max_length=255, blank=True, null=True)
    erase_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voice_transcripts'
