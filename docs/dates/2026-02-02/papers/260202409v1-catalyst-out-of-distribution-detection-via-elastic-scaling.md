---
layout: default
title: Catalyst: Out-of-Distribution Detection via Elastic Scaling
---

# Catalyst: Out-of-Distribution Detection via Elastic Scaling
**arXiv**：[2602.02409v1](https://arxiv.org/abs/2602.02409) · [PDF](https://arxiv.org/pdf/2602.02409.pdf)  
**作者**：Abid Hassan, Tuan Ngo, Saad Shafiq, Nenad Medvidovic  

**一句话要点**：提出Catalyst框架，通过弹性缩放提升分布外检测性能

**关键词**：分布外检测, 后处理方法, 弹性缩放, 特征图统计, 深度学习安全

## 3 点简述
- 核心问题：现有后处理方法依赖全局平均池化后的特征，忽略了池化前特征图的原始通道统计信息。
- 方法要点：利用池化前特征图的统计（如均值、标准差）动态计算缩放因子，与基线分数融合进行弹性缩放。
- 实验或效果：在CIFAR-10、CIFAR-100和ImageNet上显著降低误报率，平均提升达22.25%至32.87%。

## 摘要（原文）

> Out-of-distribution (OOD) detection is critical for the safe deployment of deep neural networks. State-of-the-art post-hoc methods typically derive OOD scores from the output logits or penultimate feature vector obtained via global average pooling (GAP). We contend that this exclusive reliance on the logit or feature vector discards a rich, complementary signal: the raw channel-wise statistics of the pre-pooling feature map lost in GAP. In this paper, we introduce Catalyst, a post-hoc framework that exploits these under-explored signals. Catalyst computes an input-dependent scaling factor ($γ$) on-the-fly from these raw statistics (e.g., mean, standard deviation, and maximum activation). This $γ$ is then fused with the existing baseline score, multiplicatively modulating it -- an ``elastic scaling'' -- to push the ID and OOD distributions further apart. We demonstrate Catalyst is a generalizable framework: it seamlessly integrates with logit-based methods (e.g., Energy, ReAct, SCALE) and also provides a significant boost to distance-based detectors like KNN. As a result, Catalyst achieves substantial and consistent performance gains, reducing the average False Positive Rate by 32.87 on CIFAR-10 (ResNet-18), 27.94% on CIFAR-100 (ResNet-18), and 22.25% on ImageNet (ResNet-50). Our results highlight the untapped potential of pre-pooling statistics and demonstrate that Catalyst is complementary to existing OOD detection approaches.

