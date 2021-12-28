from kivy.app import App # importing app
from kivy.uix.widget import Widget # importing kivy widgets
from kivy.lang import Builder # importing kivy builder
from kivy.core.window import Window # import kivy window
from kivy.core.text import LabelBase # importing kivy LabelBase

# font
LabelBase.register(name= "Quicksand", fn_regular="Quicksand-Light.ttf") # font

# Set the app size
Window.size = (500,700) # window size

# Designate Our .kv design file 
Builder.load_file("calculator.kv") # loads the kv file for graphics

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = "" # text input is empty at start

	
	# all functions
	def button_press(self, button): 
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""

	
	def add(self): # addition # add sign
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}+" # adds + after last number or sign
		if "+" in prior:
			self.ids.calc_input.text = f"{prior}"
	
	def subtract(self): #subtraction
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}-" # adds - after last number or sign
		


	def multiply(self): # multiply sign
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		
		self.ids.calc_input.text = self.ids.calc_input.text = f"{prior}*" # adds * after last number or sign
		if "*" in prior:
			self.ids.calc_input.text = f"{prior}"
		
	
	def divide(self): # divide sign
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}/" # adds / after last number
		if "/" in prior:
			self.ids.calc_input.text = f"{prior}"
	
	def one(self): # number 1
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}1" # adds 1 after last number or sign
	
	def two(self): # number 2
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}2" # adds 2 after last number or sign
	
	def three(self): # number 3
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}3" # adds 3 after last number or sign
	
	def four(self): # number 4
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}4" # adds 4 after last number or sign

	def five(self): # number 5
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}5" # adds 5 after last number or sign

	def six(self): # number 6
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}6" # adds 6 after last number or sign
	
	def seven(self): # number 7
		prior = self.ids.calc_input.text 
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}7" # adds 7 after last number or sign
	
	def eight(self): # number 8
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}8" # adds 8 after last number or sign
	
	def nine(self): # number 9
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}9" # adds 9 after last number or sign
	
	def zero(self): # number 0
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		self.ids.calc_input.text = f"{prior}0" # adds 0 after last number or sign
	
	def dot(self): # decimal
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		if "." in prior:
			pass
		else:
			self.ids.calc_input.text = f"{prior}." # adds decimal after last number
			if "." in prior:
				self.ids.calc_input.text = f"{prior}"

	def equal(self): # equal sign
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		if "%" in prior:
			self.ids.calc_input.text = f"{prior}/10"
		
		self.ids.calc_input.text = f"{prior}="
		
		try:
			prior2 = eval(prior)
				

			self.ids.calc_input.text = f"{prior2}"
		except:
			self.ids.calc_input.text = "error"
		
		
	
	def C(self): # delete all numbers
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		prior = prior[:-1]		# removes last item in text box
		self.ids.calc_input.text = prior
	
	def pos_neg(self):
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		# Test to see if there's a - sign already
		if "-" in prior:
			 self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}' # negative numbers
	
	def percent(self):
		prior = self.ids.calc_input.text
		if "error" in prior:
			prior = ""
		if "/10" in prior:
			 self.ids.calc_input.text = f'{prior.replace("/10", "")}'
		else:
			priorx = float(prior)
			priorx = priorx/100
			self.ids.calc_input.text = f'{priorx}'
			
		


class CalculatorApp(App):
	def build(self):
		return MyLayout()


if __name__ == '__main__':
	CalculatorApp().run()
