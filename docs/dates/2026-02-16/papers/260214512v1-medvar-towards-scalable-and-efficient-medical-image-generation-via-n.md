---
layout: default
title: MedVAR: Towards Scalable and Efficient Medical Image Generation via Next-scale Autoregressive Prediction
---

# MedVAR: Towards Scalable and Efficient Medical Image Generation via Next-scale Autoregressive Prediction
**arXiv**：[2602.14512v1](https://arxiv.org/abs/2602.14512) · [PDF](https://arxiv.org/pdf/2602.14512.pdf)  
**作者**：Zhicheng He, Yunpeng Zhao, Junde Wu, Ziwei Niu, Zijun Li, Lanfen Lin, Yueming Jin  

**一句话要点**：提出MedVAR，基于下一尺度自回归预测实现可扩展高效的医学图像生成

**关键词**：医学图像生成, 自回归模型, 下一尺度预测, 多尺度表示, CT和MRI数据集

## 3 点简述
- 核心问题：医学图像生成需解决架构效率、多器官数据和评估方法不足的问题
- 方法要点：采用下一尺度预测范式，以粗到细方式生成结构化多尺度表示
- 实验或效果：在保真度、多样性和可扩展性实验中达到最先进性能

## 摘要（原文）

> Medical image generation is pivotal in applications like data augmentation for low-resource clinical tasks and privacy-preserving data sharing. However, developing a scalable generative backbone for medical imaging requires architectural efficiency, sufficient multi-organ data, and principled evaluation, yet current approaches leave these aspects unresolved. Therefore, we introduce MedVAR, the first autoregressive-based foundation model that adopts the next-scale prediction paradigm to enable fast and scale-up-friendly medical image synthesis. MedVAR generates images in a coarse-to-fine manner and produces structured multi-scale representations suitable for downstream use. To support hierarchical generation, we curate a harmonized dataset of around 440,000 CT and MRI images spanning six anatomical regions. Comprehensive experiments across fidelity, diversity, and scalability show that MedVAR achieves state-of-the-art generative performance and offers a promising architectural direction for future medical generative foundation models.

