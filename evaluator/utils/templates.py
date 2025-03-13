from jinja2 import Environment


def render_template(template, **kwargs):
    env = Environment()
    template = env.from_string(template)
    return template.render(**kwargs)
