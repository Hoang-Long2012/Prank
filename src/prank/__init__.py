"""Turns every uncaught exception into emotional damage."""

import sys
import random

__version__ = "0.1.5"
__author__ = "Hoàng Long"
__all__ = ["install", "uninstall", "is_installed", "__version__", "__author__"]

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
	),
	FileNotFoundError: (
		"The file has successfully escaped.",
		"This file is currently on a long vacation.",
		"The path you've chosen is spiritually absent.",
	),
	KeyboardInterrupt: (
		"Coward.",
		"You pressed Ctrl+C in a moment of weakness.",
		"The program heard your panic and stopped.",
	),
	MemoryError: (
		"Have you considered downloading more RAM?",
		"The machine is tired of your ambition.",
		"This process has exceeded the memory of reality.",
	),
	RecursionError: (
		"Have you tried recursing less?",
		"The recursion rabbit hole has gone too deep.",
		"Infinite recursion is a lifestyle choice, apparently.",
	),
	PermissionError: (
		"The OS said no.",
		"The operating system has a boundary issue.",
		"You are not allowed to touch that file.",
	),
	AttributeError: (
		"Maybe None isn't what you thought it was.",
		"That object has no idea what you're asking for.",
		"Attribute access: 0% confidence.",
	),
	KeyError: (
		"The key has gone on vacation.",
		"That dictionary key has left the chat.",
		"The map says the value is somewhere else.",
	),
	(ImportError, ModuleNotFoundError): (
		"pip install hope",
		"The dependency politely declined.",
		"A module named 'this' does not exist.",
	),
	AssertionError: (
		"Your assumptions were... optimistic.",
		"Reality has disagreed with your hypothesis.",
		"The assertion was stronger than your confidence.",
	),
	TypeError: (
		"Those types were never meant to be together.",
		"The type system has filed a complaint.",
		"Python is refusing to be creative today.",
	),
	IndexError: (
		"That index is beyond the horizon.",
		"The list has no interest in your ambition.",
		"Your index is trying to escape the bounds.",
	),
	(NameError, UnboundLocalError): (
		"Did you forget to introduce yourself?",
		"That variable has not been born yet.",
		"You referenced a name that never existed.",
	),
	NotImplementedError: (
		"Future you will deal with this.",
		"This feature exists in theory only.",
		"The code was never finished, but the bug is.",
	),
	TimeoutError: (
		"Patience.exe has stopped responding.",
		"The network took a very long coffee break.",
		"The operation timed out and left you hanging.",
	),
	UnicodeDecodeError: (
		"Your bytes are speaking another language.",
		"The text was encoded with bad manners.",
		"Unicode had an unexpected opinion.",
	),
	UnicodeEncodeError: (
		"Unicode strikes again.",
		"Your text cannot be represented in this format.",
		"The characters refused to fit.",
	),
	UnicodeTranslateError: (
		"Lost in translation.",
		"The interpreter could not translate the vibes.",
		"Unicode is not in the mood for that conversion.",
	),
	UnicodeError: (
		"Unicode is once again reminding us who's boss.",
		"The bytes are trying to cause trouble.",
		"Your encoding assumptions have been challenged.",
	),
	ValueError: (
		"Right type. Wrong value.",
		"The value is valid in theory, invalid in practice.",
		"This value has been rejected by reality.",
	),
	BrokenPipeError: (
		"The pipe has retired.",
		"The output stream has quit the chat.",
		"The connection ended before the message did.",
	),
	OSError: (
		"The operating system chose violence.",
		"The OS is not feeling cooperative today.",
		"Something below Python has a problem.",
	),
	RuntimeError: (
		"Runtime had a bad day.",
		"Something happened at runtime, and it was not graceful.",
		"The program has entered an unfortunate chapter.",
	),
	EOFError: (
		"The input gave up.",
		"Your file ended before the program did.",
		"The stream reached the end and so did your patience.",
	),
	OverflowError: (
		"Congratulations, you found infinity.",
		"The number has exceeded the mood of the system.",
		"This arithmetic operation got too ambitious.",
	),
	SyntaxError: (
		"Python couldn't even parse your creativity.",
		"The code was written in a language only the parser hates.",
		"Syntax is not optional, even for genius ideas.",
	),
	(IndentationError, TabError): (
		"Tabs and spaces have declared war.",
		"Indentation is not optional, apparently.",
		"The code has a disagreement about spacing.",
	),
	StopIteration: (
		"Nothing more to iterate. Literally.",
		"The iterator has reached the end of the story.",
		"There are no more values to harvest.",
	),
	StopAsyncIteration: (
		"The async universe has ended.",
		"The async iterator is done speaking.",
		"The await chain has reached its final breath.",
	),
	ConnectionRefusedError: (
		"The server left you on read.",
		"The remote host has decided not to connect.",
		"Connection refused by the universe.",
	),
	ConnectionResetError: (
		"Connection rage-quit.",
		"The socket decided to reset its dignity.",
		"The connection was interrupted by pure spite.",
	),
	ConnectionAbortedError: (
		"The connection changed its mind.",
		"The remote side quit the handshake.",
		"Your connection has been unexpectedly canceled.",
	),
	ConnectionError: (
		"Have you tried blaming the internet?",
		"The network has chosen chaos.",
		"Connection issues are not a personal attack, but they feel like one.",
	),
	IsADirectoryError: (
		"That's a folder. Nice try.",
		"You tried to treat a directory like a file. Bold.",
		"Directories are not for that kind of operation.",
	),
	NotADirectoryError: (
		"Folders don't work that way.",
		"That path is a directory, not a file. Obvious in hindsight.",
		"This operation expects a file and gets a folder instead.",
	),
	FileExistsError: (
		"That file already exists. Like your bugs.",
		"The file refuses to be created twice.",
		"This path already has a resident occupant.",
	),
	InterruptedError: (
		"Something interrupted your masterpiece.",
		"The system call was rudely interrupted.",
		"Your operation did not get to finish its monologue.",
	),
	ProcessLookupError: (
		"The process vanished into thin air.",
		"The process ID is not returning to the party.",
		"That process has become a ghost story.",
	),
	ChildProcessError: (
		"The child process has run away.",
		"Your subprocess has decided to leave early.",
		"The child process is not participating today.",
	),
	LookupError: (
		"Whatever you wanted isn't here.",
		"The lookup failed in a very dramatic way.",
		"Search results: 0, confidence: 0.",
	),
	ReferenceError: (
		"That object has moved on.",
		"The variable is still a ghost in memory.",
		"This object has gone to a place your code cannot reach.",
	),
	BufferError: (
		"The buffer is buffering... too much.",
		"The buffer has reached its emotional limit.",
		"This memory buffer is currently overwhelmed.",
	),
	ArithmeticError: (
		"Math has filed a complaint.",
		"Arithmetic has become a legal dispute.",
		"The numbers have collectively rejected your logic.",
	),
	FloatingPointError: (
		"Floating point strikes again.",
		"The decimal point has lost its nerve.",
		"The float is not behaving well under pressure.",
	),
	BlockingIOError: (
		"The operation is taking a coffee break.",
		"The I/O call is currently unavailable.",
		"The system is politely refusing to block itself.",
	),
	GeneratorExit: (
		"The generator has retired peacefully.",
		"The generator heard enough and left.",
		"This generator has chosen a dignified exit.",
	),
	SystemError: (
		"Congratulations. You confused Python itself.",
		"The interpreter has entered a state of existential doubt.",
		"A system error means the internals are now judging you.",
	),
	SystemExit: (
		"See you next execution.",
		"The process decided it was time to leave.",
		"The program has exited with style.",
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
