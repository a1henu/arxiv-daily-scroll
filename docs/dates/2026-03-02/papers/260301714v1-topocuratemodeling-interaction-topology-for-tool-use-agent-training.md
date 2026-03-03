---
layout: default
title: TopoCurate:Modeling Interaction Topology for Tool-Use Agent Training
---

# TopoCurate:Modeling Interaction Topology for Tool-Use Agent Training
**arXiv**：[2603.01714v1](https://arxiv.org/abs/2603.01714) · [PDF](https://arxiv.org/pdf/2603.01714.pdf)  
**作者**：Jinluan Yang, Yuxin Liu, Zhengyu Chen, Chengcheng Han, Yueqing Sun, Qi Gu, Hui Su, Xunliang Cai, Fei Wu, Kun Kuang  

**一句话要点**：提出TopoCurate框架，通过交互拓扑建模提升工具使用代理的训练效果

**关键词**：工具使用代理, 交互拓扑建模, 监督微调, 强化学习, 语义商拓扑, 双选择机制

## 3 点简述
- 核心问题：传统基于结果的训练忽略交互动态，导致轨迹冗余和任务选择偏差
- 方法要点：将多轮试验投影到语义商拓扑，基于双选择机制优化SFT和RL训练
- 实验或效果：在BFCLv3和Tau2 Bench上，SFT和RL分别提升4.2%和6.9%

## 摘要（原文）

> Training tool-use agents typically relies on outcome-based filtering: Supervised Fine-Tuning (SFT) on successful trajectories and Reinforcement Learning (RL) on pass-rate-selected tasks. However, this paradigm ignores interaction dynamics: successful trajectories may lack error recovery or exhibit redundancy, while pass rates fail to distinguish structurally informative tasks from trivial ones. We propose \textbf{TopoCurate}, an interaction-aware framework that projects multi-trial rollouts from the same task into a unified semantic quotient topology. By merging equivalent action-observation states, this projection transforms scattered linear trajectories into a structured manifold that explicitly captures how tool invocations and environmental responses drive the divergence between effective strategies and failure modes. Leveraging this representation, we introduce a dual-selection mechanism: for SFT, we prioritize trajectories demonstrating reflective recovery, semantic efficiency, and strategic diversity to mitigate covariate shift and mode collapse; for RL, we select tasks with high error branch ratios and strategic heterogeneity, maximizing gradient Signal-to-Noise Ratio to address vanishing signals in sparse-reward settings. Evaluations on BFCLv3 and Tau2 Bench show that TopoCurate achieves consistent gains of 4.2\% (SFT) and 6.9\% (RL) over state-of-the-art baselines. We will release the code and data soon for further investigations.

