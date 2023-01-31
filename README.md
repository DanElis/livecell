# livecell


## This repository is designed to solve 2 tasks: 
1) Training yolov8 model and data preparation
2) To deploy the solution

## Training and prepare data
1) You need to download the [LIVECell dataset](https://sartorius-research.github.io/LIVECell/), there is already a split into train, validation and test 
2) Convert to yolo format. [convert_coco_to_yolo.ipynb](train%2Fconvert_coco_to_yolo.ipynb)
3) Train. [train.ipynb](train%2Ftrain.ipynb)

## Deploy
The solution is wrapped in a docker image
To run it on localhost:8001 you need to run the following commands. To change the model, you need to replace best.pt with your solution

1) docker compose build --force-rm --no-cache livecell_backend
2) docker compose up -d

## Checkpoint 
The cell-30 folder contains the training results of the yolov8n-seg model