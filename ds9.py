#Python library for accessing DS9 and XPA.
#Written by Kyle Kaplan March 2014.
import subprocess
from subprocess import call, PIPE #Allow python to access command line
from subprocess import check_output #Allow python to access command line and return result to a variable
import time #To put in delays
  

#Open DS9
def open():
  call('xpans &', shell=True) #Load XPA immediately, so XPA commands can be sent to ds9
  call('ds9 &', shell=True) #Load DS9
  time.sleep(2) #Give computer a few seconds to respond after opening DS9
  
def close():
  call('xpaset -p ds9 exit')
  
#Get xpaget statements from ds9
def get(command):
  result = check_output('xpaget ds9 ' + command, shell=True) #Get information from ds9 using XPA get
  return str(result).strip() #return information grabbed from ds9

#Send xpaset commands to ds9
def set(command):
  call('xpaset -p ds9 ' + command, shell=True)
  #time.sleep(0.5) #Set delay after each command to give computer time to respond before the next command

#Allow user to set delays in DS9 scripts
def wait(delay):
  time.sleep(delay)

#Special command for drawing regions onto ds9
def draw(command):
  #print 'echo "' + command + '" | xpaset ds9 regions'
  call('echo "' + command + '" | xpaset ds9 regions', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
  
def rot(angle):
  set('rotate '+str(angle))

def rotto(angle):
  set('rotate to '+str(angle))
  
def north():
  set('rotate to 0')

def show(fits_file, new = False):
  if new: #Check if there are any frames, default no, but user can set new = True
    set('frame new') #If not create a new frame
  set('fits '+ fits_file) #open fits file
  set('scale log') #Set view to log scale
  set('scale Zscale') #Set scale limits to Zmax, looks okay
