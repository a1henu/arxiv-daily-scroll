---
layout: default
title: Contrastive Heliophysical Image Pretraining for Solar Dynamics Observatory Records
---

# Contrastive Heliophysical Image Pretraining for Solar Dynamics Observatory Records
**arXiv**：[2511.22958v1](https://arxiv.org/abs/2511.22958) · [PDF](https://arxiv.org/pdf/2511.22958.pdf)  
**作者**：Shiyu Shen, Zhe Gao, Taifeng Chai, Yang Huang, Bin Pan  

**一句话要点**：提出SolarCHIP对比预训练方法，针对SDO多仪器数据解决模态差异与弱可分性问题。

**关键词**：太阳图像分析, 对比学习, 多模态预训练, SDO数据, 视觉骨干网络, 低资源学习

## 3 点简述
- 核心问题：SDO数据存在多模态感知、类间弱可分性和类内强变异性挑战。
- 方法要点：采用多粒度对比目标，联合对齐全局类令牌、局部补丁令牌和跨空间补丁。
- 实验效果：在跨模态翻译和耀斑分类任务中实现SOTA，尤其在低资源设置下表现优异。

## 摘要（原文）

> Deep learning has revolutionized solar image analysis, yet most approaches train task-specific encoders from scratch or rely on natural-image pretraining that ignores the unique characteristics of Solar Dynamics Observatory (SDO) data. We introduce SolarCHIP, a family of contrastively pretrained visual backbones tailored to multi-instrument SDO observations. SolarCHIP addresses three key challenges in solar imaging: multimodal sensing across AIA and HMI instruments, weak inter-class separability due to slow temporal evolution, and strong intra-class variability with sparse activity signals. Our pretraining framework employs a multi-granularity contrastive objective that jointly aligns (1) global class tokens across co-temporal AIA-HMI pairs to enhance temporal discrimination, (2) local patch tokens at fixed spatial indices to enforce position-consistent, modality-invariant features, and (3) intra-sample patches across different spatial locations to preserve fine-grained spatial structure. We train both CNN- and Vision Transformer-based autoencoders and demonstrate their effectiveness on two downstream tasks: cross-modal translation between HMI and AIA passbands via ControlNet, and full-disk flare classification. Experimental results show that SolarCHIP achieves state-of-the-art performance across both tasks, with particularly strong gains in low-resource settings where labeled data is limited. Ablation studies confirm that each contrastive component contributes essential discriminative capacity at different granularities. By publicly releasing pretrained weights and training code, we provide the heliophysics community with a practical, plug-and-play feature extractor that reduces computational requirements, improves label efficiency, and establishes a reusable foundation for diverse solar imaging applications.

