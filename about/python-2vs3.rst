**************
Python 2 vs. 3
**************


Rationale
=========
* `six <http://pythonhosted.org/six/>`_
* `Wall of Super Powers <https://python3wos.appspot.com>`_
* Unicode - bytes


Standard Library Renames
========================

+------------------------------+-------------------------------------+-------------------------------------+
| Name                         | Python 2 name                       | Python 3 name                       |
+==============================+=====================================+=====================================+
| ``builtins``                 | ``__builtin__``                     | ``builtins``                        |
+------------------------------+-------------------------------------+-------------------------------------+
| ``configparser``             | ``ConfigParser``                    | ``configparser``                    |
+------------------------------+-------------------------------------+-------------------------------------+
| ``copyreg``                  | ``copy_reg``                        | ``copyreg``                         |
+------------------------------+-------------------------------------+-------------------------------------+
| ``cPickle``                  | ``cPickle``                         | ``pickle``                          |
+------------------------------+-------------------------------------+-------------------------------------+
| ``cStringIO``                | ``cStringIO.StringIO``              | ``io.StringIO``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``dbm_gnu``                  | ``gdbm``                            | ``dbm.gnu``                         |
+------------------------------+-------------------------------------+-------------------------------------+
| ``_dummy_thread``            | ``dummy_thread``                    | ``_dummy_thread``                   |
+------------------------------+-------------------------------------+-------------------------------------+
| ``email_mime_multipart``     | ``email.MIMEMultipart``             | ``email.mime.multipart``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``email_mime_nonmultipart``  | ``email.MIMENonMultipart``          | ``email.mime.nonmultipart``         |
+------------------------------+-------------------------------------+-------------------------------------+
| ``email_mime_text``          | ``email.MIMEText``                  | ``email.mime.text``                 |
+------------------------------+-------------------------------------+-------------------------------------+
| ``email_mime_base``          | ``email.MIMEBase``                  | ``email.mime.base``                 |
+------------------------------+-------------------------------------+-------------------------------------+
| ``filter``                   | ``itertools.ifilter``               | ``filter``                          |
+------------------------------+-------------------------------------+-------------------------------------+
| ``filterfalse``              | ``itertools.ifilterfalse``          | ``itertools.filterfalse``           |
+------------------------------+-------------------------------------+-------------------------------------+
| ``getcwd``                   | ``os.getcwdu``                      | ``os.getcwd``                       |
+------------------------------+-------------------------------------+-------------------------------------+
| ``getcwdb``                  | ``os.getcwd``                       | ``os.getcwdb``                      |
+------------------------------+-------------------------------------+-------------------------------------+
| ``http_cookiejar``           | ``cookielib``                       | ``http.cookiejar``                  |
+------------------------------+-------------------------------------+-------------------------------------+
| ``http_cookies``             | ``Cookie``                          | ``http.cookies``                    |
+------------------------------+-------------------------------------+-------------------------------------+
| ``html_entities``            | ``htmlentitydefs``                  | ``html.entities``                   |
+------------------------------+-------------------------------------+-------------------------------------+
| ``html_parser``              | ``HTMLParser``                      | ``html.parser``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``http_client``              | ``httplib``                         | ``http.client``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``BaseHTTPServer``           | ``BaseHTTPServer``                  | ``http.server``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``CGIHTTPServer``            | ``CGIHTTPServer``                   | ``http.server``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``SimpleHTTPServer``         | ``SimpleHTTPServer``                | ``http.server``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``input``                    | ``raw_input``                       | ``input``                           |
+------------------------------+-------------------------------------+-------------------------------------+
| ``intern``                   | ``intern``                          | ``sys.intern``                      |
+------------------------------+-------------------------------------+-------------------------------------+
| ``map``                      | ``itertools.imap``                  | ``map``                             |
+------------------------------+-------------------------------------+-------------------------------------+
| ``queue``                    | ``Queue``                           | ``queue``                           |
+------------------------------+-------------------------------------+-------------------------------------+
| ``range``                    | ``xrange``                          | ``range``                           |
+------------------------------+-------------------------------------+-------------------------------------+
| ``reduce``                   | ``reduce``                          | ``functools.reduce``                |
+------------------------------+-------------------------------------+-------------------------------------+
| ``reload_module``            | ``reload``                          | ``importlib.reload``                |
+------------------------------+-------------------------------------+-------------------------------------+
| ``reprlib``                  | ``repr``                            | ``reprlib``                         |
+------------------------------+-------------------------------------+-------------------------------------+
| ``shlex_quote``              | ``pipes.quote``                     | ``shlex.quote``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``socketserver``             | ``SocketServer``                    | ``socketserver``                    |
+------------------------------+-------------------------------------+-------------------------------------+
| ``_thread``                  | ``thread``                          | ``_thread``                         |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter``                  | ``Tkinter``                         | ``tkinter``                         |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_dialog``           | ``Dialog``                          | ``tkinter.dialog``                  |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_filedialog``       | ``FileDialog``                      | ``tkinter.FileDialog``              |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_scrolledtext``     | ``ScrolledText``                    | ``tkinter.scrolledtext``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_simpledialog``     | ``SimpleDialog``                    | ``tkinter.simpledialog``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_ttk``              | ``ttk``                             | ``tkinter.ttk``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_tix``              | ``Tix``                             | ``tkinter.tix``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_constants``        | ``Tkconstants``                     | ``tkinter.constants``               |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_dnd``              | ``Tkdnd``                           | ``tkinter.dnd``                     |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_colorchooser``     | ``tkColorChooser``                  | ``tkinter.colorchooser``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_commondialog``     | ``tkCommonDialog``                  | ``tkinter.commondialog``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_tkfiledialog``     | ``tkFileDialog``                    | ``tkinter.filedialog``              |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_font``             | ``tkFont``                          | ``tkinter.font``                    |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_messagebox``       | ``tkMessageBox``                    | ``tkinter.messagebox``              |
+------------------------------+-------------------------------------+-------------------------------------+
| ``tkinter_tksimpledialog``   | ``tkSimpleDialog``                  | ``tkinter.simpledialog``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``urllib.parse``             | ``six.moves.urllib.parse``          | ``urllib.parse``                    |
+------------------------------+-------------------------------------+-------------------------------------+
| ``urllib.error``             | ``six.moves.urllib.error``          | ``urllib.error``                    |
+------------------------------+-------------------------------------+-------------------------------------+
| ``urllib.request``           | ``six.moves.urllib.request``        | ``urllib.request``                  |
+------------------------------+-------------------------------------+-------------------------------------+
| ``urllib.response``          | ``six.moves.urllib.response``       | ``urllib.response``                 |
+------------------------------+-------------------------------------+-------------------------------------+
| ``urllib.robotparser``       | ``robotparser``                     | ``urllib.robotparser``              |
+------------------------------+-------------------------------------+-------------------------------------+
| ``urllib_robotparser``       | ``robotparser``                     | ``urllib.robotparser``              |
+------------------------------+-------------------------------------+-------------------------------------+
| ``UserDict``                 | ``UserDict.UserDict``               | ``collections.UserDict``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``UserList``                 | ``UserList.UserList``               | ``collections.UserList``            |
+------------------------------+-------------------------------------+-------------------------------------+
| ``UserString``               | ``UserString.UserString``           | ``collections.UserString``          |
+------------------------------+-------------------------------------+-------------------------------------+
| ``winreg``                   | ``_winreg``                         | ``winreg``                          |
+------------------------------+-------------------------------------+-------------------------------------+
| ``xmlrpc_client``            | ``xmlrpclib``                       | ``xmlrpc.client``                   |
+------------------------------+-------------------------------------+-------------------------------------+
| ``xmlrpc_server``            | ``SimpleXMLRPCServer``              | ``xmlrpc.server``                   |
+------------------------------+-------------------------------------+-------------------------------------+
| ``xrange``                   | ``xrange``                          | ``range``                           |
+------------------------------+-------------------------------------+-------------------------------------+
| ``zip``                      | ``itertools.izip``                  | ``zip``                             |
+------------------------------+-------------------------------------+-------------------------------------+
| ``zip_longest``              | ``itertools.izip_longest``          | ``itertools.zip_longest``           |
+------------------------------+-------------------------------------+-------------------------------------+
