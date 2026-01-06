---
layout: default
title: Adaptive Hybrid Optimizer based Framework for Lumpy Skin Disease Identification
---

# Adaptive Hybrid Optimizer based Framework for Lumpy Skin Disease Identification
**arXiv**：[2601.01807v1](https://arxiv.org/abs/2601.01807) · [PDF](https://arxiv.org/pdf/2601.01807.pdf)  
**作者**：Ubaidullah, Muhammad Abid Hussain, Mohsin Raza Jafri, Rozi Khan, Moid Sandhu, Abd Ullah Khan, Hyundong Shin  

**一句话要点**：提出LUMPNet框架，基于自适应混合优化器实现牛结节性皮肤病早期识别

**关键词**：牛结节性皮肤病识别, 自适应混合优化器, YOLOv11检测, EfficientNet分类, 深度学习框架

## 3 点简述
- 核心问题：牛结节性皮肤病（LSD）传播迅速，需早期精准识别以防控疫情。
- 方法要点：结合YOLOv11检测皮肤结节，EfficientNet分类，并引入自适应混合优化器加速训练。
- 实验或效果：在公开数据集上达到99%训练准确率和98%验证准确率，优于现有方法。

## 摘要（原文）

> Lumpy Skin Disease (LSD) is a contagious viral infection that significantly deteriorates livestock health, thereby posing a serious threat to the global economy and food security. Owing to its rapid spread characteristics, early and precise identification is crucial to prevent outbreaks and ensure timely intervention. In this paper, we propose a hybrid deep learning-based approach called LUMPNet for the early detection of LSD. LUMPNet utilizes image data to detect and classify skin nodules -- the primary indicator of LSD. To this end, LUMPNet uses YOLOv11, EfficientNet-based CNN classifier with compound scaling, and a novel adaptive hybrid optimizer. More precisely, LUMPNet detects and localizes LSD skin nodules and lesions on cattle images. It exploits EfficientNet to classify the localized cattle images into LSD-affected or healthy categories. To stabilize and accelerate the training of YOLOv11 and EfficientNet hybrid model, a novel adaptive hybrid optimizer is proposed and utilized. We evaluate LUMPNet at various stages of LSD using a publicly available dataset. Results indicate that the proposed scheme achieves 99% LSD detection training accuracy, and outperforms existing schemes. The model also achieves validation accuracy of 98%. Moreover, for further evaluation, we conduct a case study using an optimized EfficientNet-B0 model trained with the AdamW optimizer, and compare its performance with LUMPNet. The results show that LUMPNet achieves superior performance.

