# SiteOnPythonDjango
Simple blank site for blog on python framework Django with:
- administration panel;
- two level menu;
- upload files.

![Alt text](screenshot/site_1.png?raw=true "Site_1")

![Alt text](screenshot/site_2.png?raw=true "Site_2")

Administration panel:<br>
Login: admin<br>
Pass: admin

![Alt text](screenshot/site_3.png?raw=true "Site_3")

![Alt text](screenshot/site_4.png?raw=true "Site_4")

Url's format siteName/subCategName/url.html<br>
  where:<br>
  subCategName (subcategory): string<br>
  url (post) : int - string<br>
Example: http://linux-bash.ru/mtext/35-pdf.html


Modify python files:<br>
/blog/linuxbash/admin.py<br>
/blog/linuxbash/models.py<br>
/blog/linuxbash/views.py<br>
/blog/blog/settings.py<br>
/blog/blog/urls.py<br>


HTML templates:<br>
/blog/templates/*<br>


CSS files:<br>
/blog/static/static/css/main.css<br>


Uploaded files from administration panel:<br>
/blog/static/files/blog/*<br>
