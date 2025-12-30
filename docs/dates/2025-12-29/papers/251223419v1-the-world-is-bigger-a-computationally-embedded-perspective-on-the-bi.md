---
layout: default
title: The World Is Bigger! A Computationally-Embedded Perspective on the Big World Hypothesis
---

# The World Is Bigger! A Computationally-Embedded Perspective on the Big World Hypothesis
**arXiv**：[2512.23419v1](https://arxiv.org/abs/2512.23419) · [PDF](https://arxiv.org/pdf/2512.23419.pdf)  
**作者**：Alex Lewandowski, Adtiya A. Ramesh, Edan Meyer, Dale Schuurmans, Marlos C. Machado  

**一句话要点**：提出计算嵌入视角与交互性目标，以评估智能体在无限状态空间中的持续学习能力。

**关键词**：持续学习, 计算嵌入视角, 交互性目标, 部分可观测马尔可夫决策过程, 模型强化学习, 深度网络评估

## 3 点简述
- 核心问题：传统持续学习基于显式约束，可能限制智能体容量扩展，需更自然约束框架。
- 方法要点：引入计算嵌入视角，将智能体建模为通用计算机中的自动机，证明其等价于部分可观测马尔可夫决策过程。
- 实验或效果：开发基于模型的强化学习算法，构建合成问题评估，发现深度非线性网络交互性低，线性网络随容量增加交互性高。

## 摘要（原文）

> Continual learning is often motivated by the idea, known as the big world hypothesis, that "the world is bigger" than the agent. Recent problem formulations capture this idea by explicitly constraining an agent relative to the environment. These constraints lead to solutions in which the agent continually adapts to best use its limited capacity, rather than converging to a fixed solution. However, explicit constraints can be ad hoc, difficult to incorporate, and may limit the effectiveness of scaling up the agent's capacity. In this paper, we characterize a problem setting in which an agent, regardless of its capacity, is constrained by being embedded in the environment. In particular, we introduce a computationally-embedded perspective that represents an embedded agent as an automaton simulated within a universal (formal) computer. Such an automaton is always constrained; we prove that it is equivalent to an agent that interacts with a partially observable Markov decision process over a countably infinite state-space. We propose an objective for this setting, which we call interactivity, that measures an agent's ability to continually adapt its behaviour by learning new predictions. We then develop a model-based reinforcement learning algorithm for interactivity-seeking, and use it to construct a synthetic problem to evaluate continual learning capability. Our results show that deep nonlinear networks struggle to sustain interactivity, whereas deep linear networks sustain higher interactivity as capacity increases.

