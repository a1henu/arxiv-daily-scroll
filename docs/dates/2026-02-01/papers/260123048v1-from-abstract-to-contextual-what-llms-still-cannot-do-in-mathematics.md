---
layout: default
title: From Abstract to Contextual: What LLMs Still Cannot Do in Mathematics
---

# From Abstract to Contextual: What LLMs Still Cannot Do in Mathematics
**arXiv**：[2601.23048v1](https://arxiv.org/abs/2601.23048) · [PDF](https://arxiv.org/pdf/2601.23048.pdf)  
**作者**：Bowen Cao, Dongdong Zhang, Yixia Li, Junpeng Liu, Shijue Huang, Chufan Shi, Hongyuan Lu, Yaokang Wu, Guanhua Chen, Wai Lam, Furu Wei  

**一句话要点**：提出ContextMATH基准以评估LLMs在上下文数学推理中的表现，揭示其瓶颈。

**关键词**：上下文数学推理, 基准评估, 问题表述错误, 模型规模效应, 微调策略, LLMs瓶颈

## 3 点简述
- 核心问题：LLMs在基准数学问题表现优异，但在真实世界上下文场景中性能显著下降。
- 方法要点：引入ContextMATH基准，将抽象问题转化为场景接地和复杂度缩放两种上下文设置。
- 实验或效果：评估61个模型，发现性能下降主要由问题表述错误主导，微调部分缓解但挑战未解。

## 摘要（原文）

> Large language models now solve many benchmark math problems at near-expert levels, yet this progress has not fully translated into reliable performance in real-world applications. We study this gap through contextual mathematical reasoning, where the mathematical core must be formulated from descriptive scenarios. We introduce ContextMATH, a benchmark that repurposes AIME and MATH-500 problems into two contextual settings: Scenario Grounding (SG), which embeds abstract problems into realistic narratives without increasing reasoning complexity, and Complexity Scaling (CS), which transforms explicit conditions into sub-problems to capture how constraints often appear in practice. Evaluating 61 proprietary and open-source models, we observe sharp drops: on average, open-source models decline by 13 and 34 points on SG and CS, while proprietary models drop by 13 and 20. Error analysis shows that errors are dominated by incorrect problem formulation, with formulation accuracy declining as original problem difficulty increases. Correct formulation emerges as a prerequisite for success, and its sufficiency improves with model scale, indicating that larger models advance in both understanding and reasoning. Nevertheless, formulation and reasoning remain two complementary bottlenecks that limit contextual mathematical problem solving. Finally, we find that fine-tuning with scenario data improves performance, whereas formulation-only training is ineffective. However, performance gaps are only partially alleviated, highlighting contextual mathematical reasoning as a central unsolved challenge for LLMs.

