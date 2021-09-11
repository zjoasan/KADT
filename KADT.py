#!/usr/bin/python3 
# Kodi Addon Dev-tool (first rough draft, no fancy icons or tabs yet)
#learning github in vscode"
# using appjar (pip3 install appjar)

# import the needed librarys
import re
from appJar import gui

# create a GUI variable called App
App = gui("Addon Dev-tool", "1200x720")

# Setting some needed globals
Toolbarcount = 0

#----------------------------------old code, yet to be removed
objlabel = []
objtype = []
#----------------------------------end oldcode

elename = ""
focelename = "notusedyet"
lblasso = [
    {
        'labelnm':"",
        'objnm':""
    }
]

elementlist = [
    {
        'guiname':"",       #the appjar object name
        #setting tag
        'elid':"",          #kodi element id
        'eltyp':"",         #kodi element type
        'ellabel':"",       #kodi element label
        'elhelp':"",        #kodi element help
        #leveltag
        'ellevel':"",       #kodi element settings level
        #default tag
        'eldefault':"",     #kodi element default value
        #constraints tag
        'addontype':"",     #kodi element constraint addon
        'allowempty':"",    #kodi element true if omitted
        'writeable':"",     #kodi element option if a file is writeable
        'masking':"",       #kodi element file masking
        'source':"",        #kodi element video/audio/picture/program
        'min':"",           #kodi element min value of slider
        'step':"",          #kodi element step value of slider
        'max':"",           #kodi element max value of slider
        'sorting':"",       #kodi element sorting accending/descending
        #controltype tag
        'elctype':"",       #kodi element controltype
        'elformat':"",      #kodi element format
        'elcoption':"",     #kodi element control option, hidden/popup
        'elmultiselect':"", #kodi element multiselect
        'show':"",          #kodi element show
        'adata':"",         #kodi element action data RunScriptRunPlugin(plugin://$ID/fo/ $ID = your addon id, $CWD your addon path
        #subsetting
        'parent':"",        #kodi element subelements need parrant (el)id
        #conditions
        'dependencies':"",  #kodi element visibility/enable depends on other setting
        'visible':"",       #kodi element boolean if visible, default true
        'enable':"",        #kodi element boolean if enabled, default true
        'infobool':"",      #kodi element dependency if another setting is boolean true
        'condition':"",     #kodi element operator="!is", "lt", "gt" else eq
        'logicalop':""      #kodi element and/or for dependency
    }
]
#------------------------------old code
cpostring = ("# Addon language file \n"
"msgid \"\"\n"
"msgstr \"\"\n"
"\"Project-Id-Version: \n\""
"\"Report-Msgid-Bugs-To: \n\""
"\"POT-Creation-Date: YEAR-MO-DA HO:MI+ZONE\n\""
"\"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n\""
"\"Last-Translator: \n\""
"\"Language-Team: \n\""
"\"MIME-Version: 1.0\n\""
"\"Content-Type: text/plain; charset=UTF-8\n\""
"\"Content-Transfer-Encoding: 8bit\n\""
"\"Language: en\n\""
"\"Plural-Forms: nplurals=2; plural=(n != 1);\n\""
"\n"
"#. Strings for $addonname\n"  #replace $addonname name with addon-properties window in the future
"\n"
"msgctxt \"#32000\" \n"
"msgid \"$addonname Configuration\" \n"
"msgstr \"\"\n"
"\n")

settingxml = ("<settings>\n"
    "<category label=\"32000\">\n")
#----------------------------------------------end of old code

# Toolbar options
tools = ["-SEP-", "TEXT", "IP#", "NUMBER", "DATE", "TIME",
        "BOOL", "SELECT", "ADDON", "ENUM", "LABELENUM",
        "SLIDER", "FILE", "AUDIO", "VIDEO", "IMAGE",
        "EXECUTABLE", "FOLDER", "ACTION"]

# Menu options
fileMenus = ["Open", "Save", "Save as...", "-", "Export", "Print", "-", "Close"]

def rmstrnum ( intext ):
    pattern = r'[a-z]'
    out_string = re.sub(pattern, '', intext)
    return out_string

def rmnumstr ( intext ):
    pattern = r'[0-9]'
    out_string = re.sub(pattern, '', intext)
    return out_string

def reqw():
    return

def addonsave():
    return

def propclear():
    App.setEntry("propent1", "")
    App.setEntry("propent2", "")
    App.setEntry("propent3", "")
    App.setEntry("propent4", "")
    App.setEntry("propent5", "")
    App.setEntry("propent6", "")
    App.setEntry("propent6", "")
    App.setEntry("propent7", "")
    App.setEntry("propent8", "")
    App.setEntry("propent9", "")
    App.setEntry("propent10", "")
    App.setEntry("propent11", "")
    App.setEntry("propent12", "")
    App.setEntry("propent13", "")
    App.setEntry("propent14", "")
    App.setEntry("propent15", "")
    App.setEntry("propent16", "")
    App.setEntry("propent17", "")
    App.setEntry("propent18", "")
    App.setEntry("propent19", "")
    App.setEntry("propent20", "")
    App.setEntry("propent21", "")
    App.setEntry("propent22", "")
    App.setEntry("propent23", "")
    App.setEntry("propent24", "")
    App.setEntry("propent25", "")
    App.setEntry("propent26", "")
    App.setEntry("propent27", "")
    App.setEntry("propent28", "")
    return

