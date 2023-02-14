# About
The app requires two images with faces. Images can be passed through form-data file in Postman.


## Requirements 
Install face-recognition library using pip package manager:
```bash
pip install face-recognition
```
Installation might take longer since the library uses other dependencies such as opencv, numpy and more.

## Usage
Open you API testing software, such as Postman and then head to the form-data section. Two variables has to be passed as shown in the picture:
<br />
![image](https://user-images.githubusercontent.com/66722574/218784981-2c256e3f-3364-42e3-954b-e2072c5fb591.png)

Afterwards, send the request to the API, in `http://localhost:8000/faceID/`. It will return JSON response object in the following way:
```python
{
    "Response": true
}
```
Or if the given images do not match it will return `false`.
