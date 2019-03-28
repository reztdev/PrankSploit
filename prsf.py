#!/usr/bin/python

# This software is free you can redistribute it and or modify
# DISCLAIMER
# ----------
# This tools is a simple network penetrations and exploit
# Author and Create by Mochammad Rizki (ReztDev)
# Follow me on Intagram: @muhammad_ryzki07
# Visit source code: https://github.com/ReztDev/PrankSploit2
# If you find bugs and error in tools/program of prank toolkit, please report to me
# Email for report bugs: ryzkialvaro07@gmail.com

import src.source.use
import src.banner.color
import src.Logging.print_stdout
import src.Logging.Author
import bin.interfaces.MainConsole

class PrankSploit_Framework_Console(object):
	def __init__(self):
		src.Logging.print_stdout.slowprint(
			"{color1}[+]{color2} Starting PrankSploit Framework Console...".format(
				color1=src.banner.color.pycolor_style.B,
				color2=src.banner.color.pycolor_style.W
			)
		); src.source.use.time.sleep(1)

	@staticmethod
	def main():
		random_banner = [
				src.banner.color.banner_sploit,
				src.banner.color.banner_bold,
				src.banner.color.banners,
				src.banner.color.banner_italic
			]
		print_out = src.source.use.random.choice(random_banner)

		if src.source.use.os.name == "nt":
			print(print_out())
			print(
				src.banner.color.word_banner()
			)
			try:
				bin.interfaces.MainConsole.main_interfaces()
			except KeyboardInterrupt:
				src.Logging.print_stdout.print_error(
					'Interrupt user, Exiting...\n'
				)
				src.source.use.sys.exit(0)

		else:
			src.source.use.os.system('clear')
			print(print_out())
			print(
				src.banner.color.word_banner()
			)
			bin.interfaces.MainConsole.main_interfaces()


class Usage(object):
	def __init__(self):
		self.parser = src.source.use.argparse.ArgumentParser(
			description="PrankSploit Framework Toolkit (PRSF) Portable 2018",
			formatter_class=lambda prog: src.source.use.argparse.HelpFormatter(
				prog, max_help_position=80, width=110
			),
			epilog='{color}Copyright (c) ReztDev 2017. All rights reserved.{color1}'.format(
				color=src.banner.color.pycolor_style.L, color1=src.banner.color.pycolor_style.W
			)
		)

	def main(self):
		self.cracking = self.parser.add_argument_group(
			">> {color1}Cracking{color2}".format(
				color1=src.banner.color.pycolor_style.R,
				color2=src.banner.color.pycolor_style.W
			)
		)
		self.cracking.add_argument(
			'-cK', '--crack', action='store_true', dest='crack', help='Cracking hash password with wordlist'
		)
		self.cracking.add_argument(
			'-pw', '--password', dest='hash', help='Specify your hash password to crack'
		)
		self.cracking.add_argument(
			'-wD', '--wordlist', dest='wordlist', help='Specify file wordlist path'
		)

		self.overflow = self.parser.add_argument_group(
			">> {color1}Buffer Overflow Attack{color2}".format(
				color1=src.banner.color.pycolor_style.R,
				color2=src.banner.color.pycolor_style.W
			)
		)
		self.overflow.add_argument(
			'-buff', '--buffer', dest='buffer_overflow', action='store_true', help='FTP Buffer Overflow Attack'
		)
		self.overflow.add_argument(
			'-T', '--target', dest='target_host', help='Specify your target host (ex: 192.168.1.1, www.target.com)'
		)
		self.overflow.add_argument(
			'-P', '--ports', dest='port_target', type=int, default=21, help='Specify port target (default port: 21)'
		)

		self.handler = self.parser.add_argument_group(
			">> {color1}Remote Shell{color2}".format(
				color1=src.banner.color.pycolor_style.R,
				color2=src.banner.color.pycolor_style.W
			)
		)
		self.handler.add_argument(
			'-rM', '--listen', dest='remote', action='store_true', help='Listener handler (Remote Connect Back Shell)'
		)
		self.handler.add_argument(
			'-lhost', '--localhost', dest='localhost', help='Specify ip address in use your machine'
		)
		self.handler.add_argument(
			'-lport', '--localport', type=int, dest='localport', help='Specify port number as listener', default=4444
		)

		self.injection = self.parser.add_argument_group(
			">> {color1}Injection{color2}".format(
				color1=src.banner.color.pycolor_style.R,
				color2=src.banner.color.pycolor_style.W
			)
		)
		self.injection.add_argument(
			'--dump', '--dumping', dest='dumping', action='store_true', help='Dumping username and password target site (vuln SQL Injection)'
		)
		self.injection.add_argument(
			'-rH', '--rhost', dest='rhost', help='Specify your target site. example: http://site-target.com/index.php?id=x'
		)

		self.ftp_bruter = self.parser.add_argument_group(
			">> {color1}FTP Brute Forcer{color2}".format(
				color1=src.banner.color.pycolor_style.R,
				color2=src.banner.color.pycolor_style.W
			)
		)
		self.ftp_bruter.add_argument(
			'-ftp', '--FTP', action='store_true', dest='ftp_force', help='Brute force with protocol FTP'
		)
		self.ftp_bruter.add_argument(
			'-H', '--host', dest='hostname', help='Specify your target hostname (ex: www.target.com)'
		)
		self.ftp_bruter.add_argument(
			'-u', '--user', dest='username', help='Specify set username to brute force (recommended: "anonymous")'
		)
		self.ftp_bruter.add_argument(
			'-pW', '--passwd', dest='password', help='Specify filename password list to brute force'
		)

		self.interactive = self.parser.add_argument_group(
			">> {color1}Interactive{color2}".format(
					color1=src.banner.color.pycolor_style.R,
					color2=src.banner.color.pycolor_style.W
				)
			)
		self.interactive.add_argument(
				'-w', '--wizard', dest='wizard', action='store_true', help='Simple wizard interfaces for beginner users'
			)

		self.parser.add_argument(
			'-v', '--version', dest='version', action='store_true', help='show version and about tools'
		)
		sploit = self.parser.parse_args()
		if sploit.version:
			print(
				src.Logging.Author.show_version()
			)

		elif sploit.crack:
			import bin.exploit.pycrack.pycrack
			crack = bin.exploit.pycrack.pycrack.MainCracking_Password(
				sploit.hash, sploit.wordlist
			)
			crack.runCrack()

		elif sploit.buffer_overflow:
			import bin.exploit.BufferOverflow
			buff = bin.exploit.BufferOverflow.Buffer_Overflow(
				sploit.target_host, sploit.port_target
			)
			buff.run_overflow()

		elif sploit.remote:
			import bin.exploit.ListenerHandler.RemoteHandler
			run = bin.exploit.ListenerHandler.RemoteHandler.Listener_Handler(
				sploit.localhost, sploit.localport
			)
			run.main_handler()

		elif sploit.dumping:
			import bin.exploit.injection
			dump = bin.exploit.injection.Injection_Username_Password(sploit.rhost)
			dump.main_injection()

		elif sploit.ftp_force:
			import bin.exploit.ftpbrute
			run = bin.exploit.ftpbrute.FTP_Brute_Force(
				sploit.hostname, sploit.username, sploit.password
			); run.mainBruteForce()

		else:
			su_root = PrankSploit_Framework_Console().main()

def main():
	use = Usage()
	use.main()

if __name__ == '__main__':
	main()
