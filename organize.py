import os
import shutil
import tkFileDialog


class OrganizeSingleFolder:
	def __init__(self):
		self.movedcounter = 0
		self.unmovedcounter = 0

		ext_and_folder = [
			
         	((".mp4", ".3gp", ".avi", ".flv", ".mkv"), "Videos"),
         	((".pdf"), "Pdfs"),
         	((".doc", ".docx", '.docm', '.dotx', '.dot', '.dotm'), "WordDocs"),
         	((".jpg", ".png", ".jpeg", ".gif"), "Pictures"),
         	((".html", ".htm"), "Webpages"),
         	(('.zip', '.tar', '.gz', '.rar'), "Compressed"),
         	((".msi", ".exe"), "Setups"),
         	((".ppt"), "Presentation"),
         	((".mp3", ".m4a", ".wav", ".wma"), "Music")
         ]

		
		#self.topdir = raw_input('Enter the path of the folder to organize>> ')
		self.topdir = tkFileDialog.askdirectory()
		if os.path.isdir(self.topdir) and self.topdir != '':
			print "*" * 70
			print "The directory to organize is %s" %self.topdir
			print "*" * 70

			allfiles = os.listdir(self.topdir) #a list of all files in topdir

			self.organize(allfiles, ext_and_folder)

		else:
			print "%s is not a valid directory" %self.topdir

		if self.movedcounter > 0:
			print self.movedcounter, 'files moved.'
		if self.unmovedcounter > 0:
			print self.unmovedcounter, 'files not moved.'

	def organize(self, allfiles, ext_folder_pair):
		for eachfile in allfiles:
			ext = os.path.splitext(eachfile)[1]
			if os.path.isfile(os.path.join(self.topdir, eachfile)):

				for extension, folder in ext_folder_pair:
					if ext.lower() in extension:
						destfolder = os.path.join(self.topdir, folder)
						self.createFolder(os.path.join(self.topdir, destfolder))
						destfile = os.path.join(self.topdir, destfolder, eachfile)

						if self.fileExists(destfile):
							print destfile, "already exists."
							self.unmovedcounter += 1
						else:
							self.moveFile(os.path.join(self.topdir, eachfile),
								os.path.join(self.topdir, destfolder))
							self.movedcounter += 1

	def createFolder(self, foldername):
		if os.path.isdir(foldername):
			pass
		else:
			os.mkdir(foldername)
			#print foldername, "was created successfully"

	def fileExists(self, destpath):
		if os.path.isfile(destpath):
			return True
		else:
			return False

	def moveFile(self, src, dest):
		try:
			if os.path.isdir(dest):

				shutil.move(src, dest)
				print src, "moved"
		except shutil.Error:
			print "%s could not be moved to %s" %(src, dest)


class OrganizeWholeFolder(OrganizeSingleFolder):
	"""Scan through every directory and subdirectories in the top directory
	and put the files into the appropriate folder based on extension
	"""
	def __init__(self):
		self.movedcounter = 0
		self.unmovedcounter = 0

		ext_and_folder = [((".mp3", ".m4a", ".wma", ".wav"), "Music"),
         ((".mp4", ".3gp", ".avi", ".flv", ".mkv"), "Videos"),
         (".pdf", "Pdfs"),
         ((".doc", ".docx", '.docm', '.dotx', '.dot', '.dotm'), "WordDocs"),
         ((".jpg", ".png", ".jpeg", ".gif"), "Pictures"),
         ((".html", ".htm"), "Webpages"),
         (('.zip', '.tar', '.gz', '.rar'), "Compressed"),
         ((".msi", ".exe"), "Setups"),
         ((".ppt"), "Presentation")
         ]

		#self.topdir = raw_input('Enter the directory to organize >> ')
		self.topdir = tkFileDialog.askdirectory()
		if os.path.isdir(self.topdir) and self.topdir != '':
			allfiles = self.dirWalker()
			self.organize(allfiles, ext_and_folder)


	def dirWalker(self):
		allfiles = []
		for dirpath, dirnames, filenames in os.walk(self.topdir):
			for filename in filenames:
				allfiles.append(os.path.join(dirpath, filename))
		return allfiles

	def organize(self, allfiles, ext_folder_pair):

		for eachfile in allfiles:
			ext = os.path.splitext(eachfile)[1]
			if os.path.isfile(os.path.join(self.topdir, eachfile)):
				for extension, folder in ext_folder_pair:
					if ext.lower() in extension:
						destfolder = os.path.join(self.topdir, folder)
						filename = os.path.split(eachfile)[1]
						destpath = os.path.join(destfolder, filename)

						OrganizeSingleFolder.createFolder(self, destfolder)

						if OrganizeSingleFolder.fileExists(self, destpath):
							print destpath, "already exists."
							self.unmovedcounter += 1
						else:
							OrganizeSingleFolder.moveFile(self, os.path.join(self.topdir,
								eachfile), os.path.join(self.topdir, 
								destfolder))
							self.movedcounter += 1
