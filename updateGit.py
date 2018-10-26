
import os
import shutil
import tempfile

def update_date_file_in_remote_git_repository(in_repo_url):
	"""Clones the remote Git repository at supplied URL and adds/updates a .date file
	containing the current date and time. The changes are then pushed back to the remote Git repository.
	"""
	# Create temporary directory to clone the Git project into.
	repo_path = tempfile.mkdtemp()
	print("Repository path: " + repo_path)
	date_file_path = repo_path + '/.date'

	try:
		# Clone the remote GitHub repository.
		git_clone(in_repo_url, repo_path)

		# Create/update file with current date and time.
		if os.path.exists(date_file_path):
			os.remove(date_file_path)
		execute_shell_command('date > ' + date_file_path, repo_path)

		# Add new .date file to repository, commit and push the changes.
		git_add(date_file_path, repo_path)
		git_commit('Updated .date file', repo_path)
		git_push(repo_path)
	finally:
		# Delete the temporary directory holding the cloned project.
		shutil.rmtree(repo_path)
