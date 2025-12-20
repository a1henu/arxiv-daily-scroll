---
layout: default
title: Plug to Place: Indoor Multimedia Geolocation from Electrical Sockets for Digital Investigation
---

# Plug to Place: Indoor Multimedia Geolocation from Electrical Sockets for Digital Investigation
**arXiv**：[2512.16620v1](https://arxiv.org/abs/2512.16620) · [PDF](https://arxiv.org/pdf/2512.16620.pdf)  
**作者**：Kanwal Aftab, Graham Adams, Mark Scanlon  

**一句话要点**：提出基于电源插座的室内多媒体地理定位管道，用于数字取证调查。

**关键词**：室内地理定位, 数字取证, 电源插座检测, 深度学习管道, 数据集构建

## 3 点简述
- 核心问题：室内多媒体地理定位因布局相似、光照变化和数据集有限而发展不足。
- 方法要点：使用深度学习管道检测和分类电源插座类型，映射到国家或地区。
- 实验或效果：在真实酒店图像数据集上评估，检测和分类准确率分别达0.843和0.912。

## 摘要（原文）

> Computer vision is a rapidly evolving field, giving rise to powerful new tools and techniques in digital forensic investigation, and shows great promise for novel digital forensic applications. One such application, indoor multimedia geolocation, has the potential to become a crucial aid for law enforcement in the fight against human trafficking, child exploitation, and other serious crimes. While outdoor multimedia geolocation has been widely explored, its indoor counterpart remains underdeveloped due to challenges such as similar room layouts, frequent renovations, visual ambiguity, indoor lighting variability, unreliable GPS signals, and limited datasets in sensitive domains. This paper introduces a pipeline that uses electric sockets as consistent indoor markers for geolocation, since plug socket types are standardised by country or region. The three-stage deep learning pipeline detects plug sockets (YOLOv11, mAP@0.5 = 0.843), classifies them into one of 12 plug socket types (Xception, accuracy = 0.912), and maps the detected socket types to countries (accuracy = 0.96 at >90% threshold confidence). To address data scarcity, two dedicated datasets were created: socket detection dataset of 2,328 annotated images expanded to 4,072 through augmentation, and a classification dataset of 3,187 images across 12 plug socket classes. The pipeline was evaluated on the Hotels-50K dataset, focusing on the TraffickCam subset of crowd-sourced hotel images, which capture real-world conditions such as poor lighting and amateur angles. This dataset provides a more realistic evaluation than using professional, well-lit, often wide-angle images from travel websites. This framework demonstrates a practical step toward real-world digital forensic applications. The code, trained models, and the data for this paper are available open source.

