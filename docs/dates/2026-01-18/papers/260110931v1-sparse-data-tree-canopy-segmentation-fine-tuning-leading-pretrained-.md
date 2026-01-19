---
layout: default
title: Sparse Data Tree Canopy Segmentation: Fine-Tuning Leading Pretrained Models on Only 150 Images
---

# Sparse Data Tree Canopy Segmentation: Fine-Tuning Leading Pretrained Models on Only 150 Images
**arXiv**：[2601.10931v1](https://arxiv.org/abs/2601.10931) · [PDF](https://arxiv.org/pdf/2601.10931.pdf)  
**作者**：David Szczecina, Hudson Sun, Anthony Bertnyk, Niloofar Azad, Kyle Gao, Lincoln Linlin Xu  

**一句话要点**：评估五种预训练模型在仅150张图像上的树冠分割性能，发现基于CNN的模型优于基于Transformer的模型。

**关键词**：树冠分割, 数据稀缺, 预训练模型, CNN与Transformer对比, 实例分割, 语义分割

## 3 点简述
- 核心问题：在数据稀缺（仅150张标注图像）下进行树冠分割，避免过拟合。
- 方法要点：微调YOLOv11、Mask R-CNN、DeepLabv3、Swin-UNet和DINOv2等代表性架构。
- 实验或效果：基于CNN的模型（如YOLOv11和Mask R-CNN）泛化能力更强，Transformer模型表现不佳。

## 摘要（原文）

> Tree canopy detection from aerial imagery is an important task for environmental monitoring, urban planning, and ecosystem analysis. Simulating real-life data annotation scarcity, the Solafune Tree Canopy Detection competition provides a small and imbalanced dataset of only 150 annotated images, posing significant challenges for training deep models without severe overfitting. In this work, we evaluate five representative architectures, YOLOv11, Mask R-CNN, DeepLabv3, Swin-UNet, and DINOv2, to assess their suitability for canopy segmentation under extreme data scarcity. Our experiments show that pretrained convolution-based models, particularly YOLOv11 and Mask R-CNN, generalize significantly better than pretrained transformer-based models. DeeplabV3, Swin-UNet and DINOv2 underperform likely due to differences between semantic and instance segmentation tasks, the high data requirements of Vision Transformers, and the lack of strong inductive biases. These findings confirm that transformer-based architectures struggle in low-data regimes without substantial pretraining or augmentation and that differences between semantic and instance segmentation further affect model performance. We provide a detailed analysis of training strategies, augmentation policies, and model behavior under the small-data constraint and demonstrate that lightweight CNN-based methods remain the most reliable for canopy detection on limited imagery.

