---
layout: default
title: Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning
---

# Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning
**arXiv**：[2511.17201v1](https://arxiv.org/abs/2511.17201) · [PDF](https://arxiv.org/pdf/2511.17201.pdf)  
**作者**：Jiayi Wang, Wei Dai, Haoyu Wang, Sihan Yang, Haixia Bi, Jian Sun  

**一句话要点**：提出CA-SAM方法以解决医学图像分割中持续学习的灾难性遗忘问题

**关键词**：医学图像分割, 持续学习, 灾难性遗忘, 对齐层, SAM模型, 轻量模块

## 3 点简述
- 核心问题：医学图像分割中，异构隐私政策阻碍联合训练，导致持续学习时灾难性遗忘
- 方法要点：引入轻量对齐层，调整SAM特征分布，提升效率与准确性
- 实验或效果：在九个数据集上测试，CA-SAM实现最先进性能，代码开源

## 摘要（原文）

> In medical image segmentation, heterogeneous privacy policies across institutions often make joint training on pooled datasets infeasible, motivating continual image segmentation-learning from data streams without catastrophic forgetting. While the Segment Anything Model (SAM) offers strong zero-shot priors and has been widely fine-tuned across downstream tasks, its large parameter count and computational overhead challenge practical deployment. This paper demonstrates that the SAM paradigm is highly promising once its computational efficiency and performance can be balanced. To this end, we introduce the Alignment Layer, a lightweight, plug-and-play module which aligns encoder-decoder feature distributions to efficiently adapt SAM to specific medical images, improving accuracy while reducing computation. Building on SAM and the Alignment Layer, we then propose Continual Alignment for SAM (CA-SAM), a continual learning strategy that automatically adapts the appropriate Alignment Layer to mitigate catastrophic forgetting, while leveraging SAM's zero-shot priors to preserve strong performance on unseen medical datasets. Experimented across nine medical segmentation datasets under continual-learning scenario, CA-SAM achieves state-of-the-art performance. Our code, models and datasets will be released on \mbox{https://github.com/azzzzyo/Continual-Alignment-for-SAM.}

