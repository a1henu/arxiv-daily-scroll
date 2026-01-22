---
layout: default
title: Rethinking Reinforcement fine-tuning of LLMs: A Multi-armed Bandit Learning Perspective
---

# Rethinking Reinforcement fine-tuning of LLMs: A Multi-armed Bandit Learning Perspective
**arXiv**：[2601.14599v1](https://arxiv.org/abs/2601.14599) · [PDF](https://arxiv.org/pdf/2601.14599.pdf)  
**作者**：Xiao Hu, Hong Xie, Tao Tan, Defu Lian, Jianyu Han  

**一句话要点**：提出基于多臂老虎机视角的LLM强化微调实验框架，以厘清优化选择的作用与瓶颈。

**关键词**：强化学习微调, 多臂老虎机, 大语言模型, 实验设计, 优化选择分析

## 3 点简述
- 核心问题：LLM强化微调中优化选择的作用与瓶颈缺乏清晰理解，存在混杂因素干扰。
- 方法要点：采用自底向上实验流程，从极简配置出发，逐步扩展以检验设计选择，并关联多臂老虎机理论。
- 实验或效果：在三个LLM和两个推理数据集上实验，揭示新理解并提供领域塑造的关键洞见。

## 摘要（原文）

> A large number of heuristics have been proposed to optimize the reinforcement fine-tuning of LLMs. However, inconsistent claims are made from time to time, making this area elusive. Reflecting on this situation, two fundamental questions still lack a clear understanding: 1) what is the role of each optimizing choice? 2) which ones are the bottlenecks? This paper aims to shed light on them, and it faces the challenge of several entangled confounding factors in the fine-tuning process. To tackle this challenge, we propose a bottom-up experiment pipeline. The bottom layer is composed of a minimalist configuration: one training data, one rollout per round and the reward directly serve as the learning signal without advantage function design. This minimalist configuration connects to multi-armed bandit learning with extremely large discrete action space, which offers theories to corroborate the experiment findings. The up procedure of the experiment pipeline expanding the minimalist configuration layer by layer, examining the role of each design choice. Experimental results on three LLMs and two reasoning datasets not only reveal new understanding of the design choice but also yield essential insights to shape the area.

