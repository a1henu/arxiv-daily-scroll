---
layout: default
title: MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning
---

# MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning
**arXiv**：[2603.09892v1](https://arxiv.org/abs/2603.09892) · [PDF](https://arxiv.org/pdf/2603.09892.pdf)  
**作者**：Yiyang Lu, Yu He, Jianlong Chen, Hongyuan Zha  

**一句话要点**：提出MSSR框架，通过自适应回放缓解大语言模型持续微调中的灾难性遗忘问题。

**关键词**：持续学习, 灾难性遗忘, 经验回放, 大语言模型微调, 自适应调度

## 3 点简述
- 核心问题：大语言模型持续微调时易发生灾难性遗忘，现有回放策略效果有限或计算开销大。
- 方法要点：基于记忆强度估计和自适应调度回放，平衡遗忘缓解与快速适应。
- 实验或效果：在三个骨干模型和11个序列任务上超越先进基线，尤其在推理密集型任务表现突出。

## 摘要（原文）

> Continual fine-tuning of large language models (LLMs) is becoming increasingly crucial as these models are deployed in dynamic environments where tasks and data distributions evolve over time. While strong adaptability enables rapid acquisition of new knowledge, it also exposes LLMs to catastrophic forgetting, where previously learned skills degrade during sequential training. Existing replay-based strategies, such as fixed interleaved replay, accuracy-supervised, and loss-driven scheduling, remain limited: some depend on heuristic rules and provide only partial mitigation of forgetting, while others improve performance but incur substantial computational overhead. Motivated by retention dynamics under sequential fine-tuning, we propose Memory-Inspired Sampler and Scheduler Replay (MSSR), an experience replay framework that estimates sample-level memory strength and schedules rehearsal at adaptive intervals to mitigate catastrophic forgetting while maintaining fast adaptation. Extensive experiments across three backbone models and 11 sequential tasks show that MSSR consistently outperforms state-of-the-art replay baselines, with particularly strong gains on reasoning-intensive and multiple-choice benchmarks.

