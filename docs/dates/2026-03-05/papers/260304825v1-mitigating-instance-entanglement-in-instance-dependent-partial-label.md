---
layout: default
title: Mitigating Instance Entanglement in Instance-Dependent Partial Label Learning
---

# Mitigating Instance Entanglement in Instance-Dependent Partial Label Learning
**arXiv**：[2603.04825v1](https://arxiv.org/abs/2603.04825) · [PDF](https://arxiv.org/pdf/2603.04825.pdf)  
**作者**：Rui Zhao, Bin Shi, Kai Sun, Bo Dong  

**一句话要点**：提出类特定增强解缠框架以缓解实例依赖部分标签学习中的实例纠缠问题

**关键词**：部分标签学习, 实例依赖学习, 实例纠缠, 类特定增强, 解缠学习, 弱监督分类

## 3 点简述
- 核心问题：实例依赖部分标签学习中，相似类实例因特征和候选标签重叠导致类混淆加剧。
- 方法要点：通过类内增强对齐和类间加权惩罚损失，增强类特定特征并扩大类间距离。
- 实验或效果：实验验证了框架在缓解纠缠和提升性能方面的有效性，代码已开源。

## 摘要（原文）

> Partial label learning is a prominent weakly supervised classification task, where each training instance is ambiguously labeled with a set of candidate labels. In real-world scenarios, candidate labels are often influenced by instance features, leading to the emergence of instance-dependent PLL (ID-PLL), a setting that more accurately reflects this relationship. A significant challenge in ID-PLL is instance entanglement, where instances from similar classes share overlapping features and candidate labels, resulting in increased class confusion. To address this issue, we propose a novel Class-specific Augmentation based Disentanglement (CAD) framework, which tackles instance entanglement by both intra- and inter-class regulations. For intra-class regulation, CAD amplifies class-specific features to generate class-wise augmentations and aligns same-class augmentations across instances. For inter-class regulation, CAD introduces a weighted penalty loss function that applies stronger penalties to more ambiguous labels, encouraging larger inter-class distances. By jointly applying intra- and inter-class regulations, CAD improves the clarity of class boundaries and reduces class confusion caused by entanglement. Extensive experimental results demonstrate the effectiveness of CAD in mitigating the entanglement problem and enhancing ID-PLL performance. The code is available at https://github.com/RyanZhaoIc/CAD.git.

