# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class EditorFrame
###########################################################################

class EditorFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Color Scheme Editor", pos = wx.DefaultPosition, size = wx.Size( 599,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_main_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_main_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer2 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_plist_name_label = wx.StaticText( self.m_main_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_plist_name_label.Wrap( -1 )
		fgSizer2.Add( self.m_plist_name_label, 0, wx.ALL, 5 )
		
		self.m_plist_name_textbox = wx.TextCtrl( self.m_main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_plist_name_textbox, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_plist_uuid_label = wx.StaticText( self.m_main_panel, wx.ID_ANY, u"UUID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_plist_uuid_label.Wrap( -1 )
		fgSizer2.Add( self.m_plist_uuid_label, 0, wx.ALL, 5 )
		
		self.m_plist_uuid_textbox = wx.TextCtrl( self.m_main_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_plist_uuid_textbox, 0, wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_uuid_button = wx.Button( self.m_main_panel, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_uuid_button, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		self.m_plist_notebook = wx.Notebook( self.m_main_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.ALWAYS_SHOW_SB|wx.FULL_REPAINT_ON_RESIZE )
		self.m_plist_notebook.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		
		fgSizer1.Add( self.m_plist_notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_main_panel.SetSizer( bSizer2 )
		self.m_main_panel.Layout()
		bSizer2.Fit( self.m_main_panel )
		bSizer1.Add( self.m_main_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_plist_name_textbox.Bind( wx.EVT_KILL_FOCUS, self.on_plist_name_blur )
		self.m_plist_uuid_textbox.Bind( wx.EVT_KILL_FOCUS, self.on_uuid_blur )
		self.m_uuid_button.Bind( wx.EVT_BUTTON, self.on_uuid_button_click )
		self.m_plist_notebook.Bind( wx.EVT_SIZE, self.on_plist_notebook_size )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_plist_name_blur( self, event ):
		event.Skip()
	
	def on_uuid_blur( self, event ):
		event.Skip()
	
	def on_uuid_button_click( self, event ):
		event.Skip()
	
	def on_plist_notebook_size( self, event ):
		event.Skip()
	

###########################################################################
## Class GlobalSettingsPanel
###########################################################################

class GlobalSettingsPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_plist_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_plist_grid.CreateGrid( 0, 2 )
		self.m_plist_grid.EnableEditing( False )
		self.m_plist_grid.EnableGridLines( False )
		self.m_plist_grid.EnableDragGridSize( False )
		self.m_plist_grid.SetMargins( 0, 0 )
		
		# Columns
		self.m_plist_grid.EnableDragColMove( False )
		self.m_plist_grid.EnableDragColSize( False )
		self.m_plist_grid.SetColLabelSize( 30 )
		self.m_plist_grid.SetColLabelValue( 0, u"Name" )
		self.m_plist_grid.SetColLabelValue( 1, u"Value" )
		self.m_plist_grid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_plist_grid.EnableDragRowSize( False )
		self.m_plist_grid.SetRowLabelSize( 0 )
		self.m_plist_grid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_plist_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_plist_grid, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_plist_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_edit_cell )
		self.m_plist_grid.Bind( wx.grid.EVT_GRID_RANGE_SELECT, self.on_grid_range_select )
		self.m_plist_grid.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select_cell )
		self.m_plist_grid.Bind( wx.EVT_KEY_DOWN, self.on_grid_key_down )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_edit_cell( self, event ):
		event.Skip()
	
	def on_grid_range_select( self, event ):
		event.Skip()
	
	def on_grid_select_cell( self, event ):
		event.Skip()
	
	def on_grid_key_down( self, event ):
		event.Skip()
	

###########################################################################
## Class StyleSettingsPanel
###########################################################################

class StyleSettingsPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_plist_grid = wx.grid.Grid( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		
		# Grid
		self.m_plist_grid.CreateGrid( 0, 5 )
		self.m_plist_grid.EnableEditing( False )
		self.m_plist_grid.EnableGridLines( False )
		self.m_plist_grid.EnableDragGridSize( False )
		self.m_plist_grid.SetMargins( 0, 0 )
		
		# Columns
		self.m_plist_grid.EnableDragColMove( False )
		self.m_plist_grid.EnableDragColSize( False )
		self.m_plist_grid.SetColLabelSize( 30 )
		self.m_plist_grid.SetColLabelValue( 0, u"Name" )
		self.m_plist_grid.SetColLabelValue( 1, u"Foreground" )
		self.m_plist_grid.SetColLabelValue( 2, u"Background" )
		self.m_plist_grid.SetColLabelValue( 3, u"Font Style" )
		self.m_plist_grid.SetColLabelValue( 4, u"Scope" )
		self.m_plist_grid.SetColLabelAlignment( wx.ALIGN_LEFT, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_plist_grid.AutoSizeRows()
		self.m_plist_grid.EnableDragRowSize( False )
		self.m_plist_grid.SetRowLabelSize( 0 )
		self.m_plist_grid.SetRowLabelAlignment( wx.ALIGN_RIGHT, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.m_plist_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.m_plist_grid.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_plist_grid.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1.Add( self.m_plist_grid, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		# Connect Events
		self.m_plist_grid.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.on_edit_cell )
		self.m_plist_grid.Bind( wx.grid.EVT_GRID_RANGE_SELECT, self.on_grid_range_select )
		self.m_plist_grid.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.on_grid_select_cell )
		self.m_plist_grid.Bind( wx.EVT_KEY_DOWN, self.on_grid_key_down )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_edit_cell( self, event ):
		event.Skip()
	
	def on_grid_range_select( self, event ):
		event.Skip()
	
	def on_grid_select_cell( self, event ):
		event.Skip()
	
	def on_grid_key_down( self, event ):
		event.Skip()
	

###########################################################################
## Class ColorSetting
###########################################################################

class ColorSetting ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Color Setting", pos = wx.DefaultPosition, size = wx.Size( 500,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_color_setting_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_color_setting_panel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_name_label = wx.StaticText( self.m_color_setting_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_name_label.Wrap( -1 )
		self.m_name_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_name_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_name_textbox = wx.TextCtrl( self.m_color_setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_name_textbox, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_scope_label = wx.StaticText( self.m_color_setting_panel, wx.ID_ANY, u"Scope", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_scope_label.Wrap( -1 )
		self.m_scope_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_scope_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_scope_textbox = wx.TextCtrl( self.m_color_setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_scope_textbox, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_bold_checkbox = wx.CheckBox( self.m_color_setting_panel, wx.ID_ANY, u"bold", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bold_checkbox, 0, wx.ALL, 5 )
		
		self.m_italic_checkbox = wx.CheckBox( self.m_color_setting_panel, wx.ID_ANY, u"italic", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_italic_checkbox, 0, wx.ALL, 5 )
		
		self.m_underline_checkbox = wx.CheckBox( self.m_color_setting_panel, wx.ID_ANY, u"underline", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_underline_checkbox, 0, wx.ALL, 5 )
		
		
		fgSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 5, 0, 0 )
		fgSizer3.AddGrowableCol( 4 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_foreground_picker = wx.Panel( self.m_color_setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_foreground_button_label = wx.StaticText( self.m_foreground_picker, wx.ID_ANY, u"foreground", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_foreground_button_label.Wrap( -1 )
		bSizer3.Add( self.m_foreground_button_label, 0, wx.ALIGN_CENTER|wx.ALL, 3 )
		
		
		self.m_foreground_picker.SetSizer( bSizer3 )
		self.m_foreground_picker.Layout()
		bSizer3.Fit( self.m_foreground_picker )
		fgSizer3.Add( self.m_foreground_picker, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_foreground_textbox = wx.TextCtrl( self.m_color_setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_foreground_textbox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_background_picker = wx.Panel( self.m_color_setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_background_button_label = wx.StaticText( self.m_background_picker, wx.ID_ANY, u"background", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_background_button_label.Wrap( -1 )
		bSizer4.Add( self.m_background_button_label, 0, wx.ALL, 3 )
		
		
		self.m_background_picker.SetSizer( bSizer4 )
		self.m_background_picker.Layout()
		bSizer4.Fit( self.m_background_picker )
		fgSizer3.Add( self.m_background_picker, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_background_textbox = wx.TextCtrl( self.m_color_setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_background_textbox, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer4 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer4.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_apply_button = wx.Button( self.m_color_setting_panel, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_apply_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_color_setting_panel.SetSizer( bSizer2 )
		self.m_color_setting_panel.Layout()
		bSizer2.Fit( self.m_color_setting_panel )
		bSizer1.Add( self.m_color_setting_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_set_color_close )
		self.m_foreground_button_label.Bind( wx.EVT_LEFT_DOWN, self.on_foreground_button_click )
		self.m_foreground_textbox.Bind( wx.EVT_KILL_FOCUS, self.on_foreground_blur )
		self.m_foreground_textbox.Bind( wx.EVT_SET_FOCUS, self.on_foreground_focus )
		self.m_foreground_textbox.Bind( wx.EVT_TEXT, self.on_foreground_change )
		self.m_background_button_label.Bind( wx.EVT_LEFT_DOWN, self.on_background_button_click )
		self.m_background_textbox.Bind( wx.EVT_KILL_FOCUS, self.on_background_blur )
		self.m_background_textbox.Bind( wx.EVT_SET_FOCUS, self.on_background_focus )
		self.m_background_textbox.Bind( wx.EVT_TEXT, self.on_background_change )
		self.m_apply_button.Bind( wx.EVT_BUTTON, self.on_apply_button_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_set_color_close( self, event ):
		event.Skip()
	
	def on_foreground_button_click( self, event ):
		event.Skip()
	
	def on_foreground_blur( self, event ):
		event.Skip()
	
	def on_foreground_focus( self, event ):
		event.Skip()
	
	def on_foreground_change( self, event ):
		event.Skip()
	
	def on_background_button_click( self, event ):
		event.Skip()
	
	def on_background_blur( self, event ):
		event.Skip()
	
	def on_background_focus( self, event ):
		event.Skip()
	
	def on_background_change( self, event ):
		event.Skip()
	
	def on_apply_button_click( self, event ):
		event.Skip()
	

###########################################################################
## Class GlobalSetting
###########################################################################

class GlobalSetting ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Global Setting", pos = wx.DefaultPosition, size = wx.Size( 500,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_global_setting_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_name_label = wx.StaticText( self.m_global_setting_panel, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_name_label.Wrap( -1 )
		self.m_name_label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_name_label, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_name_textbox = wx.TextCtrl( self.m_global_setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_name_textbox, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer2.AddGrowableCol( 2 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_color_checkbox = wx.CheckBox( self.m_global_setting_panel, wx.ID_ANY, u"Color", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_color_checkbox, 0, wx.ALL, 5 )
		
		self.m_color_picker = wx.Panel( self.m_global_setting_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 30,-1 ), wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL )
		fgSizer2.Add( self.m_color_picker, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_value_textbox = wx.TextCtrl( self.m_global_setting_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_value_textbox, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		fgSizer3 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_apply_button = wx.Button( self.m_global_setting_panel, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.m_apply_button, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		fgSizer1.Add( fgSizer3, 1, wx.EXPAND, 5 )
		
		
		bSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		self.m_global_setting_panel.SetSizer( bSizer2 )
		self.m_global_setting_panel.Layout()
		bSizer2.Fit( self.m_global_setting_panel )
		bSizer1.Add( self.m_global_setting_panel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.on_set_color_close )
		self.m_color_checkbox.Bind( wx.EVT_CHECKBOX, self.on_global_checkbox )
		self.m_color_picker.Bind( wx.EVT_LEFT_DOWN, self.on_color_button_click )
		self.m_value_textbox.Bind( wx.EVT_KILL_FOCUS, self.on_color_blur )
		self.m_value_textbox.Bind( wx.EVT_SET_FOCUS, self.on_color_focus )
		self.m_value_textbox.Bind( wx.EVT_TEXT, self.on_color_change )
		self.m_apply_button.Bind( wx.EVT_BUTTON, self.on_apply_button_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_set_color_close( self, event ):
		event.Skip()
	
	def on_global_checkbox( self, event ):
		event.Skip()
	
	def on_color_button_click( self, event ):
		event.Skip()
	
	def on_color_blur( self, event ):
		event.Skip()
	
	def on_color_focus( self, event ):
		event.Skip()
	
	def on_color_change( self, event ):
		event.Skip()
	
	def on_apply_button_click( self, event ):
		event.Skip()
	