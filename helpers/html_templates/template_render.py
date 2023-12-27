from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from helpers.chart import Chart


class TemplateRender:
    TIMESTAMP = None
    env = None
    DF = None

    def __init__(self, template_folder, TIMESTAMP, CSV_FILE_NAME, DF):
        self.env = Environment(loader=FileSystemLoader(template_folder))
        self.TIMESTAMP = TIMESTAMP
        self.CSV_FILE_NAME = CSV_FILE_NAME
        self.DF = DF


    def build_report(self):
        table_component = self.generate_trade_report_table()
        trade_counts_by_symbol_chart = Chart.generate_trade_counts_by_symbol(self.DF)
        average_trade_duration_by_symbol_chart = Chart.generate_average_trade_duration_by_symbol(self.DF)

        full_html_report = self.compile_full_report(table_component=table_component, trade_counts_by_symbol_chart=trade_counts_by_symbol_chart, average_trade_duration_by_symbol_chart=average_trade_duration_by_symbol_chart)
        self.save_html_file(html_content=full_html_report)


    def _render_template(self, template_name, data):
        """
        Description:
        This function serves as a universal helper for rendering HTML templates using the Jinja2 template engine.
        It takes the name of the template file (template_name) and a dictionary of data (data) to be injected into the template.
        The function loads the template from the Jinja2 environment associated with the class instance and renders it with the provided data.
        The compiled HTML content is then returned.

        Parameters:
        - template_name (str): The name of the Jinja2 template file to be rendered.
            I.E. template_name = 'index.html'
        - data (dict): A dictionary containing the data to be injected into the template.
            I.E. data = {'title': 'Welcome', 'content': 'Hello, World!'}

        Returns:
        - str: The compiled HTML content generated by rendering the template with the provided data.

        Raises:
        - TemplateNotFound: If the specified template file is not found in the Jinja2 environment.
        """
        try:
            template = self.env.get_template(template_name)
        except TemplateNotFound as e:
            raise TemplateNotFound(f"Template not found: {template_name}") from e
        return template.render(data)

    
    def generate_trade_report_table(self):
        table_data = { 'tableTitle': 'MY TABLE TITLE', 'df': self.DF}
        table_component = self._render_template('/components/table_component.html', table_data)
        return table_component


    def compile_full_report(self, table_component, trade_counts_by_symbol_chart, average_trade_duration_by_symbol_chart):
        data = {
            'title': 'Analysis Report',
            'description': 'This is a sample analysis report.',
            'table_component': table_component,  # Injected table component
            'trade_counts_by_symbol_chart': trade_counts_by_symbol_chart, 
            'average_trade_duration_by_symbol_chart': average_trade_duration_by_symbol_chart, 
        }
        html_content = self._render_template('base_template.html', data)
        return html_content


    def save_html_file(self, html_content):
        html_output_filename = f'./data/reports/{self.TIMESTAMP}_{self.CSV_FILE_NAME}-report.html'
        with open(html_output_filename, 'w') as f:
            f.write(html_content)
        print(f'Report written. File saved in {html_output_filename}')



