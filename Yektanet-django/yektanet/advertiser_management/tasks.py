from celery import shared_task


@shared_task
def send_sms_task():
    pass
    # print(list(ModelView.objects.annotate(hour_and_date=TruncHour('time')).values('ad_id', 'hour_and_date') \
    # .filter(ad_id=1, hour_and_date__hour=timezone.now().hour).annotate(repeat=Count('ad_id')).values('ad_id', 'hour_and_date', 'repeat')))
