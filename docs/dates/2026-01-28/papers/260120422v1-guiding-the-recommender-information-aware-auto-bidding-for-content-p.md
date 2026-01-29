---
layout: default
title: Guiding the Recommender: Information-Aware Auto-Bidding for Content Promotion
---

# Guiding the Recommender: Information-Aware Auto-Bidding for Content Promotion
**arXiv**：[2601.20422v1](https://arxiv.org/abs/2601.20422) · [PDF](https://arxiv.org/pdf/2601.20422.pdf)  
**作者**：Yumou Liu, Zhenzhe Zheng, Jiang Rong, Yao Hu, Fan Wu, Guihai Chen  

**一句话要点**：提出信息感知自动出价框架，以平衡内容推广的短期收益与长期模型性能

**关键词**：内容推广, 自动出价, 信息感知, 双目标优化, 梯度覆盖, 在线拍卖

## 3 点简述
- 揭示内容推广可能损害高质量内容的推荐性能，因曝光给次优受众污染信号
- 设计基于拉格朗日对偶的两阶段自动出价算法，动态调整预算并优化每次曝光的边际效用
- 在合成和真实数据集上验证，框架优于基线，提升最终AUC/LogLoss并严格遵循预算

## 摘要（原文）

> Modern content platforms offer paid promotion to mitigate cold start by allocating exposure via auctions. Our empirical analysis reveals a counterintuitive flaw in this paradigm: while promotion rescues low-to-medium quality content, it can harm high-quality content by forcing exposure to suboptimal audiences, polluting engagement signals and downgrading future recommendation. We recast content promotion as a dual-objective optimization that balances short-term value acquisition with long-term model improvement. To make this tractable at bid time in content promotion, we introduce a decomposable surrogate objective, gradient coverage, and establish its formal connection to Fisher Information and optimal experimental design. We design a two-stage auto-bidding algorithm based on Lagrange duality that dynamically paces budget through a shadow price and optimizes impression-level bids using per-impression marginal utilities. To address missing labels at bid time, we propose a confidence-gated gradient heuristic, paired with a zeroth-order variant for black-box models that reliably estimates learning signals in real time. We provide theoretical guarantees, proving monotone submodularity of the composite objective, sublinear regret in online auction, and budget feasibility. Extensive offline experiments on synthetic and real-world datasets validate the framework: it outperforms baselines, achieves superior final AUC/LogLoss, adheres closely to budget targets, and remains effective when gradients are approximated zeroth-order. These results show that strategic, information-aware promotion can improve long-term model performance and organic outcomes beyond naive impression-maximization strategies.

