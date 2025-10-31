---
layout: default
title: Detecting Unauthorized Vehicles using Deep Learning for Smart Cities: A Case Study on Bangladesh
---

# Detecting Unauthorized Vehicles using Deep Learning for Smart Cities: A Case Study on Bangladesh
**arXiv**：[2510.26154v1](https://arxiv.org/abs/2510.26154) · [PDF](https://arxiv.org/pdf/2510.26154.pdf)  
**作者**：Sudipto Das Sukanto, Diponker Roy, Fahim Shakil, Nirjhar Singha, Abdullah Asik, Aniket Joarder, Mridha Md Nafis Fuad, Muhammad Ibrahim  

**一句话要点**：提出基于YOLOv8的自动检测方法以解决孟加拉国城市中机动三轮车监控难题

**关键词**：目标检测, YOLOv8模型, 智能城市监控, 机动三轮车识别, 实时视频分析, 交通管理

## 3 点简述
- 核心问题：机动三轮车与非机动三轮车相似，现有监控系统难以区分，手动分析耗时。
- 方法要点：使用YOLOv8模型进行实时目标检测，训练集包含1,730张标注图像。
- 实验或效果：模型在密集和稀疏交通场景中表现良好，mAP50达83.447%，精度和召回率超78%。

## 摘要（原文）

> Modes of transportation vary across countries depending on geographical
> location and cultural context. In South Asian countries rickshaws are among the
> most common means of local transport. Based on their mode of operation,
> rickshaws in cities across Bangladesh can be broadly classified into non-auto
> (pedal-powered) and auto-rickshaws (motorized). Monitoring the movement of
> auto-rickshaws is necessary as traffic rules often restrict auto-rickshaws from
> accessing certain routes. However, existing surveillance systems make it quite
> difficult to monitor them due to their similarity to other vehicles, especially
> non-auto rickshaws whereas manual video analysis is too time-consuming. This
> paper presents a machine learning-based approach to automatically detect
> auto-rickshaws in traffic images. In this system, we used real-time object
> detection using the YOLOv8 model. For training purposes, we prepared a set of
> 1,730 annotated images that were captured under various traffic conditions. The
> results show that our proposed model performs well in real-time auto-rickshaw
> detection and offers an mAP50 of 83.447% and binary precision and recall values
> above 78%, demonstrating its effectiveness in handling both dense and sparse
> traffic scenarios. The dataset has been publicly released for further research.

