import requests

# 1. Session 
s = requests.Session()

# 2. Login 
login_response = s.post("http://127.0.0.1:5000/login", data={
    "username": "baris225",
    "password": "baris55"
})
print("Login:", login_response.status_code)

# 3. Create Post
create_response = s.post("http://127.0.0.1:5000/api/posts", json={
    "title": "API Test Title",
    "content": "API Test Content"
})
print("Create Post:", create_response.status_code, create_response.json())

# 4. GET POST 
get_all = s.get("http://127.0.0.1:5000/api/posts")
print("All Posts:", get_all.status_code)
posts = get_all.json()
last_post_id = posts[0]["id"] if posts else None

# 5. Update Post
if last_post_id:
    update = s.put(f"http://127.0.0.1:5000/api/post/{last_post_id}", json={
        "title": "Updated API Title",
        "content": "Updated via API"
    })
    print("Update Post:", update.status_code, update.json())

# 6. GET DETAIL
if last_post_id:
    detail = s.get(f"http://127.0.0.1:5000/api/post/{last_post_id}")
    print("Post Detail:", detail.status_code, detail.json())

 #7. DELETE
if last_post_id:
    delete = s.delete(f"http://127.0.0.1:5000/api/post/{last_post_id}")
    print("Delete Post:", delete.status_code, delete.json())
