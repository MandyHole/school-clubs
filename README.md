## School Clubs Website 
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1677704293/School-Clubs-logo_iv88ip.png" width = 15% alt="School Clubs Logo"></a>

This responsive website is designed based on requirements of a particular independent prep school in the UK who offer a Breakfast and Supper Club, to give the necessary functionality for both parents and school administrators. Parents are able to book their child/children onto regular sessions (eg every Monday morning), edit their contact details as well as request one-off additions or cancellations. Administrators are able to see who has recently requested a change requiring approval, edit details if needed, approve/deny requests and see who is signed up to attend a particular session. 

For the purpose of this project, all references to the name of the school have been removed although their overall branding has been used. In a real-world scenario, the school’s logo would be used in the main menu to reassure the users that it is a legitimate website and their contact details would be on the website.

Link to deployed site: <a href="https://school-clubs.herokuapp.com/" target="new" aria-label="Deployed School CLubs website">https://school-clubs.herokuapp.com/</a>

<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1681989521/sampleviews_smx7zw.png" width = 95% alt="Sample views of School Clubs website"></a>

## Contents
<a href="#UX" aria-label="Jump to User Experience">User Experience</a>
<ul>
<li><a href="#stories" aria-label="Jump to User Exeperience: User Stories">User Stories</a></li>
<li><a href="#design" aria-label="Jump to User Exeperience: Design">Design (typography, colour and imagery)</a></li>
<li><a href="#wireframes" aria-label="Jump to User Exeperience: Wireframes">Wireframes</a></li></ul>
<p><a href="#features" aria-label="Jump to Features">Key Features</a></p>
<p><a href="#technologies" aria-label="Jump to Technologies">Technologies Used</a></p>
<ul>
<li><a href="#languages" aria-label="Jump to Technologies: Languages Used">Languages Used</a></li>
<li><a href="#frameworks" aria-label="Jump to Technologies: Frameworks, Programmes and Libraries">Frameworks, Programmes and Libraries</a></li>
</ul>
<p><a href="#testing" aria-label="Jump to Testing">Testing</a></p>
<ul>
<li><a href="#html" aria-label="Jump to Testing: HTML">HTML</a></li>
<li><a href="#css" aria-label="Jump to Testing: CSS">CSS</a></li>
<li><a href="#java" aria-label="Jump to Testing: Javascript">Javascript</a></li>
<li><a href="#lighthouse" aria-label="Jump to Testing: Lighthouse">Lighthouse</a></li>
<li><a href="#python" aria-label="Jump to Testing: Python">Python</a></li>
<li><a href="#contrast" aria-label="Jump to Testing: Colour Contrast">Colour Contrast</a></li>
<li><a href="#UX-test" aria-label="Jump to Testing: User Experience">User Story: Experience Testing</a></li>
<li><a href="#feature-test" aria-label="Jump to Testing: Feature Testing">Feature Testing</a></li>
<li><a href="#further-testing" aria-label="Jump to Testing: Feature Testing">Further Testing</a></li>
<li><a href="#fixed-bugs" aria-label="Jump to Testing: Fixed bugs">Fixed bugs</a></li>
<li><a href="#known-bugs" aria-label="Jump to Testing: Known bugs">Known bugs</a></li>
</ul>
<p><a href="#deploy" aria-label="Jump to Deployment and Local Development">Deployment and Local Development</a></p>
<ul>
<li><a href="#deployment" aria-label="Jump to Deployment">Deployment</a></li>
<li><a href="#fork" aria-label="Jump to How to fork the repo">How to fork the repo</a></li>
<li><a href="#clone" aria-label="Jump to How to clone the repo">How to clone the repo</a></li>
</ul>
<p><a href="#credits" aria-label="Jump to Credits">Credits</a></p>
<ul>
<li><a href="#code" aria-label="Jump to Credits - Code">Code</a></li>
<li><a href="#content" aria-label="Jump to Credits - Content">Content</a></li>
<li><a href="#media" aria-label="Jump to Credits - Media">Media</a></li>
</ul>


<h2 id="UX">User Experience</h2>

<ul id="stories"><li><strong>User Stories</strong></li>
<ul><li>Site Users</li><ul><li>As a Site User, I would like to be able to create an account so I can view/amend my bookings.</li>
<li>As a Site User, I would like to be able to block book specified days so that I don’t have to select dates individually.
</li>
<li>As a Site User, I would like to be able to add/amend my details so that I can manage how I am contacted.
</li>
<li>As a Site User, I would like my child’s year to be automatically updated at the start of the next academic year so that I don't have to do it manually.</li>
<li>As a Site User, I would like past dates to automatically disappear from the booking option so that it is easier to find the date that I want.</li>
<li>As a Site User I would like to know the status of my requests so I know whether or not the sessions have been successful booked.</li>
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

