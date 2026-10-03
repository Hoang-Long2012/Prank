"""Turns every uncaught exception into emotional damage."""

import random
import sys

__version__ = "0.1.5"
__author__ = "Hoàng Long"
__all__ = ["__author__", "__version__", "install", "is_installed", "uninstall"]

random_messages = [
	"Stack Overflow is waiting for you.",
	"git blame won't save you this time.",
	"Expected behavior.",
	"Feature, not a bug.",
	"I'm disappointed in you.",
	"Fucking bug.",
	"It worked yesterday.",
	"Congratulations, you found another bug.",
	"Skill issue.",
	"Have you tried turning it off and on again?",
	"Who wrote this code?",
]

rare_messages = [
	"This message has a 1% drop rate.",
	"The debugger is judging you.",
	"Congratulations, you found the developer's secret.",
	"Error successfully generated.",
	"Please don't report this.",
	"The universe has decided against your code today.",
	"Trust me, it's not DNS... probably.",
	"This exception is sponsored by coffee.",
	"404: Motivation not found.",
	"Your bug has evolved.",
	"Congratulations. This bug unlocks the secret ending.",
	"You weren't supposed to see this.",
	"Developer mode activated.",
	"The bug is now self-aware.",
	"Achievement unlocked: Segmentation Imagination.",
]

ultra_rare_messages = [
	"You have been chosen.",
	"Developer console unlocked.",
	"Thanks for finding me.",
	"This line exists solely for people with terrible luck.",
]

