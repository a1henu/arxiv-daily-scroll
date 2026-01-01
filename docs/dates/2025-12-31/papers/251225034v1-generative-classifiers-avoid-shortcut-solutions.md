---
layout: default
title: Generative Classifiers Avoid Shortcut Solutions
---

# Generative Classifiers Avoid Shortcut Solutions
**arXiv**：[2512.25034v1](https://arxiv.org/abs/2512.25034) · [PDF](https://arxiv.org/pdf/2512.25034.pdf)  
**作者**：Alexander C. Li, Ananya Kumar, Deepak Pathak  

**一句话要点**：提出生成式分类器以避免分布偏移下的捷径学习问题

**关键词**：生成式分类器, 分布偏移, 捷径学习, 虚假相关, 扩散模型, 自回归模型

## 3 点简述
- 判别式分类器易学习虚假相关特征，导致分布偏移时性能下降
- 生成式分类器通过建模所有特征避免捷径，无需额外正则化或先验知识
- 在图像和文本分布偏移基准上实现最优性能，并分析高斯玩具模型以理解其归纳偏置

## 摘要（原文）

> Discriminative approaches to classification often learn shortcuts that hold in-distribution but fail even under minor distribution shift. This failure mode stems from an overreliance on features that are spuriously correlated with the label. We show that generative classifiers, which use class-conditional generative models, can avoid this issue by modeling all features, both core and spurious, instead of mainly spurious ones. These generative classifiers are simple to train, avoiding the need for specialized augmentations, strong regularization, extra hyperparameters, or knowledge of the specific spurious correlations to avoid. We find that diffusion-based and autoregressive generative classifiers achieve state-of-the-art performance on five standard image and text distribution shift benchmarks and reduce the impact of spurious correlations in realistic applications, such as medical or satellite datasets. Finally, we carefully analyze a Gaussian toy setting to understand the inductive biases of generative classifiers, as well as the data properties that determine when generative classifiers outperform discriminative ones.

