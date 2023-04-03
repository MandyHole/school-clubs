![School Clubs logo]{% static 'media/School-Clubs-white-logo.png' %}

## School Clubs Website

This website is designed for a particular independent prep school in the UK who offer a Breakfast and Supper Club, offering functionality for both parents and school administrators. Parents are able to book their child/children onto regular sessions (eg every Monday morning), edit their contact details as well as request one-off additions or cancellations. Administrators are able to see who has recently requested a change requiring approval, edit details if needed and approve/deny requests. 

For the purpose of this project, all references to the name of the school have been removed although their overall branding has been used. In a real-world scenario, the school’s logo would be used in the main menu to reassure the users that it is a legitimate website.


## User Experience

<ul><li><strong>User Stories</strong></li>
<ul><li>Site Users</li><ul><li>As a Site User, I would like to be able to create an account so I can view/amend my bookings.</li>
<li>As a Site User, I would like to be able to block book specified days so that I don’t have to select dates individually.
</li>
<li>As a Site User, I would like to be able to add/amend my details so that I can manage how I am contacted.
</li>
<li>As a Site User, I would like my child’s year to be automatically updated at the start of the next academic year so that I don't have to do it manually.</li>
<li>As a Site User, I would like past dates to automatically disappear from the booking option so that it is easier to find the date that I want.</li>
</ul></ul>
<ul><li>Site Administrators</li><ul><li>As a Site Admin, I would like to be able to see who is signed up for a particular date so that I can prepare resources accordingly.</li>
<li>As a Site Admin, I would like to easily move pupils up a Year Group at the start of the next academic year and not allow parents to amend this field so that I know the Year Groups remain accurate.
</li>
<li>As a Site Admin, I would like to know if someone makes an amendment so that I can update my record for who is attending each session.
<li>As a Site Admin, I would like to be able to add / remove a particular pupil from a club on a specified date so that an approved last minute cancellation or a pupil who showed up without booking can be accounted for.</li>
<li>As a Site Admin, I would like to restrict users’ ability to amend a booking so that they can only cancel bookings that are more than one day in the future.</li>
<li>As a Site Admin, I would like to be able to limit the dates so that people can only book dates where the club is available.</li>
</li>
</ul>


</ul>

<li><strong>Design</strong></li>
<ul><li>Typography</li>
<ul><li>Quattrocento (used throughout the site) and Rotis Sans Serif (logo only) were chosen based on the brand guidelines of the Independent Prep School that inspired this project. They convey the quality and prestige provided by the school, which (whilst historic) still embraces modern ideas.</li></ul>
<li>Colour Scheme</li>
<ul><li>The colours were chosen based off of brand guidelines of the Independent School who inspired this project. Again, these specific colours were chosen to convey the quality and prestige the historic yet modern school has to offer.</li>
</ul>

<li>Imagery</li>
<ul><li>The images at the top were chosen to reassure parents and their children about the delicious and nutritious food that is on offer at the clubs. The images are large and prominent to entice people new to the clubs and also remind them why they like going.</li>
<li>In an ideal scenario, these would be pictures of food served at the actual club. However, given the fictional nature of this project, images were sourced from the Pexel website.</ul></ul>

<li><strong>Wireframes</strong></li>
<ul><li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1680528111/Prep-School-homepage-mockup-web_zqbmkw.jpg" aria-label="a wireframe of the desktop homepage" target="new">Mockup of the Homepage (desktop view)</a></li>
<li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1680528326/Prep-School-mockup-mobile2_copy_gvhyxs.jpg" aria-label="a wireframe of the mobile homepage" target="new">Mockup of the Homepage (mobile view)</a></li>
<li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1680528410/Prep-School-form-page_p73el3.jpg" aria-label="a wireframe of a small form (desktop)" target="new">Mockup of a small form (desktop view)</a></li></ul>
</ul>

## Features
<ul>
<li>Responsive on all device sizes</li>
<li>Login authentication</li>
<li>Linked to a database that users can amend/delete/create content to</li>
<li>Admin control panel for superusers</li>
</ul>


## Technologies Used

### Languages Used
<ul>
<li>HTML5</li>
<li>CSS</li>
<li>Javascript</li>
<li>Python</li>
</ul>

### Frameworks, Libraries & Programs Used
<ul>
<li><strong>Bootstrap 5.0:</strong> used to assist with the responsiveness and styling of the website.</li>
<li><strong>Google Fonts:</strong> used to import the 'Quattrocento' font into the base.html file which is used on all pages.</li>
<li><strong>Font Awesome:</strong> used in the navigation (mobile view).</li>
<li><strong>Git:</strong> used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.</li>
<li><strong>GitHub:</strong> used to store the projects code after being pushed from Git.</li>
<li><strong>Adobe Photoshop:</strong> used to resize images for the website.</li>
<li><strong>Adobe InDesign:</strong> used to create the wireframes during the design process.</li>
<li><strong>Adobe Illustrator:</strong> used to create the logo.</li>
<li><strong>Django:</strong> used to help make the website more quickly and with less code.</li>
<li><strong>Cloudinary:</strong> used to store photographs for the project</li>
</ul>

