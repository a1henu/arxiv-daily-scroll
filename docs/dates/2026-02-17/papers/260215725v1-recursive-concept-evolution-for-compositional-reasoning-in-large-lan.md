---
layout: default
title: Recursive Concept Evolution for Compositional Reasoning in Large Language Models
---

# Recursive Concept Evolution for Compositional Reasoning in Large Language Models
**arXiv**：[2602.15725v1](https://arxiv.org/abs/2602.15725) · [PDF](https://arxiv.org/pdf/2602.15725.pdf)  
**作者**：Sarim Chaudhry  

**一句话要点**：提出递归概念演化框架，以增强大语言模型在组合推理任务中的性能。

**关键词**：组合推理, 表示学习, 动态子空间, 大语言模型, 推理增强

## 3 点简述
- 大语言模型在组合推理基准上表现不佳，因潜在表示空间固定导致抽象能力不足。
- RCE在推理时动态生成低秩概念子空间，通过检测、选择、合并和优化来构建新抽象。
- 集成Mistral-7B后，在ARC-AGI-2等基准上获得12-18点提升，减少深度诱导错误。

## 摘要（原文）

> Large language models achieve strong performance on many complex reasoning tasks, yet their accuracy degrades sharply on benchmarks that require compositional reasoning, including ARC-AGI-2, GPQA, MATH, BBH, and HLE. Existing methods improve reasoning by expanding token-level search through chain-of-thought prompting, self-consistency, or reinforcement learning, but they leave the model's latent representation space fixed. When the required abstraction is not already encoded in this space, performance collapses. We propose Recursive Concept Evolution (RCE), a framework that enables pretrained language models to modify their internal representation geometry during inference. RCE introduces dynamically generated low-rank concept subspaces that are spawned when representational inadequacy is detected, selected through a minimum description length criterion, merged when synergistic, and consolidated via constrained optimization to preserve stability. This process allows the model to construct new abstractions rather than recombining existing ones. We integrate RCE with Mistral-7B and evaluate it across compositional reasoning benchmarks. RCE yields 12-18 point gains on ARC-AGI-2, 8-14 point improvements on GPQA and BBH, and consistent reductions in depth-induced error on MATH and HLE.