<li id="design"><strong>Design</strong></li>
<ul><li>Typography</li>
<ul><li>Quattrocento, a serif font available on Google Font, (used throughout the site) and Rotis Sans Serif, a semi-serif font, (logo only) were chosen based on the brand guidelines of the Independent Prep School that inspired this project. They convey the quality and prestige provided by the school, which (whilst historic) still embraces modern ideas. By following the brand guidelines of the school used on their other sites, it reassures users of authenticity.</li></ul>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1681990321/text_sample_cyv8xj.png" width = 75% alt="Examples of fonts used"></a>
<li>Colour Scheme</li>
<ul><li>The colours were chosen based off of brand guidelines of the Independent School who inspired this project. Again, these specific colours were chosen to convey the quality and prestige the historic yet modern school has to offer and by following the brand guidelines of the school used on their other sites, it reassures users of authenticity.</li>
</ul>
<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1681990075/colour-usage_yfosyw.png" width = 25% alt="Examples of colours used"></a>


<li>Imagery</li>
<ul><li>The images at the top were chosen to reassure parents and their children about the delicious and nutritious food that is on offer at the clubs. The images are large and prominent to entice people new to the clubs and also remind them why they like going.</li>
<li>In an ideal scenario, these would be pictures of food served at the actual club. However, given the fictional nature of this project, images were sourced with thanks from the Pexel website.</ul></ul>

<img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1681992301/imagery-examples_fhbfp1.png" width = 95% alt="Sample images used in School Clubs website"></a>

<li id="wireframes"><strong>Wireframes</strong></li>
<ul><li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1680528111/Prep-School-homepage-mockup-web_zqbmkw.jpg" aria-label="a wireframe of the desktop homepage" target="new">Mockup of the Homepage (desktop view)</a></li>
<li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1680528326/Prep-School-mockup-mobile2_copy_gvhyxs.jpg" aria-label="a wireframe of the mobile homepage" target="new">Mockup of the Homepage (mobile view)</a></li>
<li><a href="https://res.cloudinary.com/dd4cchm7g/image/upload/v1680528410/Prep-School-form-page_p73el3.jpg" aria-label="a wireframe of a small form (desktop)" target="new">Mockup of a small form (desktop view)</a></li></ul>
</ul>

<h2 id="features">Key Features</h2>
<ul>
<li>Responsive on all device sizes</li>
<li>Login authentication</li>
<li>Linked to a database that users can amend/delete/create content to</li>
<li>Admin control panel for superusers</li>
</ul>


<h2 id="technologies">Technologies Used</h2>

<h3 id="languages">Languages Used</h3>
<ul>
<li>HTML5</li>
<li>CSS</li>
<li>Javascript</li>
<li>Python</li>
</ul>

<h3 id="frameworks"> Frameworks, Libraries & Programmes Used</h3>
<ul>
<li><strong>Bootstrap 5.0:</strong> used to assist with the responsiveness and styling of the website.</li>
<li><strong>J Query:</strong> used alongside Bootstrap.</li>
<li><strong>Google Fonts:</strong> used to import the 'Quattrocento' font into the base.html file which is used on all pages.</li>
<li><strong>Font Awesome:</strong> used in the navigation (mobile view).</li>
<li><strong>Git:</strong> used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.</li>
<li><strong>GitHub:</strong> used to store the projects code after being pushed from Git.</li>
<li><strong>Adobe Photoshop:</strong> used to resize images for the website.</li>
<li><strong>Adobe InDesign:</strong> used to create the wireframes during the design process.</li>
<li><strong>Adobe Illustrator:</strong> used to create the logo.</li>
<li><strong>Django:</strong> used to help make the website more quickly and with less code.</li>
<li><strong>Cloudinary:</strong> used to store photographs for the project</li>
<li><strong>ICO Converter:</strong> used to create a favicon from an image created in Illustrator <a href="https://www.icoconverter.com/" aria-label="ICO Converter website" target="new">ICO Converter website</a></li>
<li><strong>ElephantSQL:</strong> used to host the database</li>
</ul>

## Testing

