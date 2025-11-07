from cx_Freeze import setup, Executable
import sys
base= 'Win32GUI' if sys.platform=='win32' else None

# List of Python files to include
files_to_include = ['images', 'ad_login.py', 'admin.py', 'app.py', 'teacher_login.py', 'st_login.py',  'register.py', 'reg_cl_data.py', 'show_br_data.py', 'show_yr_data.py', 'teacher.py', 'student.py', 'show_cl_data.py']

setup(
    name="MyApp",
    version="0.1",
    description="My Merged Python Application",
    executables=[Executable("app.py",  base=base, icon="images/logo.ico")],
    options={
        'build_exe': {
            'include_files':files_to_include,
        }
    }
)