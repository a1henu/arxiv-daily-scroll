---
layout: default
title: A 360-degree Multi-camera System for Blue Emergency Light Detection Using Color Attention RT-DETR and the ABLDataset
---

# A 360-degree Multi-camera System for Blue Emergency Light Detection Using Color Attention RT-DETR and the ABLDataset
**arXiv**：[2603.05058v1](https://arxiv.org/abs/2603.05058) · [PDF](https://arxiv.org/pdf/2603.05058.pdf)  
**作者**：Francisco Vacalebri-Lloret, Lucas Banchero, Jose J. Lopez, Jose M. Mossi  

**一句话要点**：提出基于颜色注意力RT-DETR的360度多相机系统，用于检测紧急车辆蓝光以增强ADAS和道路安全。

**关键词**：蓝光检测, 多相机系统, RT-DETR, 颜色注意力, ADAS, 道路安全

## 3 点简述
- 核心问题：检测欧洲紧急车辆蓝光，需应对多变气候和地理条件，并集成到多模态系统中。
- 方法要点：使用四鱼眼相机配置，结合校准和几何变换进行方位定位，并优化RT-DETR模型加入颜色注意力块。
- 实验或效果：在测试集上准确率达94.7%，召回率94.1%，现场测试检测距离达70米，系统高效且具应用前景。

## 摘要（原文）

> This study presents an advanced system for detecting blue lights on emergency vehicles, developed using ABLDataset, a curated dataset that includes images of European emergency vehicles under various climatic and geographic conditions. The system employs a configuration of four fisheye cameras, each with a 180-degree horizontal field of view, mounted on the sides of the vehicle. A calibration process enables the azimuthal localization of the detections. Additionally, a comparative analysis of major deep neural network algorithms was conducted, including YOLO (v5, v8, and v10), RetinaNet, Faster R-CNN, and RT-DETR. RT-DETR was selected as the base model and enhanced through the incorporation of a color attention block, achieving an accuracy of 94.7 percent and a recall of 94.1 percent on the test set, with field test detections reaching up to 70 meters. Furthermore, the system estimates the approach angle of the emergency vehicle relative to the center of the car using geometric transformations. Designed for integration into a multimodal system that combines visual and acoustic data, this system has demonstrated high efficiency, offering a promising approach to enhancing Advanced Driver Assistance Systems (ADAS) and road safety.

