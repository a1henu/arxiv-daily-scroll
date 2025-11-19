---
layout: default
title: DoGCLR: Dominance-Game Contrastive Learning Network for Skeleton-Based Action Recognition
---

# DoGCLR: Dominance-Game Contrastive Learning Network for Skeleton-Based Action Recognition
**arXiv**：[2511.14179v1](https://arxiv.org/abs/2511.14179) · [PDF](https://arxiv.org/pdf/2511.14179.pdf)  
**作者**：Yanshan Li, Ke Ma, Miaomiao Wei, Linhui Dai  

**一句话要点**：提出DoGCLR以解决骨架动作识别中对比学习的运动信息损失和负样本选择问题

**关键词**：骨架动作识别, 自监督对比学习, 博弈论, 时空权重定位, 熵驱动策略, 负样本优化

## 3 点简述
- 现有方法均匀处理骨架区域并使用FIFO队列，导致运动信息损失和非最优负样本选择
- 基于博弈论建模正负样本构建为支配游戏，结合时空权重定位和熵驱动策略优化样本
- 在NTU RGB+D和PKU-MMD数据集上超越SOTA，最高提升2.7%，在挑战场景中鲁棒性强

## 摘要（原文）

> Existing self-supervised contrastive learning methods for skeleton-based action recognition often process all skeleton regions uniformly, and adopt a first-in-first-out (FIFO) queue to store negative samples, which leads to motion information loss and non-optimal negative sample selection. To address these challenges, this paper proposes Dominance-Game Contrastive Learning network for skeleton-based action Recognition (DoGCLR), a self-supervised framework based on game theory. DoGCLR models the construction of positive and negative samples as a dynamic Dominance Game, where both sample types interact to reach an equilibrium that balances semantic preservation and discriminative strength. Specifically, a spatio-temporal dual weight localization mechanism identifies key motion regions and guides region-wise augmentations to enhance motion diversity while maintaining semantics. In parallel, an entropy-driven dominance strategy manages the memory bank by retaining high entropy (hard) negatives and replacing low-entropy (weak) ones, ensuring consistent exposure to informative contrastive signals. Extensive experiments are conducted on NTU RGB+D and PKU-MMD datasets. On NTU RGB+D 60 X-Sub/X-View, DoGCLR achieves 81.1%/89.4% accuracy, and on NTU RGB+D 120 X-Sub/X-Set, DoGCLR achieves 71.2%/75.5% accuracy, surpassing state-of-the-art methods by 0.1%, 2.7%, 1.1%, and 2.3%, respectively. On PKU-MMD Part I/Part II, DoGCLR performs comparably to the state-of-the-art methods and achieves a 1.9% higher accuracy on Part II, highlighting its strong robustness on more challenging scenarios.

