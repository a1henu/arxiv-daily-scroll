---
layout: default
title: Attribute Distribution Modeling and Semantic-Visual Alignment for Generative Zero-shot Learning
---

# Attribute Distribution Modeling and Semantic-Visual Alignment for Generative Zero-shot Learning
**arXiv**：[2603.06281v1](https://arxiv.org/abs/2603.06281) · [PDF](https://arxiv.org/pdf/2603.06281.pdf)  
**作者**：Haojie Pu, Zhuoming Li, Yongbiao Gao, Yuheng Jia  

**一句话要点**：提出ADiVA方法以解决生成式零样本学习中的类实例差距和语义视觉域差距问题

**关键词**：生成式零样本学习, 属性分布建模, 语义视觉对齐, 类实例差距, 域差距, 特征合成

## 3 点简述
- 核心问题：类级属性无法捕捉实例级视觉外观，导致类实例差距；语义与视觉特征分布不匹配，引发语义视觉域差距。
- 方法要点：通过属性分布建模模块学习可转移属性分布并采样实例级属性，结合视觉引导对齐模块优化语义表示以反映视觉结构。
- 实验或效果：在三个基准数据集上显著优于现有方法，如AWA2和SUN分别提升4.7%和6.1%，并可作为插件增强其他方法。

## 摘要（原文）

> Generative zero-shot learning (ZSL) synthesizes features for unseen classes, leveraging semantic conditions to transfer knowledge from seen classes. However, it also introduces two intrinsic challenges: (1) class-level attributes fails to capture instance-specific visual appearances due to substantial intra-class variability, thus causing the class-instance gap; (2) the substantial mismatch between semantic and visual feature distributions, manifested in inter-class correlations, gives rise to the semantic-visual domain gap. To address these challenges, we propose an Attribute Distribution Modeling and Semantic-Visual Alignment (ADiVA) approach, jointly modeling attribute distributions and performing explicit semantic-visual alignment. Specifically, our ADiVA consists of two modules: an Attribute Distribution Modeling (ADM) module that learns a transferable attribute distribution for each class and samples instance-level attributes for unseen classes, and a Visual-Guided Alignment (VGA) module that refines semantic representations to better reflect visual structures. Experiments on three widely used benchmark datasets demonstrate that ADiVA significantly outperforms state-of-the-art methods (e.g., achieving gains of 4.7% and 6.1% on AWA2 and SUN, respectively). Moreover, our approach can serve as a plugin to enhance existing generative ZSL methods.

