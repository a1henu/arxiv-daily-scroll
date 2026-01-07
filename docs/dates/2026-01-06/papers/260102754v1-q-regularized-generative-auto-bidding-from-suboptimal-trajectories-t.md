---
layout: default
title: Q-Regularized Generative Auto-Bidding: From Suboptimal Trajectories to Optimal Policies
---

# Q-Regularized Generative Auto-Bidding: From Suboptimal Trajectories to Optimal Policies
**arXiv**：[2601.02754v1](https://arxiv.org/abs/2601.02754) · [PDF](https://arxiv.org/pdf/2601.02754.pdf)  
**作者**：Mingming Zhang, Na Li, Zhuang Feiqing, Hongyang Zheng, Jiangbing Zhou, Wang Wuyin, Sheng-jie Sun, XiaoWei Chen, Junxiong Zhu, Lixin Zou, Chenliang Li  

**一句话要点**：提出QGA方法，通过Q值正则化与双重探索解决自动出价中次优轨迹问题

**关键词**：自动出价, 强化学习, 生成模型, Q值正则化, 决策变换器, 双重探索

## 3 点简述
- 核心问题：自动出价依赖强化学习和生成模型，但面临次优轨迹和超参数调优困难
- 方法要点：在决策变换器中集成Q值正则化与双重Q学习，结合策略模仿与动作价值最大化
- 实验或效果：在公开基准和模拟环境中表现优异，真实A/B测试提升广告GMV 3.27%和ROI 2.49%

## 摘要（原文）

> With the rapid development of e-commerce, auto-bidding has become a key asset in optimizing advertising performance under diverse advertiser environments. The current approaches focus on reinforcement learning (RL) and generative models. These efforts imitate offline historical behaviors by utilizing a complex structure with expensive hyperparameter tuning. The suboptimal trajectories further exacerbate the difficulty of policy learning.
>   To address these challenges, we proposes QGA, a novel Q-value regularized Generative Auto-bidding method. In QGA, we propose to plug a Q-value regularization with double Q-learning strategy into the Decision Transformer backbone. This design enables joint optimization of policy imitation and action-value maximization, allowing the learned bidding policy to both leverage experience from the dataset and alleviate the adverse impact of the suboptimal trajectories. Furthermore, to safely explore the policy space beyond the data distribution, we propose a Q-value guided dual-exploration mechanism, in which the DT model is conditioned on multiple return-to-go targets and locally perturbed actions. This entire exploration process is dynamically guided by the aforementioned Q-value module, which provides principled evaluation for each candidate action. Experiments on public benchmarks and simulation environments demonstrate that QGA consistently achieves superior or highly competitive results compared to existing alternatives. Notably, in large-scale real-world A/B testing, QGA achieves a 3.27% increase in Ad GMV and a 2.49% improvement in Ad ROI.

