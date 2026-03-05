---
layout: default
title: SaFeR: Safety-Critical Scenario Generation for Autonomous Driving Test via Feasibility-Constrained Token Resampling
---

# SaFeR: Safety-Critical Scenario Generation for Autonomous Driving Test via Feasibility-Constrained Token Resampling
**arXiv**：[2603.04071v1](https://arxiv.org/abs/2603.04071) · [PDF](https://arxiv.org/pdf/2603.04071.pdf)  
**作者**：Jinlong Cui, Fenghua Liang, Guo Yang, Chengcheng Tang, Jianxun Cui  

**一句话要点**：提出SaFeR方法，通过可行性约束令牌重采样生成自动驾驶安全关键场景

**关键词**：自动驾驶测试, 安全关键场景生成, 令牌重采样, 可行性约束, 差分注意力机制, 离线强化学习

## 3 点简述
- 核心问题：现有方法难以平衡对抗关键性、物理可行性和行为真实性
- 方法要点：基于Transformer的真实性先验结合差分注意力机制，通过可行性约束重采样策略诱导对抗行为
- 实验或效果：在Waymo和nuPlan数据集上，SaFeR在解决方案率和运动学真实性方面优于基线，保持强对抗效果

## 摘要（原文）

> Safety-critical scenario generation is crucial for evaluating autonomous driving systems. However, existing approaches often struggle to balance three conflicting objectives: adversarial criticality, physical feasibility, and behavioral realism. To bridge this gap, we propose SaFeR: safety-critical scenario generation for autonomous driving test via feasibility-constrained token resampling. We first formulate traffic generation as a discrete next token prediction problem, employing a Transformer-based model as a realism prior to capture naturalistic driving distributions. To capture complex interactions while effectively mitigating attention noise, we propose a novel differential attention mechanism within the realism prior. Building on this prior, SaFeR implements a novel resampling strategy that induces adversarial behaviors within a high-probability trust region to maintain naturalism, while enforcing a feasibility constraint derived from the Largest Feasible Region (LFR). By approximating the LFR via offline reinforcement learning, SaFeR effectively prevents the generation of theoretically inevitable collisions. Closed-loop experiments on the Waymo Open Motion Dataset and nuPlan demonstrate that SaFeR significantly outperforms state-of-the-art baselines, achieving a higher solution rate and superior kinematic realism while maintaining strong adversarial effectiveness.

