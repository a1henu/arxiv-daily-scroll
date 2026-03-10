---
layout: default
title: SGG-R$^{\rm 3}$: From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation
---

# SGG-R$^{\rm 3}$: From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation
**arXiv**：[2603.07961v1](https://arxiv.org/abs/2603.07961) · [PDF](https://arxiv.org/pdf/2603.07961.pdf)  
**作者**：Jiaye Feng, Qixiang Yin, Yuankun Liu, Tong Mo, Weiping Li  

**一句话要点**：提出SGG-R³框架，通过结构化推理解决端到端场景图生成中的偏差和稀疏性问题。

**关键词**：场景图生成, 结构化推理, 长尾分布, 强化学习, 多模态大语言模型, 端到端学习

## 3 点简述
- 核心问题：现有方法因缺乏任务特定推理和长尾关系分布，导致场景图不完整和预测偏差。
- 方法要点：结合链式思维引导的监督微调、强化学习与组序列策略优化，分三阶段进行关系增强和奖励优化。
- 实验或效果：在两个基准测试中表现优于现有方法，验证了框架的有效性和泛化能力。

## 摘要（原文）

> Scene Graph Generation (SGG) structures visual scenes as graphs of objects and their relations. While Multimodal Large Language Models (MLLMs) have advanced end-to-end SGG, current methods are hindered by both a lack of task-specific structured reasoning and the challenges of sparse, long-tailed relation distributions, resulting in incomplete scene graphs characterized by low recall and biased predictions. To address these issues, we introduce SGG-R$^{\rm 3}$, a structured reasoning framework that integrates task-specific chain-of-thought (CoT)-guided supervised fine-tuning (SFT) and reinforcement learning (RL) with group sequence policy optimization (GSPO), designed to engage in three sequential stages to achieve end-to-end unbiased scene graph generation. During the SFT phase, we propose a relation augmentation strategy by leveraging an MLLM and refined via embedding similarity filtering to alleviate relation sparsity. Subsequently, a stage-aligned reward scheme optimizes the procedural reasoning during RL. Specifically, we propose a novel dual-granularity reward which integrates fine-grained and coarse-grained relation rewards, simultaneously mitigating the long-tail issue via frequency-based adaptive weighting of predicates and improving relation coverage through semantic clustering. Experiments on two benchmarks show that SGG-R$^{\rm 3}$ achieves superior performance compared to existing methods, demonstrating the effectiveness and generalization of the framework.

