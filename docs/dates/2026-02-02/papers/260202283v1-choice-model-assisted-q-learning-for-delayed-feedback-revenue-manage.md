---
layout: default
title: Choice-Model-Assisted Q-learning for Delayed-Feedback Revenue Management
---

# Choice-Model-Assisted Q-learning for Delayed-Feedback Revenue Management
**arXiv**：[2602.02283v1](https://arxiv.org/abs/2602.02283) · [PDF](https://arxiv.org/pdf/2602.02283.pdf)  
**作者**：Owen Shen, Patrick Jaillet  

**一句话要点**：提出选择模型辅助Q学习以解决延迟反馈收益管理问题

**关键词**：延迟反馈收益管理, 强化学习, 离散选择模型, Q学习, 鲁棒性分析

## 3 点简述
- 研究延迟反馈收益管理中的强化学习，客户取消和修改导致价值延迟确定
- 使用校准离散选择模型作为固定部分世界模型，在决策时估算学习目标的延迟部分
- 实验显示在参数偏移下提升鲁棒性，但在结构误设时导致收益下降

## 摘要（原文）

> We study reinforcement learning for revenue management with delayed feedback, where a substantial fraction of value is determined by customer cancellations and modifications observed days after booking. We propose \emph{choice-model-assisted RL}: a calibrated discrete choice model is used as a fixed partial world model to impute the delayed component of the learning target at decision time. In the fixed-model deployment regime, we prove that tabular Q-learning with model-imputed targets converges to an $O(\varepsilon/(1-γ))$ neighborhood of the optimal Q-function, where $\varepsilon$ summarizes partial-model error, with an additional $O(t^{-1/2})$ sampling term. Experiments in a simulator calibrated from 61{,}619 hotel bookings (1{,}088 independent runs) show: (i) no statistically detectable difference from a maturity-buffer DQN baseline in stationary settings; (ii) positive effects under in-family parameter shifts, with significant gains in 5 of 10 shift scenarios after Holm--Bonferroni correction (up to 12.4\%); and (iii) consistent degradation under structural misspecification, where the choice model assumptions are violated (1.4--2.6\% lower revenue). These results characterize when partial behavioral models improve robustness under shift and when they introduce harmful bias.