<p id="html"><strong>HTML:</strong> Tested the following pages with <a href="https://validator.w3.org/" target="new" aria-label="W3C Markup Validator website">W3C Markup Validator</a> (I initially had some errors due to location of div elements in relation to python if / for statements, which I subsequently modified so they now pass)</p>
<ul>
<li>account/login.html</li>
<li>account/signup.html</li>
<li>account/logout.html</li>
<li>add_pupil.html</li>
<li>amend_pupil.html</li>
<li>date_request.html</li>
<li>index.html</li>
<li>manage_bookings.html</li>
</ul>

<p id="css"><strong>CSS:</strong> Tested static/css/style.css with <a href="https://jigsaw.w3.org/css-validator/" aria-label="W3C CSS Validator" target="new"> W3C CSS Validator</a> using the direct input method (no errors found) </p>

<p id="java"><strong>Javascript:</strong> Tested static/javascript/script.js with <a href="https://jshint.com/" target="new" aria-label="jshint website">Jshint website</a> (no errors found)</p>

<p id="python"><strong>Python:</strong> Tested the pages I created/used with Pycode Style (no errors found). See steps below:</p>
<ul><li>In the terminal, check you have pycodestyle installed by running: pip install pycodestyle</li>
<li>In the terminal, run pycodestyle --first *ADD RELATIVE FILEPATH HERE* for each of the pages you wish to check until no errors are found (see examples below)</li><ul>
<li>pycodestyle --first pupils/models.py</li>
<li>pycodestyle --first pupils/admin.py</li>
<li>pycodestyle --first pupils/forms.py</li>
<li>pycodestyle --first pupils/views.py</li>
<li>pycodestyle --first schoolclubs/urls.py</li>
<li>pycodestyle --first schoolclubs/settings.py (Please note that some pre-existing code from Django on settings.py failed due to line length, but all code that I added passed)</li></ul>
</ul>

<p id="lighthouse"><strong>Lighthouse:</strong> Overall good although I'd recommened exploring the performance recommendations in a future release, but left for now due to time constraints</p>
<img 
              src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682160626/Screenshot_2023-04-22_at_11.00.42_qrlqxz.png" width = 25% alt="Lighthouse report"></a>

<p id="contrast"><strong>Colour contrast:</strong> Tested using <a href="https://webaim.org/resources/contrastchecker/" target="new" aria-label="Webaim Contrast Checker Website">Webaim Contrast Checker Website</a></p>
<ul><li>#be9f56 (gold) passed with black on gold / vice versa</li>
<li>#003e6b (navy) passed with white on navy / vice versa</li>
<li>#56a0d8(light blue) passed with black / vice versa</li>
</li></ul>

<img 
              src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1681988623/colour-check_g139go.png" width = 25% alt="Visual of colour contrast"></a>

<h3 id="UX-test"> User Story: Experience Testing</h3>