def propsave():
    tempname = App.getLabel("swhead")
    temptype = rmnumstr(tempname)
    tempnum = rmstrnum(tempname)
    App.hideSubWindow("Properties")
    od = next(item for item in elementlist if item['guiname'] == tempname)
    od['guiname'] = App.getLabel("swhead")
    od['elid'] = App.getEntry("propent1")
    od['eltyp'] = App.getEntry("propent2")
    od['ellabel'] = App.getEntry("propent3")
    od['elhelp'] = App.getEntry("propent4")
    od['ellevel'] = App.getEntry("propent5")
    od['eldefault'] = App.getEntry("propent6")
    od['addontype'] = App.getEntry("propent7")
    od['allowempty'] = App.getEntry("propent8")
    od['writeable'] = App.getEntry("propent9")
    od['masking'] = App.getEntry("propent10")
    od['source'] = App.getEntry("propent11")
    od['min'] = App.getEntry("propent12")
    od['step'] = App.getEntry("propent13")
    od['max'] = App.getEntry("propent14")
    od['sorting'] = App.getEntry("propent15")
    od['elctype'] = App.getEntry("propent16")
    od['elformat'] = App.getEntry("propent17")
    od['elcoption'] = App.getEntry("propent18")
    od['elmultiselect'] = App.getEntry("propent19")
    od['show'] = App.getEntry("propent20"),
    od['adata'] = App.getEntry("propent21")
    od['parent'] = App.getEntry("propent22")
    od['dependencies'] = App.getEntry("propent23")
    od['visible'] = App.getEntry("propent24")
    od['enable'] = App.getEntry("propent25")
    od['infobool'] = App.getEntry("propent26"),
    od['condition'] = App.getEntry("propent27")
    od['logicalop'] = App.getEntry("propent28")
    print(str(od))
    if temptype == "label":
        App.setLabel(str(tempname), App.getEntry("propent3"))
    else:
        App.setEntry(tempname, App.getEntry("propent6"))
        App.setLabel("label"+str(tempnum), App.getEntry("propent3"))
    propclear()
    return

def propabort():
    App.hideSubWindow("Properties")
    propclear()
    return

def focname( obname ): # Needed since linux often focuses on the rightclick menu insted of the object that you clicked on
    global focelename
    focelename = obname
    return

def fillpropsw(elnm):
    propobj = next(dictionary for dictionary in elementlist if dictionary["guiname"] == elnm)
    App.setEntry("propent1", propobj.get("elid"))
    App.setEntry("propent2", propobj.get("eltyp"))
    App.setEntry("propent3", propobj.get("ellabel"))
    App.setEntry("propent4", propobj.get("elhelp"))
    App.setEntry("propent5", propobj.get("ellevel"))
    if rmnumstr(elnm) == "label":
        App.setEntry("propent6", str(App.getLabel(elnm)))
    else: 
        App.setEntry("propent6", str(App.getEntry(elnm)))
    App.setEntry("propent7", propobj.get("addontype"))
    App.setEntry("propent8", propobj.get("allowempty"))
    App.setEntry("propent9", propobj.get("writeable"))
    App.setEntry("propent10", propobj.get("masking"))
    App.setEntry("propent11", propobj.get("source"))
    App.setEntry("propent12", propobj.get("min"))
    App.setEntry("propent13", propobj.get("step"))
    App.setEntry("propent14", propobj.get("max"))
    App.setEntry("propent15", propobj.get("sorting"))
    App.setEntry("propent16", propobj.get("elctype"))
    App.setEntry("propent17", propobj.get("elformat"))
    App.setEntry("propent18", propobj.get("elcoption"))
    App.setEntry("propent19", propobj.get("elmultiselect"))
    App.setEntry("propent20", propobj.get("show"))
    App.setEntry("propent21", propobj.get("adata"))
    App.setEntry("propent22", propobj.get("parent"))
    App.setEntry("propent23", propobj.get("dependencies"))
    App.setEntry("propent24", propobj.get("visible"))
    App.setEntry("propent25", propobj.get("enable"))
    App.setEntry("propent26", propobj.get("infobool"))
    App.setEntry("propent27", propobj.get("condition"))
    App.setEntry("propent28", propobj.get("logicalop"))
    return

def rcMenu (rcchoice):
    global focelename
    elename = App.getFocus()
    if elename == None:
        elename = focelename
    elif elename == "Information":
        elename = focelename
    if rcchoice == "Properties":
        App.setLabel("swhead", elename)
        fillpropsw(elename)
        App.showSubWindow("Properties")
    elif rcchoice == "Delete":
        temptype = rmnumstr(elename)
        tempnum = rmstrnum(elename)
        if temptype == "label":
            App.removeLabel(elename)
            objectis = next(item for item in lblasso if item['labelnm'] == elename)
            relobj = objectis['objnm']
            relobjshort = rmnumstr(relobj)
            reloobjnum = rmstrnum(relobj)
            if relobj == "entry":
                App.removeEntry(relobj)
            elif relobj == "ipnum":
                App.removeEntry(relobj)
            elif relobj == "numbe":
                App.removeNumericEntry(relobj)
            # elif code to delete the other elementtypes and their related label when deleteing labels
            else:
                
                print(elename)
        elif temptype == "entry":
            App.removeLabel("label"+tempnum)
            App.removeEntry(elename)
        elif temptype == "ipnum":
            App.removeLabel("label"+tempnum)
            App.removeEntry(elename)
        elif temptype == "numbe":
            App.removeLabel("label"+tempnum)
            App.removeNumericEntry(elename)
        elif temptype == "sepel":
            if App.getLabel(elename) == "-":
                App.removeLabel(elename)
                App.removeLabel("seper"+tempnum)
            else:
                App.removeLabel(elename)
                App.removeLabel("lsepe"+tempnum)
        elif temptype == "seper":
            App.removeLabel("sepel"+tempnum)
            App.removeLabel(elename)
        elif temptype == "lsepe":
            App.removeLabel("sepel"+tempnum)
            App.removeLabel(elename)
        # elif Here to delete the other elementtypes and their related label when deleteing elements
        else:
            print(elename)
    else:
        # Here will be code for other rightclick choices
        print(rcchoice)
    return

