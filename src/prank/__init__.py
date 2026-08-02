"""Turns every uncaught exception into emotional damage."""

import sys
import random

__version__ = "0.1.1"
__all__ = ["install", "uninstall", "is_installed", "__version__"]

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
	ZeroDivisionError: "Math is hard.",
	FileNotFoundError: "The file has successfully escaped.",
	KeyboardInterrupt: "Coward.",
	MemoryError: "Have you considered downloading more RAM?",
	RecursionError: "Have you tried recursing less?",
	PermissionError: "The OS said no.",
	AttributeError: "Maybe None isn't what you thought it was.",
	KeyError: "The key has gone on vacation.",
	(ImportError, ModuleNotFoundError): "pip install hope",
	AssertionError: "Your assumptions were... optimistic.",
	TypeError: "Those types were never meant to be together.",
	IndexError: "That index is beyond the horizon.",
	(NameError, UnboundLocalError): "Did you forget to introduce yourself?",
	NotImplementedError: "Future you will deal with this.",
	TimeoutError: "Patience.exe has stopped responding.",
	UnicodeDecodeError: "Your bytes are speaking another language.",
	UnicodeEncodeError: "Unicode strikes again.",
	UnicodeTranslateError: "Lost in translation.",
	UnicodeError: "Unicode is once again reminding us who's boss.",
	ValueError: "Right type. Wrong value.",
	BrokenPipeError: "The pipe has retired.",
	OSError: "The operating system chose violence.",
	RuntimeError: "Runtime had a bad day.",
	EOFError: "The input gave up.",
	OverflowError: "Congratulations, you found infinity.",
	SyntaxError: "Python couldn't even parse your creativity.",
	(IndentationError, TabError): "Tabs and spaces have declared war.",
	StopIteration: "Nothing more to iterate. Literally.",
	StopAsyncIteration: "The async universe has ended.",
	ConnectionRefusedError: "The server left you on read.",
	ConnectionResetError: "Connection rage-quit.",
	ConnectionAbortedError: "The connection changed its mind.",
	ConnectionError: "Have you tried blaming the internet?",
	IsADirectoryError: "That's a folder. Nice try.",
	NotADirectoryError: "Folders don't work that way.",
	FileExistsError: "That file already exists. Like your bugs.",
	InterruptedError: "Something interrupted your masterpiece.",
	ProcessLookupError: "The process vanished into thin air.",
	ChildProcessError: "The child process has run away.",
	LookupError: "Whatever you wanted isn't here.",
	ReferenceError: "That object has moved on.",
	BufferError: "The buffer is buffering... too much.",
	ArithmeticError: "Math has filed a complaint.",
	FloatingPointError: "Floating point strikes again.",
	BlockingIOError: "The operation is taking a coffee break.",
	GeneratorExit: "The generator has retired peacefully.",
	SystemError: "Congratulations. You confused Python itself.",
	SystemExit: "See you next execution.",
}

old_hook = None
_installed = False

def my_hook(exc_type, exc_value, exc_tb):
	if old_hook is not None:
		old_hook(exc_type, exc_value, exc_tb)
	msg = random.choice(random_messages)
	for exception, message in exception_messages.items():
		if issubclass(exc_type, exception):
			msg = message
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
		sys.excepthook = my_hook
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