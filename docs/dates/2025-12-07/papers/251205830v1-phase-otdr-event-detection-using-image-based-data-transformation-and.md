---
layout: default
title: Phase-OTDR Event Detection Using Image-Based Data Transformation and Deep Learning
---

# Phase-OTDR Event Detection Using Image-Based Data Transformation and Deep Learning
**arXiv**：[2512.05830v1](https://arxiv.org/abs/2512.05830) · [PDF](https://arxiv.org/pdf/2512.05830.pdf)  
**作者**：Muhammet Cagri Yeke, Samil Sirin, Kivilcim Yuksel, Abdurrahman Gumus  

**一句话要点**：提出基于图像转换和深度学习的Phase-OTDR事件检测方法，以提升光纤传感数据分析的准确性和效率。

**关键词**：Phase-OTDR事件检测, 图像数据转换, 深度学习分类, 光纤传感, 迁移学习, 公开数据集

## 3 点简述
- 核心问题：光纤中事件检测，需分类六种事件，传统Phase-OTDR数据分析复杂且效率低。
- 方法要点：将1D数据转换为灰度图像（如Gramian Angular Field和Recurrence Plot），组合成多通道RGB表示，利用迁移学习模型（如EfficientNetB0和DenseNet121）进行分析。
- 实验或效果：在公开数据集上实现高分类准确率（最高99.07%），通过5折交叉验证确认可靠性，并公开代码和数据集以促进研究。

## 摘要（原文）

> This study focuses on event detection in optical fibers, specifically classifying six events using the Phase-OTDR system. A novel approach is introduced to enhance Phase-OTDR data analysis by transforming 1D data into grayscale images through techniques such as Gramian Angular Difference Field, Gramian Angular Summation Field, and Recurrence Plot. These grayscale images are combined into a multi-channel RGB representation, enabling more robust and adaptable analysis using transfer learning models. The proposed methodology achieves high classification accuracies of 98.84% and 98.24% with the EfficientNetB0 and DenseNet121 models, respectively. A 5-fold cross-validation process confirms the reliability of these models, with test accuracy rates of 99.07% and 98.68%. Using a publicly available Phase-OTDR dataset, the study demonstrates an efficient approach to understanding optical fiber events while reducing dataset size and improving analysis efficiency. The results highlight the transformative potential of image-based analysis in interpreting complex fiber optic sensing data, offering significant advancements in the accuracy and reliability of fiber optic monitoring systems. The codes and the corresponding image-based dataset are made publicly available on GitHub to support further research: https://github.com/miralab-ai/Phase-OTDR-event-detection.

