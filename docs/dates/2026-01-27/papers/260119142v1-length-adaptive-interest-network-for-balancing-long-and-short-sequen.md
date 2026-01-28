---
layout: default
title: Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling in CTR Prediction
---

# Length-Adaptive Interest Network for Balancing Long and Short Sequence Modeling in CTR Prediction
**arXiv**：[2601.19142v1](https://arxiv.org/abs/2601.19142) · [PDF](https://arxiv.org/pdf/2601.19142.pdf)  
**作者**：Zhicheng Zhang, Zhaocheng Du, Jieming Zhu, Jiwei Tang, Fengyuan Lu, Wang Jiaheng, Song-Li Wu, Qianhui Zhu, Jingyu Li, Hai-Tao Zheng, Zhenhua Dong  

**一句话要点**：提出LAIN框架以解决CTR预测中长短期序列建模不平衡问题

**关键词**：CTR预测, 序列建模, 长度自适应, 注意力机制, 推荐系统

## 3 点简述
- 核心问题：用户行为序列长度异质性导致现有CTR模型在长序列下性能下降，尤其影响短序列用户。
- 方法要点：LAIN通过谱长度编码器、长度条件提示和长度调制注意力，自适应调整建模策略。
- 实验或效果：在三个真实基准测试中，LAIN提升整体性能，AUC增益达1.15%，对数损失减少2.25%。

## 摘要（原文）

> User behavior sequences in modern recommendation systems exhibit significant length heterogeneity, ranging from sparse short-term interactions to rich long-term histories. While longer sequences provide more context, we observe that increasing the maximum input sequence length in existing CTR models paradoxically degrades performance for short-sequence users due to attention polarization and length imbalance in training data. To address this, we propose LAIN(Length-Adaptive Interest Network), a plug-and-play framework that explicitly incorporates sequence length as a conditioning signal to balance long- and short-sequence modeling. LAIN consists of three lightweight components: a Spectral Length Encoder that maps length into continuous representations, Length-Conditioned Prompting that injects global contextual cues into both long- and short-term behavior branches, and Length-Modulated Attention that adaptively adjusts attention sharpness based on sequence length. Extensive experiments on three real-world benchmarks across five strong CTR backbones show that LAIN consistently improves overall performance, achieving up to 1.15% AUC gain and 2.25% log loss reduction. Notably, our method significantly improves accuracy for short-sequence users without sacrificing longsequence effectiveness. Our work offers a general, efficient, and deployable solution to mitigate length-induced bias in sequential recommendation.

