---
layout: default
title: Efficient RLVR Training via Weighted Mutual Information Data Selection
---

# Efficient RLVR Training via Weighted Mutual Information Data Selection
**arXiv**：[2603.01907v1](https://arxiv.org/abs/2603.01907) · [PDF](https://arxiv.org/pdf/2603.01907.pdf)  
**作者**：Xinyu Zhou, Boyu Zhu, Haotian Zhang, Huiming Wang, Zhijiang Guo  

**一句话要点**：提出InSight方法，基于加权互信息选择数据，提升强化学习训练效率。

**关键词**：强化学习训练, 数据选择策略, 加权互信息, 贝叶斯建模, 训练效率优化

## 3 点简述
- 现有在线数据选择策略依赖难度启发式，忽视认知不确定性。
- InSight通过贝叶斯潜在成功率建模，分解不确定性为难度和证据依赖成分。
- 实验显示InSight在推理基准上提升性能，加速训练达2.2倍。

## 摘要（原文）

> Reinforcement learning (RL) plays a central role in improving the reasoning and alignment of large language models, yet its efficiency critically depends on how training data are selected. Existing online selection strategies predominantly rely on difficulty-based heuristics, favouring datapoints with intermediate success rates, implicitly equating difficulty with informativeness and neglecting epistemic uncertainty arising from limited evidence. We introduce InSight, an INformation-guided data SamplInG metHod for RL Training, grounded in a weighted mutual information objective. By modeling data outcomes with Bayesian latent success rates, we show that expected uncertainty reduction decomposes into complementary difficulty- and evidence-dependent components, revealing a fundamental limitation of difficulty-only selection. Leveraging this observation, InSight constructs a stable acquisition score based on the mean belief of datapoints' success rather than noisy sampled outcomes, and naturally extends to multi-rollout settings common in reinforcement learning with verifiable rewards (RLVR). Extensive experiments demonstrate that InSight consistently achieves state-of-the-art performance and improves training efficiency, including a +1.41 average gain on Planning & Mathmatics benchmarks, +1.01 improvement on general reasoning, and up to ~2.2x acceleration, with negligible additional computational overhead.

