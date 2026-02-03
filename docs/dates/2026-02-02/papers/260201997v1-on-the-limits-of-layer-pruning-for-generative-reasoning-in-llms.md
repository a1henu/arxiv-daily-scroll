---
layout: default
title: On the Limits of Layer Pruning for Generative Reasoning in LLMs
---

# On the Limits of Layer Pruning for Generative Reasoning in LLMs
**arXiv**：[2602.01997v1](https://arxiv.org/abs/2602.01997) · [PDF](https://arxiv.org/pdf/2602.01997.pdf)  
**作者**：Safal Shrestha, Anubhav Shrestha, Aadim Nepal, Minwu Kim, Keith Ross  

**一句话要点**：研究层剪枝在LLMs生成推理中的极限，提出基于自生成响应的微调策略以缓解性能下降

**关键词**：层剪枝, 生成推理, 大语言模型, 监督微调, 训练后优化, 性能恢复

## 3 点简述
- 核心问题：层剪枝在LLMs中导致生成推理任务性能严重下降，特别是多步推理任务
- 方法要点：在训练后约束下，采用基于自生成响应的监督微调作为缓解策略
- 实验或效果：该方法在分类任务上恢复至基线90%性能，生成任务提升20-30个百分点，但恢复有限且主要适用于低剪枝率

## 摘要（原文）

> Recent works have shown that layer pruning can compress large language models (LLMs) while retaining strong performance on classification benchmarks with little or no finetuning. However, existing pruning techniques often suffer severe degradation on generative reasoning tasks. Through a systematic study across multiple model families, we find that tasks requiring multi-step reasoning are particularly sensitive to depth reduction. Beyond surface-level text degeneration, we observe degradation of critical algorithmic capabilities, including arithmetic computation for mathematical reasoning and balanced parenthesis generation for code synthesis. Under realistic post-training constraints, without access to pretraining-scale data or compute, we evaluate a simple mitigation strategy based on supervised finetuning with Self-Generated Responses. This approach achieves strong recovery on classification tasks, retaining up to 90\% of baseline performance, and yields substantial gains of up to 20--30 percentage points on generative benchmarks compared to prior post-pruning techniques. Crucially, despite these gains, recovery for generative reasoning remains fundamentally limited relative to classification tasks and is viable primarily at lower pruning ratios. Overall, we characterize the practical limits of layer pruning for generative reasoning and provide guidance on when depth reduction can be applied effectively under constrained post-training regimes.

