---
layout: default
title: PRISM: Diversifying Dataset Distillation by Decoupling Architectural Priors
---

# PRISM: Diversifying Dataset Distillation by Decoupling Architectural Priors
**arXiv**：[2511.09905v1](https://arxiv.org/abs/2511.09905) · [PDF](https://arxiv.org/pdf/2511.09905.pdf)  
**作者**：Brian B. Moser, Shalini Strode, Federico Raue, Stanislav Frolov, Krzysztof Adamkiewicz, Arundhati Shanbhag, Joachim Folk, Tobias C. Nauen, Andreas Dengel  

**一句话要点**：提出PRISM框架以解决数据集蒸馏中单一教师模型偏差问题

**关键词**：数据集蒸馏, 模型偏差, 多样性增强, 对数匹配, 批归一化对齐, 合成数据生成

## 3 点简述
- 核心问题：单一教师模型偏差导致合成数据平滑、多样性不足，影响泛化能力
- 方法要点：解耦对数匹配和正则化目标，使用不同教师架构进行监督
- 实验或效果：在ImageNet-1K上优于单教师和多教师方法，提升类内多样性

## 摘要（原文）

> Dataset distillation (DD) promises compact yet faithful synthetic data, but existing approaches often inherit the inductive bias of a single teacher model. As dataset size increases, this bias drives generation toward overly smooth, homogeneous samples, reducing intra-class diversity and limiting generalization. We present PRISM (PRIors from diverse Source Models), a framework that disentangles architectural priors during synthesis. PRISM decouples the logit-matching and regularization objectives, supervising them with different teacher architectures: a primary model for logits and a stochastic subset for batch-normalization (BN) alignment. On ImageNet-1K, PRISM consistently and reproducibly outperforms single-teacher methods (e.g., SRe2L) and recent multi-teacher variants (e.g., G-VBSM) at low- and mid-IPC regimes. The generated data also show significantly richer intra-class diversity, as reflected by a notable drop in cosine similarity between features. We further analyze teacher selection strategies (pre- vs. intra-distillation) and introduce a scalable cross-class batch formation scheme for fast parallel synthesis. Code will be released after the review period.