| Goals | How are they achieved? | Image |
| :--- | :--- | :--- |
| `Site Users` |
|  |  |  |
| Account facility to add/view/amend bookings | If a user isn't currently signed in, they are given very limited options as to what they are able to do when they get to the homepage (either sign in or sign up) so that they are aware that they can create an account. Once signed in, they have two other options: Add a child or manage bookings so they can easily see by the buttons/menu that they have the facility to add and amend bookings | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682152659/Screenshot_2023-04-22_at_09.34.14_pupfzq.png" alt="Screenshot of account facility"> |
| Block bookings for specified days | When adding a child, users have the option to tick which session(s) they'd like the child to have each week (for example, Breakfast on Mondays and Supper on Tuesdays) rather than requesting a series of dates. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682152737/Screenshot_2023-04-22_at_09.38.46_sexpvi.png" alt="Screenshot of block bookings facility"> |
| Add/amend contact details | Users aren't asked to provide an email when initially adding a child as the information is pulled from their user login information (they are required to add an email when creating an account). However, they have the option to update their email when they amend their child in case it changes in future. They can also add/amend a contact number when adding/amending a child. Both are required fields| <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682153110/contact_h7fcxj.png" alt="Screenshot of amending contact details"> 
|
| Automatic updates for child's year | Admininstrators can make the Year Group go up a year in the admin panel (using the pupil model) by selecting all pupils and using the action "Advance year". After Year 6, the clubs would no longer be available so those pupils' records would be deleted during the advancement process. I didn't give users the ability to amend a pupil's year as it isn't something that would need to be changed apart from during the summer when the admins will run the action. By allowing users this ability, there would be a risk that parents would advance it in the summer before the admins had a chance, which would then make it inaccurate when the admin ran the function. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682153592/advance-year_r0ikqi.png" alt="Screenshot of amending contact details">  |
| Past dates to automatically disappear from the booking option | The date request form has been designed using a date picker that defaults to the current date. Should they select a date that is in the past or doesn't give the 48 hours required notice, the admins will have the opportunity to deny the request based on insufficient notice. Once the term has ended, admins would delete all the requested dates for that term. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682154766/approve-request_bpy9ru.png" alt="Screenshot of date picker and admin response">  |
| Know approval status for bookings | Messages appear that show when a form is successfully submitted. On the "Manage Booking" page, you can see the status of any requests and whether they are pending approval, declined (with a reason) or approved. Admins should review requests at a set time each workday to approve/deny in a timely manner. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682154837/Screenshot_2023-04-22_at_10.12.23_qnuie6.png" alt="Screenshot of date approval status"> |
|`Site Admins`|
|  |  |  |
| See who has signed up to attend a session| In the admin area, under the Date Request model, admins can order the list based on the date of the request to see if there are any approved cancellations/additional date requests for any particular date. That, in conjunction with the regular attendees, which can be found in the pupil model by filtering by session, will provide all of the pupils who should be at a particular session. In an ideal world, this would be streamlined better and cause less administrative work. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682156458/Attendance_lxsvyj.png" alt="Screenshot of accessing attendance">  |
| Move pupils up a Year Group / keep records accurate | Admininstrators can make the Year Group go up a year in the admin panel (using the pupil model) by selecting all pupils and using the action "Advance year". After Year 6, the clubs would no longer be available so those pupils' records would be deleted during the advancement process. I didn't give users the ability to amend a pupil's year as it isn't something that would need to be changed apart from during the summer when the admins will run the action. Giving them the ability would create a risk that parents would advance it in the summer before the admins had a chance. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682153592/advance-year_r0ikqi.png" alt="Screenshot of amending contact details"> |
| Know about amendments | When a user adds / amends their details or requests a one-off request, the approval status is set at either 'Pending Approval' / 'Awaiting Approval' respectively. The admin can use these as a filter and then approve/decline the request as required and update their records for that session. The approval status is conveyed to the user on the "Manage Bookings" page. This system requires admins to regularly check the admin panel and could be improved if they were instead notified by email or an alert (a potential enhancement in future). | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682156994/filter-edit_wrjshr.jpg" alt="Screenshot of amending contact details">|
|  Add / remove pupil from session | Site Admins can add/remove pupils using the Date Request Model in the admin section of the website. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682157232/Screenshot_2023-04-22_at_10.51.53_vruvhg.png" alt="Screenshot of amending contact details">|
| Restrict users’ ability to amend a booking: Insufficient notice | Site Admins have the ability to decline/approve any requests that are made. A 'pending' notice will be shown on the Manage Booking page until an admin declines the request, siting a reason of insufficient notice. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682154837/Screenshot_2023-04-22_at_10.12.23_qnuie6.png" alt="Screenshot of date approval status"> |
| Limit the dates booked | Site Admins have the ability to decline/approve any requests that are made. A 'pending' notice will be shown on the Manage Booking page until an admin declines the request, siting a reason of unavailable date if the date requested falls on a day when the club isn't running. | <img src="https://res.cloudinary.com/dd4cchm7g/image/upload/v1682154837/Screenshot_2023-04-22_at_10.12.23_qnuie6.png" alt="Screenshot of date approval status"> |  |


<h3 id="feature-test">Feature Testing</h3>


`Home Page - not logged in`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Reloads Home page | Clicked logo image | Home page reloads | Pass |
| Home Link in Navbar | Reloads Home page | Clicked link | Home page reloads | Pass |
| Sign In link in Navbar | Takes to Login form | Clicked Sign In | Opens /accounts/login/ | Pass |
| Sign Up link in Navbar | Takes to sign up form | Clicked Sign Up | Opens /accounts/signup/ | Pass |
| Hero Sign Up Button | Takes to sign up form | Clicked Sign Up button | Opens /accounts/signup/ | Pass |
| Hero Login Button | Takes to Login form | Clicked Login button | Opens /accounts/login/ | Pass |
| Breakfast Sign Up Button | Takes to sign up form | Clicked Sign Up button | Opens /accounts/signup/ | Pass |
| Breakfast Login Button | Takes to Login form | Clicked Login button | Opens /accounts/login/ | Pass |
| Supper Sign Up Button | Takes to sign up form | Clicked Sign Up button | Opens /accounts/signup/ | Pass |
| Supper Login Button | Takes to Login form | Clicked Login button | Opens /accounts/login/ | Pass |
| All buttons - hover effect | All buttons should go to a white background with navy text and a coloured border (the border becomes the same colour as the button in the normal state) when hovered over. | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu and one column design should appear in smaller screen sizes. The buttons in the hero image should disappear. The buttons in the Breakfast/Supper Club should appear on separate lines. | Reduced the width of the screen | Hamburger menu appeared, buttons in hero disappeared, buttons in body sections went onto separate lines | Pass |