exception_messages = {
	ZeroDivisionError: (
		"Math is hard.",
		"You divided by zero. Some days are just not your day.",
		"The calculator has left the building.",
		"Division by zero: a classic act of rebellion.",
		"Zero is not a valid emotional support number.",
		"Even mathematics has given up on you.",
	),
	FileNotFoundError: (
		"The file has successfully escaped.",
		"This file is currently on a long vacation.",
		"The path you've chosen is spiritually absent.",
		"Your file is not in the building anymore.",
		"The operating system has no idea where that thing went.",
		"This path has entered the witness protection program.",
	),
	KeyboardInterrupt: (
		"Coward.",
		"You pressed Ctrl+C in a moment of weakness.",
		"The program heard your panic and stopped.",
		"You gave up on the process. It did not return the favor.",
		"Interrupting a program is not a personality trait.",
		"The keyboard has judged your resolve.",
	),
	MemoryError: (
		"Have you considered downloading more RAM?",
		"The machine is tired of your ambition.",
		"This process has exceeded the memory of reality.",
		"Your code has become a memory goblin.",
		"The machine is now in a full-blown existential crisis.",
		"It appears your variables are overachieving.",
	),
	RecursionError: (
		"Have you tried recursing less?",
		"The recursion rabbit hole has gone too deep.",
		"Infinite recursion is a lifestyle choice, apparently.",
		"Your function found the bottomless pit.",
		"The stack is now participating in a dramatic collapse.",
		"This recursion has gone beyond the cartoon stage.",
	),
	PermissionError: (
		"The OS said no.",
		"The operating system has a boundary issue.",
		"You are not allowed to touch that file.",
		"The system is enforcing a personal boundary.",
		"Security says: no, and means it.",
		"Access denied. The universe has rules.",
	),
	AttributeError: (
		"Maybe None isn't what you thought it was.",
		"That object has no idea what you're asking for.",
		"Attribute access: 0% confidence.",
		"The object has decided to be a mystery today.",
		"This attribute was never invited to the party.",
		"No attribute found. The object is keeping secrets.",
	),
	KeyError: (
		"The key has gone on vacation.",
		"That dictionary key has left the chat.",
		"The map says the value is somewhere else.",
		"Your dictionary has decided to be unhelpful.",
		"That key is currently refusing all contact.",
		"The mapping has expired emotionally.",
	),
	(ImportError, ModuleNotFoundError): (
		"pip install hope",
		"The dependency politely declined.",
		"A module named 'this' does not exist.",
		"The library is currently hiding from you.",
		"Import failed. The environment has opinions.",
		"Python cannot find your missing companion module.",
	),
	AssertionError: (
		"Your assumptions were... optimistic.",
		"Reality has disagreed with your hypothesis.",
		"The assertion was stronger than your confidence.",
		"Your code has been challenged by facts.",
		"An assumption failed. The truth won.",
		"The assertion found your confidence lacking.",
	),
	TypeError: (
		"Those types were never meant to be together.",
		"The type system has filed a complaint.",
		"Python is refusing to be creative today.",
		"The types have turned against each other.",
		"This operation was built on incompatible vibes.",
		"Data types are not sharing the same worldview.",
	),
	IndexError: (
		"That index is beyond the horizon.",
		"The list has no interest in your ambition.",
		"Your index is trying to escape the bounds.",
		"The sequence has politely told you to stop.",
		"Your list is shorter than your dreams.",
		"The index is no longer in this dimension.",
	),
	(NameError, UnboundLocalError): (
		"Did you forget to introduce yourself?",
		"That variable has not been born yet.",
		"You referenced a name that never existed.",
		"The variable exists only in your imagination.",
		"You tried to use a name with no legal identity.",
		"Somebody forgot to declare this character.",
	),
	NotImplementedError: (
		"Future you will deal with this.",
		"This feature exists in theory only.",
		"The code was never finished, but the bug is.",
		"This method has not yet discovered purpose.",
		"The author left TODOs in the shape of this error.",
		"A half-finished idea is now haunting your runtime.",
	),
	TimeoutError: (
		"Patience.exe has stopped responding.",
		"The network took a very long coffee break.",
		"The operation timed out and left you hanging.",
		"The server has decided not to answer today.",
		"Your request has gone to the void.",
		"This call is still waiting for a miracle.",
	),
	UnicodeDecodeError: (
		"Your bytes are speaking another language.",
		"The text was encoded with bad manners.",
		"Unicode had an unexpected opinion.",
		"Your bytes are not speaking plain English.",
		"The decoding process has become a cultural conflict.",
		"This string has been encoded by a very rude algorithm.",
	),
	UnicodeEncodeError: (
		"Unicode strikes again.",
		"Your text cannot be represented in this format.",
		"The characters refused to fit.",
		"The output device has rejected your personality.",
		"Unicode is not feeling cooperative.",
		"This encoding format has a personal vendetta.",
	),
	UnicodeTranslateError: (
		"Lost in translation.",
		"The interpreter could not translate the vibes.",
		"Unicode is not in the mood for that conversion.",
		"This text has no passport to the target encoding.",
		"The Unicode gods have denied your request.",
		"The translation layer has gone rogue.",
	),
	UnicodeError: (
		"Unicode is once again reminding us who's boss.",
		"The bytes are trying to cause trouble.",
		"Your encoding assumptions have been challenged.",
		"This text has entered a character crisis.",
		"Unicode is not accepting your explanation.",
		"A byte sequence has chosen chaos.",
	),
	ValueError: (
		"Right type. Wrong value.",
		"The value is valid in theory, invalid in practice.",
		"This value has been rejected by reality.",
		"A good value, in all the wrong circumstances.",
		"This input has the wrong energy.",
		"The value is trying to be a different kind of variable.",
	),
	BrokenPipeError: (
		"The pipe has retired.",
		"The output stream has quit the chat.",
		"The connection ended before the message did.",
		"The pipe has chosen a dramatic exit.",
		"The stream is tired of being used.",
		"A broken pipe is just a relationship gone cold.",
	),
	OSError: (
		"The operating system chose violence.",
		"The OS is not feeling cooperative today.",
		"Something below Python has a problem.",
		"The system layer is throwing a tantrum.",
		"Your program met the OS and did not win.",
		"The kernel has entered a mood.",
	),
	RuntimeError: (
		"Runtime had a bad day.",
		"Something happened at runtime, and it was not graceful.",
		"The program has entered an unfortunate chapter.",
		"Your code survived execution and then immediately betrayed you.",
		"The runtime is now asking for a therapist.",
		"The application has become a cautionary tale.",
	),
	EOFError: (
		"The input gave up.",
		"The file ended before the program did.",
		"The stream reached the end and so did your patience.",
		"The input ended with unexpected finality.",
		"Your data stream ran out of excuses.",
		"The source has closed early, like a bad farewell.",
	),
	OverflowError: (
		"Congratulations, you found infinity.",
		"The number has exceeded the mood of the system.",
		"This arithmetic operation got too ambitious.",
		"Your integer has gone beyond the limits of reality.",
		"The number is trying to escape the container.",
		"This calculation is a little too much for the universe.",
	),
	SyntaxError: (
		"Python couldn't even parse your creativity.",
		"The code was written in a language only the parser hates.",
		"Syntax is not optional, even for genius ideas.",
		"The parser has rejected your masterpiece.",
		"Your code is missing a comma and a personality.",
		"The grammar of this script has been betrayed.",
	),
	(IndentationError, TabError): (
		"Tabs and spaces have declared war.",
		"Indentation is not optional, apparently.",
		"The code has a disagreement about spacing.",
		"Your indentation strategy has become a legal issue.",
		"The block structure is currently in a civil war.",
		"The parser is offended by your visual choices.",
	),
	StopIteration: (
		"Nothing more to iterate. Literally.",
		"The iterator has reached the end of the story.",
		"There are no more values to harvest.",
		"The sequence is done talking.",
		"The loop ended before your expectations did.",
		"The iterable has gone to sleep.",
	),
	StopAsyncIteration: (
		"The async universe has ended.",
		"The async iterator is done speaking.",
		"The await chain has reached its final breath.",
		"The event loop is no longer interested in continuing.",
		"This coroutine decided to stop being dramatic.",
		"Async iteration has left the chat.",
	),
	ConnectionRefusedError: (
		"The server left you on read.",
		"The remote host has decided not to connect.",
		"Connection refused by the universe.",
		"The port is currently pretending to be unavailable.",
		"The server has taken a very strong stance against you.",
		"This connection was rejected before it even began.",
	),
	ConnectionResetError: (
		"Connection rage-quit.",
		"The socket decided to reset its dignity.",
		"The connection was interrupted by pure spite.",
		"The network has chosen to restart the relationship.",
		"Your TCP handshake got ghosted.",
		"The remote host has been emotionally unavailable.",
	),
	ConnectionAbortedError: (
		"The connection changed its mind.",
		"The remote side quit the handshake.",
		"Your connection has been unexpectedly canceled.",
		"The peer walked away mid-protocol.",
		"The network was never committed to this conversation.",
		"The socket has left the building.",
	),
	ConnectionError: (
		"Have you tried blaming the internet?",
		"The network has chosen chaos.",
		"Connection issues are not a personal attack, but they feel like one.",
		"The internet is briefly becoming an abstract concept.",
		"This connection is currently in a suspicious mood.",
		"The remote side has asserted its independence.",
	),
	IsADirectoryError: (
		"That's a folder. Nice try.",
		"You tried to treat a directory like a file. Bold.",
		"Directories are not for that kind of operation.",
		"A folder was used where a file was expected. Puzzling.",
		"The OS is correcting your misunderstanding.",
		"This path is a directory and has no interest in your plan.",
	),
	NotADirectoryError: (
		"Folders don't work that way.",
		"That path is a directory, not a file. Obvious in hindsight.",
		"This operation expects a file and gets a folder instead.",
		"The path insistently remains a directory.",
		"A folder is not pretending to be a file.",
		"The OS has pointed at the folder and laughed.",
	),
	FileExistsError: (
		"That file already exists. Like your bugs.",
		"The file refuses to be created twice.",
		"This path already has a resident occupant.",
		"The file has already been there since before you wrote this code.",
		"The filesystem does not allow duplicate destiny.",
		"The path is already occupied by a stubborn little ghost.",
	),
	InterruptedError: (
		"Something interrupted your masterpiece.",
		"The system call was rudely interrupted.",
		"Your operation did not get to finish its monologue.",
		"The world has chosen to interrupt your flow.",
		"Something outside the program has done a dramatic stop.",
		"This operation was canceled by fate and an OS signal.",
	),
	ProcessLookupError: (
		"The process vanished into thin air.",
		"The process ID is not returning to the party.",
		"That process has become a ghost story.",
		"The process was here a second ago and now is not.",
		"A process lookup failed, and the universe is smug about it.",
		"The PID has gone somewhere without leaving a map.",
	),
	ChildProcessError: (
		"The child process has run away.",
		"Your subprocess has decided to leave early.",
		"The child process is not participating today.",
		"The subprocess escaped before your code could finish.",
		"This child process has entered a rebellion phase.",
		"The worker process is not replying to calls anymore.",
	),
	LookupError: (
		"Whatever you wanted isn't here.",
		"The lookup failed in a very dramatic way.",
		"Search results: 0, confidence: 0.",
		"The object has disappeared from the registry.",
		"The lookup ended with a sigh and no answer.",
		"This value was never found and never will be.",
	),
	ReferenceError: (
		"That object has moved on.",
		"The variable is still a ghost in memory.",
		"This object has gone to a place your code cannot reach.",
		"You are trying to reach an object that no longer exists.",
		"The reference has left the building.",
		"Your pointer is now wandering a dead memory lane.",
	),
	BufferError: (
		"The buffer is buffering... too much.",
		"The buffer has reached its emotional limit.",
		"This memory buffer is currently overwhelmed.",
		"The buffer is now experiencing a full-scale existential crisis.",
		"The memory block has become dramatically unstable.",
		"The buffer wishes to file a complaint.",
	),
	ArithmeticError: (
		"Math has filed a complaint.",
		"Arithmetic has become a legal dispute.",
		"The numbers have collectively rejected your logic.",
		"This calculation has become an emotional offense.",
		"The arithmetic gods have decided to be petty.",
		"Your numbers are not negotiating in good faith.",
	),
	FloatingPointError: (
		"Floating point strikes again.",
		"The decimal point has lost its nerve.",
		"The float is not behaving well under pressure.",
		"This number has exceeded the limits of representation.",
		"The float is suffering from a very specific kind of chaos.",
		"Binary floating point has become your enemy.",
	),
	BlockingIOError: (
		"The operation is taking a coffee break.",
		"The I/O call is currently unavailable.",
		"The system is politely refusing to block itself.",
		"The file descriptor is taking a little timeout.",
		"The device is not ready, and the universe is not helping.",
		"This I/O operation has decided not to cooperate today.",
	),
	GeneratorExit: (
		"The generator has retired peacefully.",
		"The generator heard enough and left.",
		"This generator has chosen a dignified exit.",
		"The generator has concluded its story without warning.",
		"A generator has closed itself with dramatic finality.",
		"The iterator has simply decided to stop being useful.",
	),
	SystemError: (
		"Congratulations. You confused Python itself.",
		"The interpreter has entered a state of existential doubt.",
		"A system error means the internals are now judging you.",
		"The Python runtime has encountered a deep identity crisis.",
		"The interpreter is raising an eyebrow at your code.",
		"The system is now asking if you really meant to do that.",
	),
	SystemExit: (
		"See you next execution.",
		"The process decided it was time to leave.",
		"The program has exited with style.",
		"This program is ending before it learns an answer.",
		"A clean exit, but emotionally it was dramatic.",
		"The runtime is taking a final bow.",
	),
}

