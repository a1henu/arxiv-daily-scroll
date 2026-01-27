---
layout: default
title: Reflect: Transparent Principle-Guided Reasoning for Constitutional Alignment at Scale
---

# Reflect: Transparent Principle-Guided Reasoning for Constitutional Alignment at Scale
**arXiv**：[2601.18730v1](https://arxiv.org/abs/2601.18730) · [PDF](https://arxiv.org/pdf/2601.18730.pdf)  
**作者**：Henry Bell, Caroline Zhang, Mohammed Mobasserul Haque, Dhaval Potdar, Samia Zaman, Brandon Fain  

**一句话要点**：提出Reflect框架，通过推理时原则引导实现大语言模型宪法对齐，无需训练或数据。

**关键词**：宪法对齐, 推理时对齐, 上下文推理, 自我评估, 原则引导, 大语言模型

## 3 点简述
- 核心问题：传统参数微调方法计算成本高、需人工标注，难以灵活对齐复杂原则。
- 方法要点：基于上下文推理，结合基础响应、自我评估、自我批判和最终修订步骤。
- 实验或效果：显著提升模型对多样原则的遵循，减少罕见违规，并生成有用训练数据。

## 摘要（原文）

> The constitutional framework of alignment aims to align large language models (LLMs) with value-laden principles written in natural language (such as to avoid using biased language). Prior work has focused on parameter fine-tuning techniques, such as reinforcement learning from human feedback (RLHF), to instill these principles. However, these approaches are computationally demanding, require careful engineering and tuning, and often require difficult-to-obtain human annotation data. We propose \textsc{reflect}, an inference-time framework for constitutional alignment that does not require any training or data, providing a plug-and-play approach for aligning an instruction-tuned model to a set of principles. \textsc{reflect} operates entirely in-context, combining a (i) constitution-conditioned base response with post-generation (ii) self-evaluation, (iii)(a) self-critique, and (iii)(b) final revision. \textsc{reflect}'s technique of explicit in-context reasoning over principles during post-generation outperforms standard few-shot prompting and provides transparent reasoning traces. Our results demonstrate that \textsc{reflect} significantly improves LLM conformance to diverse and complex principles, including principles quite distinct from those emphasized in the model's original parameter fine-tuning, without sacrificing factual reasoning. \textsc{reflect} is particularly effective at reducing the rate of rare but significant violations of principles, thereby improving safety and robustness in the tail end of the distribution of generations. Finally, we show that \textsc{reflect} naturally generates useful training data for traditional parameter fine-tuning techniques, allowing for efficient scaling and the reduction of inference-time computational overhead in long-term deployment scenarios.

