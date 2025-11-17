---
layout: default
title: OpenUS: A Fully Open-Source Foundation Model for Ultrasound Image Analysis via Self-Adaptive Masked Contrastive Learning
---

# OpenUS: A Fully Open-Source Foundation Model for Ultrasound Image Analysis via Self-Adaptive Masked Contrastive Learning
**arXiv**：[2511.11510v1](https://arxiv.org/abs/2511.11510) · [PDF](https://arxiv.org/pdf/2511.11510.pdf)  
**作者**：Xiaoyu Zheng, Xu Chen, Awais Rauf, Qifan Fu, Benedetta Monosi, Felice Rivellese, Myles J. Lewis, Shaogang Gong, Gregory Slabaugh  

**一句话要点**：提出OpenUS开源基础模型，通过自适应掩码对比学习解决超声图像分析泛化性问题

**关键词**：超声图像分析, 基础模型, 自适应掩码学习, 对比学习, 视觉Mamba, 开源数据集

## 3 点简述
- 超声图像分析面临操作依赖性强、设备差异大、标注稀缺等泛化性挑战
- 采用视觉Mamba骨干网络和自适应掩码框架，结合对比学习与掩码图像建模
- 在最大公共超声数据集上预训练，支持标签高效微调，代码开源

## 摘要（原文）

> Ultrasound (US) is one of the most widely used medical imaging modalities, thanks to its low cost, portability, real-time feedback, and absence of ionizing radiation. However, US image interpretation remains highly operator-dependent and varies significantly across anatomical regions, acquisition protocols, and device types. These variations, along with unique challenges such as speckle, low contrast, and limited standardized annotations, hinder the development of generalizable, label-efficient ultrasound AI models. In this paper, we propose OpenUS, the first reproducible, open-source ultrasound foundation model built on a large collection of public data. OpenUS employs a vision Mamba backbone, capturing both local and global long-range dependencies across the image. To extract rich features during pre-training, we introduce a novel self-adaptive masking framework that combines contrastive learning with masked image modeling. This strategy integrates the teacher's attention map with student reconstruction loss, adaptively refining clinically-relevant masking to enhance pre-training effectiveness. OpenUS also applies a dynamic learning schedule to progressively adjust the difficulty of the pre-training process. To develop the foundation model, we compile the largest to-date public ultrasound dataset comprising over 308K images from 42 publicly available datasets, covering diverse anatomical regions, institutions, imaging devices, and disease types. Our pre-trained OpenUS model can be easily adapted to specific downstream tasks by serving as a backbone for label-efficient fine-tuning. Code is available at https://github.com/XZheng0427/OpenUS.

