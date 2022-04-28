# SiteOnPythonDjango
Simple blank site for blog on python framework Django with:
- administration panel;
- two level menu;
- upload files;
- desktop\mobile view.

![Alt text](screenshot/screen_mobile.jpg?raw=true "Mobile")

![Alt text](screenshot/screen_1.jpg?raw=true "Site_1")

![Alt text](screenshot/screen_2.jpg?raw=true "Site_2")

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
*This format url created for transfer articles from old site on joomla. You can change for yourself.

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