App.createRightClickMenu("Information", False)
App.addMenuList("Information", ["Delete", "Properties"], rcMenu)

#------------------------------ old "workingcode"
def addxml ( objname, objnum):
    global Toolbarcount, objtype, objlabel, cpostring, settingxml
    entname = rmnumstr(objname)
    if entname == "entry":
        xmlstring = ("<setting id=\"" + objname + "\" type=\"string\" label=\"#" + str(32001 + objnum) + "\" help=\"\">\n"
	        "\t<level>0</level>\n"
	        "\t<default/>\n"
	        "\t<constraints>\n"
	        "\t\t<allowempty>true</allowempty>\n"
	        "\t</constraints>\n"
	        "\t<control type=\"edit\" format=\"string\">\n"
	        "\t\t<heading>" + str(32001 + objnum) + "</heading>\n"
	        "\t</control>\n"
            "</setting>\n\n")
    elif entname == "ipnum":
        xmlstring = ("<setting id=\"" + objname + "\" type=\"string\" label=\"#" + str(32001 + objnum) + "\" help=\"\">\n"
	        "\t<level>0</level>\n"
	        "\t<default/>\n"
	        "\t<constraints>\n"
	        "\t\t<allowempty>true</allowempty>\n"
	        "\t</constraints>\n"
	        "\t<control type=\"edit\" format=\"ip\">\n"
	        "\t\t<heading>" + str(32001 + objnum) + "</heading>\n"
	        "\t</control>\n"
            "</setting>\n\n")
    elif entname == "numbe":
        xmlstring = ("<setting id=\"" + objname + "\" type=\"integer\" label=\"#" + str(32001 + objnum) + "\" help=\"\">n"
	        "\t<level>0</level>\n"
	        "\t<default/>\n"
	        "\t<constraints>\n"
	        "\t\t<allowempty>true</allowempty>\n"
	        "\t</constraints>\n"
	        "\t<control type=\"edit\" format=\"integer\">\n"
	        "\t\t<heading>" + str(32001 + objnum) + "</heading>\n"
	        "\t</control>\n"
            "</setting>\n\n")
    elif entname == "seper":
        xmlstring = "<setting type=\"sep\"/>\n"
    elif entname == "lsepe":
        xmlstring = "<setting label=\"#" + str(32001 + objnum) + "\" type=\"sep\"/>\n"
    else:
        xmlstring =" invalid "
    return xmlstring
#---------------------- end of old code

