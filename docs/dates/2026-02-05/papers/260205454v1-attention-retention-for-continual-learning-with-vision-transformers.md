---
layout: default
title: Attention Retention for Continual Learning with Vision Transformers
---

# Attention Retention for Continual Learning with Vision Transformers
**arXiv**：[2602.05454v1](https://arxiv.org/abs/2602.05454) · [PDF](https://arxiv.org/pdf/2602.05454.pdf)  
**作者**：Yue Lu, Xiangyu Zhou, Shizhou Zhang, Yinghui Xing, Guoqiang Liang, Wencong Zhang  

**一句话要点**：提出注意力保留框架以缓解视觉Transformer在持续学习中的灾难性遗忘

**关键词**：持续学习, 视觉Transformer, 注意力机制, 灾难性遗忘, 梯度掩码, 神经科学启发

## 3 点简述
- 核心问题：视觉Transformer在持续学习中因注意力漂移导致灾难性遗忘。
- 方法要点：通过梯度掩码和比例缩放，约束注意力漂移以保护已学视觉概念。
- 实验或效果：在多种持续学习场景中实现最先进性能，并展示鲁棒泛化能力。

## 摘要（原文）

> Continual learning (CL) empowers AI systems to progressively acquire knowledge from non-stationary data streams. However, catastrophic forgetting remains a critical challenge. In this work, we identify attention drift in Vision Transformers as a primary source of catastrophic forgetting, where the attention to previously learned visual concepts shifts significantly after learning new tasks. Inspired by neuroscientific insights into the selective attention in the human visual system, we propose a novel attention-retaining framework to mitigate forgetting in CL. Our method constrains attention drift by explicitly modifying gradients during backpropagation through a two-step process: 1) extracting attention maps of the previous task using a layer-wise rollout mechanism and generating instance-adaptive binary masks, and 2) when learning a new task, applying these masks to zero out gradients associated with previous attention regions, thereby preventing disruption of learned visual concepts. For compatibility with modern optimizers, the gradient masking process is further enhanced by scaling parameter updates proportionally to maintain their relative magnitudes. Experiments and visualizations demonstrate the effectiveness of our method in mitigating catastrophic forgetting and preserving visual concepts. It achieves state-of-the-art performance and exhibits robust generalizability across diverse CL scenarios.

