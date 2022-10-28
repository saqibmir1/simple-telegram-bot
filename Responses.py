from datetime import datetime
import random

def sample_responses(input_text):
	user_message = str(input_text).lower()

	if user_message in ("hello", "hi", "sup"):
		return "hey how is it going?"

	if user_message in ("who are you", "what are you?"):
		return "im simple bot made by @saqibmir0_0"

	if user_message in ("am i gay", "am i gae"):
		return "yeas"

	if user_message in ("tell me about your penis", "hows your penis", "how is your penis"):
		return "massive cock"

	if user_message in ("time", "time?"):
		now = datetime.now()
		date_time=now.strftime("%d/%m/%y, %H:%M:%S")
		return str(date_time)

	if user_message in ("diss my mama", "insult my mama", "jo mama jokes"):
		insult_list=[
	"Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up",
"Yo mama's so fat, when she skips a meal, the stock market drops.",
"Yo mama's so fat, it took me two buses and a train to get to her good side",
"Yo mama's so fat, when she goes camping, the bears hide their food.",
"Yo mama's so fat, if she buys a fur coat, a whole species will become extinct.",
"Yo mama's so fat, she stepped on a scale and it said: To be continued.",
"Yo mama's so fat, I swerved to miss her in my car and ran out of gas.",
"Yo mama's so fat, when she wears high heels, she strikes oil.",
"Yo mama's so fat, she was overthrown by a small militia group, and now she's known as the Republic of Yo Mama.",
"Yo mama's so fat, when she sits around the house, she SITS AROUND the house.",
"Yo mama's so fat, she can't even jump to a conclusion.",
"Yo mama's so fat, she brought a spoon to the Super Bowl.",
"Yo mama's so stupid, she stared at a cup of orange juice for 12 hours because it said concentrate",
"Yo mama's so stupid, she put lipstick on her forehead to make up her mind",
"Yo mama's so stupid, when they said, Order in the court, she asked for fries and a shake."
"Yo mama's so stupid, she thought a quarterback was a refund.",
"Yo mama's so stupid, she took a ruler to bed to see how long she slept.",
"Yo mama's so ugly, she threw a boomerang and it refused to come back",
"Yo mama's so old, her social security number is one.",
"Yo mama's so ugly, she made a blind kid cry.",
"Yo mama's teeth are so yellow when she smiles at traffic, it slows down.",
"Yo mama's so ugly, when she was little, she had to trick-or-treat by phone.",
"Yo mama's so ugly, her birth certificate is an apology letter.",
"Yo mama's so poor, she can't even afford to pay attention.",
"Yo mama so big, her belt size is equator.",
"Yo mama so scary, the government moved Halloween to her birthday."
]
		random_insult=random.choice(insult_list)
		return str(random_insult)

	if user_message in ("diss me", "insult me"):
		insult_list=[
"You must have been born on a highway, because that's where most accidents happen.",
"You're a failed abortion whose birth certificate is an apology from the condom factory.",
"It looks like your face caught on fire and someone tried to put it out with a fork. :fork_and_knife:",
"Your family tree is a cactus, because everybody on it is a prick. :cactus:",
"You're so ugly Hello Kitty said goodbye to you.",
"You're so ugly that when your mama dropped you off at school she got a fine for littering.",
"If you were twice as smart, you'd still be stupid.",
"Do you have to leave so soon? I was just about to poison the tea. :tea:",
"You're so ugly when you popped out the doctor said 'aww, what a treasure!' and your mom said 'yeah, lets bury it!'",
"We all sprang from apes, but you didn't spring far enough.",
"I hear when you were a child your mother wanted to hire somebody to take care of you, but the mafia wanted too much.",
"Out of 100,000 sperm, you were the fastest?",
"I would ask how old you are, but I know you can't count that high.",
"If you really want to know about mistakes, you should ask your parents.",
"I could eat a bowl of alphabet soup and crap out a smarter comeback than what you just said. :hankey:",
"When you were born, the police arrested your dad, the doctor slapped your mom, animal control euthanized your brother, and A&E made a documentary that saved your life.",
"Your mamma so fat she has to wear 2 watches because she covers two time zones. :watch:",
"You must be the arithmetic man; you add trouble, subtract pleasure, divide attention, and multiply ignorance.",
"You're so fat the only letters of the alphabet you know are KFC.",
"You're so fat you need cheat codes to play Wii Fit.",
"With a face like yours, I wish I was blind.",
"Why don't you check up on eBay and see if they have a life for sale. :moneybag:",
"Is that your face? Or did your neck just throw up?",
"The only positive thing about you is your HIV status.",
"Here's 20 cents, call all your friends and give me back the change. :moneybag:",
"Your mom is so stupid she tried to wake a sleeping bag.",
"Your mom is so fat when she jumped in the ocean the whales :whale: :whale2: started singing 'We Are Family' :notes:",
"Can I borrow your face? My arse is on holiday.",
"Your mom is so fat, when she went to a doctor, she stepped on a scale and the doctor said hey kid thats my phone number"
"How many times do I need to flush to get rid of you?",
"I bet your brain feels as good as new, seeing that you never use it.",
"I could eat a bowl of alphabet soup and shit out a smarter statement than that.",
"I do not exactly hate you, but if you were on fire and I had water, I would drink it.",
"I have neither the time nor the crayons to explain this to you.",
"I may love to shop but I am not buying your bullshit.",
"I was not born with enough middle fingers to let you know how I feel about you.",
"I would like to see things from your point of view but I cannot seem to get my head that far up my ass.",
"I would slap you, but shit stains.",
"I am no proctologist, but I know an asshole when I see one.",
"I am not saying I hate you, but I would unplug your life support to charge my phone.",
"If I wanted to kill myself I would climb your ego and jump to your IQ.",
"If I were to slap you, it would be considered animal abuse!",
"If laughter is the best medicine, your face must be curing the world.",
"If you are going to be two faced, at least make one of them pretty.",
"If you are gonna be a smartass, first you have to be smart. Otherwise you are just an ass.",
"Is your ass jealous of the amount of shit that just came out of your mouth?",
"It looks like your face caught on fire and someone tried to put it out with a hammer.",
"It is better to let someone think you are an idiot than to open your mouth and prove it.",
"I am jealous of all the people that have not met you!",
"Maybe if you ate some of that makeup you could be pretty on the inside.",
"Roses are red violets are blue, God made me pretty, what happened to you?",
"Roses are red, violets are blue, I have 5 fingers, the 3rd ones for you.",
"Shut up, you will never be the man your mother is.",
"Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology.",
"The last time I saw a face like yours I fed it a banana.",
"The only way you will ever get laid is if you crawl up a chicken ass and wait.",
"Two wrongs do not make a right, take your parents as an example.",
"Well I could agree with you, but then we would both be wrong.",
"What are you going to do for a face when the baboon wants his butt back?",
"You are so ugly, when your mom dropped you off at school she got a fine for littering.",
"You bring everyone a lot of joy, when you leave the room.",
"You must have been born on a highway because that is where most accidents happen.",
"You should not play hide and seek, no one would look for you.",
"Your birth certificate is an apology letter from the condom factory.",
"Your family tree must be a cactus because everybody on it is a prick.",

]
		random_insult=random.choice(insult_list)
		return str(random_insult)

	return "i dont understand you"
