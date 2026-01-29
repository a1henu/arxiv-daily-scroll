---
layout: default
title: Less is More: Clustered Cross-Covariance Control for Offline RL
---

# Less is More: Clustered Cross-Covariance Control for Offline RL
**arXiv**：[2601.20765v1](https://arxiv.org/abs/2601.20765) · [PDF](https://arxiv.org/pdf/2601.20765.pdf)  
**作者**：Nan Qiao, Sheng Yue, Shuning Wang, Yongheng Deng, Ju Ren  

**一句话要点**：提出聚类交叉协方差控制方法以缓解离线强化学习中的分布偏移问题

**关键词**：离线强化学习, 分布偏移, 交叉协方差控制, 分区缓冲采样, 梯度校正

## 3 点简述
- 核心问题：离线强化学习中分布偏移导致TD交叉协方差偏差，尤其在OOD区域加剧。
- 方法要点：采用分区缓冲采样和梯度校正惩罚，减少协方差影响并保持优化目标下界。
- 实验或效果：方法在小型数据集和OOD区域上表现更稳定，回报提升高达30%。

## 摘要（原文）

> A fundamental challenge in offline reinforcement learning is distributional shift. Scarce data or datasets dominated by out-of-distribution (OOD) areas exacerbate this issue. Our theoretical analysis and experiments show that the standard squared error objective induces a harmful TD cross covariance. This effect amplifies in OOD areas, biasing optimization and degrading policy learning. To counteract this mechanism, we develop two complementary strategies: partitioned buffer sampling that restricts updates to localized replay partitions, attenuates irregular covariance effects, and aligns update directions, yielding a scheme that is easy to integrate with existing implementations, namely Clustered Cross-Covariance Control for TD (C^4). We also introduce an explicit gradient-based corrective penalty that cancels the covariance induced bias within each update. We prove that buffer partitioning preserves the lower bound property of the maximization objective, and that these constraints mitigate excessive conservatism in extreme OOD areas without altering the core behavior of policy constrained offline reinforcement learning. Empirically, our method showcases higher stability and up to 30% improvement in returns over prior methods, especially with small datasets and splits that emphasize OOD areas.

