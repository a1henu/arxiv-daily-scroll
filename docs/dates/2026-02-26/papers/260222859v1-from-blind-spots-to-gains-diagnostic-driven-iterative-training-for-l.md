---
layout: default
title: From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models
---

# From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models
**arXiv**：[2602.22859v1](https://arxiv.org/abs/2602.22859) · [PDF](https://arxiv.org/pdf/2602.22859.pdf)  
**作者**：Hongrui Jia, Chaoya Jiang, Shikun Zhang, Wei Ye  

**一句话要点**：提出诊断驱动渐进演化（DPE）以解决大型多模态模型训练中能力盲点难以诊断和动态强化的问题。

**关键词**：大型多模态模型, 诊断驱动训练, 迭代强化学习, 多模态数据生成, 能力盲点诊断, 开放任务分布

## 3 点简述
- 核心问题：大型多模态模型训练依赖静态数据和固定方法，难以诊断能力盲点或进行动态针对性强化。
- 方法要点：DPE采用螺旋循环，通过诊断指导数据生成和强化，迭代更新模型以驱动下一轮针对性改进。
- 实验或效果：在Qwen3-VL-8B-Instruct和Qwen2.5-VL-7B-Instruct上，DPE在11个基准测试中实现稳定持续提升。

## 摘要（原文）

> As Large Multimodal Models (LMMs) scale up and reinforcement learning (RL) methods mature, LMMs have made notable progress in complex reasoning and decision making. Yet training still relies on static data and fixed recipes, making it difficult to diagnose capability blind spots or provide dynamic, targeted reinforcement. Motivated by findings that test driven error exposure and feedback based correction outperform repetitive practice, we propose Diagnostic-driven Progressive Evolution (DPE), a spiral loop where diagnosis steers data generation and reinforcement, and each iteration re-diagnoses the updated model to drive the next round of targeted improvement. DPE has two key components. First, multiple agents annotate and quality control massive unlabeled multimodal data, using tools such as web search and image editing to produce diverse, realistic samples. Second, DPE attributes failures to specific weaknesses, dynamically adjusts the data mixture, and guides agents to generate weakness focused data for targeted reinforcement. Experiments on Qwen3-VL-8B-Instruct and Qwen2.5-VL-7B-Instruct show stable, continual gains across eleven benchmarks, indicating DPE as a scalable paradigm for continual LMM training under open task distributions. Our code, models, and data are publicly available at https://github.com/hongruijia/DPE.