`Home Page - logged in`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Reloads Home page | Clicked logo image | Home page reloads | Pass |
| Home Link in Navbar | Reloads Home page | Clicked link | Home page reloads | Pass |
| Add a Child link in Navbar | Takes to a form to add new pupil's info | Clicked Add a Child | Opens /add_pupil/ | Pass |
| Manage Bookings link in Navbar | Takes to page with info on previously made bookings | Clicked Manage Bookings | Opens /manage_bookings/ | Pass |
| Logout link in Navbar | Takes to page to logout | Clicked Logout | Opens /accounts/logout/ | Pass |
| Hero Add a Child Button | Takes to a form to add new pupil's info | Clicked Add a Child | Opens /add_pupil/ | Pass |
| Hero Manage Bookings Button | Takes to page with info on previously made bookings | Clicked Manage Bookings | Opens /manage_bookings/ | Pass |
| Breakfast Add a Child  Button | Takes to a form to add new pupil's info | Clicked Add a Child button | Opens /add_pupil/signup/ | Pass |
| Breakfast Manage Bookings Button | Takes to page with info on previously made bookings | Clicked Manage Bookings button | Opens /manage_bookings/ | Pass |
| Supper Add a Child  Button | Takes to a form to add new pupil's info | Clicked Add a Child button | Opens /add_pupil/signup/ | Pass |
| Supper Manage Bookings Button | Takes to page with info on previously made bookings | Clicked Manage Bookings button | Opens /manage_bookings/ | Pass |
| All buttons - hover effect | All buttons should go to a white background with navy text and a coloured border (the border becomes the same colour as the button in the normal state) when hovered over. | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu and one column design should appear in smaller screen sizes. The buttons in the hero image should disappear. The buttons in the Breakfast/Supper Club should appear on separate lines. | Reduced the width of the screen | Hamburger menu appeared, buttons in hero disappeared, buttons in body sections went onto separate lines | Pass |

`Sign In Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page Loads | Pass |
| Sign In link in Navbar | Reloads page | Clicked Sign In | /accounts/login/ reloaded | Pass |
| Sign Up link in Navbar | Takes to sign up form | Clicked Sign Up | Opens /accounts/signup/ | Pass |
| Sign Up link in navy box | Takes to sign up form | Clicked Sign Up | Opens /accounts/signup/ | Pass |
| Form validation: no blank fields | Get error | Submitted form without filling in fields | Saw message to fill in required field | Pass |
| Form validation: check details in database | Get error | Submitted form with incorrect information | Saw message 'The username and/or password you specified are not correct.' | Pass |
| Form validation: successful submission | Get success message and return to homepage with new options | Submitted form with correct info in full | Saw message stating I was successfully signed in and returned to homepage with options to manage bookings/add a child | Pass |
| Submit button - hover effect | Submit button should go to a white background with navy text and a gold border when hovered over. | Hover over the button on the page | The button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu should appear in smaller screen sizes, and the proportion of the sign up box width to screen should increase. | Reduced the width of the screen | Hamburger menu appeared, sign up box took up relatively more width | Pass |
| Redirects if already logged in | If a user is already logged in, they should be automatically redirected to the homepage with the options for logged in users if they go to /accounts/login/ . | Visited /accounts/login/ when logged in | Took me to homepage with logged in options | Pass |

`Sign Up Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page Loads | Pass |
| Sign In link in Navbar | Takes to Login form | Clicked Sign In | Opens /accounts/login/ | Pass |
| Sign Up link in Navbar | Reloads page | Clicked Sign Up | /accounts/signup/ reloaded | Pass |
| Sign In link in navy box | Takes to Login form | Clicked Sign In | Opens /accounts/login/ | Pass |
| Form validation: no blank fields | Get error | Submitted form without filling in fields | Saw message to fill in required field | Pass |
| Form validation: check existing username | Get error | Submitted form with a username already in use | Saw message 'A user with that username already exists.' | Pass |
| Form validation: check existing email address | Get error | Submitted form with an email already in use | Saw message 'A user is already registered with this e-mail address.' | Pass |
| Form validation: check passwords match | Get error | Submitted form with two different passwords | Saw message 'You must type the same password each time.' | Pass |
| Form validation: check password length | Get error | Submitted form with short password | Saw message 'This password is too short. It must contain at least 8 characters.' | Pass |
| Form validation: correct details | Get success message and return to homepage with new options | Submitted form with correct info in full | Returned to homepage with options to manage bookings/add a child and saw message stating I was successfully signed in and | Pass |
| Submit button - hover effect | Submit button should go to a white background with navy text and a gold border when hovered over. | Hover over the button on the page | The button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu should appear in smaller screen sizes, and the proportion of the sign up box width to screen should increase. | Reduced the width of the screen | Hamburger menu appeared, sign up box took up relatively more width | Pass |
| Redirects if already logged in | If a user is already logged in, they should be automatically redirected to the homepage with the options for logged in users if they go to /accounts/signup/ . | Visited /accounts/signup/ when logged in | Took me to homepage with logged in options | Pass |

