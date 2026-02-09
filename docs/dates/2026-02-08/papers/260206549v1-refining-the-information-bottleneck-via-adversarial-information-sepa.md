---
layout: default
title: Refining the Information Bottleneck via Adversarial Information Separation
---

# Refining the Information Bottleneck via Adversarial Information Separation
**arXiv**：[2602.06549v1](https://arxiv.org/abs/2602.06549) · [PDF](https://arxiv.org/pdf/2602.06549.pdf)  
**作者**：Shuai Ning, Zhenpeng Wang, Lin Wang, Bing Chen, Shuangrong Liu, Xu Wu, Jin Zhou, Bo Yang  

**一句话要点**：提出AdverISF框架，通过自监督对抗机制在数据稀缺场景中分离任务相关特征与噪声。

**关键词**：信息瓶颈, 对抗学习, 特征分离, 自监督学习, 材料科学, 数据稀缺

## 3 点简述
- 核心问题：实验数据中任务相关特征常与测量噪声和实验伪影混淆，现有方法依赖显式分离标签。
- 方法要点：引入自监督对抗机制强制统计独立性，采用多层分离架构回收噪声信息以精细提取特征。
- 实验或效果：在数据稀缺场景中优于现有方法，在真实材料设计任务中实现优越泛化性能。

## 摘要（原文）

> Generalizing from limited data is particularly critical for models in domains such as material science, where task-relevant features in experimental datasets are often heavily confounded by measurement noise and experimental artifacts. Standard regularization techniques fail to precisely separate meaningful features from noise, while existing adversarial adaptation methods are limited by their reliance on explicit separation labels. To address this challenge, we propose the Adversarial Information Separation Framework (AdverISF), which isolates task-relevant features from noise without requiring explicit supervision. AdverISF introduces a self-supervised adversarial mechanism to enforce statistical independence between task-relevant features and noise representations. It further employs a multi-layer separation architecture that progressively recycles noise information across feature hierarchies to recover features inadvertently discarded as noise, thereby enabling finer-grained feature extraction. Extensive experiments demonstrate that AdverISF outperforms state-of-the-art methods in data-scarce scenarios. In addition, evaluations on real-world material design tasks show that it achieves superior generalization performance.

