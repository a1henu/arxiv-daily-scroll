---
layout: default
title: The Trajectory Alignment Coefficient in Two Acts: From Reward Tuning to Reward Learning
---

# The Trajectory Alignment Coefficient in Two Acts: From Reward Tuning to Reward Learning
**arXiv**：[2601.16906v1](https://arxiv.org/abs/2601.16906) · [PDF](https://arxiv.org/pdf/2601.16906.pdf)  
**作者**：Calarina Muslimani, Yunshu Du, Kenta Kawamoto, Kaushik Subramanian, Peter Stone, Peter Wurman  

**一句话要点**：提出轨迹对齐系数以支持奖励函数调优与学习，应用于强化学习任务

**关键词**：强化学习, 奖励函数设计, 轨迹对齐系数, 偏好学习, 可微近似, 人类实验

## 3 点简述
- 核心问题：强化学习中奖励函数设计耗时且易出错，需工具支持调优与学习。
- 方法要点：利用轨迹对齐系数评估奖励函数与专家偏好匹配度，并开发可微近似Soft-TAC用于奖励模型训练。
- 实验或效果：人类实验显示轨迹对齐系数提升调优效果，在赛车模拟器中Soft-TAC训练模型产生更独特行为。

## 摘要（原文）

> The success of reinforcement learning (RL) is fundamentally tied to having a reward function that accurately reflects the task objective. Yet, designing reward functions is notoriously time-consuming and prone to misspecification. To address this issue, our first goal is to understand how to support RL practitioners in specifying appropriate weights for a reward function. We leverage the Trajectory Alignment Coefficient (TAC), a metric that evaluates how closely a reward function's induced preferences match those of a domain expert. To evaluate whether TAC provides effective support in practice, we conducted a human-subject study in which RL practitioners tuned reward weights for Lunar Lander. We found that providing TAC during reward tuning led participants to produce more performant reward functions and report lower cognitive workload relative to standard tuning without TAC. However, the study also underscored that manual reward design, even with TAC, remains labor-intensive. This limitation motivated our second goal: to learn a reward model that maximizes TAC directly. Specifically, we propose Soft-TAC, a differentiable approximation of TAC that can be used as a loss function to train reward models from human preference data. Validated in the racing simulator Gran Turismo 7, reward models trained using Soft-TAC successfully captured preference-specific objectives, resulting in policies with qualitatively more distinct behaviors than models trained with standard Cross-Entropy loss. This work demonstrates that TAC can serve as both a practical tool for guiding reward tuning and a reward learning objective in complex domains.