def TbFunc( button ):
    global Toolbarcount, objtype, objlabel, cpostring, settingxml
    aettingxml = ""
    apostring = ""
    Toolbarcount = Toolbarcount +1
    if button == 'TEXT':
        App.openLabelFrame("Labels")
        lbltxt = App.stringBox("Label text", "What should the label say?")
        App.addLabel( "label" + str(Toolbarcount), text = lbltxt )
        App.setLabelOverFunction("label" + str(Toolbarcount), [focname("label" + str(Toolbarcount)), focname("label" + str(Toolbarcount))])
        elementlist.append(
            {'guiname':"label" + str(Toolbarcount),
            'elid':"label" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getLabel("label" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setLabelRightClick("label" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objlabel.append(App.getLabel("label" + str(Toolbarcount)))
        #--------------------------- end of old code
        App.stopLabelFrame()
        App.openLabelFrame("Objects")
        App.entry( "entry" + str(Toolbarcount), justify="left")
        elementlist.append(
            {'guiname':"entry" + str(Toolbarcount),
            'elid':"entry" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getEntry("entry" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setEntryOverFunction("entry" + str(Toolbarcount), [focname("entry" + str(Toolbarcount)), focname("entry" + str(Toolbarcount))])
        App.setEntryRightClick("entry" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objtype.append("entry" + str(Toolbarcount))
        #--------------------------- end of old code
        App.stopLabelFrame()
    elif button == 'IP#':
        App.openLabelFrame("Labels")
        lbltxt = App.stringBox("IP#", "What should the label say?")
        App.addLabel( "label" + str(Toolbarcount), text = lbltxt )
        elementlist.append(
            {'guiname':"label" + str(Toolbarcount),
            'elid':"label" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getLabel("label" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setLabelRightClick("label" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objlabel.append(App.getLabel("label" + str(Toolbarcount)))
        #--------------------------- end of old code
        App.stopLabelFrame()
        App.openLabelFrame("Objects")
        App.addEntry("ipnum" + str(Toolbarcount))
        App.setEntryDefault("ipnum" + str(Toolbarcount), "127.0.0.1")
        App.setEntryWidth("ipnum" + str(Toolbarcount),16)
        elementlist.append(
            {'guiname':"ipnum" + str(Toolbarcount),
            'elid':"ipnum" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getEntry("ipnum" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"ip", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setEntryOverFunction("ipnum" + str(Toolbarcount), [focname("ipnum" + str(Toolbarcount)), focname("ipnum" + str(Toolbarcount))])
        App.setEntryRightClick("ipnum" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objtype.append("ipnum" + str(Toolbarcount))
        #--------------------------- end of old code
        App.stopLabelFrame()
    elif button == 'NUMBER':
        App.openLabelFrame("Labels")
        lbltxt = App.stringBox("Numeric Input", "What should the label say?")
        App.addLabel("label"+str(Toolbarcount), text = lbltxt )
        elementlist.append(
            {'guiname':"label" + str(Toolbarcount),
            'elid':"label" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getLabel("label" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setLabelRightClick("label" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objlabel.append(App.getLabel("label"+str(Toolbarcount)))
        #--------------------------- end of old code
        App.stopLabelFrame()
        App.openLabelFrame("Objects")
        App.addNumericEntry("numbe"+str(Toolbarcount))
        elementlist.append(
            {'guiname':"numbe" + str(Toolbarcount),
            'elid':"numbe" + str(Toolbarcount), 'eltyp':"integer", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getNumericEntry("numbe" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"integer", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setEntryOverFunction("numbe" + str(Toolbarcount), [focname("numbe" + str(Toolbarcount)), focname("numbe" + str(Toolbarcount))])
        App.setEntryRightClick("numbe" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objtype.append("numbe"+str(Toolbarcount))
        #--------------------------- end of old code
        App.stopLabelFrame()
    elif button == '-SEP-':
        App.openLabelFrame("Labels")
        lbltxt = App.stringBox("Seperator", "'-'for no label, else write you label her")
        App.addLabel( "sepel" + str(Toolbarcount), text = lbltxt )
        elementlist.append(
            {'guiname':"sepel" + str(Toolbarcount),
            'elid':"sepel" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("sepel" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getLabel("sepel" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setLabelRightClick("sepel" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        if lbltxt == "-":
            objlabel.append(" ")
        else:
            objlabel.append(lbltxt)
        #--------------------------- end of old code
        App.stopLabelFrame()
        App.openLabelFrame("Objects")
        if  lbltxt == "-":
            elementlist.append(
                {'guiname':"seper" + str(Toolbarcount),
                'elid':"seper" + str(Toolbarcount), 'eltyp':"sep", 'ellabel':"", 'elhelp':"",
                'ellevel':"0",
                'eldefault':"",
                'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
                'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
                'parent':"",
                'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
            )
            App.addLabel("seper"+ str(Toolbarcount),"-------------")
            App.setLabelRightClick("seper" + str(Toolbarcount), "Information")
            # -------------------------- old code still working
            objtype.append("seper"+str(Toolbarcount))
            #--------------------------- end of old code)
        else:
            elementlist.append(
                {'guiname':"lsepe" + str(Toolbarcount),
                'elid':"lsepe" + str(Toolbarcount), 'eltyp':"lsep", 'ellabel':lbltxt, 'elhelp':"",
                'ellevel':"0",
                'eldefault':lbltxt,
                'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
                'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
                'parent':"",
                'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
            )
            App.addLabel("lsepe"+ str(Toolbarcount),"-------------")
            App.setLabelRightClick("lsepe" + str(Toolbarcount), "Information")
            # -------------------------- old code still working
            objtype.append("lsepe"+str(Toolbarcount))
            #--------------------------- end of old code
        App.stopLabelFrame()
    #elif for the rest of kodi elements
    elif button == 'DATE':
        App.openLabelFrame("Labels")
        lbltxt = App.stringBox("Date input", "Label for Date-input?")
        App.addLabel( "label" + str(Toolbarcount), text = lbltxt )
        App.setLabelOverFunction("label" + str(Toolbarcount), [focname("label" + str(Toolbarcount)), focname("label" + str(Toolbarcount))])
        elementlist.append(
            {'guiname':"label" + str(Toolbarcount),
            'elid':"label" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':"2021-09-02",
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setLabelRightClick("label" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objlabel.append(App.getLabel("label" + str(Toolbarcount)))
        #--------------------------- end of old code
        App.stopLabelFrame()
        App.openLabelFrame("Objects")
        App.entry( "ddate" + str(Toolbarcount), justify="left")
        elementlist.append(
            {'guiname':"ddate" + str(Toolbarcount),
            'elid':"ddate" + str(Toolbarcount), 'eltyp':"date", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getEntry("ddate" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"date", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setEntryOverFunction("ddate" + str(Toolbarcount), [focname("ddate" + str(Toolbarcount)), focname("ddate" + str(Toolbarcount))])
        App.setEntryRightClick("ddate" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objtype.append("ddate" + str(Toolbarcount))
        #--------------------------- end of old code
        App.stopLabelFrame()
    elif button == 'TIME':
        App.openLabelFrame("Labels")
        lbltxt = App.stringBox("Time input", "Label for Time-input?")
        App.addLabel( "label" + str(Toolbarcount), text = lbltxt )
        App.setLabelOverFunction("label" + str(Toolbarcount), [focname("label" + str(Toolbarcount)), focname("label" + str(Toolbarcount))])
        elementlist.append(
            {'guiname':"label" + str(Toolbarcount),
            'elid':"label" + str(Toolbarcount), 'eltyp':"string", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':"2021-09-02",
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"string", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setLabelRightClick("label" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objlabel.append(App.getLabel("label" + str(Toolbarcount)))
        #--------------------------- end of old code
        App.stopLabelFrame()
        App.openLabelFrame("Objects")
        App.entry( "ttime" + str(Toolbarcount), justify="left")
        elementlist.append(
            {'guiname':"ttime" + str(Toolbarcount),
            'elid':"ttime" + str(Toolbarcount), 'eltyp':"time", 'ellabel':App.getLabel("label" + str(Toolbarcount)), 'elhelp':"",
            'ellevel':"0",
            'eldefault':App.getEntry("ttime" + str(Toolbarcount)),
            'addontype':"", 'allowempty':"true", 'writeable':"", 'masking':"", 'source':"", 'min':"", 'step':"", 'max':"", 'sorting':"",
            'elctype':"edit",'elformat':"time", 'elcoption':"", 'elmultiselect':"", 'show':"", 'adata':"",
            'parent':"",
            'dependencies':"", 'visible':"true", 'enable':"true", 'infobool':"", 'condition':"", 'logicalop':""}
        )
        App.setEntryOverFunction("ttime" + str(Toolbarcount), [focname("ttime" + str(Toolbarcount)), focname("ttime" + str(Toolbarcount))])
        App.setEntryRightClick("ttime" + str(Toolbarcount), "Information")
        # -------------------------- old code still working
        objtype.append("ttime" + str(Toolbarcount))
        #--------------------------- end of old code
        App.stopLabelFrame()
    else:
        # Do the default
        print(button)
    # -------------------------- old code still working
    # Before return we should create the updated strings.po tab
    App.openTab("TabbedFrame", "stringspo")
    App.clearTextArea("potext")
    for x in range(len(objlabel)):
        apostring = apostring + ("msgctxt \"#" + str(32001 + x) +"\"\n"
        "msgid \"" + str(objlabel[x]) +"\"\n"
        "msgstr \"\"\n"
        "\n")
    tmpstring = cpostring + apostring
    App.setTextArea("potext", tmpstring)
    App.stopTab()
    # Before we retorn we should populate xml tab too (old code)
    App.openTab("TabbedFrame", "xml")
    App.clearTextArea("xmltext")
    for x in range(len(objtype)):
        aettingxml = aettingxml + addxml(objtype[x],x)
    tmpxml = settingxml + aettingxml
    App.setTextArea("xmltext", tmpxml)
    App.stopTab()

    return

def MenuPress( menuchoice ):
    if menuchoice == 'Open':
        fileload=App.openBox(title="Open", dirName=None, fileTypes=[('KodiGuis', '*.xml')], asFile=True, mode='r')
        # here comes the call to code to make a gui out of a xml
    elif menuchoice == 'Save':
        filesave=App.saveBox(title="Save", fileName=None, dirName=None, fileExt=".xml", fileTypes=None, asFile=None, parent=None)
    return



App.setBg("grey")
App.setFont(10)

App.addMenuList("File", fileMenus, MenuPress)
App.addMenuItem("appJar", "Help", App.appJarHelp)
App.addMenuItem("appJar", "About", App.appJarAbout)

App.addToolbar(tools, TbFunc, findIcon=False)


App.startTabbedFrame("TabbedFrame")
App.startTab("Gui")
App.startLabelFrame("Labels", row=0, column=0)
App.setSticky("NEW")
App.setStretch("COLUMN")
App.addHorizontalSeparator(0,0,0,0, colour="red")
App.stopLabelFrame()
App.startLabelFrame("Objects", row=0, column=1)
App.setSticky("NEW")
App.setStretch("COLUMN")
App.addHorizontalSeparator(0,0,0,0, colour="blue")
App.stopLabelFrame()
App.stopTab()
App.startTab("stringspo")
App.addScrolledTextArea("potext")
App.stopTab()
App.startTab("xml")
App.addScrolledTextArea("xmltext")
App.stopTab()
App.startTab("addon")
App.addScrolledTextArea("addontxt")
App.stopTab()
App.stopTabbedFrame()

#Settings for addon.xml
App.startSubWindow("Addon", modal=True)
App.addLabel("adhead", "Header" ,0,0,2,0)
App.startLabelFrame("LabelHere", row=1, column=0, colspan=1, rowspan=35)
App.addLabel("addon1", "ID" )
App.addLabel("addon2", "Name" )
App.addLabel("addon3", "Version" )
App.addLabel("addon4", "Provider-name" )
App.addLabel("addon5", "Require more" ) #radio, click opens subwindow
App.addLabel("addon6", "Extension" ) #dropdown
App.addLabel("addon7", "Library attribute" )
App.addLabel("addon8", "Provides" ) #dropdown
App.addHorizontalSeparator(9,0,0,0, colour="blue")
App.addLabel("addon9", "Summary" )
App.addLabel("addon10", "Description" )
App.addLabel("addon11", "Disclaimer" )
App.addLabel("addon12", "News" )
App.addLabel("addon13", "Platform" ) #dropdown
App.addLabel("addon14", "Language" ) #dropdown
App.addLabel("addon15", "License" )
App.addLabel("addon16", "Forum" )
App.addLabel("addon17", "Website" )
App.addLabel("addon18", "Source" )
App.addLabel("addon19", "Email" )
App.addLabel("addon20", "Lifecyclestate" ) #dropdown
App.addHorizontalSeparator(21,0,0,0, colour="blue")
App.addLabel("addon21", "Icon" )
App.addLabel("addon22", "Fanart" )
App.addLabel("addon23", "Screenshot" )
App.addLabel("addon24", "Banner" )
App.addLabel("addon25", "Clearlogo" ) 
App.stopLabelFrame()
App.startLabelFrame("InputHere", row=1, column=1, colspan=1, rowspan=35)
App.entry("adpropent1",focus=True)
App.entry("adpropent2")
App.entry("adpropent3")
App.entry("adpropent4")
App.addRadioButton("addon", "Yes")
App.addRadioButton("addon", "No")
App.setRadioButton("addon", "No", callFunction=False)
App.setRadioButtonChangeFunction("addon", reqw)
App.addLabelOptionBox("adpropent6", ["image","audio","video","executable"])
App.entry("adpropent7")
App.addLabelOptionBox("adpropent8",[ "xbmc.python.pluginsource", "xbmc.python.script",
    "xbmc.gui.skin", "xbmc.webinterface", "xbmc.addon.repository",
    "xbmc.service", "xbmc.metadata.scraper.albums", "xbmc.metadata.scraper.artists",
    "xbmc.metadata.scraper.movies", "xbmc.metadata.scraper.musicvideos", "xbmc.metadata.scraper.tvshows",
    "xbmc.metadata.scraper.library", "xbmc.ui.screensaver", "xbmc.player.musicviz",
    "xbmc.python.weather", "xbmc.subtitle.module", "xbmc.python.lyrics",
    "xbmc.python.library", "xbmc.python.module", "xbmc.addon.video",
    "xbmc.addon.audio", "xbmc.addon.image", "kodi.resource.font",
    "kodi.resource.images", "kodi.resource.language", "kodi.resource.uisounds"
])
App.addHorizontalSeparator(9,0,0,0, colour="blue")
App.entry("adpropent9")
App.entry("adpropent10")
App.entry("adpropent11")
App.entry("adpropent12")
App.addLabelOptionBox("adpropent13", ["all", "linux", "osx", "osx64", "osx-x86_64", "osx32", "osx-i686", "ios", "ios-armv7", "ios-aarch64", "windx", "windows", "windows-i686", 
    "windows-x86_64", "windowsstore", "android", "android-armv7", "android-aarch64", "android-i686", "tvos", "tvos-aarch64"
])
App.addLabelOptionBox("adpropent14", ["en_gb", "af_za", "am_et", "ar_sa", "ast_es", "az_az", "be_by", "bg_bg", "bs_ba", "ca_es", "cs_cz", "cy_gb", "da_dk",
    "de_de", "el_gr", "en_au", "en_nz", "en_us", "eo", "es_ar", "es_es", "es_mx", "et_ee", "eu_es", "fa_af", "fa_ir", "fi_fi", "fo_fo", "fr_ca", "fr_fr",
    "gl_es", "he_il", "hi_in", "hr_hr", "hu_hu", "hy_am", "id_id", "is_is", "it_it", "ja_jp", "kn_in", "ko_kr", "lt_lt", "lv_lv", "mi", "mk_mk", "ml_in", "mn_mn",
    "ms_my", "mt_mt", "my_mm", "nb_no", "nl_nl", "pl_pl", "pt_br", "pt_pt", "ro_ro", "ru_ru", "si_lk", "sk_sk", "sl_si", "sq_al", "sr_rs", "sr_rs@latin", "sv_se", "szl",
    "ta_in", "te_in", "tg_tj", "th_th", "tr_tr", "uk_ua", "uz_uz", "vi_vn", "zh_cn","zh_tw"
])
App.entry("adpropent15")
App.entry("adpropent16")
App.entry("adpropent17")
App.entry("adpropent18")
App.entry("adpropent19")
App.addLabelOptionBox("adpropent20", ["normal", "broken", "deprecated"])
App.entry("adpropent21")
App.entry("adpropent22")
App.entry("adpropent23")
App.entry("adpropent24")
App.entry("adpropent25")
App.stopLabelFrame()
App.addHorizontalSeparator(26,0,2,0, colour="red")
App.addButton("Apply", addonsave(),27,0,0,0)

App.setLabelTooltip("addon1", "label_help_text_here_1")
App.setEntryTooltip("adpropent1", "entry_help_text_here_1")
App.setLabelTooltip("addon2", "label_help_text_here_2")
App.setEntryTooltip("adpropent2", "entry_help_text_here_2")
App.setLabelTooltip("addon3", "label_help_text_here_3")
App.setEntryTooltip("adpropent3", "entry_help_text_here_3")
App.setLabelTooltip("addon4", "label_help_text_here_1")
App.setEntryTooltip("adpropent4", "entry_help_text_here_4")
App.setLabelTooltip("addon5", "If clicked will open subwindow")
App.setRadioButtonTooltip("addon", "new window to enter requirements")
App.setLabelTooltip("addon6", "label_help_text_here_6")
App.setOptionBoxTooltip("adpropent6", "entry_help_text_here_6")
App.setLabelTooltip("addon7", "label_help_text_here_7")
App.setEntryTooltip("adpropent7", "entry_help_text_here_7")
App.setLabelTooltip("addon8", "label_help_text_here_8")
App.setOptionBoxTooltip("adpropent8", "entry_help_text_here_8")
App.setLabelTooltip("addon9", "label_help_text_here_9")
App.setEntryTooltip("adpropent9", "entry_help_text_here_9")
App.setLabelTooltip("addon10", "label_help_text_here_10")
App.setEntryTooltip("adpropent10", "entry_help_text_here_10")
App.setLabelTooltip("addon11", "label_help_text_here_11")
App.setEntryTooltip("adpropent11", "entry_help_text_here_11")
App.setLabelTooltip("addon12", "label_help_text_here_12")
App.setEntryTooltip("adpropent12", "entry_help_text_here_12")
App.setLabelTooltip("addon13", "label_help_text_here_13")
App.setOptionBoxTooltip("adpropent13", "entry_help_text_here_13")
App.setLabelTooltip("addon14", "label_help_text_here_14")
App.setOptionBoxTooltip("adpropent14", "entry_help_text_here_14")
App.setLabelTooltip("addon15", "label_help_text_here_15")
App.setEntryTooltip("adpropent15", "entry_help_text_here_15")
App.setLabelTooltip("addon16", "label_help_text_here_16")
App.setEntryTooltip("adpropent16", "entry_help_text_here_16")
App.setLabelTooltip("addon17", "label_help_text_here_17")
App.setEntryTooltip("adpropent17", "entry_help_text_here_17")
App.setLabelTooltip("addon18", "label_help_text_here_18")
App.setEntryTooltip("adpropent18", "entry_help_text_here_18")
App.setLabelTooltip("addon19", "label_help_text_here_19")
App.setEntryTooltip("adpropent19", "entry_help_text_here_19")
App.setLabelTooltip("addon20", "label_help_text_here_20")
App.setOptionBoxTooltip("adpropent20", "entry_help_text_here_20")
App.setLabelTooltip("addon21", "label_help_text_here_21")
App.setEntryTooltip("adpropent21", "entry_help_text_here_21")
App.setLabelTooltip("addon22", "label_help_text_here_22")
App.setEntryTooltip("adpropent22", "entry_help_text_here_22")
App.setLabelTooltip("addon23", "label_help_text_here_23")
App.setEntryTooltip("adpropent23", "entry_help_text_here_23")
App.setLabelTooltip("addon24", "label_help_text_here_24")
App.setEntryTooltip("adpropent24", "entry_help_text_here_24")
App.setLabelTooltip("addon25", "label_help_text_here_25")
App.setEntryTooltip("adpropent25", "entry_help_text_here_25")


#Setting up Properties subwindow
App.startSubWindow("Properties", modal=True)
App.addLabel("swhead", "Header" ,0,0,2,0)
App.startLabelFrame("Descript", row=1, column=0, colspan=1, rowspan=35)
App.addLabel("prop1", "ID" )
App.addLabel("prop2", "Type" )
App.addLabel("prop3", "Label" )
App.addLabel("prop4", "Help" )
App.addHorizontalSeparator(6,0,0,0, colour="blue")
App.addLabel("prop5", "SettingLevel" )
App.addHorizontalSeparator(8,0,0,0, colour="blue")
App.addLabel("prop6", "DefautValue" )
App.addHorizontalSeparator(10,0,0,0, colour="blue")
App.addLabel("prop7", "Addontype" )
App.addLabel("prop8", "Allowempty" )
App.addLabel("prop9", "Writeable" )
App.addLabel("prop10", "Masking" )
App.addLabel("prop11", "Source" )
App.addLabel("prop12", "Min" )
App.addLabel("prop13", "Step" )
App.addLabel("prop14", "Max" )
App.addLabel("prop15", "Sorting" )
App.addHorizontalSeparator(20,0,0,0, colour="blue")
App.addLabel("prop16", "ControlType" )
App.addLabel("prop17", "Format" )
App.addLabel("prop18", "ControlOption" )
App.addLabel("prop19", "Multiselect" )
App.addLabel("prop20", "Show" )
App.addLabel("prop21", "ActionData" )
App.addHorizontalSeparator(27,0,0,0, colour="blue")
App.addLabel("prop22", "Parent" )
App.addHorizontalSeparator(29,0,0,0, colour="blue")
App.addLabel("prop23", "Dependencies" )
App.addLabel("prop24", "Visible" )
App.addLabel("prop25", "Enable" )
App.addLabel("prop26", "Infobool" )
App.addLabel("prop27", "Condition" )
App.addLabel("prop28", "LogicalOp" )
App.stopLabelFrame()
App.startLabelFrame("Input", row=1, column=1, colspan=1, rowspan=35)
App.entry("propent1")
App.entry("propent2")
App.entry("propent3")
App.entry("propent4")
App.addHorizontalSeparator(6,0,0,0, colour="blue")
App.entry("propent5")
App.addHorizontalSeparator(8,0,0,0, colour="blue")
App.entry("propent6")
App.addHorizontalSeparator(10,0,0,0, colour="blue")
App.entry("propent7")
App.entry("propent8")
App.entry("propent9")
App.entry("propent10")
App.entry("propent11")
App.entry("propent12")
App.entry("propent13")
App.entry("propent14")
App.entry("propent15")
App.addHorizontalSeparator(20,0,0,0, colour="blue")
App.entry("propent16")
App.entry("propent17")
App.entry("propent18")
App.entry("propent19")
App.entry("propent20")
App.entry("propent21")
App.addHorizontalSeparator(27,0,0,0, colour="blue")
App.entry("propent22")
App.addHorizontalSeparator(29,0,0,0, colour="blue")
App.entry("propent23")
App.entry("propent24")
App.entry("propent25")
App.entry("propent26")
App.entry("propent27")
App.entry("propent28")
App.stopLabelFrame()
App.addHorizontalSeparator(36,0,2,0, colour="red")
App.addButton("Store", propsave,37,0,0,0)
App.addButton("Cancel", propabort,37,1,0,0)
App.setLabelTooltip("prop1", "Element ID(Kodi-uniquname)")
App.setEntryTooltip("propent1", "The variable name stored in settings")
App.setLabelTooltip("prop2", "Element type")
App.setEntryTooltip("propent2", "string|urlencodedstring|integer|date|time|boolean|addon|list[addon]|number|path|action|button")
App.setLabelTooltip("prop3", "Element Label")
App.setEntryTooltip("propent3", "Taken from gui Label, will be stored in stringspo")
App.setLabelTooltip("prop4", "Element Help")
App.setEntryTooltip("propent4", "Small tooltip")
App.setLabelTooltip("prop5", "Element level(based on settings level)")
App.setEntryTooltip("propent5", "0 - Basic, 1 - Standard, 2 - Advanced, 3 - Expert and 4 - Internal (will never be shown in the GUI)")
App.setLabelTooltip("prop6", "Element Default value")
App.setEntryTooltip("propent6", "Default value(taken from gui)")
App.setLabelTooltip("prop7", "Constraint addontype")
App.setEntryTooltip("propent7", "Example: xbmc.metadata.scraper.movies")
App.setLabelTooltip("prop8", "Constraint allowempty")
App.setEntryTooltip("propent8", "true or false, true if omitted")
App.setLabelTooltip("prop9", "Constraint writeable")
App.setEntryTooltip("propent9", "If a file is writable, true or false")
App.setLabelTooltip("prop10", "Constraint masking")
App.setEntryTooltip("propent10", "Example: *.txt|executable|video|audio")
App.setLabelTooltip("prop11", "Constraint source")
App.setEntryTooltip("propent11", "video|music|pictures|programs|files|local|blank - will show the respective folders from sources.xml.\n blank will list both local drives and network shares.")
App.setLabelTooltip("prop12", "Constraint min")
App.setEntryTooltip("propent12", "Min value in slider")
App.setLabelTooltip("prop13", "Constraint step)")
App.setEntryTooltip("propent13", "Size of steps in slider")
App.setLabelTooltip("prop14", "Constraint max")
App.setEntryTooltip("propent14", "Max value in a slider")
App.setLabelTooltip("prop15", "Constraint sorting")
App.setEntryTooltip("propent15", "Sorting of options in a list-box: accending|decending")
App.setLabelTooltip("prop16", "Control type")
App.setEntryTooltip("propent16", "edit|button|toggle|list|spinner|slider")
App.setLabelTooltip("prop17", "Control format")
App.setEntryTooltip("propent17", "string|urlencoded|ip|integer|date|time|addon|number|percentage|file|image|path|action")
App.setLabelTooltip("prop18", "Control option")
App.setEntryTooltip("propent18", "hidden(for password inputs)|popup(for a tooltip in sliders)")
App.setLabelTooltip("prop19", "Control multiselect")
App.setEntryTooltip("propent19", "true|false . allows to select several addons")
App.setLabelTooltip("prop20", "Control Show")
App.setEntryTooltip("propent20", "Used in conjunction with addon and list[addon] \n<show more=\"true\" details=\"true\">installed</show>")
App.setLabelTooltip("prop21", "Control Data")
App.setEntryTooltip("propent21", "In use with control format 'action'\nExample: RunScriptRunPlugin(plugin://$ID/fo/) $ID = your addon id, $CWD your addon path")
App.setLabelTooltip("prop22", "Element parent(If you wish to define a subsetting)")
App.setEntryTooltip("propent22", "Use the parent attribute with the id here.")
App.setLabelTooltip("prop23", "Condition dependencies")
App.setEntryTooltip("propent23", "Element visibility|enable depends on other setting. Example 'type=\"visible\" setting=\"")
App.setLabelTooltip("prop24", "Condition visible")
App.setEntryTooltip("propent24", "Boolean set if visible or not, default true")
App.setLabelTooltip("prop25", "Condition enable")
App.setEntryTooltip("propent25", "Boolean set if enable or not, default tru")
App.setLabelTooltip("prop26", "Condition infobool")
App.setEntryTooltip("propent26", "Based on a boolean condition. Example:\n<dependency type='enable' on='property' name='infobool'>system.platform.android</dependency>")
App.setLabelTooltip("prop27", "Condition type")
App.setEntryTooltip("propent27", "true/false|integer|string(for eq) or !eq|lt|gt")
App.setLabelTooltip("prop28", "Condition Logical operators and|or")
App.setEntryTooltip("propent28", "And: for 2 or more conditions to be meet.\nOr: If 1 of many conditions are meet.\nWith this GUI you will just ve able to set 1 condition.")
App.stopSubWindow()


App.go()