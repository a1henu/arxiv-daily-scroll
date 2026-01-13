---
layout: default
title: Variational Contrastive Learning for Skeleton-based Action Recognition
---

# Variational Contrastive Learning for Skeleton-based Action Recognition
**arXiv**：[2601.07666v1](https://arxiv.org/abs/2601.07666) · [PDF](https://arxiv.org/pdf/2601.07666.pdf)  
**作者**：Dang Dinh Nguyen, Decky Aspandi Latif, Titus Zaharia  

**一句话要点**：提出变分对比学习框架，以解决骨架动作识别中对比学习难以捕捉运动不确定性的问题。

**关键词**：骨架动作识别, 变分对比学习, 自监督学习, 概率潜在建模, 低标签学习

## 3 点简述
- 核心问题：现有对比学习方法多为判别式，难以捕捉人类运动的变异性与不确定性。
- 方法要点：集成概率潜在建模与对比自监督学习，学习结构化且语义丰富的表示。
- 实验或效果：在三个基准数据集上表现优异，尤其在低标签场景下，特征更关注重要关节。

## 摘要（原文）

> In recent years, self-supervised representation learning for skeleton-based action recognition has advanced with the development of contrastive learning methods. However, most of contrastive paradigms are inherently discriminative and often struggle to capture the variability and uncertainty intrinsic to human motion. To address this issue, we propose a variational contrastive learning framework that integrates probabilistic latent modeling with contrastive self-supervised learning. This formulation enables the learning of structured and semantically meaningful representations that generalize across different datasets and supervision levels. Extensive experiments on three widely used skeleton-based action recognition benchmarks show that our proposed method consistently outperforms existing approaches, particularly in low-label regimes. Moreover, qualitative analyses show that the features provided by our method are more relevant given the motion and sample characteristics, with more focus on important skeleton joints, when compared to the other methods.

