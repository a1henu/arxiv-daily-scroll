---
layout: default
title: LexiSafe: Offline Safe Reinforcement Learning with Lexicographic Safety-Reward Hierarchy
---

# LexiSafe: Offline Safe Reinforcement Learning with Lexicographic Safety-Reward Hierarchy
**arXiv**：[2602.17312v1](https://arxiv.org/abs/2602.17312) · [PDF](https://arxiv.org/pdf/2602.17312.pdf)  
**作者**：Hsin-Jung Yang, Zhanhong Jiang, Prajwal Koirala, Qisai Liu, Cody Fleming, Soumik Sarkar  

**一句话要点**：提出LexiSafe离线安全强化学习框架，通过字典序优先级处理安全-奖励层次，用于安全关键系统决策。

**关键词**：离线强化学习, 安全强化学习, 字典序优化, 样本复杂度分析, 安全关键系统

## 3 点简述
- 核心问题：离线安全强化学习中缺乏结构机制防止安全漂移，现有方法平衡奖励-安全权衡但效果有限。
- 方法要点：开发LexiSafe-SC单成本公式和LexiSafe-MC多成本扩展，基于字典序优先级确保安全对齐行为，并提供样本复杂度保证。
- 实验或效果：相比基线方法，LexiSafe在实验中减少安全违规并提升任务性能，适用于安全关键系统。

## 摘要（原文）

> Offline safe reinforcement learning (RL) is increasingly important for cyber-physical systems (CPS), where safety violations during training are unacceptable and only pre-collected data are available. Existing offline safe RL methods typically balance reward-safety tradeoffs through constraint relaxation or joint optimization, but they often lack structural mechanisms to prevent safety drift. We propose LexiSafe, a lexicographic offline RL framework designed to preserve safety-aligned behavior. We first develop LexiSafe-SC, a single-cost formulation for standard offline safe RL, and derive safety-violation and performance-suboptimality bounds that together yield sample-complexity guarantees. We then extend the framework to hierarchical safety requirements with LexiSafe-MC, which supports multiple safety costs and admits its own sample-complexity analysis. Empirically, LexiSafe demonstrates reduced safety violations and improved task performance compared to constrained offline baselines. By unifying lexicographic prioritization with structural bias, LexiSafe offers a practical and theoretically grounded approach for safety-critical CPS decision-making.

