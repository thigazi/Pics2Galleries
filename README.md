# Pics2Galleries

Aim of this project is to provide a Web Picture Gallery System that everybody can use for it's own purposes.  
This WebSystem will have the capabilities to create PhotoAlbums, upload pictures and share those for those with
restricted (authenticated) and unrestricted access.

All the pictures will be accessed and stored generally in binary form in the Database and not in the filesystem or one
of the Filesharing Providers which are Google Drive, Microsoft OneDrive, Dropbox, Huddle.

As the Python ORM Module takes place, this Picture Managment System will have a broad support for a large number of
Databases as we will use SQLAlchemy.

If you want to check if your database is supported you can check the Dialects here:  
url: https://docs.sqlalchemy.org/en/14/dialects/

The Software makes use of the MicroFramework Flask and will have over the time Backend support for ZODB, MongoDB and
SQLAlchemy are the Database Engines that will be used in this entire development process.

Authentication should be possible with OAuth with further security feature 2FA that can be used with Google
Authenticator or Redhat's FreeOTP that is available for Android and Iphone.

I splitted up the project itself in Taks:

- [X] Basic Application Skeleton
- [ ] Backend Development
- [ ] Frontend Development
- [ ] FileSharing Google Drive, DropBox API
- [ ] Database ZODB, SqlAlchemy, MongoDB API
- [ ] Access API with XML-RPC and REST to access restricted Picture Album Access or to perform administration tasks like
  adding/deleting Albums or Pictures
