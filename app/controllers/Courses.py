from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        # Note that we have to load the model before using it
        self.load_model('Course')
    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses=courses)
    
    # This is how a method with a route parameter that provides the id would work
    def show(self, id):
        # Note how we access the model using self.models
        print id
        course = self.models['Course'].get_course_by_id(id)
        print course
        return self.load_view('confirmation.html', course=course)
    
    # This is how a method used to add a course would look
    def add(self):
        print request.form
        self.models['Course'].add_course(request.form)
        return redirect('/')

    # To delete a course
    def delete(self,id):
        print id
        self.models['Course'].delete_course(id)
        return redirect('/')
