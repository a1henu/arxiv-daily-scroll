---
layout: default
title: Self-Attention with State-Object Weighted Combination for Compositional Zero Shot Learning
---

# Self-Attention with State-Object Weighted Combination for Compositional Zero Shot Learning
**arXiv**：[2512.18969v1](https://arxiv.org/abs/2512.18969) · [PDF](https://arxiv.org/pdf/2512.18969.pdf)  
**作者**：Cheng-Hong Chang, Pei-Hsuan Tsai  

**一句话要点**：提出SASOW方法，通过自注意力与状态-对象加权组合提升组合零样本学习性能

**关键词**：组合零样本学习, 自注意力机制, 状态-对象加权, 对象识别, 语义组合

## 3 点简述
- 核心问题：现有组合零样本学习方法如KG-SP在状态和对象识别精度不足，且未考虑组合时的权重分配
- 方法要点：在状态和对象分类器中引入自注意力机制，并在组合过程中加入状态-对象加权策略
- 实验或效果：在MIT-States、UT Zappos和C-GQA数据集上，对未见组合的准确率分别提升2.1%、1.7%和0.4%

## 摘要（原文）

> Object recognition has become prevalent across various industries. However, most existing applications are limited to identifying objects alone, without considering their associated states. The ability to recognize both the state and object simultaneously remains less common. One approach to address this is by treating state and object as a single category during training. However, this approach poses challenges in data collection and training since it requires comprehensive data for all possible combinations. Compositional Zero-shot Learning (CZSL) emerges as a viable solution by treating the state and object as distinct categories during training. CZSL facilitates the identification of novel compositions even in the absence of data for every conceivable combination. The current state-of-the-art method, KG-SP, addresses this issue by training distinct classifiers for states and objects, while leveraging a semantic model to evaluate the plausibility of composed compositions. However, KG-SP's accuracy in state and object recognition can be further improved, and it fails to consider the weighting of states and objects during composition. In this study, we propose SASOW, an enhancement of KG-SP that considers the weighting of states and objects while improving composition recognition accuracy. First, we introduce self-attention mechanisms into the classifiers for states and objects, leading to enhanced accuracy in recognizing both. Additionally, we incorporate the weighting of states and objects during composition to generate more reasonable and accurate compositions. Our validation process involves testing SASOW on three established benchmark datasets. Experimental outcomes affirm when compared against OW-CZSL approach, KG-SP, SASOW showcases improvements of 2.1%, 1.7%, and 0.4% in terms of accuracy for unseen compositions across the MIT-States, UT Zappos, and C-GQA datasets, respectively.

