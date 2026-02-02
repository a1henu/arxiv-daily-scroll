---
layout: default
title: Toward IIT-Inspired Consciousness in LLMs: A Reward-Based Learning Framework
---

# Toward IIT-Inspired Consciousness in LLMs: A Reward-Based Learning Framework
**arXiv**：[2601.22786v1](https://arxiv.org/abs/2601.22786) · [PDF](https://arxiv.org/pdf/2601.22786.pdf)  
**作者**：Hamid Reza Akbari, Mohammad Hossein Sameti, Amir M. Mansourian, Mohammad Hossein Rohban, Hossein Sameti  

**一句话要点**：提出基于IIT启发的奖励学习框架，以优化语言模型的文本生成简洁性

**关键词**：集成信息理论, 奖励学习, 语言模型优化, 文本生成, 意识模拟, AGI发展

## 3 点简述
- 核心问题：如何在语言模型中实现类似意识的处理以促进AGI发展，当前模型缺乏意识但表现出相关行为
- 方法要点：基于集成信息理论（IIT）设计奖励函数，量化文本的因果性、连贯性和集成性，通过奖励学习优化模型
- 实验或效果：优化后模型在域外任务中输出长度减少达31%，同时保持与基础模型相当的准确性，并分析了校准和计算扩展影响

## 摘要（原文）

> The pursuit of Artificial General Intelligence (AGI) is a central goal in language model development, in which consciousness-like processing could serve as a key facilitator. While current language models are not conscious, they exhibit behaviors analogous to certain aspects of consciousness. This paper investigates the implementation of a leading theory of consciousness, Integrated Information Theory (IIT), within language models via a reward-based learning paradigm. IIT provides a formal, axiom-based mathematical framework for quantifying consciousness. Drawing inspiration from its core principles, we formulate a novel reward function that quantifies a text's causality, coherence and integration, characteristics associated with conscious processing. Empirically, it is found that optimizing for this IIT-inspired reward leads to more concise text generation. On out of domain tasks, careful tuning achieves up to a 31% reduction in output length while preserving accuracy levels comparable to the base model. In addition to primary task performance, the broader effects of this training methodology on the model's confidence calibration and test-time computational scaling is analyzed. The proposed framework offers significant practical advantages: it is conceptually simple, computationally efficient, requires no external data or auxiliary models, and leverages a general, capability-driven signal rather than task-specific heuristics. Code available at https://github.com/MH-Sameti/LLM_PostTraining.git

