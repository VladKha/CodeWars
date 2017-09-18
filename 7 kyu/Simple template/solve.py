from jinja2 import Template


def create_template(template):
    return lambda **vals: Template(template).render(vals)
