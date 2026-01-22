---
layout: default
title: Spatially Generalizable Mobile Manipulation via Adaptive Experience Selection and Dynamic Imagination
---

# Spatially Generalizable Mobile Manipulation via Adaptive Experience Selection and Dynamic Imagination
**arXiv**：[2601.14649v1](https://arxiv.org/abs/2601.14649) · [PDF](https://arxiv.org/pdf/2601.14649.pdf)  
**作者**：Ping Zhong, Liangbai Liu, Bolei Chen, Tao Wu, Jiazhi Xia, Chaoxu Mu, Jianxin Wang  

**一句话要点**：提出自适应经验选择与动态想象方法，以提升移动操作的空间泛化能力与样本效率。

**关键词**：移动操作, 自适应经验选择, 循环状态空间模型, 模型预测规划, 空间泛化, 样本效率

## 3 点简述
- 核心问题：移动操作面临样本效率低和空间泛化差，源于冗余数据利用不足和策略对新布局适应困难。
- 方法要点：采用自适应经验选择关注关键轨迹片段，结合循环状态空间模型进行模型预测前向规划，以想象未来操作动态。
- 实验或效果：在多种配置下显著优于现有方法，并通过真实世界实验验证了可行性与实用性。

## 摘要（原文）

> Mobile Manipulation (MM) involves long-horizon decision-making over multi-stage compositions of heterogeneous skills, such as navigation and picking up objects. Despite recent progress, existing MM methods still face two key limitations: (i) low sample efficiency, due to ineffective use of redundant data generated during long-term MM interactions; and (ii) poor spatial generalization, as policies trained on specific tasks struggle to transfer to new spatial layouts without additional training. In this paper, we address these challenges through Adaptive Experience Selection (AES) and model-based dynamic imagination. In particular, AES makes MM agents pay more attention to critical experience fragments in long trajectories that affect task success, improving skill chain learning and mitigating skill forgetting. Based on AES, a Recurrent State-Space Model (RSSM) is introduced for Model-Predictive Forward Planning (MPFP) by capturing the coupled dynamics between the mobile base and the manipulator and imagining the dynamics of future manipulations. RSSM-based MPFP can reinforce MM skill learning on the current task while enabling effective generalization to new spatial layouts. Comparative studies across different experimental configurations demonstrate that our method significantly outperforms existing MM policies. Real-world experiments further validate the feasibility and practicality of our method.

