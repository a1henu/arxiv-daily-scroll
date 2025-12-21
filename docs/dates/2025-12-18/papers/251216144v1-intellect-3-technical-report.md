---
layout: default
title: INTELLECT-3: Technical Report
---

# INTELLECT-3: Technical Report
**arXiv**：[2512.16144v1](https://arxiv.org/abs/2512.16144) · [PDF](https://arxiv.org/pdf/2512.16144.pdf)  
**作者**：Prime Intellect Team, Mika Senghaas, Fares Obeid, Sami Jaghouar, William Brown, Jack Min Ong, Daniel Auras, Matej Sirovatka, Jannik Straube, Andrew Baker, Sebastian Müller, Justus Mattern, Manveer Basra, Aiman Ismail, Dominik Scherm, Cooper Miller, Ameen Patel, Simon Kirsten, Mario Sieg, Christian Reetz, Kemal Erdem, Vincent Weisser, Johannes Hagemann  

**一句话要点**：提出INTELLECT-3模型及prime-rl框架，实现大规模强化学习训练与开源基础设施。

**关键词**：混合专家模型, 大规模强化学习, 开源基础设施, 基准性能, 异步训练, 多轮交互

## 3 点简述
- 核心问题：如何高效训练大规模混合专家模型以提升数学、代码、科学和推理基准性能。
- 方法要点：基于GLM-4.5-Air-Base模型，使用prime-rl框架进行大规模异步强化学习训练，支持多轮交互和工具使用。
- 实验或效果：在106B参数规模下，INTELLECT-3在多个基准上超越更大前沿模型，并开源完整基础设施。

## 摘要（原文）

> We present INTELLECT-3, a 106B-parameter Mixture-of-Experts model (12B active) trained with large-scale reinforcement learning on our end-to-end RL infrastructure stack. INTELLECT-3 achieves state of the art performance for its size across math, code, science and reasoning benchmarks, outperforming many larger frontier models. We open-source the model together with the full infrastructure stack used to create it, including RL frameworks, complete recipe, and a wide collection of environments, built with the verifiers library, for training and evaluation from our Environments Hub community platform. Built for this effort, we introduce prime-rl, an open framework for large-scale asynchronous reinforcement learning, which scales seamlessly from a single node to thousands of GPUs, and is tailored for agentic RL with first-class support for multi-turn interactions and tool use. Using this stack, we run both SFT and RL training on top of the GLM-4.5-Air-Base model, scaling RL training up to 512 H200s with high training efficiency.

