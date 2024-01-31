﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Silver
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(10, 286)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 118)
		self._button1.TabIndex = 0
		self._button1.Text = " Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Silver
		self._listBox1.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 34
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(380, 242)
		self._listBox1.TabIndex = 1
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Silver
		self._button2.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(126, 286)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(157, 118)
		self._button2.TabIndex = 2
		self._button2.Text = "Calc"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Silver
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(289, 286)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 118)
		self._button3.TabIndex = 3
		self._button3.Text = "Quit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Maroon
		self.ClientSize = System.Drawing.Size(404, 415)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		for i in range(41):
			self._listBox1.Items.Add(str(i) + "\t" + str(i*4))

	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()