---
layout: default
title: Contextual Drag: How Errors in the Context Affect LLM Reasoning
---

# Contextual Drag: How Errors in the Context Affect LLM Reasoning
**arXiv**：[2602.04288v1](https://arxiv.org/abs/2602.04288) · [PDF](https://arxiv.org/pdf/2602.04288.pdf)  
**作者**：Yun Cheng, Xingyu Zhu, Haoyu Zhao, Sanjeev Arora  

**一句话要点**：提出上下文拖累现象，揭示LLM推理中错误上下文导致性能下降

**关键词**：上下文拖累, LLM推理, 自我改进, 错误模式分析, 性能下降, 缓解策略

## 3 点简述
- 核心问题：LLM自我改进中，上下文中的失败尝试会引发后续推理的结构性错误偏差
- 方法要点：通过树编辑距离分析错误模式，评估11个模型在8个任务上的性能影响
- 实验或效果：上下文拖累导致10-20%性能下降，自我精炼可能恶化，缓解策略仅部分有效

## 摘要（原文）

> Central to many self-improvement pipelines for large language models (LLMs) is the assumption that models can improve by reflecting on past mistakes. We study a phenomenon termed contextual drag: the presence of failed attempts in the context biases subsequent generations toward structurally similar errors. Across evaluations of 11 proprietary and open-weight models on 8 reasoning tasks, contextual drag induces 10-20% performance drops, and iterative self-refinement in models with severe contextual drag can collapse into self-deterioration. Structural analysis using tree edit distance reveals that subsequent reasoning trajectories inherit structurally similar error patterns from the context. We demonstrate that neither external feedback nor successful self-verification suffices to eliminate this effect. While mitigation strategies such as fallback-behavior fine-tuning and context denoising yield partial improvements, they fail to fully restore baseline performance, positioning contextual drag as a persistent failure mode in current reasoning architectures.

