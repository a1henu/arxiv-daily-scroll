---
layout: default
title: Neural Scaling Laws for Boosted Jet Tagging
---

# Neural Scaling Laws for Boosted Jet Tagging
**arXiv**：[2602.15781v1](https://arxiv.org/abs/2602.15781) · [PDF](https://arxiv.org/pdf/2602.15781.pdf)  
**作者**：Matthias Vigl, Nicole Hartman, Michael Kagan, Lukas Heinrich  

**一句话要点**：提出高能物理中喷注分类的神经缩放定律，以量化计算资源对性能的影响。

**关键词**：神经缩放定律, 喷注分类, 高能物理机器学习, 计算最优训练, 数据集重复, 特征选择

## 3 点简述
- 核心问题：高能物理机器学习模型计算资源远低于工业基础模型，缩放定律研究不足。
- 方法要点：基于JetClass数据集，推导计算最优缩放定律，分析数据重复和特征选择的影响。
- 实验或效果：发现增加计算可逼近性能极限，低层特征能提升极限和固定数据集下的结果。

## 摘要（原文）

> The success of Large Language Models (LLMs) has established that scaling compute, through joint increases in model capacity and dataset size, is the primary driver of performance in modern machine learning. While machine learning has long been an integral component of High Energy Physics (HEP) data analysis workflows, the compute used to train state-of-the-art HEP models remains orders of magnitude below that of industry foundation models. With scaling laws only beginning to be studied in the field, we investigate neural scaling laws for boosted jet classification using the public JetClass dataset. We derive compute optimal scaling laws and identify an effective performance limit that can be consistently approached through increased compute. We study how data repetition, common in HEP where simulation is expensive, modifies the scaling yielding a quantifiable effective dataset size gain. We then study how the scaling coefficients and asymptotic performance limits vary with the choice of input features and particle multiplicity, demonstrating that increased compute reliably drives performance toward an asymptotic limit, and that more expressive, lower-level features can raise the performance limit and improve results at fixed dataset size.

