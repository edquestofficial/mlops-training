cd 07_day7/workshop/
docker build -t ice-cream_image .
docker run -it -p 8001:8001 ice-cream_image

to test into the browser 

http://localhost:8001

to test use curl 

curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d "{\"temps\": [47, 20, 7]}"