old_hook = None
_installed = False


def excepthook(exc_type, exc_value, exc_tb):
	if old_hook is not None:
		old_hook(exc_type, exc_value, exc_tb)
	if not issubclass(exc_type, Warning):
		msg = random.choice(random_messages)
		for exception, messages in exception_messages.items():
			if issubclass(exc_type, exception):
				msg = random.choice(messages)
				break
		bad_luck = random.random()
		if bad_luck < 0.001:
			msg = random.choice(ultra_rare_messages)
		elif bad_luck < 0.01:
			msg = random.choice(rare_messages)
		print(msg, file=sys.stderr)


def install():
	"""Start your fun debugging journey."""
	global _installed
	if not _installed:
		global old_hook
		old_hook = sys.excepthook
		sys.excepthook = excepthook
		_installed = True
		if random.random() < 0.01:
			print("You shouldn't have installed me.", file=sys.stderr)
		else:
			print("Welcome, hope the bug comes your way.", file=sys.stderr)


def uninstall():
	"""Call this function to end this debugging trip."""
	global _installed
	if _installed:
		global old_hook
		sys.excepthook = old_hook
		old_hook = None
		_installed = False
		if random.random() < 0.001:
			print("Goodbye. See you after the next bug.", file=sys.stderr)
		else:
			print("Goodbye, hope you had fun.", file=sys.stderr)


def is_installed():
	"""Check your mental state."""
	return _installed
