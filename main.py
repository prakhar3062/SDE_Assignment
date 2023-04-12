from flask import Flask, request, Response
from PIL import Image
import io
app = Flask(__name__)
@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Your code here
    # Parse the request parameters
    width = request.args.get('width', type=int)
    height = request.args.get('height', type=int)
    color = request.args.get('color', type=str)
    format = request.args.get('format', type=str)
        # Validate the parameters
    if not all([width, height, color, format]):
        return Response('Missing parameter(s)', status=400)

    if format not in ['jpeg', 'png', 'gif']:
        return Response('Invalid format', status=400)

    if color not in ['red', 'green', 'blue']:
        return Response('Invalid color', status=400)
        # Generate the image
    image = Image.new('RGB', (width, height), color)

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=format.upper())
    image_bytes.seek(0)

    # Return the response
    return Response(image_bytes, mimetype=f'image/{format}')
if __name__ == '__main__':
    app.run(debug=True)

