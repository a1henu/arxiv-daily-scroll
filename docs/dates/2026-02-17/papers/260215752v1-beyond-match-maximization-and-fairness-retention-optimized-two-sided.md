---
layout: default
title: Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching
---

# Beyond Match Maximization and Fairness: Retention-Optimized Two-Sided Matching
**arXiv**：[2602.15752v1](https://arxiv.org/abs/2602.15752) · [PDF](https://arxiv.org/pdf/2602.15752.pdf)  
**作者**：Ren Kishimoto, Rikiya Takehi, Koichi Tanaka, Masahiro Nomura, Riku Togashi, Yoji Tomita, Yuta Saito  

**一句话要点**：提出MRet算法以优化双边匹配平台中的用户留存问题

**关键词**：双边匹配, 用户留存, 学习排序, 推荐算法, 在线平台

## 3 点简述
- 核心问题：传统匹配最大化导致用户流失，公平性目标不直接提升留存
- 方法要点：基于个性化留存曲线动态学习排序，联合考虑双方留存增益
- 实验或效果：在合成和真实约会数据上验证MRet比传统方法提高用户留存

## 摘要（原文）

> On two-sided matching platforms such as online dating and recruiting, recommendation algorithms often aim to maximize the total number of matches. However, this objective creates an imbalance, where some users receive far too many matches while many others receive very few and eventually abandon the platform. Retaining users is crucial for many platforms, such as those that depend heavily on subscriptions. Some may use fairness objectives to solve the problem of match maximization. However, fairness in itself is not the ultimate objective for many platforms, as users do not suddenly reward the platform simply because exposure is equalized. In practice, where user retention is often the ultimate goal, casually relying on fairness will leave the optimization of retention up to luck.
>   In this work, instead of maximizing matches or axiomatically defining fairness, we formally define the new problem setting of maximizing user retention in two-sided matching platforms. To this end, we introduce a dynamic learning-to-rank (LTR) algorithm called Matching for Retention (MRet). Unlike conventional algorithms for two-sided matching, our approach models user retention by learning personalized retention curves from each user's profile and interaction history. Based on these curves, MRet dynamically adapts recommendations by jointly considering the retention gains of both the user receiving recommendations and those who are being recommended, so that limited matching opportunities can be allocated where they most improve overall retention. Naturally but importantly, empirical evaluations on synthetic and real-world datasets from a major online dating platform show that MRet achieves higher user retention, since conventional methods optimize matches or fairness rather than retention.

