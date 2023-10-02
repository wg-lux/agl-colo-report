def as_bootstrap(form):
    bootstrap_form = ""
    for field in form:
        bootstrap_form += f'<div class="form-group">{field.label_tag()} {field}</div>'
    return bootstrap_form