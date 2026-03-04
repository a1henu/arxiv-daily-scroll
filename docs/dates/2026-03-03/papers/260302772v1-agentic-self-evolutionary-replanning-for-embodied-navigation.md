---
layout: default
title: Agentic Self-Evolutionary Replanning for Embodied Navigation
---

# Agentic Self-Evolutionary Replanning for Embodied Navigation
**arXiv**：[2603.02772v1](https://arxiv.org/abs/2603.02772) · [PDF](https://arxiv.org/pdf/2603.02772.pdf)  
**作者**：Guoliang Li, Ruihua Han, Chengyang Li, He Li, Shuai Wang, Wenchao Ding, Hong Zhang, Chengzhong Xu  

**一句话要点**：提出SERP方法，通过运行时学习和自适应模型进化，提升具身导航在复杂环境中的鲁棒性和效率。

**关键词**：具身导航, 重规划, 模型进化, 上下文学习, 图链式思维, 大语言模型推理

## 3 点简述
- 核心问题：现有具身导航重规划方法冻结动作模型，无法通过升级机器人自身探索更优计划。
- 方法要点：引入SERP，结合ILAD实现自适应函数调整和全局参数重置，并采用GCOT进行令牌高效重规划。
- 实验或效果：在模拟和真实世界实验中，SERP在多种基准测试中实现更高成功率且令牌消耗更低。

## 摘要（原文）

> Failure is inevitable for embodied navigation in complex environments. To enhance the resilience, replanning (RP) is a viable option, where the robot is allowed to fail, but is capable of adjusting plan until success. However, existing RP approaches freeze the ego action model and miss the opportunities to explore better plans by upgrading the robot itself. To address this limitation, we propose Self-Evolutionary RePlanning, or SERP for short, which leads to a paradigm shift from frozen models towards evolving models by run-time learning from recent experiences. In contrast to existing model evolution approaches that often get stuck at predefined static parameters, we introduce agentic self-evolving action model that uses in-context learning with auto-differentiation (ILAD) for adaptive function adjustment and global parameter reset. To achieve token-efficient replanning for SERP, we also propose graph chain-of-thought (GCOT) replanning with large language model (LLM) inference over distilled graphs. Extensive simulation and real-world experiments demonstrate that SERP achieves higher success rate with lower token expenditure over various benchmarks, validating its superior robustness and efficiency across diverse environments.

