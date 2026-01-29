---
layout: default
title: C2:Cross learning module enhanced decision transformer with Constraint-aware loss for auto-bidding
---

# C2:Cross learning module enhanced decision transformer with Constraint-aware loss for auto-bidding
**arXiv**：[2601.20257v1](https://arxiv.org/abs/2601.20257) · [PDF](https://arxiv.org/pdf/2601.20257.pdf)  
**作者**：Jinren Ding, Xuejian Xu, Shen Jiang, Zhitong Hao, Jinhui Yang, Peng Jiang  

**一句话要点**：提出C2框架，通过交叉学习模块和约束感知损失增强决策变换器，用于自动出价任务。

**关键词**：自动出价, 决策变换器, 交叉注意力, 约束优化, 离线评估

## 3 点简述
- 决策变换器在自动出价中建模时序依赖，但存在序列间相关性不足和最优/次优行为学习不区分的问题。
- C2引入交叉学习块增强序列间相关性建模，并设计约束感知损失以选择性学习最优轨迹。
- 在AuctionNet数据集上离线评估显示性能提升，消融研究验证了模块的协同作用。

## 摘要（原文）

> Decision Transformer (DT) shows promise for generative auto-bidding by capturing temporal dependencies, but suffers from two critical limitations: insufficient cross-correlation modeling among state, action, and return-to-go (RTG) sequences, and indiscriminate learning of optimal/suboptimal behaviors. To address these, we propose C2, a novel framework enhancing DT with two core innovations: (1) a Cross Learning Block (CLB) via cross-attention to strengthen inter-sequence correlation modeling; (2) a Constraint-aware Loss (CL) incorporating budget and Cost-Per-Acquisition (CPA) constraints for selective learning of optimal trajectories. Extensive offline evaluations on the AuctionNet dataset demonstrate consistent performance gains (up to 3.23\% over state-of-the-art GAVE) across diverse budget settings; ablation studies verify the complementary synergy of CLB and CL, confirming C2's superiority in auto-bidding. The code for reproducing our results is available at: https://github.com/Dingjinren/C2.

