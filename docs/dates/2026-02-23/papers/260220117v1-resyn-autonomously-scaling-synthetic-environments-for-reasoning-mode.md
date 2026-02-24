---
layout: default
title: ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models
---

# ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models
**arXiv**：[2602.20117v1](https://arxiv.org/abs/2602.20117) · [PDF](https://arxiv.org/pdf/2602.20117.pdf)  
**作者**：Andre He, Nathaniel Weir, Kaj Bostrom, Allen Nie, Darion Cassel, Sam Bayless, Huzefa Rangwala  

**一句话要点**：提出ReSyn以规模化生成推理环境，增强推理语言模型的训练效果

**关键词**：推理语言模型, 强化学习, 合成环境生成, 验证器监督, 任务多样性, 基准测试

## 3 点简述
- 核心问题：现有合成数据生成方法以解决方案为中心，基于验证器的方法依赖少量手工环境，限制了推理语言模型的训练规模。
- 方法要点：引入ReSyn管道，自动生成多样推理环境，包括约束满足、算法谜题和空间推理任务，配备实例生成器和验证器。
- 实验或效果：使用ReSyn数据通过强化学习训练Qwen2.5-7B-Instruct模型，在推理和数学基准测试中取得一致提升，包括BBEH基准相对改进27%。

## 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has emerged as a promising approach for training reasoning language models (RLMs) by leveraging supervision from verifiers. Although verifier implementation is easier than solution annotation for many tasks, existing synthetic data generation methods remain largely solution-centric, while verifier-based methods rely on a few hand-crafted procedural environments. In this work, we scale RLVR by introducing ReSyn, a pipeline that generates diverse reasoning environments equipped with instance generators and verifiers, covering tasks such as constraint satisfaction, algorithmic puzzles, and spatial reasoning. A Qwen2.5-7B-Instruct model trained with RL on ReSyn data achieves consistent gains across reasoning benchmarks and out-of-domain math benchmarks, including a 27\% relative improvement on the challenging BBEH benchmark. Ablations show that verifier-based supervision and increased task diversity both contribute significantly, providing empirical evidence that generating reasoning environments at scale can enhance reasoning abilities in RLMs

