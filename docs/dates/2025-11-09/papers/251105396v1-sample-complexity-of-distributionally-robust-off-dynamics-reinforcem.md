---
layout: default
title: Sample Complexity of Distributionally Robust Off-Dynamics Reinforcement Learning with Online Interaction
---

# Sample Complexity of Distributionally Robust Off-Dynamics Reinforcement Learning with Online Interaction
**arXiv**：[2511.05396v1](https://arxiv.org/abs/2511.05396) · [PDF](https://arxiv.org/pdf/2511.05396.pdf)  
**作者**：Yiting He, Zhishuai Liu, Weixin Wang, Pan Xu  

**一句话要点**：提出在线算法以解决训练与部署动态不匹配的强化学习问题

**关键词**：分布鲁棒强化学习, 在线学习, 样本复杂度, 上确界访问比, 次线性遗憾, 动态不匹配

## 3 点简述
- 核心问题：在线交互中训练与部署动态不匹配导致探索困难
- 方法要点：引入上确界访问比并设计高效算法实现次线性遗憾
- 实验或效果：数值实验验证理论结果，算法达到最优遗憾界

## 摘要（原文）

> Off-dynamics reinforcement learning (RL), where training and deployment
> transition dynamics are different, can be formulated as learning in a robust
> Markov decision process (RMDP) where uncertainties in transition dynamics are
> imposed. Existing literature mostly assumes access to generative models
> allowing arbitrary state-action queries or pre-collected datasets with a good
> state coverage of the deployment environment, bypassing the challenge of
> exploration. In this work, we study a more realistic and challenging setting
> where the agent is limited to online interaction with the training environment.
> To capture the intrinsic difficulty of exploration in online RMDPs, we
> introduce the supremal visitation ratio, a novel quantity that measures the
> mismatch between the training dynamics and the deployment dynamics. We show
> that if this ratio is unbounded, online learning becomes exponentially hard. We
> propose the first computationally efficient algorithm that achieves sublinear
> regret in online RMDPs with $f$-divergence based transition uncertainties. We
> also establish matching regret lower bounds, demonstrating that our algorithm
> achieves optimal dependence on both the supremal visitation ratio and the
> number of interaction episodes. Finally, we validate our theoretical results
> through comprehensive numerical experiments.

