---
layout: default
title: GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling
---

# GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling
**arXiv**：[2602.05202v1](https://arxiv.org/abs/2602.05202) · [PDF](https://arxiv.org/pdf/2602.05202.pdf)  
**作者**：Shivanshu Shekhar, Uttaran Bhattacharya, Raghavendra Addanki, Mehrab Tanjim, Somdeb Sarkhel, Tong Zhang  

**一句话要点**：提出基于生成-Transformer的自监督视频评判模型，以解决视频生成模型对齐中时间动态建模不足的问题。

**关键词**：视频奖励建模, 自监督学习, 生成模型, 时间动态建模, 能量模型, 对比学习

## 3 点简述
- 核心问题：现有基于视觉语言模型的奖励建模难以捕捉视频的细微时间动态。
- 方法要点：将视频生成模型重构为能量模型，通过对比学习训练以区分视频质量。
- 实验或效果：在GenAI-Bench和MonteBench上实现最优性能，仅需3万人类标注。

## 摘要（原文）

> Aligning video generative models with human preferences remains challenging: current approaches rely on Vision-Language Models (VLMs) for reward modeling, but these models struggle to capture subtle temporal dynamics. We propose a fundamentally different approach: repurposing video generative models, which are inherently designed to model temporal structure, as reward models. We present the Generative-Transformer-based Self-Supervised Video Judge (\modelname), a novel evaluation model that transforms state-of-the-art video generation models into powerful temporally-aware reward models. Our key insight is that generative models can be reformulated as energy-based models (EBMs) that assign low energy to high-quality videos and high energy to degraded ones, enabling them to discriminate video quality with remarkable precision when trained via contrastive objectives. To prevent the model from exploiting superficial differences between real and generated videos, we design challenging synthetic negative videos through controlled latent-space perturbations: temporal slicing, feature swapping, and frame shuffling, which simulate realistic but subtle visual degradations. This forces the model to learn meaningful spatiotemporal features rather than trivial artifacts. \modelname achieves state-of-the-art performance on GenAI-Bench and MonteBench using only 30K human-annotations: $6\times$ to $65\times$ fewer than existing VLM-based approaches.