`Add a Child Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page loads | Pass |
| Add a Child link in Navbar | Reloads page | Clicked Add a Child | reloaded /add_pupil/ | Pass |
| Manage Bookings link in Navbar | Takes to page with info on previously made bookings | Clicked Manage Bookings | Opens /manage_bookings/ | Pass |
| Logout link in Navbar | Takes to page to logout | Clicked Logout | Opens /accounts/logout/ | Pass |
| Restricted access | Form only available to logged in users | visited /add_pupil/ when logged out| Only see message "Please login to add a pupil" and a button to login page | Pass |
| Login button | Login button takes you to /accounts/login/ | when logged out, I clicked on login button | opens /accounts/login/ | Pass |
| Form validation: required fields aren't blank | Get error | Submitted form without filling in all required fields | Saw message to fill in field(s) | Pass |
| Form validation: confirmation of charges required | Get error | Submitted form correctly apart from ticking confirmation | Saw message " Please confirm you understand the charges" and "This field is required" in red | Pass |
| Form validation: correct details | Get success message and return to manage bookings with details showing that the booking is pending approval | Submitted form with correct info in full | Automatically redirected to /manage-bookings and saw message "Your child has been added successfully." Newly added info shows message "Booking Status: Pending Approval" | Pass |
| All buttons - hover effect | All buttons should go to a white background with navy text and a coloured border (the border becomes the same colour as the button in the normal state) when hovered over. | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu should appear in smaller screen sizes, and the proportion of the sign up box width to screen should increase. | Reduced the width of the screen | Hamburger menu appeared, sign up box took up relatively more width | Pass |

`Manage Bookings Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page loads | Pass |
| Add a Child link in Navbar | Takes to a page with a form to add a child | Clicked Add a Child | /add_pupil/ loads | Pass |
| Manage Bookings link in Navbar | Reloads page | Clicked Manage Bookings | reloaded /manage_bookings/ | Pass |
| Logout link in Navbar | Takes to page to logout | Clicked Logout | Opens /accounts/logout/ | Pass |
| Restricted access | page only available to logged in users | visited /manage_bookings/ when logged out| Only see message "Please login to see this page" and a button to login page | Pass |
| Login button | Login button takes you to /accounts/login/ | when logged out, I clicked on login button | opens /accounts/login/ | Pass |
| Content restricted by user | user should only see details of pupils added by them | visited /manage_bookings/ when logged in| Only see pupils associated with the current user | Pass |
| Page shows pupil's regular and requested slots | user should see their name, Year Group, Booking status and what they have booked | added/updated slots and added date requests | Saw all relevant details for the pupil as expected | Pass |
| Edit button | Should take to a page to edit details for the pupil named in the same box | Clicked button | Correct edit page appeared | Pass |
| Request button | Should take to a page to request a specific session change for the pupil named in the same box | Clicked button | Correct date request page appeared | Pass |
| Cancel button | Should only appear when status for a one-off date is 'Awaiting approval' | Approved / Denied requests as an admin | Cancel button disappeared | Pass |
| Cancel button | Should open modal to confirm deletion | Clicked cancel button | modal appeared | Pass |
| Modal - Cancel button | Should close modal without deleting request | Clicked cancel button on modal | modal disappeared | Pass |
| Modal - x button | Should close modal without deleting request | Clicked cancel button on modal | modal disappeared | Pass |
| Modal - Delete button | Should close modal and delete relevant request | Clicked delete button on modal | modal disappeared and relevant request was gone | Pass |
| Modal buttons - hover effect | Should turn gold and black text (if not black already) | Hovered over buttons | buttons turned gold and had black text | Pass |
| All buttons on page (not modal) - hover effect | All buttons should go to a white background with navy text and a coloured border (the border becomes the same colour as the button in the normal state) when hovered over. | Hover over each button on the page | Each button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu and one column design should appear on smaller screen sizes. | Reduced the width of the screen | Hamburger menu appeared, went to one column | Pass |

