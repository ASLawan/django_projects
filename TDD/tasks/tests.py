from django.test import TestCase
from .models import Task
from .forms import NewTaskForm, UpdateTaskForm
# Create your tests here.

class TaskModelTest(TestCase):
    def test_task_model_exists(self):
        """Test if the model exists"""
        tasks = Task.objects.count()

        self.assertEqual(tasks, 0)
    
    def test_model_has_str_representation(self):
        """Tests if model has string representation method"""
        task = Task.objects.create(title="Learn Django")

        self.assertEqual(str(task), task.title)


class IndexPageTest(TestCase):

    def setUp(self):
        """Prepare environment for test cases"""
        self.task = Task.objects.create(title="Learn Django")

    def test_index_page_returns_correct_response(self):
        """Tests if home page returns right response"""
        response = self.client.get("/")

        self.assertTemplateUsed(response, "tasks/index.html")
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_has_tasks(self):
        """Test if home page contains text"""
        response = self.client.get("/")

        self.assertContains(response, self.task)

class DetailPageTest(TestCase):

    def setUp(self):
        """Prepare environment for test cases"""
        self.task = Task.objects.create(title="Learn Django",
                                        description="Makes of you a better Python developer")
        self.task2 = Task.objects.create(title="Build Ticket",
                                        description="Cuz then you get to build a lifetime business")
    def test_detail_page_returns_correct_response(self):
        """Tests if home page returns right response"""
        response = self.client.get(f"/{self.task.id}/")

        self.assertTemplateUsed(response, "tasks/detail.html")
        self.assertEqual(response.status_code, 200)
    
    def test_detail_page_contains_right_information(self):
        """Test detail page content"""
        response = self.client.get(f"/{self.task.id}/")

        self.assertContains(response, self.task.title)
        self.assertContains(response, self.task.description)
        self.assertNotContains(response, self.task2.title)
        self.assertNotContains(response, self.task2.description)
    

class NewPageTest(TestCase):

    def setUp(self):
        self.form = NewTaskForm

    def test_new_page_returns_correct_response(self):
        """Test that a new page returns correct response"""
        response = self.client.get("/new/")

        self.assertTemplateUsed(response, "tasks/new.html")
        self.assertEqual(response.status_code, 200)
    
    def test_form_can_be_valid(self):
        """Test that the new form instance can be valid"""
        self.assertTrue(issubclass(self.form, NewTaskForm))
        self.assertTrue('title', self.form.Meta.fields)
        self.assertTrue('description', self.form.Meta.fields)
        # test for valid form
        form = self.form(
            {
                'title': 'Learn Django',
                'description': 'It will change your life'
            }
        )
        self.assertTrue(form.is_valid())


    def test_new_page_form_rendering(self):
        """Test that form is being rendered on new page"""
        response = self.client.get("/new/")

        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<label for')

        # test for invalid form

        response = self.client.post('/new/',
            {
                'title': "",
                'description': 'Description with no title'
            }
        )

        self.assertContains(response, '<ul class="errorlist">')
        self.assertContains(response, 'This field is required')
    

    def test_page_redirect(self):
        """Test the redirect route after form submission"""
        response = self.client.post(
            '/new/',
            {
                'title': 'Improvement',
                'description': "I am getting better and better by the day"
            }
        )

        expected_url = "/"

        self.assertRedirects(response, expected_url)
        self.assertEqual(Task.objects.count(), 1)


class UpdatePageTest(TestCase):

    def setUp(self):
        """Prepares environment for the subsequent tests"""
        self.task = Task.objects.create(
            title='Update Test',
            description='Testing if update works as expected'
        )

        self.form = UpdateTaskForm
    
    def test_update_page_returns_correct_response(self):
        """Test update page renders correctly"""
        response = self.client.get(f"/{self.task.id}/update/")
        template = "tasks/update.html"
        self.assertTemplateUsed(response, template)
        self.assertEqual(response.status_code, 200)
    

    def test_form_can_be_valid(self):
        """Test if form is valid upon update"""
        self.assertTrue(issubclass(self.form, UpdateTaskForm))
        self.assertTrue('title', self.form.Meta.fields)
        self.assertTrue('description', self.form.Meta.fields)
        # test for valid form
        form = self.form(
            {
                'title': 'Update Test Updated',
                'description': 'It will change your life'
            }, 
            instance=self.task
        )
        self.assertTrue(form.is_valid())

        form.save()

        self.assertTrue(self.task.title, "Update Test Updated")
    
    def test_form_can_be_invalid(self):
        """Test if update form can be invalid"""
        form = self.form(
            {
                'title': '',
                'description': 'It will change your life'
            }, 
            instance=self.task
        )
        self.assertFalse(form.is_valid())
    

    def test_update_page_returns_correct_response(self):
        """Test that a new page returns correct response"""
        response = self.client.get(f"/{self.task.id}/update/")

        self.assertTemplateUsed(response, "tasks/update.html")
        self.assertEqual(response.status_code, 200)
    
    def test_form_can_be_valid(self):
        """Test that the new form instance can be valid"""
        self.assertTrue(issubclass(self.form, UpdateTaskForm))
        self.assertTrue('title', self.form.Meta.fields)
        self.assertTrue('description', self.form.Meta.fields)
        # test for valid form
        form = self.form(
            {
                'title': 'Learn Django',
                'description': 'It will change your life'
            }, instance=self.task
        )
        self.assertTrue(form.is_valid())


    def test_update_page_form_rendering(self):
        """Test that form is being rendered on new page"""
        response = self.client.get(f"/{self.task.id}/update/")

        self.assertContains(response, '<form')
        self.assertContains(response, 'csrfmiddlewaretoken')
        self.assertContains(response, '<label for')

        # test for invalid form

        response = self.client.post(f"/{self.task.id}/update/",
            {
                'title': "",
                'description': 'Description with no title'
            }
        )

        self.assertContains(response, '<ul class="errorlist">')
        self.assertContains(response, 'This field is required')
    

    def test_update_page_redirect(self):
        """Test the redirect route after form submission"""
        response = self.client.post(
            '/new/',
            {
                'title': 'Improvement',
                'description': "I am getting better and better by the day"
            }, instance=self.task
        )

        expected_url = "/"

        self.assertRedirects(response, expected_url)
        self.assertEqual(Task.objects.count(), 2)


class DeletePageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title="Learn Django")


    def test_delete_page_deletes_task(self):
        """Tests the if we can delete tasks"""
        self.assertEqual(Task.objects.count(), 1)

        response = self.client.get(f"/{self.task.id}/delete/")
        expected_url = "/"

        self.assertRedirects(response, expected_url)
        self.assertEqual(Task.objects.count(), 0)