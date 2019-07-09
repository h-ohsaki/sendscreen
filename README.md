# NAME

sendscreen - Display local desktop on remove host over LAN without VGA/HDMI cable

# SYNOPSIS

```
sendscreen [-vrf] [-s host] [-p port] [-W width] [-H height] [-F #]
  -v       verbose mode
  -r       receiver mode
  -f       full speed mode (no frame rate limit)
  -s host  specify receiver hostname/address
  -p port  port number
  -W #     screen width (default: 800 [pixel])
  -H #     screen height (default: 600 [pixel])
  -F #     maximum frame rate (default: 10 [frame/second])
```

# DESCRIPTION

This manual page documents **sendscreen**, a Python program to continuously
capture and transmit the desktop to remote host over LAN (Local Area
Networking) using UDP (User Datagram Protocol).

**sendscreen** was developed to eliminate hassles at research meetings in our
laboratory.  At a meeting, participants bring their own laptops, and during a
meeting, they repeatedly (1) take the VGA/HDMI video cable connected to the
LCD projector, (2) plug the VGA/HDMI video connector to his/her laptop, (3)
enable the external video output (e.g., by pressing Fn + F7), (4) unplug the
VGA/HDMI video connector, and (5) pass it to another participant.  Such
awkward procedure had been endlessly performed during the meeting.  With
**sendscreen**, you no longer need to worry about the video cable and enabling
the external video output on your laptop.

**sendscreen** works either as a *sender* or a *receiver*.  
**sendscreen** works as a sender by default, and it repeatedly capture the
desktop and send the zlib-compressed image (frame) to the receiver.  When
invoked with `-r` option, **sendscreen** works as a *receiver*.  It waits for
incoming frame data over LAN.  When it receives the frame data from a sender,
the frame is uncompressed and displayed on the screen of the receiver.

# USAGE

On a computer connected with the LCD projector:

```sh
sendscreen -r
```

On a client computer:

```sh
sendscreen -s server_name
```
where *server_name* is the hostname or the IP address of the receiver.

**sendscreen** uses the UDP protocol with port 5000 by default.  Please make
sure that the sender reaches the port 5000 of the receiver using the UDP
protocol; i.e., disalbe the network firewall and packet filtering (e.g.,
`iptagles -F; iptables -X`).

# OPTIONS

- -v

  Verbose mode.  **sendscreen** will display additional information during
  execution.

- -r

  Receiver mode.  **sendscreen** receives frames from a sender in your LAN.

- -f

  Full throttle mode.  **sendscreen** tries to send frames as fast as
  possible.

- -s host

  Specify receiver's hostname or IP address.

- -p port

  Port number at which the receiver receives frame data.

- -w width

  Specify the screen width (default: 800 [pixel]).

- -h height

  Specify the screen height (default: 600 [pixel]).

- -F rate

  Maximum frate rate is limited by *rate* (default: 5 [frame/s])

# REQUIREMENTS

**sendscreen** runs on X Window System.  It uses Xlib, pygame, and rgbconv
modules as well as several Python standard modules.  **sendsceeen** asumes a
TrueType font is available at
`/usr/share/fonts/truetype/freefont/FreeSans.ttf', which is included in
*fonts-freefont-ttf* package in Debian GNU/Linux although **sendscreen** works
with any TrueType font.

# INSTALLATION

```sh
$ pip3 install sendscreen
```

# AVAILABILITY

The latest version of **sendscreen** is available at PyPI
(https://pypi.org/project/sendscreen/) .

# SEE ALSO

xset(1)

# AUTHOR

Hiroyuki Ohsaki <ohsaki[atmark]lsnl.jp>