`Amend Pupil Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page loads | Pass |
| Add a Child link in Navbar | Takes to a page with a form to add a child | Clicked Add a Child | /add_pupil/ loads | Pass |
| Manage Bookings link in Navbar | Takes to a page with info on previous bookings | Clicked Manage Bookings | loaded /manage_bookings/ | Pass |
| Logout link in Navbar | Takes to page to logout | Clicked Logout | Opens /accounts/logout/ | Pass |
| Restricted access | page content only available to logged in users | visited /amend_pupil/4 when not logged in | Only see message "Login to edit this booking." with a Login button" | Pass |
| Restricted access | page content only available to logged in users associated with the particular child| visited /amend_pupil/4 when logged in as the wrong user (not admin) | Only see message "You need to login to the correct account before you can edit this booking." | Pass |
| Login button | Login button takes you to /accounts/login/ | when logged out, I clicked on login button | opens /accounts/login/ | Pass |
| Content restricted by user | user should only see details of pupils added by them | visited /manage_bookings/ when logged in| Only see pupils associated with the current user | Pass |
| Error if no pupil found | If the slug doesn't have a current pupil's id, then get a 404 | visited amend_pupil/400 | generates 404 error | Pass |
| Form validation: required fields aren't blank | Get error | Submitted form without filling in all required fields | Prompted to fill in field(s) | Pass |
| Form validation: correct details | Get success message and return to manage bookings with details showing that the booking is pending approval | Submitted form with correct info in full | Automatically redirected to /manage-bookings and saw message "Your requested amendments have been received successfully." Newly updated info shows message "Booking Status: Pending Approval" | Pass |
| Submit button - hover effect | Submit button should go to a white background with navy text and a gold border when hovered over. | Hover over the button on the page | The button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu and one column design should appear on smaller screen sizes. | Reduced the width of the screen | Hamburger menu appeared, went to one column | Pass |

`Date Request Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page loads | Pass |
| Add a Child link in Navbar | Takes to a page with a form to add a child | Clicked Add a Child | /add_pupil/ loads | Pass |
| Manage Bookings link in Navbar | Takes to a page with info on previous bookings | Clicked Manage Bookings | loaded /manage_bookings/ | Pass |
| Logout link in Navbar | Takes to page to logout | Clicked Logout | Opens /accounts/logout/ | Pass |
| Restricted access | page content only available to logged in users | visited /date_request/4 when not logged in | Only see message "Login to make a request." with a Login button" | Pass |
| Login button | Login button takes you to /accounts/login/ | when logged out, I clicked on login button | opens /accounts/login/ | Pass |
| Restricted access | page content only available to logged in users associated with the particular child| visited /date_request/5 when logged in as the wrong user (admin) | Only see message "You need to login to the correct account before you can make this request." | Pass |
| Error if no pupil found | If the slug doesn't have a current pupil's id, then get a 404 | visited date_request/400 | generates 404 error | Pass |
| Manage Bookings link in form box | Takes to a page with info on previous bookings | Clicked Manage Bookings page | loaded /manage_bookings/ | Pass |
| Form validation: required fields aren't blank | Get error | Submitted form without filling in all required fields | Prompted to fill in field(s) | Pass |
| Form validation: date format | Get error | Submitted form without year and tried typing a number higher than 12 in months | returned error / wouldn't allow | Pass |
| Form validation: correct details | Get success message and return to manage bookings with details showing that the request is pending approval and option to cancel request | Submitted form with correct info in full | Automatically redirected to /manage-bookings and saw message "Your date request has been submitted successfully." Date request in relevant box with Awaiting Approval status and a cancel button | Pass |
| Submit button - hover effect | Submit button should go to a white background with navy text and a gold border when hovered over. | Hover over the button on the page | The button displayed the correct styling when hovered over | Pass |
| Responsive Design | The 'hamburger' menu and one column design should appear on smaller screen sizes. | Reduced the width of the screen | Hamburger menu appeared, went to one column | Pass |


`Logout Page`

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Logo Image | Loads Home page | Clicked logo image | Home page loads | Pass |
| Home Link in Navbar | Loads Home page | Clicked link | Home page loads | Pass |
| Add a Child link in Navbar | Takes to a page with a form to add a child | Clicked Add a Child | /add_pupil/ loads | Pass |
| Manage Bookings link in Navbar | Takes to a page with info on previous bookings | Clicked Manage Bookings | loaded /manage_bookings/ | Pass |

<h3 id="further-testing">Further Testing</h3>
The Website was tested on Google Chrome and Safari browsers.

