# codegen.py: code generator functions for wxDialog objects
# $Id: codegen.py,v 1.10 2003/05/15 19:05:00 agriggio Exp $
#
# Copyright (c) 2002-2003 Alberto Griggio <albgrig@tiscalinet.it>
# License: MIT (see license.txt)
# THIS PROGRAM COMES WITH NO WARRANTY

import common

class PythonCodeGenerator:
    def get_code(self, obj):
        return [], [], []

    def get_properties_code(self, dialog):
        prop = dialog.properties
        pygen = common.code_writers['python']
        out = []
        title = prop.get('title')
        if title: out.append('self.SetTitle(%s)\n' % pygen.quote_str(title))
        icon = prop.get('icon')
        if icon: 
            out.append('_icon = wxEmptyIcon()\n')
            out.append('_icon.CopyFromBitmap(wxBitmap(%s, '
                       'wxBITMAP_TYPE_ANY))\n' % pygen.quote_str(icon))
            out.append('self.SetIcon(_icon)\n')
        out.extend(pygen.generate_common_properties(dialog))
        return out

    def get_layout_code(self, dialog):
        ret = ['self.Layout()\n']
        try:
            if int(dialog.properties['centered']):
                ret.append('self.Centre()\n')
        except (KeyError, ValueError):
            pass
        return ret

# end of class PythonCodeGenerator


class CppCodeGenerator:
    constructor = [('wxWindow*', 'parent'), ('int', 'id'),
                   ('const wxString&', 'title'),
                   ('const wxPoint&', 'pos', 'wxDefaultPosition'),
                   ('const wxSize&', 'size', 'wxDefaultSize'),
                   ('long', 'style', 'wxDEFAULT_DIALOG_STYLE')]

    def get_code(self, obj):
        return [], [], [], []
    
    def get_properties_code(self, dialog):
        """\
        generates the code for the various wxDialog specific properties.
        Returns a list of strings containing the generated code
        """
        prop = dialog.properties
        cppgen = common.code_writers['C++']
        out = []
        title = prop.get('title')
        if title: out.append('SetTitle(%s);\n' % cppgen.quote_str(title))
        icon = prop.get('icon')
        if icon:
            out.append('wxIcon _icon;\n')
            out.append('_icon.CopyFromBitmap(wxBitmap(%s, '
                       'wxBITMAP_TYPE_ANY));\n' % cppgen.quote_str(icon))
            out.append('SetIcon(_icon);\n')
        out.extend(cppgen.generate_common_properties(dialog))
        return out

    def get_layout_code(self, dialog):
        ret = ['Layout();\n']
        try:
            if int(dialog.properties['centered']):
                ret.append('Centre();\n')
        except (KeyError, ValueError):
            pass
        return ret

# end of class CppCodeGenerator


def xrc_code_generator(obj):
    xrcgen = common.code_writers['XRC']

    class DialogXrcObject(xrcgen.DefaultXrcObject):
        def write(self, *args, **kwds):
            if 'icon' in self.properties:
                del self.properties['icon']
            xrcgen.DefaultXrcObject.write(self, *args, **kwds)

    # end of class DialogXrcObject

    return DialogXrcObject(obj)


def initialize():
    cn = common.class_names
    cn['EditDialog'] = 'wxDialog'
    common.toplevels['EditDialog'] = 1
    
    pygen = common.code_writers.get('python')
    if pygen:
        pygen.add_widget_handler('wxDialog', PythonCodeGenerator())
    cppgen = common.code_writers.get('C++')
    if cppgen:
        cppgen.add_widget_handler('wxDialog', CppCodeGenerator())
    xrcgen = common.code_writers.get('XRC')
    if xrcgen:
        xrcgen.add_widget_handler('wxDialog', xrc_code_generator)
