from pypresence import Presence
import time
import json
import os
import datetime
import calendar
import tkinter as tk  
from tkinter import ttk

# set default start once the app start run
now = datetime.datetime.utcnow()
timeStamp = calendar.timegm(now.utctimetuple())
myStart = str(timeStamp)

# read json file
if os.path.exists(os.getcwd() + '/config.json'):
    # if json file exist, read it!
    with open("./config.json") as f:
        configData = json.load(f)
else:
    # if json file not exist, create new one with these template
    configTemplate = { 
        "Client_ID": ""
    }
    # write the template
    with open (os.getcwd() + '/config.json', 'w+') as f:
        json.dump(configTemplate, f, indent=4, sort_keys=False)

# Load uid on json
myClientID = configData["Client_ID"]

# Start the RPC
RPC = Presence(str(myClientID))
RPC.connect()

# Window
app = tk.Tk() # Application Name  
app.iconbitmap('E:\Icons\Applications\Icon.ico')
app.title("AX.Discord Rich Presence") # Label
app.geometry("290x310") # Size

# Label
label_state = ttk.Label(app, text = "State:")# Click event  
label_state.place(x=5, y=5)

label_details = ttk.Label(app, text = "Details:")# Click event  
label_details.place(x=5, y=50) # +45

label_LImage = ttk.Label(app, text = "Large Image:")# Click event  
label_LImage.place(x=5, y=95) # +45

label_SImage = ttk.Label(app, text = "Small Image:")# Click event  
label_SImage.place(x=5, y=140) # +45

label_LImageT = ttk.Label(app, text = "Large Image Tooltip:")# Click event  
label_LImageT.place(x=5, y=185) # +45

label_SImageT = ttk.Label(app, text = "Small Image Tooltip:")# Click event  
label_SImageT.place(x=5, y=230) # +45

# Click event
def CMDStatus():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
def CMDDetails():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
def CMDLimage():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
def CMDSimage():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
def CMDLimageT():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
def CMDSimageT():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
def CMDConnect():
    try:
        RPC.update(state=state.get(), details=details.get(), large_image=limage.get(), small_image=simage.get(), large_text=limaget.get(), small_text=simaget.get(), start=myStart)
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Rich Presence updated.')
        
def CMDDisconnect():
    try:
        RPC.close()
    except Exception:
        print('Something went wrong while updating rich Presence')
    else:
        print('Disconnected')
        app.quit()

# Widget text box 
state = tk.StringVar() 
stateEntered = ttk.Entry(app, width = 30, textvariable = state) 
stateEntered.place(x=5, y=25)

details = tk.StringVar() 
detailsEntered = ttk.Entry(app, width = 30, textvariable = details) 
detailsEntered.place(x=5, y=70) # +45 

limage = tk.StringVar() 
limageEntered = ttk.Entry(app, width = 30, textvariable = limage) 
limageEntered.place(x=5, y=115) # +45 

simage = tk.StringVar() 
simageEntered = ttk.Entry(app, width = 30, textvariable = simage) 
simageEntered.place(x=5, y=160) # +45 

limaget = tk.StringVar() 
limagetEntered = ttk.Entry(app, width = 30, textvariable = limaget) 
limagetEntered.place(x=5, y=205) # +45 

simaget = tk.StringVar() 
simagetEntered = ttk.Entry(app, width = 30, textvariable = simaget) 
simagetEntered.place(x=5, y=250) # +45 

# Buttons position
SetState = ttk.Button(app, text = "Update", command = CMDStatus)
SetState.place(x=210, y=23)

SetDetail = ttk.Button(app, text = "Update", command = CMDDetails)
SetDetail.place(x=210, y=69) # +46 

SetLImage = ttk.Button(app, text = "Update", command = CMDLimage)
SetLImage.place(x=210, y=113) # +43 

SetSImage = ttk.Button(app, text = "Update", command = CMDSimage)
SetSImage.place(x=210, y=156) # +43 

SetLImageT = ttk.Button(app, text = "Update", command = CMDLimageT)
SetLImageT.place(x=210, y=199) # +43 

SetSImageT = ttk.Button(app, text = "Update", command = CMDSimageT)
SetSImageT.place(x=210, y=242) # +43 

ConnectButton= ttk.Button(app, text="Connect", command= CMDConnect)
# ConnectButton.pack(side=tk.BOTTOM, padx=5, pady=5)
ConnectButton.place(x=5, y=275)

DisconnectButton= ttk.Button(app, text="Disconnect", command= CMDDisconnect)
# DisconnectButton.pack(side=tk.BOTTOM, padx=5, pady=5)
DisconnectButton.place(x=210, y=275) 

app.mainloop()

# print(RPC.update(state='myState', details='myDetails', large_image='py-large', small_image='py-file', large_text='myLargeText', small_text='mySmallText', start=myStart))

# while True:
#     time.sleep(15)