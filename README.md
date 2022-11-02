<h1>Event Planner with MongoDB and Flask</h1>

<h3>Functionalities: </h3>
<ul>
<li>Lets user register to the app and plan an event which they can save to access later. Logged in user can reschedule or delete an event. </li>

<li>If the user is not logged in: They are first asked to register/Login before they can schedule any event. </li>

<li>All events are linked to user – with a one-to-many relationship [User can have many events but a event can only have one user]. </li>

<li>All Password are stored as Hash format in database which adds an extra layer of security. </li>
</ul>
