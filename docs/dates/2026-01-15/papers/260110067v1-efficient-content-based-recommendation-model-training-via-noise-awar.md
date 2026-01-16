---
layout: default
title: Efficient Content-based Recommendation Model Training via Noise-aware Coreset Selection
---

# Efficient Content-based Recommendation Model Training via Noise-aware Coreset Selection
**arXiv**：[2601.10067v1](https://arxiv.org/abs/2601.10067) · [PDF](https://arxiv.org/pdf/2601.10067.pdf)  
**作者**：Hung Vinh Tran, Tong Chen, Hechuan Wen, Quoc Viet Hung Nguyen, Bin Cui, Hongzhi Yin  

**一句话要点**：提出噪声感知核心集选择方法以提升基于内容的推荐系统训练效率

**关键词**：基于内容的推荐系统, 核心集选择, 噪声标签校正, 子模优化, 不确定性量化, 高效训练

## 3 点简述
- 核心问题：大规模训练基于内容的推荐系统计算成本高，且用户-物品交互噪声影响核心集质量
- 方法要点：通过基于梯度的子模优化构建核心集，结合渐进训练模型校正噪声标签，并量化不确定性过滤低置信样本
- 实验或效果：仅用1%训练数据恢复93-95%全数据集性能，优于现有核心集选择技术

## 摘要（原文）

> Content-based recommendation systems (CRSs) utilize content features to predict user-item interactions, serving as essential tools for helping users navigate information-rich web services. However, ensuring the effectiveness of CRSs requires large-scale and even continuous model training to accommodate diverse user preferences, resulting in significant computational costs and resource demands. A promising approach to this challenge is coreset selection, which identifies a small but representative subset of data samples that preserves model quality while reducing training overhead. Yet, the selected coreset is vulnerable to the pervasive noise in user-item interactions, particularly when it is minimally sized. To this end, we propose Noise-aware Coreset Selection (NaCS), a specialized framework for CRSs. NaCS constructs coresets through submodular optimization based on training gradients, while simultaneously correcting noisy labels using a progressively trained model. Meanwhile, we refine the selected coreset by filtering out low-confidence samples through uncertainty quantification, thereby avoid training with unreliable interactions. Through extensive experiments, we show that NaCS produces higher-quality coresets for CRSs while achieving better efficiency than existing coreset selection techniques. Notably, NaCS recovers 93-95\% of full-dataset training performance using merely 1\% of the training data. The source code is available at \href{https://github.com/chenxing1999/nacs}{https://github.com/chenxing1999/nacs}.

