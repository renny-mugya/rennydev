from django.shortcuts import render
from .models import Course, Day, Visitor
# from tracking_analyzer.models import Tracker


def create_detail_page(courses):
    for course in courses:
        page=open(f'table/static/details/{course}.html', 'w')
        page.write(
f'''
<div class="cd-schedule-modal__event-info">
    <div class="over">
        <div class="row">
        <div class="col-md-6">
            <table class="table table-bordered table-dark table-striped ">
                <caption class="caption-top"><b>Course Info</b></caption>
                <tr>
                    <th>Title</th>
                    <td>{ course.title }</td>
                </tr>
                <tr>
                    <th>Code</th>
                    <td>{ course.code }</td>
                </tr>
                <tr>
                    <th>Credit</th>
                    <td>{ course.credit }</td>
                </tr>
                <tr>
                    <th>Status</th>
                    <td>{ course.status }</td>
                </tr>
            </table>
        </div>
        <div class="col-md-6">
        <table class="table table-bordered table-dark table-striped ">
            <caption class="caption-top"><strong>Lecturer Info</strong></caption>
            <tr>
                <th>Name</th>
                <td>{ course.lecturer.name }</td>
            </tr>
            <tr>
                <th>Office</th>
                <td>{ course.lecturer.office }</td>
            </tr>
            <tr>
                <th>Phone</th>
                <td>{ course.lecturer.phone }</td>
            </tr>
            <tr>
                <th>Email</th>
                <td>{ course.lecturer.email }</td>
            </tr>
        </table>
        </div>
        </div>
    </div>
</div>
'''
        )
        page.close()


def index(request):
    # REMOTE_ADDR=request.META.get('REMOTE_ADDR')
    # HTTP_SEC_CH_UA_PLATFORM=request.META.get('HTTP_SEC_CH_UA_PLATFORM')
    # session_key=request.session.session_key
    # visitor=Visitor.objects.get_or_create(ip_addr=request.META.get('REMOTE_ADDR'), session_key=request.session.session_key)
    # Tracker.objects.create_from_request(request, visitor)
    
    courses = Course.objects.all()
    create_detail_page(courses)
    days = Day.objects.all()
    context = {
        'days' : days,
    }
    return render(request, 'index.html', context)

