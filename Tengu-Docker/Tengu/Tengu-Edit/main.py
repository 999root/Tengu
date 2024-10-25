from flask import Flask, render_template, request, redirect, url_for, flash
import os
import shutil

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Set your base folder for editable files and directories
BASE_DIR = os.path.join(os.getcwd(), '', 'app', 'templates')


def get_all_files_and_directories(path):
    """Get list of all files and directories in the given path."""
    items = os.listdir(path)
    directories = [item for item in items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in items if os.path.isfile(os.path.join(path, item)) and item.endswith('.html')]
    return directories, files


@app.route('/')
@app.route('/<path:subpath>')
def index(subpath=''):
    """Display files and directories."""
    current_path = os.path.join(BASE_DIR, subpath)

    if not os.path.exists(current_path):
        return "Path not found", 404

    directories, files = get_all_files_and_directories(current_path)

    # Calculate parent directory for "Go Up" functionality
    parent_dir = os.path.dirname(subpath) if subpath else None

    return render_template('directory_view.html', directories=directories, files=files, subpath=subpath, parent_dir=parent_dir)


@app.route('/new_directory', methods=['GET', 'POST'])
@app.route('/<path:subpath>/new_directory', methods=['GET', 'POST'])
def new_directory(subpath=''):
    """Create a new directory."""
    current_path = os.path.join(BASE_DIR, subpath)

    if request.method == 'POST':
        dir_name = request.form['directory_name']
        new_dir_path = os.path.join(current_path, dir_name)
        try:
            if not os.path.exists(new_dir_path):
                os.makedirs(new_dir_path)
                flash(f"Directory '{dir_name}' created successfully.", 'success')
            else:
                flash(f"Directory '{dir_name}' already exists.", 'error')
        except Exception as e:
            flash(f"Failed to create directory: {e}", 'error')

        return redirect(url_for('index', subpath=subpath))

    return render_template('new_directory.html', subpath=subpath)


@app.route('/new_file', methods=['GET', 'POST'])
@app.route('/<path:subpath>/new_file', methods=['GET', 'POST'])
def new_file(subpath=''):
    """Create a new HTML file."""
    current_path = os.path.join(BASE_DIR, subpath)

    if request.method == 'POST':
        filename = request.form['filename']
        if not filename.endswith('.html'):
            filename += '.html'
        file_path = os.path.join(current_path, filename)
        try:
            with open(file_path, 'w') as f:
                f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>New File</title>\n</head>\n<body>\n</body>\n</html>')
            flash(f"File '{filename}' created successfully.", 'success')
        except Exception as e:
            flash(f"Failed to create file: {e}", 'error')

        return redirect(url_for('index', subpath=subpath))

    return render_template('new.html', subpath=subpath)


@app.route('/edit/<path:filepath>', methods=['GET', 'POST'])
def edit_file(filepath):
    """Edit an existing HTML file."""
    file_path = os.path.join(BASE_DIR, filepath)

    if request.method == 'POST':
        content = request.form['content']
        with open(file_path, 'w') as f:
            f.write(content)
        flash(f"File '{filepath}' saved successfully.", 'success')
        return redirect(url_for('index', subpath=os.path.dirname(filepath)))

    # Check if the file exists before trying to read it
    if not os.path.exists(file_path):
        return "File not found", 404

    with open(file_path, 'r') as f:
        content = f.read()

    return render_template('editor.html', filename=os.path.basename(filepath), content=content)


@app.route('/delete_file/<path:filepath>', methods=['POST'])
def delete_file(filepath):
    """Delete an existing file."""
    file_path = os.path.join(BASE_DIR, filepath)
    try:
        os.remove(file_path)
        flash(f"File '{filepath}' deleted successfully.", 'success')
    except Exception as e:
        flash(f"Failed to delete file: {e}", 'error')
    
    return redirect(url_for('index', subpath=os.path.dirname(filepath)))


@app.route('/delete_directory/<path:dirpath>', methods=['POST'])
def delete_directory(dirpath):
    """Delete an existing directory."""
    dir_path = os.path.join(BASE_DIR, dirpath)
    try:
        shutil.rmtree(dir_path)
        flash(f"Directory '{dirpath}' deleted successfully.", 'success')
    except Exception as e:
        flash(f"Failed to delete directory: {e}", 'error')
    
    return redirect(url_for('index', subpath=os.path.dirname(dirpath)))


if __name__ == '__main__':
    # Create the base directory if it doesn't exist
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    app.run(debug=True, port=8080)