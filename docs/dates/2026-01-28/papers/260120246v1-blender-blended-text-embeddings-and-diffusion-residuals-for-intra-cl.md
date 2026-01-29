---
layout: default
title: BLENDER: Blended Text Embeddings and Diffusion Residuals for Intra-Class Image Synthesis in Deep Metric Learning
---

# BLENDER: Blended Text Embeddings and Diffusion Residuals for Intra-Class Image Synthesis in Deep Metric Learning
**arXiv**：[2601.20246v1](https://arxiv.org/abs/2601.20246) · [PDF](https://arxiv.org/pdf/2601.20246.pdf)  
**作者**：Jan Niklas Kolf, Ozan Tezcan, Justin Theiss, Hyung Jun Kim, Wentao Bao, Bhargav Bhushanam, Khushi Gupta, Arun Kejariwal, Naser Damer, Fadi Boutros  

**一句话要点**：提出BLenDeR方法，通过扩散残差操作增强深度度量学习中的类内多样性

**关键词**：深度度量学习, 扩散模型, 图像合成, 类内多样性, 可控生成

## 3 点简述
- 核心问题：现有生成方法在深度度量学习中难以可控地增加类内多样性。
- 方法要点：利用集合论启发的并集和交集操作处理去噪残差，可控合成类内多样属性组合。
- 实验或效果：在标准基准测试中优于现有方法，如CUB-200上Recall@1提升3.7%。

## 摘要（原文）

> The rise of Deep Generative Models (DGM) has enabled the generation of high-quality synthetic data. When used to augment authentic data in Deep Metric Learning (DML), these synthetic samples enhance intra-class diversity and improve the performance of downstream DML tasks. We introduce BLenDeR, a diffusion sampling method designed to increase intra-class diversity for DML in a controllable way by leveraging set-theory inspired union and intersection operations on denoising residuals. The union operation encourages any attribute present across multiple prompts, while the intersection extracts the common direction through a principal component surrogate. These operations enable controlled synthesis of diverse attribute combinations within each class, addressing key limitations of existing generative approaches. Experiments on standard DML benchmarks demonstrate that BLenDeR consistently outperforms state-of-the-art baselines across multiple datasets and backbones. Specifically, BLenDeR achieves 3.7% increase in Recall@1 on CUB-200 and a 1.8% increase on Cars-196, compared to state-of-the-art baselines under standard experimental settings.