The website was viewed on a variety of devices such as Desktop, Laptop, iPhones and tablets.

A large amount of testing was done to ensure that all pages were linking correctly.

A large amount of testing was done to ensure that all database additions/updates were working correctly.

A large amount of testing was done to ensure that only users who were logged in had access to certain content. Also, the user had to match the pupil to view/amend personal details.

Testing was done to ensure that the site deployed by Heroku matched the local version on Gitpod.

Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

<h3 id="fixed-bugs">Key Fixed Bugs</h3>

The modal to confirm deletion was deleting the wrong record. This was because it was based on an ID that wasn't unique so it would delete the first record each time. Adding the variable for the date request id to the Modal's name and reference in the for loop fixed this issue (with thanks to my mentor for the support) with this.

The form to submit the date request would reject dates in an incorrect format without giving the user any feedback as to why their submission didn't work. Adding a date picker put the date in the correct format to make it user friendly and obvious to the user.

<h3 id="known-bugs">Known Bugs</h3>
<p>On mobile devices, the hamburger/x menu icons move slightly when clicked.</p>


<h2 id="deploy"> Deployment & Local Development</h2>

<h3 id="deployment">Deployment</h3>
This project was deployed through Heroku (live link found here: https://school-clubs.herokuapp.com/) using the following steps:
<ol>
<li>Login / Sign up to Heroku</li>
<li>Click New -- Create New App</li>
<li>Name your app (must be unique), select your nearest revious and click “Create app” to confirm.</li>
<li>Go to settings and add the following Key/Data information (which match the information in your env.py file that should be set up to be ignored by git), to the config vars:<ul>
<li>DATABASE_URL (from your database, eg elephant sql)</li>
<li>SECRET_KEY</li>
<li>CLOUDINARY_URL (from your Cloudinary account)</li>
<li>PORT (8000)</li>
<li>DISABLE_COLLECTSTATIC (1) if you haven't added static files yet. NB This can be removed once you deploy your site</li>
</ul></li>
<li>Add your Heroku app and local host to the 'Allowed Hosts' section of the settings.py file (example below)<ul><li>ALLOWED_HOSTS = ["school-clubs.herokuapp.com", "localhost"]
</li></ul></li>
<li>Create a Profile in the main directory with the following info: web: gunicorn schoolclubs.wsgi where 'schoolclubs' is the name of your project</li>
<li>Add/Commit/Push all changes to Github</li>
<li>Click Deploy in the Heroku App dashboard - then deploy via Github - connect to the repository, scroll down and click on deploy branch</li>
</ol>

<h3 id="fork">How to fork this repo</h3>

Visit the repo (https://github.com/MandyHole/school-clubs) and click the 'Fork' button in the top right part of the screen. You may need to sign in to Github.

<h3 id="clone">How to clone this repo</h3>

Visit the repo (https://github.com/MandyHole/school-clubs) and click the green 'Code' button above the list of files. Click on the 'local' and select from the following options: HTTPS, SSH and GitHub CLI. Copy the link. Open the terminal in your code editor, ensuring the current working directory is where you want the files, and type git clone and paste in the copied URL before clicking enter.

<h2 id="credits"> Credits</h2>

<h3 id="code"> Code</h3>

The Modal to confirm before deleting: https://www.tutorialrepublic.com/codelab.php?topic=bootstrap&file=delete-confirmation-modal

Bootstrap5: Bootstrap was used throughout the project mainly to make site responsive using the Bootstrap Grid System, the nav bar as well as for minor styling (e.g. message formats).

Django: Django was used throughout the project to help make the website more quickly and with less code.

Getting a datepicker in the Date Request form: https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django

Getting custom messages to appear upon form submissions: https://www.csestack.org/display-messages-form-submit-django/

Inspiration for the project, getting started with Django and in particular for displaying messages and working with views/databases: Code Institute Django walkthrough examples

<h3 id="content"> Content</h3>
All content was written by the developer.

<h3 id="media"> Media</h3>
All Images were sourced from <a href="https://www.pexels.com/" aria-label="Go to Pexels website">Pexels.</a> I'd like to give a particular thanks to the following photographers:</li>
<ul><li>pexels-alexander-mils-2103949</li>
<li>pexels-chan-walrus-958545</li>
<li>pexels-elviss-railijs-bitans-1448665</li>
<li>pexels-jer-chung-2116094</li>
<li>pexels-nicola-barts-7937469</li>
<li>pexels-lukas-1352270</li>
<li>pexels-sydney-troxell-718739</li>
</li></ul>