## DRF
1\. The application have an authentication system using Django's built-in User model.  
2\. The Post model  have the following fields:  
● title (CharField): The title of the post.  
● body (TextField): The body of the post.  
● author (ForeignKey to User model): The user who wrote the post.  
3\. The API endpoints follow RESTful conventions:  
● GET `/api/posts/`: Returns a list of all posts.  
● POST `/api/posts/`: Creates a new post owned by the authenticated user.  
● GET `/api/posts/<int:pk>/`: Returns a single post by ID.  
● PUT `/api/posts/<int:pk>/`: Updates a single post owned by the authenticated  
user.  
● DELETE `/api/posts/<int:pk>/`: Deletes a single post owned by the authenticated user.  
4\. The user only be able to CRUD their own posts.  
5\. All API endpoints return JSON responses.  
6\. You should use DRF's API Views and serializers whenever possible.  
7\. Use of DRF's authentication and permission classes to enforce authentication and ownership of Post.  
8\. Whenever a new post is created, an email should be sent to the author notifying them of the creation.  
9\. Use Django signals to trigger the email notification whenever a new post is created.  
10.  Allow users to filter posts by title, body, and author using query parameters on the GET  
/api/posts/ endpoint.  
11\. Implement pagination for the GET /api/posts/ endpoint.  
12\. Implement rate limiting to prevent abuse of the API.

### API Documentation

https://documenter.getpostman.com/view/22767825/2s9Y5eNfEG
