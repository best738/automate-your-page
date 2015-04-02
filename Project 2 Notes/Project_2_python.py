def generate_concept_html(concept_title, concept_description):
	html_text_1 = """
<div class="concept">
	<div class="concept_title">
	""" + concept_title
	html_text_2 = """
	</div>
	<div class="concept_description">
		<p>
			""" + concept_description
	html_text_3 = """
		</p>
	</div>
</div>"""
	full_html = html_text_1 + html_text_2 + html_text_3
	return full_html

def make_html (concept):
	concept_title = concept[0]
	concept_description = concept[1]
	return generate_concept_html(concept_title, concept_description)

programming_concepts = [['Python', "Python is a programming language to tell the computer what to do. Python code is input into another program (Python interpreter) that follows instructions in your code and it does that by following instruction in its own code. This is all done through you web browser. It uses very specific grammer rules, although much more specific than human language. This allows for unambiguous interpretations"],
					    ['Variables and Strings', 'Variables give names to values. In other words its an assignment statement. An example would be <span class="code">this variable = 4</span>. The equals (=) sign does not mean equal as in mathematics, but rather means to take the value of. Variables improve code readability, give programmers a way to store values, and give a way to change a value easily. A string is a sequence of characters. For example <span class="code">"4" + "6"</span> would result in <span class="code">"46"</span>, not <span class="code">"10"</span>. Note the <span class="code">+</span> concatenates.'],
					    ['Procedures', 'Procedures are also called functions. Procedures take an input(s), does something with the input, then produces and output. Procedures start with a line of code with the keyword <span class="code">def</span> and a function name followed by parameters in parentheses. Then we write what to do with input.'],
					    ['If and While Statements', 'A Boolean Value outputs a True or False. For example,<span class="code">print 2 > 3</span> would produce an output of False. Other operators are <span class="code">!=</span> for not equal and <span class="code">==</span> is equal to. <span class="code">if</span> statements are used to make comparisons. <span class="code">While</span> statements create loops and dont stop running until a certain event occurs.'],
					    ['Lists and For Loops', 'Lists can can contain strings, numbers, numbers and strings, and other lists. Lists can be mutated, meaning we can change its value after it is created. We can also append to a list, which adds an element to the end of the loop. The plus (+) operator essentially concatentes two list to create a new list. For loops loop through the elements in the list. Length (len) determines the number of characters in a string or the number of elements in a list.']
					   ]

def make_html_for_all_concepts (all_concepts):
	html = ""
	for concept in all_concepts:
		concept_html = make_html (concept)
		html = html + concept_html
	return html

print make_html_for_all_concepts (programming_concepts)
                