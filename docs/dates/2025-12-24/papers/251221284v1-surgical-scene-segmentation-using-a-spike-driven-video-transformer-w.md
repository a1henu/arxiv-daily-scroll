---
layout: default
title: Surgical Scene Segmentation using a Spike-Driven Video Transformer with Real-Time Potential
---

# Surgical Scene Segmentation using a Spike-Driven Video Transformer with Real-Time Potential
**arXiv**：[2512.21284v1](https://arxiv.org/abs/2512.21284) · [PDF](https://arxiv.org/pdf/2512.21284.pdf)  
**作者**：Shihao Zou, Jingjing Li, Wei Ji, Jincai Huang, Kai Wang, Guo Dan, Weixin Si, Yi Pan  

**一句话要点**：提出SpikeSurgSeg，一种基于脉冲神经网络的视频Transformer框架，用于资源受限手术场景的实时分割。

**关键词**：脉冲神经网络, 手术场景分割, 视频Transformer, 实时推理, 掩码自编码, 资源受限环境

## 3 点简述
- 核心问题：现有深度学习模型在手术场景分割中计算量大、功耗高，难以在资源受限环境中实时部署。
- 方法要点：采用手术场景掩码自编码预训练策略，结合轻量级脉冲驱动分割头，实现高效时空表示学习。
- 实验或效果：在EndoVis18和SurgBleed数据集上，mIoU与SOTA ANN模型相当，推理延迟降低至少8倍，加速超过20倍。

## 摘要（原文）

> Modern surgical systems increasingly rely on intelligent scene understanding to provide timely situational awareness for enhanced intra-operative safety. Within this pipeline, surgical scene segmentation plays a central role in accurately perceiving operative events. Although recent deep learning models, particularly large-scale foundation models, achieve remarkable segmentation accuracy, their substantial computational demands and power consumption hinder real-time deployment in resource-constrained surgical environments. To address this limitation, we explore the emerging SNN as a promising paradigm for highly efficient surgical intelligence. However, their performance is still constrained by the scarcity of labeled surgical data and the inherently sparse nature of surgical video representations. To this end, we propose \textit{SpikeSurgSeg}, the first spike-driven video Transformer framework tailored for surgical scene segmentation with real-time potential on non-GPU platforms. To address the limited availability of surgical annotations, we introduce a surgical-scene masked autoencoding pretraining strategy for SNNs that enables robust spatiotemporal representation learning via layer-wise tube masking. Building on this pretrained backbone, we further adopt a lightweight spike-driven segmentation head that produces temporally consistent predictions while preserving the low-latency characteristics of SNNs. Extensive experiments on EndoVis18 and our in-house SurgBleed dataset demonstrate that SpikeSurgSeg achieves mIoU comparable to SOTA ANN-based models while reducing inference latency by at least $8\times$. Notably, it delivers over $20\times$ acceleration relative to most foundation-model baselines, underscoring its potential for time-critical surgical scene segmentation.

