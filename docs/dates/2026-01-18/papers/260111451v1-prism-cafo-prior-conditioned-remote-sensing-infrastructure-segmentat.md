---
layout: default
title: PRISM-CAFO: Prior-conditioned Remote-sensing Infrastructure Segmentation and Mapping for CAFOs
---

# PRISM-CAFO: Prior-conditioned Remote-sensing Infrastructure Segmentation and Mapping for CAFOs
**arXiv**：[2601.11451v1](https://arxiv.org/abs/2601.11451) · [PDF](https://arxiv.org/pdf/2601.11451.pdf)  
**作者**：Oishee Bintey Hoque, Nibir Chandra Mandal, Kyle Luong, Amanda Wilson, Samarth Swarup, Madhav Marathe, Abhijin Adiga  

**一句话要点**：提出PRISM-CAFO方法，通过先验条件遥感基础设施分割与映射，以识别和表征集中动物饲养操作。

**关键词**：遥感图像分割, 基础设施检测, 集中动物饲养操作, 可解释人工智能, 空间交叉注意力, YOLOv8

## 3 点简述
- 核心问题：大规模畜牧业操作对人类健康和环境构成风险，需准确、可扩展的映射方法。
- 方法要点：使用领域调优的YOLOv8检测器识别基础设施，结合SAM2掩码和结构化描述符，通过空间交叉注意力分类器进行预测。
- 实验或效果：在多样化美国区域评估中，Swin-B+PRISM-CAFO超越最佳基线性能达15%，并提供可解释的掩码级归因。

## 摘要（原文）

> Large-scale livestock operations pose significant risks to human health and the environment, while also being vulnerable to threats such as infectious diseases and extreme weather events. As the number of such operations continues to grow, accurate and scalable mapping has become increasingly important. In this work, we present an infrastructure-first, explainable pipeline for identifying and characterizing Concentrated Animal Feeding Operations (CAFOs) from aerial and satellite imagery. Our method (1) detects candidate infrastructure (e.g., barns, feedlots, manure lagoons, silos) with a domain-tuned YOLOv8 detector, then derives SAM2 masks from these boxes and filters component-specific criteria, (2) extracts structured descriptors (e.g., counts, areas, orientations, and spatial relations) and fuses them with deep visual features using a lightweight spatial cross-attention classifier, and (3) outputs both CAFO type predictions and mask-level attributions that link decisions to visible infrastructure. Through comprehensive evaluation, we show that our approach achieves state-of-the-art performance, with Swin-B+PRISM-CAFO surpassing the best performing baseline by up to 15\%. Beyond strong predictive performance across diverse U.S. regions, we run systematic gradient--activation analyses that quantify the impact of domain priors and show ho

