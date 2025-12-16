---
layout: default
title: ADHint: Adaptive Hints with Difficulty Priors for Reinforcement Learning
---

# ADHint: Adaptive Hints with Difficulty Priors for Reinforcement Learning
**arXiv**：[2512.13095v1](https://arxiv.org/abs/2512.13095) · [PDF](https://arxiv.org/pdf/2512.13095.pdf)  
**作者**：Feng Zhang, Zezhong Tan, Xinhong Ma, Ziqiang Dong, Xi Leng, Jianfei Zhao, Xin Sun, Yang Yang  

**一句话要点**：提出ADHint，通过难度先验和后验优化提示调度与优势估计，以提升强化学习中的推理泛化能力。

**关键词**：强化学习, 提示调度, 难度先验, 梯度调制, 优势估计, 推理泛化

## 3 点简述
- 核心问题：现有基于提示的强化学习方法忽略难度因素，导致学习不稳定和过度模仿。
- 方法要点：引入自适应提示调度、基于一致性的梯度调制和选择性掩码，以及基于难度后验的优势估计。
- 实验或效果：在多模态、多规模和领域实验中，ADHint在推理能力和分布外泛化上优于现有方法。

## 摘要（原文）

> To combine the advantages of Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL), recent methods have integrated ''hints'' into post-training, which are prefix segments of complete reasoning trajectories, aiming for powerful knowledge expansion and reasoning generalization. However, existing hint-based RL methods typically ignore difficulty when scheduling hint ratios and estimating relative advantages, leading to unstable learning and excessive imitation of off-policy hints. In this work, we propose ADHint, which treats difficulty as a key factor in both hint-ratio schedule and relative-advantage estimation to achieve a better trade-off between exploration and imitation. Specifically, we propose Adaptive Hint with Sample Difficulty Prior, which evaluates each sample's difficulty under the policy model and accordingly schedules an appropriate hint ratio to guide its rollouts. We also introduce Consistency-based Gradient Modulation and Selective Masking for Hint Preservation to modulate token-level gradients within hints, preventing biased and destructive updates. Additionally, we propose Advantage Estimation with Rollout Difficulty Posterior, which leverages the relative difficulty of rollouts with and without hints to estimate their respective advantages, thereby achieving more balanced updates. Extensive experiments across diverse modalities, model scales, and domains demonstrate that ADHint delivers superior reasoning ability and out-of-distribution generalization, consistently surpassing existing methods in both pass@1 and avg@8. Our code and dataset will be made publicly available upon paper acceptance.

