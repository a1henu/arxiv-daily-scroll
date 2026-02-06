---
layout: default
title: When Are RL Hyperparameters Benign? A Study in Offline Goal-Conditioned RL
---

# When Are RL Hyperparameters Benign? A Study in Offline Goal-Conditioned RL
**arXiv**：[2602.05459v1](https://arxiv.org/abs/2602.05459) · [PDF](https://arxiv.org/pdf/2602.05459.pdf)  
**作者**：Jan Malte Töpperwien, Aditya Mohan, Marius Lindauer  

**一句话要点**：研究离线目标条件强化学习中超参数敏感性，揭示自举目标加剧敏感性并提供诊断方法。

**关键词**：离线强化学习, 目标条件强化学习, 超参数敏感性, 自举学习, 梯度对齐, 鲁棒性分析

## 3 点简述
- 核心问题：深度强化学习超参数敏感性是否不可避免，还是由特定训练机制加剧。
- 方法要点：在离线目标条件强化学习中，控制数据分布和非平稳性，比较HIQL和QRL算法。
- 实验或效果：发现超参数鲁棒性高于在线强化学习，自举目标导致梯度干扰和敏感性。

## 摘要（原文）

> Hyperparameter sensitivity in Deep Reinforcement Learning (RL) is often accepted as unavoidable. However, it remains unclear whether it is intrinsic to the RL problem or exacerbated by specific training mechanisms. We investigate this question in offline goal-conditioned RL, where data distributions are fixed, and non-stationarity can be explicitly controlled via scheduled shifts in data quality. Additionally, we study varying data qualities under both stationary and non-stationary regimes, and cover two representative algorithms: HIQL (bootstrapped TD-learning) and QRL (quasimetric representation learning). Overall, we observe substantially greater robustness to changes in hyperparameter configurations than commonly reported for online RL, even under controlled non-stationarity. Once modest expert data is present ($\approx$ 20\%), QRL maintains broad, stable near-optimal regions, while HIQL exhibits sharp optima that drift significantly across training phases. To explain this divergence, we introduce an inter-goal gradient alignment diagnostic. We find that bootstrapped objectives exhibit stronger destructive gradient interference, which coincides directly with hyperparameter sensitivity. These results suggest that high sensitivity to changes in hyperparameter configurations during training is not inevitable in RL, but is amplified by the dynamics of bootstrapping, offering a pathway toward more robust algorithmic objective design.