## Testing

<strong>HTML:</strong> Tested with W3C Markup Validator

<strong>CSS:</strong> Tested with W3C CSS Validator

<strong>Javascript:</strong> Tested with https://codebeautify.org/jsvalidate

<strong>Python:</strong> Tested with Pep8

<strong>Colour contrast:</strong> Tested using https://webaim.org/resources/contrastchecker/

### User Story Testing

<ol><li>As a Site User, I would like to be able to create an account so I can view/amend my bookings.
<ul><li>If a user isn't currently signed in, they are given very limited options as to what they are able to do when they get to the homepage (either sign in or sign up) so that they are aware that they can create an account. Once signed in, they have two other options: Add a child or manage bookings so they can easily see by the buttons/menu that they have the facility to add and amend bookings"</li></ul></li>
<li>As a Site User, I would like to be able to block book specified days so that I don’t have to select dates individually.
<ul><li>When adding a child, users have the option to tick which session(s) they'd like the child to have each week (for example, Breakfast on Mondays and Supper on Tuesdays) rather than requesting a series of dates.</li></ul>
</li>
<li>As a Site User, I would like to be able to add/amend my details so that I can manage how I am contacted.<ul>
<li>Users aren't asked to provide an email when initially adding a child as the information is pulled from their user login information. However, they have the option to update their email when they amend their child in case it changes in future. </li></ul>
</li>
<li>As a Site User, I would like my child’s year to be automatically updated at the start of the next academic year so that I don't have to do it manually.
<ul><li>Admininstrators can make the Year Group go up a year in the admin panel (using the pupil model) by selecting all pupils and using the action "Advance year". After Year 6, the clubs would no longer be available so those pupils' records would be deleted during the advancement process. I didn't give users the ability to amend a pupil's year as it isn't something that would need to be changed apart from during the summer when the admins will run the action. Giving them the ability would create a risk that parents would advance it in the summer before the admins had a chance. </li></ul>
</li>
<li>As a Site User, I would like past dates to automatically disappear from the booking option so that it is easier to find the date that I want.<ul>
<li>The date request form has been designed using a date picker that defaults to the current date. Should they select a date that is in the past or doesn't give the 48 hours required notice, the admins will have the opportunity to deny the request based on insufficient notice. </li></ul>
</li>
<li>As a Site Admin, I would like to be able to see who is signed up for a particular date so that I can prepare resources accordingly.
<ul><li>In the admin area, under the Date Request model, admins can order the list based on the date of the request to see if there are any approved cancellations/additional date requests for any particular date. That, in conjunction with the regular attendees, which can be found in the pupil model by filtering by session, will provide all of the pupils who should be at a particular session.</li></ul></li>
<li>As a Site Admin, I would like to easily move pupils up a Year Group at the start of the next academic year and not allow parents to amend this field so that I know the Year Groups remain accurate.
<ul><li>Admininstrators can make the Year Group go up a year in the admin panel (using the pupil model) by selecting all pupils and using the action "Advance year". After Year 6, the clubs would no longer be available so those pupils' records would be deleted during the advancement process. I didn't give users the ability to amend a pupil's year as it isn't something that would need to be changed apart from during the summer when the admins will run the action. Giving them the ability would create a risk that parents would advance it in the summer before the admins had a chance. </li></ul>
</li>
<li>As a Site Admin, I would like to know if someone makes an amendment so that I can update my record for who is attending each session.
<ul><li>When a user adds / amends their details or requests a one-off request, the approval status is set at either 'Pending Approval' / 'Awaiting Approval' respectively. The admin can use this as a filter and then approve/decline the request as required and update their records for that session. The approval status is conveyed to the user on the "Manage Bookings" page.</li></ul>
</li>
<li>As a Site Admin, I would like to be able to add / remove a particular pupil from a club on a specified date so that an approved last minute cancellation or a pupil who showed up without booking can be accounted for.</li>
<li>As a Site Admin, I would like to restrict users’ ability to amend a booking so that they can only cancel bookings that are more than one day in the future.</li>
<li>As a Site Admin, I would like to be able to limit the dates so that people can only book dates where the club is available.</li>
</li>
</ul>


</ul>



To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!



<ul><li>#be9f56 (gold) passed with black on gold / vice versa</li>
<li>#003e6b (navy) passed with white on navy / vice versa</li>
<li>#56a0d8(light blue) passed with black / vice versa</li>
</li></ul>

 with a particular thanks to the following photographers:</li>
<ul><li>pexels-alexander-mils-2103949</li>
<li>pexels-chan-walrus-958545</li>
<li>pexels-elviss-railijs-bitans-1448665</li>
<li>pexels-jer-chung-2116094</li>
<li>pexels-nicola-barts-7937469</li>
<li>pexels-lukas-1352270</li>
<li>pexels-sydney-troxell-718739</li>
</li></ul>

<li>The colours were tested for contrast using https://webaim.org/resources/contrastchecker/</li>