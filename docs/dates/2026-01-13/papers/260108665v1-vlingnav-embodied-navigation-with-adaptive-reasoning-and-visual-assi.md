---
layout: default
title: VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory
---

# VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory
**arXiv**：[2601.08665v1](https://arxiv.org/abs/2601.08665) · [PDF](https://arxiv.org/pdf/2601.08665.pdf)  
**作者**：Shaoan Wang, Yuanfei Luo, Xingyu Chen, Aocheng Luo, Dongyue Li, Chang Liu, Sheng Chen, Yangang Zhang, Junzhi Yu  

**一句话要点**：提出VLingNav模型，通过自适应推理和视觉辅助语言记忆解决具身导航中的复杂长程任务。

**关键词**：具身导航, 视觉语言模型, 自适应推理, 语言记忆, 强化学习, 零样本迁移

## 3 点简述
- 现有VLA模型依赖反应式映射，缺乏显式推理和持久记忆能力。
- 引入自适应思维链机制和视觉辅助语言记忆模块，实现动态推理和跨模态语义记忆。
- 在多个基准测试中达到最优性能，并零样本迁移到真实机器人平台。

## 摘要（原文）

> VLA models have shown promising potential in embodied navigation by unifying perception and planning while inheriting the strong generalization abilities of large VLMs. However, most existing VLA models rely on reactive mappings directly from observations to actions, lacking the explicit reasoning capabilities and persistent memory required for complex, long-horizon navigation tasks. To address these challenges, we propose VLingNav, a VLA model for embodied navigation grounded in linguistic-driven cognition. First, inspired by the dual-process theory of human cognition, we introduce an adaptive chain-of-thought mechanism, which dynamically triggers explicit reasoning only when necessary, enabling the agent to fluidly switch between fast, intuitive execution and slow, deliberate planning. Second, to handle long-horizon spatial dependencies, we develop a visual-assisted linguistic memory module that constructs a persistent, cross-modal semantic memory, enabling the agent to recall past observations to prevent repetitive exploration and infer movement trends for dynamic environments. For the training recipe, we construct Nav-AdaCoT-2.9M, the largest embodied navigation dataset with reasoning annotations to date, enriched with adaptive CoT annotations that induce a reasoning paradigm capable of adjusting both when to think and what to think about. Moreover, we incorporate an online expert-guided reinforcement learning stage, enabling the model to surpass pure imitation learning and to acquire more robust, self-explored navigation behaviors. Extensive experiments demonstrate that VLingNav achieves state-of-the-art performance across a wide range of embodied navigation benchmarks. Notably, VLingNav transfers to real-world robotic platforms in a zero-shot manner, executing various navigation tasks and demonstrating strong cross-domain and cross-task generalization.

