---
layout: default
title: Trust Regions Sell, But Who's Buying? Overlap Geometry as an Alternative Trust Region for Policy Optimization
---

# Trust Regions Sell, But Who's Buying? Overlap Geometry as an Alternative Trust Region for Policy Optimization
**arXiv**：[2602.06627v1](https://arxiv.org/abs/2602.06627) · [PDF](https://arxiv.org/pdf/2602.06627.pdf)  
**作者**：Gaurish Trivedi, Alakh Sharma, Kartikey Singh Bhandari, Yash Sinha, Pratik Narang, Dhruv Kumar, Jagat Sesh Challa  

**一句话要点**：提出基于重叠几何的信任区域方法，以替代KL散度提升策略优化的稳定性。

**关键词**：策略优化, 信任区域方法, 分布重叠, Bhattacharyya系数, 强化学习稳定性

## 3 点简述
- 标准KL信任区域方法无法有效控制罕见的大似然比偏移，导致训练不稳定。
- 使用Bhattacharyya系数约束分布重叠，直接惩罚似然比尾部分离，提供更紧的控制。
- 实验表明，在匹配训练预算下，基于重叠的方法提高了鲁棒性和聚合性能。

## 摘要（原文）

> Standard trust-region methods constrain policy updates via Kullback-Leibler (KL) divergence. However, KL controls only an average divergence and does not directly prevent rare, large likelihood-ratio excursions that destabilize training--precisely the failure mode that motivates heuristics such as PPO's clipping. We propose overlap geometry as an alternative trust region, constraining distributional overlap via the Bhattacharyya coefficient (closely related to the Hellinger/Renyi-1/2 geometry). This objective penalizes separation in the ratio tails, yielding tighter control over likelihood-ratio excursions without relying on total variation bounds that can be loose in tail regimes. We derive Bhattacharyya-TRPO (BTRPO) and Bhattacharyya-PPO (BPPO), enforcing overlap constraints via square-root ratio updates: BPPO clips the square-root ratio q = sqrt(r), and BTRPO applies a quadratic Hellinger/Bhattacharyya penalty. Empirically, overlap-based updates improve robustness and aggregate performance as measured by RLiable under matched training budgets, suggesting overlap constraints as a practical, principled alternative to KL for stable policy optimization.

