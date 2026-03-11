---
layout: default
title: The Costs of Reproducibility in Music Separation Research: a Replication of Band-Split RNN
---

# The Costs of Reproducibility in Music Separation Research: a Replication of Band-Split RNN
**arXiv**：[2603.09187v1](https://arxiv.org/abs/2603.09187) · [PDF](https://arxiv.org/pdf/2603.09187.pdf)  
**作者**：Paul Magron, Romain Serizel, Constance Douwes  

**一句话要点**：复制BSRNN模型以探讨音乐分离研究的可复现性成本，并发布优化代码

**关键词**：音乐源分离, 可复现性研究, BSRNN模型, 模型优化, 代码公开

## 3 点简述
- 核心问题：音乐源分离研究中复杂架构和训练协议加剧可复现性问题，BSRNN模型因代码未公开难以复现
- 方法要点：通过大量实验尝试复制BSRNN模型，分析模型设计和训练流程，探索优化变体
- 实验或效果：未能复现原始结果，但开发出性能显著提升的优化BSRNN模型，并公开代码和预训练模型

## 摘要（原文）

> Music source separation is the task of isolating the instrumental tracks from a music song. Despite its spectacular recent progress, the trend towards more complex architectures and training protocols exacerbates reproducibility issues. The band-split recurrent neural networks (BSRNN) model is promising in this regard, since it yields close to state-of-the-art results on public datasets, and requires reasonable resources for training. Unfortunately, it is not straightforward to reproduce since its full code is not available. In this paper, we attempt to replicate BSRNN as closely as possible to the original paper through extensive experiments, which allows us to conduct a critical reflection on this reproducibility issue. Our contributions are three-fold. First, this study yields several insights on the model design and training pipeline, which sheds light on potential future improvements. In particular, since we were unsuccessful in reproducing the original results, we explore additional variants that ultimately yield an optimized BSRNN model, whose performance largely improves that of the original. Second, we discuss reproducibility issues from both methodological and practical perspectives. We notably underline how substantial time and energy costs could have been saved upon availability of the full pipeline. Third, our code and pre-trained models are released publicly to foster reproducible research. We hope that this study will contribute to spread awareness on the importance of reproducible research in the music separation community, and help promoting more transparent and sustainable practices.

