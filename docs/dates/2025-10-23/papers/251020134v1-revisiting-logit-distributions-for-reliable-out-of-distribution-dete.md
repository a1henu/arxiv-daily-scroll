---
layout: default
title: Revisiting Logit Distributions for Reliable Out-of-Distribution Detection
---

# Revisiting Logit Distributions for Reliable Out-of-Distribution Detection
**arXiv**：[2510.20134v1](https://arxiv.org/abs/2510.20134) · [PDF](https://arxiv.org/pdf/2510.20134.pdf)  
**作者**：Jiachen Liang, Ruibing Hou, Minyang Hu, Hong Chang, Shiguang Shan, Xilin Chen  

**一句话要点**：提出LogitGap方法以增强开放世界应用中OOD检测的可靠性

**关键词**：OOD检测, logits分布, 后处理方法, 视觉语言模型, 开放世界应用

## 3 点简述
- 核心问题：现有后处理方法未充分利用logits空间信息，影响OOD检测效果。
- 方法要点：利用最大logit与其余logit关系，自动选择信息丰富子集进行评分。
- 实验或效果：在视觉语言和纯视觉模型中，多场景基准测试达到SOTA性能。

## 摘要（原文）

> Out-of-distribution (OOD) detection is critical for ensuring the reliability
> of deep learning models in open-world applications. While post-hoc methods are
> favored for their efficiency and ease of deployment, existing approaches often
> underexploit the rich information embedded in the model's logits space. In this
> paper, we propose LogitGap, a novel post-hoc OOD detection method that
> explicitly exploits the relationship between the maximum logit and the
> remaining logits to enhance the separability between in-distribution (ID) and
> OOD samples. To further improve its effectiveness, we refine LogitGap by
> focusing on a more compact and informative subset of the logit space.
> Specifically, we introduce a training-free strategy that automatically
> identifies the most informative logits for scoring. We provide both theoretical
> analysis and empirical evidence to validate the effectiveness of our approach.
> Extensive experiments on both vision-language and vision-only models
> demonstrate that LogitGap consistently achieves state-of-the-art performance
> across diverse OOD detection scenarios and benchmarks. Code is available at
> https://github.com/GIT-LJc/LogitGap.

