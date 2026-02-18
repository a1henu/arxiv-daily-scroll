---
layout: default
title: A Novel Public Dataset for Strawberry (Fragaria x ananassa) Ripeness Detection and Comparative Evaluation of YOLO-Based Models
---

# A Novel Public Dataset for Strawberry (Fragaria x ananassa) Ripeness Detection and Comparative Evaluation of YOLO-Based Models
**arXiv**：[2602.15656v1](https://arxiv.org/abs/2602.15656) · [PDF](https://arxiv.org/pdf/2602.15656.pdf)  
**作者**：Mustafa Yurdakul, Zeynep Sena Bastug, Ali Emre Gok, Sakir Taşdemir  

**一句话要点**：提出公开草莓成熟度检测数据集，并基于YOLO模型进行对比评估以支持智能农业应用。

**关键词**：草莓成熟度检测, 公开数据集, YOLO模型, 智能农业, 目标检测

## 3 点简述
- 核心问题：传统草莓成熟度视觉评估主观且误差大，缺乏公开数据集阻碍研究比较。
- 方法要点：发布包含566张图像和1201个标注对象的草莓成熟度数据集，采集于土耳其两个温室的不同光照环境。
- 实验或效果：在YOLOv8、YOLOv9和YOLO11模型上测试，YOLOv8s在mAP@50上表现最佳，达86.09%。

## 摘要（原文）

> The strawberry (Fragaria x ananassa), known worldwide for its economic value and nutritional richness, is a widely cultivated fruit. Determining the correct ripeness level during the harvest period is crucial for both preventing losses for producers and ensuring consumers receive a quality product. However, traditional methods, i.e., visual assessments alone, can be subjective and have a high margin of error. Therefore, computer-assisted systems are needed. However, the scarcity of comprehensive datasets accessible to everyone in the literature makes it difficult to compare studies in this field. In this study, a new and publicly available strawberry ripeness dataset, consisting of 566 images and 1,201 labeled objects, prepared under variable light and environmental conditions in two different greenhouses in Turkey, is presented to the literature. Comparative tests conducted on the data set using YOLOv8, YOLOv9, and YOLO11-based models showed that the highest precision value was 90.94% in the YOLOv9c model, while the highest recall value was 83.74% in the YOLO11s model. In terms of the general performance criterion mAP@50, YOLOv8s was the best performing model with a success rate of 86.09%. The results show that small and medium-sized models work more balanced and efficiently on this type of dataset, while also establishing a fundamental reference point for smart agriculture applications.

