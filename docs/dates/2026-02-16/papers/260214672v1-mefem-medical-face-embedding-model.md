---
layout: default
title: MeFEm: Medical Face Embedding model
---

# MeFEm: Medical Face Embedding model
**arXiv**：[2602.14672v1](https://arxiv.org/abs/2602.14672) · [PDF](https://arxiv.org/pdf/2602.14672.pdf)  
**作者**：Yury Borets, Stepan Botman  

**一句话要点**：提出MeFEm模型，基于改进JEPA架构，用于面部图像的生物特征和医学分析。

**关键词**：面部图像分析, 生物特征识别, 医学图像处理, JEPA架构, 线性探测, BMI估计

## 3 点简述
- 核心问题：解决面部图像中生物特征和医学分析任务，如人体测量和BMI估计，现有数据存在领域偏差。
- 方法要点：采用轴向条纹掩码策略、循环损失加权和CLS令牌概率重分配，以增强语义区域学习和线性探测质量。
- 实验或效果：在整合数据集上训练，使用较少数据优于FaRL和Franca等基线，在BMI估计上表现良好。

## 摘要（原文）

> We present MeFEm, a vision model based on a modified Joint Embedding Predictive Architecture (JEPA) for biometric and medical analysis from facial images. Key modifications include an axial stripe masking strategy to focus learning on semantically relevant regions, a circular loss weighting scheme, and the probabilistic reassignment of the CLS token for high quality linear probing. Trained on a consolidated dataset of curated images, MeFEm outperforms strong baselines like FaRL and Franca on core anthropometric tasks despite using significantly less data. It also shows promising results on Body Mass Index (BMI) estimation, evaluated on a novel, consolidated closed-source dataset that addresses the domain bias prevalent in existing data. Model weights are available at https://huggingface.co/boretsyury/MeFEm , offering a strong baseline for future work in this domain.

