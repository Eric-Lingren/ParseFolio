class TemplateData:
    # def __init__(self, template_folder):
    #     self.env = Environment(loader=FileSystemLoader(template_folder))

    def get_table_template_data(self, template_name, data):
        template = self.env.get_template(template_name)
        return template.render(data)