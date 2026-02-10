---
layout: default
title: Is Meta-Path Attention an Explanation? Evidence of Alignment and Decoupling in Heterogeneous GNNs
---

# Is Meta-Path Attention an Explanation? Evidence of Alignment and Decoupling in Heterogeneous GNNs
**arXiv**：[2602.08500v1](https://arxiv.org/abs/2602.08500) · [PDF](https://arxiv.org/pdf/2602.08500.pdf)  
**作者**：Maiqi Jiang, Noman Ali, Yiran Ding, Yanfu Zhang  

**一句话要点**：提出MetaXplain协议以评估异质图神经网络中元路径注意力的解释可靠性

**关键词**：异质图神经网络, 元路径注意力, 后验解释, 解释可靠性, 去噪效应

## 3 点简述
- 核心问题：元路径注意力是否反映语义重要性，何时可能解耦
- 方法要点：设计MetaXplain协议，支持视图分解解释和模式有效扰动
- 实验或效果：在ACM等数据集上验证，发现对齐与解耦现象，解释可去噪

## 摘要（原文）

> Meta-path-based heterogeneous graph neural networks aggregate over meta-path-induced views, and their semantic-level attention over meta-path channels is widely used as a narrative for ``which semantics matter.'' We study this assumption empirically by asking: when does meta-path attention reflect meta-path importance, and when can it decouple? A key challenge is that most post-hoc GNN explainers are designed for homogeneous graphs, and naive adaptations to heterogeneous neighborhoods can mix semantics and confound perturbations. To enable a controlled empirical analysis, we introduce MetaXplain, a meta-path-aware post-hoc explanation protocol that applies existing explainers in the native meta-path view domain via (i) view-factorized explanations, (ii) schema-valid channel-wise perturbations, and (iii) fusion-aware attribution, without modifying the underlying predictor. We benchmark representative gradient-, perturbation-, and Shapley-style explainers on ACM, DBLP, and IMDB with HAN and HAN-GCN, comparing against xPath and type-matched random baselines under standard faithfulness metrics. To quantify attention reliability, we propose Meta-Path Attention--Explanation Alignment (MP-AEA), which measures rank correlation between learned attention weights and explanation-derived meta-path contribution scores across random runs. Our results show that meta-path-aware explanations typically outperform random controls, while MP-AEA reveals both high-alignment and statistically significant decoupling regimes depending on the dataset and backbone; moreover, retraining on explanation-induced subgraphs often preserves, and in some noisy regimes improves, predictive performance, suggesting an explanation-as-denoising effect.

