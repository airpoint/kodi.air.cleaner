#
#   Air Cleaner
#	
#	Fork (C) 2015 @airpoint
#   Original code (C) 2015  Spencer Kuzara
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


import urllib,urllib2,re, time
import xbmcgui,xbmcplugin,xbmcaddon
import os

thumbnailPath = xbmc.translatePath('special://thumbnails');
cachePath = os.path.join(xbmc.translatePath('special://home'), 'cache')
tempPath = xbmc.translatePath('special://temp')
addonId = xbmcaddon.Addon().getAddonInfo('id')
addonPath = os.path.join(os.path.join(xbmc.translatePath('special://home'), 'addons'),addonId)
mediaPath = os.path.join(addonPath, 'media')
databasePath = xbmc.translatePath('special://database')


#RUN ALL SCRIPTS
def clearAll():
	choice = xbmcgui.Dialog().yesno('Air Cleaner', 'This will delete all the temporary files, cache and thumbnails from your device. Do you want to continue?', nolabel='Cancel',yeslabel='Continue')
	if choice == 0:
		return
	elif choice == 1:
		pass

	dp = xbmcgui.DialogProgress()
	dp.create('Air Cleaner','Deleting cache...')
	time.sleep(2)

	dp.update(50,'Deleting cache...')
	clearCache()
	time.sleep(1)

	dp.update(75,'Deleting packages...')
	purgePackages()
	time.sleep(1)

	dp.update(100,'Deleting thumbnails...')
	deleteThumbnails()
	time.sleep(1)

	dp.close()
	xbmcgui.Dialog().ok('Air Cleaner','All clean!')


#CLASSES
class cacheEntry:
	def __init__(self, namei, pathi):
		self.name = namei
		self.path = pathi

#WORK FUNCTIONS
def setupCacheEntries():
	entries = 5 #make sure this reflects the amount of entries you have
	dialogName = ["WTF", "4oD", "BBC iPlayer", "Simple Downloader", "ITV"]
	pathName = ["special://profile/addon_data/plugin.video.whatthefurk/cache", "special://profile/addon_data/plugin.video.4od/cache",
					"special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache","special://profile/addon_data/script.module.simple.downloader",
					"special://profile/addon_data/plugin.video.itv/Images"]
					
	cacheEntries = []
	
	for x in range(entries):
		cacheEntries.append(cacheEntry(dialogName[x],pathName[x]))
	
	return cacheEntries


#SCRIPTS
def clearCache():
	if os.path.exists(cachePath)==True:
		for root, dirs, files in os.walk(cachePath):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				for f in files:
					try:
						if (f == "xbmc.log" or f == "xbmc.old.log"): continue
						os.unlink(os.path.join(root, f))
					except:
						pass
				for d in dirs:
					try:
						shutil.rmtree(os.path.join(root, d))
					except:
						pass

	if os.path.exists(tempPath)==True:
		for root, dirs, files in os.walk(tempPath):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				for f in files:
					try:
						if (f == "xbmc.log" or f == "xbmc.old.log"): continue
						os.unlink(os.path.join(root, f))
					except:
						pass
				for d in dirs:
					try:
						shutil.rmtree(os.path.join(root, d))
					except:
						pass

	if xbmc.getCondVisibility('system.platform.ATV2'):
		atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
		
		for root, dirs, files in os.walk(atv2_cache_a):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				for f in files:
					os.unlink(os.path.join(root, f))
				for d in dirs:
					shutil.rmtree(os.path.join(root, d))

		atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
		
		for root, dirs, files in os.walk(atv2_cache_b):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				for f in files:
					os.unlink(os.path.join(root, f))
				for d in dirs:
					shutil.rmtree(os.path.join(root, d))
				
	cacheEntries = setupCacheEntries()
										 
	for entry in cacheEntries:
		clear_cache_path = xbmc.translatePath(entry.path)
		if os.path.exists(clear_cache_path)==True:    
			for root, dirs, files in os.walk(clear_cache_path):
				file_count = 0
				file_count += len(files)
				if file_count > 0:
					for f in files:
						os.unlink(os.path.join(root, f))
					for d in dirs:
						shutil.rmtree(os.path.join(root, d))


def purgePackages():
	purgePath = xbmc.translatePath('special://home/addons/packages')
	for root, dirs, files in os.walk(purgePath):
			file_count = 0
			file_count += len(files)
	for root, dirs, files in os.walk(purgePath):
		file_count = 0
		file_count += len(files)
		if file_count > 0:            
			for f in files:
				os.unlink(os.path.join(root, f))
			for d in dirs:
				shutil.rmtree(os.path.join(root, d))

	
def deleteThumbnails():
	if os.path.exists(thumbnailPath)==True:
		for root, dirs, files in os.walk(thumbnailPath):
			file_count = 0
			file_count += len(files)
			if file_count > 0:
				for f in files:
					try:
						os.unlink(os.path.join(root, f))
					except:
						pass
	text13 = os.path.join(databasePath,"Textures13.db")
	try:
		os.unlink(text13)
	except:
		pass

clearAll()