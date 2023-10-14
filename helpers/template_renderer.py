from jinja2 import Environment, FileSystemLoader

class TemplateRenderer:
    def __init__(self, template_folder):
        self.env = Environment(loader=FileSystemLoader(template_folder))

    def render_template(self, template_name, data):
        template = self.env.get_template(template_name)
        return template.render(data)