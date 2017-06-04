from unittest import TestCase

from template.template_engine import Template


class TestTemplate(TestCase):

    def test_render(self):
        html = '''
<h1>Hello {{name|upper}} {{surnames.good}}!</h1>
{% for topic in topics %}
    <p>You want some {{topic|coursify}}</p>
{% endfor %}
<p>This is some extra text</p>
        '''
        template = Template(html)
        template.compile()
        result = template.render({
            'upper': str.upper,
            'name': "Ned",
            'coursify': lambda x: x + " courses",
            'surnames': {'good': 'Waynerman', 'better': 'Vinerman', 'best': 'Winerman'},
            'topics': ['Python', 'Geometry', 'Juggling']
        })

        expected = '''
<h1>Hello NED Waynerman!</h1>

    <p>You want some Python courses</p>

    <p>You want some Geometry courses</p>

    <p>You want some Juggling courses</p>

<p>This is some extra text</p>
        '''

        self.assertEqual(result, expected)