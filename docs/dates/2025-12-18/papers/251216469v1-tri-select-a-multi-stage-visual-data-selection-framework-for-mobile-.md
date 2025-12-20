---
layout: default
title: Tri-Select: A Multi-Stage Visual Data Selection Framework for Mobile Visual Crowdsensing
---

# Tri-Select: A Multi-Stage Visual Data Selection Framework for Mobile Visual Crowdsensing
**arXiv**：[2512.16469v1](https://arxiv.org/abs/2512.16469) · [PDF](https://arxiv.org/pdf/2512.16469.pdf)  
**作者**：Jiayu Zhang, Kaixing Zhao, Tianhao Shao, Bin Guo, Liang He  

**一句话要点**：提出Tri-Select多阶段视觉数据选择框架以解决移动视觉众包中数据冗余与异质性问题

**关键词**：移动视觉众包, 数据选择框架, 多阶段处理, 冗余过滤, 图像质量评估, 可扩展应用

## 3 点简述
- 移动视觉众包采集的图像存在冗余和异质性，影响环境监测效率
- Tri-Select通过元数据过滤、空间相似性聚类和视觉特征引导选择三阶段处理
- 实验表明该框架提升选择效率和数据集质量，适用于可扩展众包应用

## 摘要（原文）

> Mobile visual crowdsensing enables large-scale, fine-grained environmental monitoring through the collection of images from distributed mobile devices. However, the resulting data is often redundant and heterogeneous due to overlapping acquisition perspectives, varying resolutions, and diverse user behaviors. To address these challenges, this paper proposes Tri-Select, a multi-stage visual data selection framework that efficiently filters redundant and low-quality images. Tri-Select operates in three stages: (1) metadata-based filtering to discard irrelevant samples; (2) spatial similarity-based spectral clustering to organize candidate images; and (3) a visual-feature-guided selection based on maximum independent set search to retain high-quality, representative images. Experiments on real-world and public datasets demonstrate that Tri-Select improves both selection efficiency and dataset quality, making it well-suited for scalable crowdsensing applications.

