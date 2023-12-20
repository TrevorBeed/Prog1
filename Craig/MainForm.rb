require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button3 = System::Windows::Forms::Button.new()
		@button1 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Blue
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ControlLightLight
		@label1.Location = System::Drawing::Point.new(196, 44)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(354, 122)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Blue
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.White
		@button3.Location = System::Drawing::Point.new(196, 208)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(118, 67)
		@button3.TabIndex = 3
		@button3.Text = "Force the spirit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Blue
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.White
		@button1.Location = System::Drawing::Point.new(432, 209)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(118, 66)
		@button1.TabIndex = 4
		@button1.Text = "Stop the spirit"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(733, 409)
		self.Controls.Add(@button1)
		self.Controls.Add(@button3)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "Craig"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = ""
	end

	def Button3Click(sender, e)
				@label1.Text = "Craig Rules!"
	end

end

