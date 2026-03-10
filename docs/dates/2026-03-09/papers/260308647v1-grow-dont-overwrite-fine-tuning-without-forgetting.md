---
layout: default
title: Grow, Don't Overwrite: Fine-tuning Without Forgetting
---

# Grow, Don't Overwrite: Fine-tuning Without Forgetting
**arXiv**：[2603.08647v1](https://arxiv.org/abs/2603.08647) · [PDF](https://arxiv.org/pdf/2603.08647.pdf)  
**作者**：Dyah Adila, Hanna Mazzawi, Benoit Dherin, Xavier Gonzalvo  

**一句话要点**：提出函数保持扩展方法以解决预训练模型微调中的灾难性遗忘问题

**关键词**：灾难性遗忘, 模型微调, 函数保持扩展, Transformer, 参数复制, 缩放校正

## 3 点简述
- 核心问题：预训练模型微调时新知识覆盖基础能力，导致灾难性遗忘
- 方法要点：通过复制参数并应用缩放校正，扩展模型容量且初始化时数学等价于原模型
- 实验或效果：消除可塑性与稳定性权衡，下游任务性能媲美全微调，无原始能力退化

## 摘要（原文）

> Adapting pre-trained models to specialized tasks often leads to catastrophic forgetting, where new knowledge overwrites foundational capabilities. Existing methods either compromise performance on the new task or struggle to balance training stability with efficient reuse of pre-trained knowledge. We introduce a novel function-preserving expansion method that resolves this dilemma. Our technique expands model capacity by replicating pre-trained parameters within transformer submodules and applying a scaling correction that guarantees the expanded model is mathematically identical to the original at initialization, enabling stable training while exploiting existing knowledge. Empirically, our method eliminates the trade-off between plasticity and stability, matching the performance of full fine-tuning on downstream tasks without any degradation of the model's original capabilities. Furthermore, we demonstrate the modularity of our approach, showing that by selectively expanding a small subset of layers we can achieve the same performance as full fine-tuning at a fraction of the computational cost.

