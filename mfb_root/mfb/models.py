# Models = Define the structure of the database
# after making any change to models.py you need to migrate django so that proper SQL backend operation is done based on the updates.

from django.db import models

# Create your models here.


class projects(models.Model):                                       # name of the table
    project_name = models.CharField(
        max_length=100, blank=False, default="NONAME")     # name of column 2
    # how to define date in django modules
    project_date_created = models.DateField(auto_now=True)
    project_date_last_executed = models.DateField(auto_now=True)
    project_status_list = (
        ('NOT STARTED', 'The project is not yet started'),
        ('RUNNING', 'The project is running now'),
        ('STOPPED', 'The was running earlier, but now it is stopped'),
        ('COMPLETED', 'The project has finished execution')
    )
    project_status = models.CharField(
        max_length=50, choices=project_status_list, blank=False, default='NOT STARTED')

    # used by django admin to return a string representation of the given object.
    def __str__(self):
        return self.project_name
        # return 'Project name is "{0}" and Date created is "{1}"'.format(self.project_name, self.project_date_created)


class tools(models.Model):
    tool_name = models.CharField(max_length=100, blank=False)
    tool_is_3rd_party = models.BooleanField(blank=False)
    tool_satisfies_m001 = models.BooleanField(blank=False, default=False)
    tool_satisfies_m002 = models.BooleanField(blank=False, default=False)
    tool_satisfies_m003 = models.BooleanField(blank=False, default=False)
    tool_satisfies_m004 = models.BooleanField(blank=False, default=False)
    tool_satisfies_m005 = models.BooleanField(blank=False, default=False)
    tool_satisfies_m006 = models.BooleanField(blank=False, default=False)
    tool_deployed_as_docker = models.BooleanField(blank=False, default=False)
    tool_deployed_as_python_script = models.BooleanField(
        blank=False, default=False)
    tool_deployed_as_bash_script = models.BooleanField(
        blank=False, default=False)
    tool_deployed_as_powershell_script = models.BooleanField(
        blank=False, default=False)

    # used by django admin to return a string representation of the given object.
    def __str__(self):
        return self.tool_name


class methodology(models.Model):
    methodology_id = models.ForeignKey(projects, on_delete=models.CASCADE)
    methodology_name = models.CharField(max_length=100, blank=False)
    # Methodology name is not needed as it is same as project name

    # used by django admin to return a string representation of the given object.
    def __str__(self):
        return self.methodology_name


class checklists(models.Model):
    check_name = models.CharField(max_length=100)
    check_details = models.CharField(max_length=100)
    check_vuln_root_cause = models.CharField(max_length=100)
    check_remediation = models.CharField(max_length=100)
    check_tags = models.CharField(max_length=100)
    check_patch_references = models.CharField(max_length=100)
    check_exploit_references = models.CharField(max_length=100)

    # used by django admin to return a string representation of the given object.
    def __str__(self):
        return self.check_name
