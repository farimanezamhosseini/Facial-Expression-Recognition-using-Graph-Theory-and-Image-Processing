# Facial-Expression-Recognition-using-Graph-Theory-and-Image-Processing
It involves two phases:

Phase 1:

Capture or load an image using a camera or from a saved file.
Detect key facial landmarks (key points on the face) and construct a graph.
Define vertices and edges based on the distance between key points.
Adjust edge count so that the number of edges is at least 10% of the total possible edges.
Display the graph.

Phase 2 (Additional Features):

Create a dataset of facial images, each labeled with an emotion (e.g., Happy, Sad, Angry).
Generate feature vectors for each image based on graph properties (e.g., average degree, shortest paths, graph diameter).
Predict the emotion of a new input image by comparing its feature vector to the dataset.
