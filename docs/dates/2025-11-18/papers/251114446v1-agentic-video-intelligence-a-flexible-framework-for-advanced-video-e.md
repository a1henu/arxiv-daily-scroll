---
layout: default
title: Agentic Video Intelligence: A Flexible Framework for Advanced Video Exploration and Understanding
---

# Agentic Video Intelligence: A Flexible Framework for Advanced Video Exploration and Understanding
**arXiv**：[2511.14446v1](https://arxiv.org/abs/2511.14446) · [PDF](https://arxiv.org/pdf/2511.14446.pdf)  
**作者**：Hong Gao, Yiming Bao, Xuezhen Tu, Yutong Xu, Yue Jin, Yiyang Mu, Bin Zhong, Linan Yue, Min-Ling Zhang  

**一句话要点**：提出Agentic Video Intelligence框架，通过免训练设计解决视频理解中的迭代推理问题

**关键词**：视频理解, 智能体框架, 免训练方法, 多粒度工具, 开源模型集成, 可解释性

## 3 点简述
- 核心问题：现有视频理解方法缺乏证据重访和迭代优化，依赖昂贵模型或强化学习
- 方法要点：引入三阶段推理过程、结构化知识库和开源模型集成，实现灵活视频探索
- 实验效果：在多个基准测试中达到竞争性能，并提供高可解释性

## 摘要（原文）

> Video understanding requires not only visual recognition but also complex reasoning. While Vision-Language Models (VLMs) demonstrate impressive capabilities, they typically process videos largely in a single-pass manner with limited support for evidence revisit and iterative refinement. While recently emerging agent-based methods enable long-horizon reasoning, they either depend heavily on expensive proprietary models or require extensive agentic RL training. To overcome these limitations, we propose Agentic Video Intelligence (AVI), a flexible and training-free framework that can mirror human video comprehension through system-level design and optimization. AVI introduces three key innovations: (1) a human-inspired three-phase reasoning process (Retrieve-Perceive-Review) that ensures both sufficient global exploration and focused local analysis, (2) a structured video knowledge base organized through entity graphs, along with multi-granularity integrated tools, constituting the agent's interaction environment, and (3) an open-source model ensemble combining reasoning LLMs with lightweight base CV models and VLM, eliminating dependence on proprietary APIs or RL training. Experiments on LVBench, VideoMME-Long, LongVideoBench, and Charades-STA demonstrate that AVI achieves competitive performance while offering superior interpretability.

