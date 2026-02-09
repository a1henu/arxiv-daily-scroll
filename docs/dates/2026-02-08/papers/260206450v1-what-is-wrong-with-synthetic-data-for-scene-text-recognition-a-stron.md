---
layout: default
title: What Is Wrong with Synthetic Data for Scene Text Recognition? A Strong Synthetic Engine with Diverse Simulations and Self-Evolution
---

# What Is Wrong with Synthetic Data for Scene Text Recognition? A Strong Synthetic Engine with Diverse Simulations and Self-Evolution
**arXiv**：[2602.06450v1](https://arxiv.org/abs/2602.06450) · [PDF](https://arxiv.org/pdf/2602.06450.pdf)  
**作者**：Xingsong Ye, Yongkun Du, JiaXin Zhang, Chen Li, Jing LYU, Zhineng Chen  

**一句话要点**：提出UnionST合成引擎与自进化学习框架，以增强场景文本识别中合成数据的多样性和真实性。

**关键词**：场景文本识别, 合成数据生成, 域差距, 自进化学习, 数据增强

## 3 点简述
- 核心问题：现有合成数据在语料、字体和布局上多样性不足，导致与真实数据存在显著域差距。
- 方法要点：开发UnionST合成引擎，生成覆盖挑战性样本的文本，并构建大规模数据集UnionST-S。
- 实验或效果：在UnionST-S上训练的模型优于现有合成数据集，某些场景下超越真实数据，自进化学习仅需9%真实标签即达竞争性能。

## 摘要（原文）

> Large-scale and categorical-balanced text data is essential for training effective Scene Text Recognition (STR) models, which is hard to achieve when collecting real data. Synthetic data offers a cost-effective and perfectly labeled alternative. However, its performance often lags behind, revealing a significant domain gap between real and current synthetic data. In this work, we systematically analyze mainstream rendering-based synthetic datasets and identify their key limitations: insufficient diversity in corpus, font, and layout, which restricts their realism in complex scenarios. To address these issues, we introduce UnionST, a strong data engine synthesizes text covering a union of challenging samples and better aligns with the complexity observed in the wild. We then construct UnionST-S, a large-scale synthetic dataset with improved simulations in challenging scenarios. Furthermore, we develop a self-evolution learning (SEL) framework for effective real data annotation. Experiments show that models trained on UnionST-S achieve significant improvements over existing synthetic datasets. They even surpass real-data performance in certain scenarios. Moreover, when using SEL, the trained models achieve competitive performance by only seeing 9% of real data labels.

