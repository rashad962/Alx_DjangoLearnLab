## Likes and Notifications API

### Like a post
- **POST** `/posts/<id>/like/`
- **Description**: Allows authenticated users to like a post.
- **Response**: `201 Created` if successfully liked, `400 Bad Request` if already liked.

### Unlike a post
- **POST** `/posts/<id>/unlike/`
- **Description**: Allows authenticated users to unlike a post.
- **Response**: `200 OK` if successfully unliked, `400 Bad Request` if not liked.

### View Notifications
- **GET** `/notifications/`
- **Description**: Allows users to view all their notifications.
- **Response**: List of notifications with actor, verb, target, timestamp, and read status.

---

This should give your Social Media API a much more interactive feel with notifications and likes. Let me know if you need further help!
