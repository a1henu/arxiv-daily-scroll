---
layout: default
title: DeRA: Decoupled Representation Alignment for Video Tokenization
---

# DeRA: Decoupled Representation Alignment for Video Tokenization
**arXiv**：[2512.04483v1](https://arxiv.org/abs/2512.04483) · [PDF](https://arxiv.org/pdf/2512.04483.pdf)  
**作者**：Pengbo Guo, Junke Wang, Zhen Xing, Chengxu Liu, Daoguo Dong, Xueming Qian, Zuxuan Wu  

**一句话要点**：提出DeRA视频分词器，通过解耦时空表示学习提升训练效率和性能。

**关键词**：视频分词, 时空解耦, 梯度冲突缓解, 自回归视频生成, 表示对齐

## 3 点简述
- 核心问题：视频分词中时空表示学习耦合导致训练效率低和性能受限。
- 方法要点：分解视频编码为外观和运动流，与预训练视觉基础模型对齐，并引入SACP模块缓解梯度冲突。
- 实验或效果：在UCF-101上rFVD指标超越LARP 25%，在视频生成任务中达到新SOTA。

## 摘要（原文）

> This paper presents DeRA, a novel 1D video tokenizer that decouples the spatial-temporal representation learning in video tokenization to achieve better training efficiency and performance. Specifically, DeRA maintains a compact 1D latent space while factorizing video encoding into appearance and motion streams, which are aligned with pretrained vision foundation models to capture the spatial semantics and temporal dynamics in videos separately. To address the gradient conflicts introduced by the heterogeneous supervision, we further propose the Symmetric Alignment-Conflict Projection (SACP) module that proactively reformulates gradients by suppressing the components along conflicting directions. Extensive experiments demonstrate that DeRA outperforms LARP, the previous state-of-the-art video tokenizer by 25% on UCF-101 in terms of rFVD. Moreover, using DeRA for autoregressive video generation, we also achieve new state-of-the-art results on both UCF-101 class-conditional generation and K600 frame prediction.

