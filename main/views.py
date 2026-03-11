from django.shortcuts import render
from django.utils import timezone
from .models import Carousel, Program, Event, LiveClass, Course, Achievement

def home(request):
    """Displays the homepage with dynamic content from the database."""
    now = timezone.now()

    context = {
        # Fetch all active carousels, ordered as specified in the model Meta
        'carousels': Carousel.objects.all(),

        # Fetch programs marked as featured
        'featured_programs': Program.objects.filter(is_featured=True),

        # Fetch the next 3 upcoming events (future dates)
        'upcoming_events': Event.objects.filter(date__gte=now).order_by('date')[:3],

        # Fetch the next 3 upcoming live classes (future dates/times)
        'live_classes': LiveClass.objects.filter(date__gte=now).order_by('date')[:3],

        # Fetch the first 3 featured courses
        'courses': Course.objects.filter(is_featured=True)[:3],

        # Fetch the 3 most recent achievements
        'achievements': Achievement.objects.order_by('-date')[:3],

        # Note: Statistics section was commented out in home.html, so no model/query for it yet.
    }
    return render(request, 'main/home.html', context)

# Placeholder for course_detail view mentioned in home.html
# You would need to implement this view and its corresponding URL pattern later.
def course_detail(request, course_id):
    # Fetch the specific course or return 404
    # course = get_object_or_404(Course, pk=course_id)
    # context = {'course': course}
    # return render(request, 'main/course_detail.html', context)
    pass # Replace with actual implementation

# Placeholder for admissions view mentioned in home.html
def admissions(request):
    """Renders the admissions page."""
    # Logic for admissions page can be added here later
    context = {}
    return render(request, 'main/admissions.html', context)

# --- List Views for Subpages --- 

def course_list(request):
    """Displays a list of all courses."""
    all_courses = Course.objects.all()
    context = {
        'courses': all_courses,
        'page_title': 'All Courses'
    }
    return render(request, 'main/course_list.html', context)

def event_list(request):
    """Displays a list of all events, ordered by date (newest first)."""
    all_events = Event.objects.order_by('-date')
    context = {
        'events': all_events,
        'page_title': 'All Events'
    }
    return render(request, 'main/event_list.html', context)

def achievement_list(request):
    """Displays a list of all achievements, ordered by date (newest first)."""
    all_achievements = Achievement.objects.order_by('-date')
    context = {
        'achievements': all_achievements,
        'page_title': 'Our Achievements'
    }
    return render(request, 'main/achievement_list.html', context) 