from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
      return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, course_id):
      # pass data to the query like so
      print "getting a course from database"
      query = "SELECT * FROM courses WHERE id = %s"
      data = [course_id]
      return self.db.query_db(query, data)

    def add_course(self, course):
      #Build the query first and then the data that goesin the query
      print "adding course"
      query = "INSERT INTO courses (title, description, created_at) VALUES ('{}', '{}', NOW())".format(course['title'],course['description'])
      print query
      return self.db.query_db(query)

    def delete_course(self, course_id):
      print "deleting course"
      query = "DELETE FROM courses where id = {}".format(int(course_id))
      return self.db.query_db(query) 
