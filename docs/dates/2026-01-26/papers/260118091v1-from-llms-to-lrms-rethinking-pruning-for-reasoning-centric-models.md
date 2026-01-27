---
layout: default
title: From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models
---

# From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models
**arXiv**：[2601.18091v1](https://arxiv.org/abs/2601.18091) · [PDF](https://arxiv.org/pdf/2601.18091.pdf)  
**作者**：Longwei Ding, Anhao Zhao, Fanghua Ye, Ziyang Chen, Xiaoyu Shen  

**一句话要点**：提出针对推理增强大语言模型的剪枝策略研究，揭示范式依赖差异并优化剪枝校准。

**关键词**：大语言模型剪枝, 推理增强模型, 静态剪枝, 动态剪枝, 任务性能评估, 校准数据对齐

## 3 点简述
- 核心问题：现有剪枝研究多关注指令遵循LLMs，对推理增强模型的适用性未知。
- 方法要点：通过校准数据对齐训练分布，对比静态深度、宽度及动态剪枝在17个任务上的效果。
- 实验或效果：发现深度剪枝在分类任务更优，宽度剪枝对生成和推理更稳健，静态剪枝更好保留推理性能。

## 摘要（原文）

> Large language models (LLMs) are increasingly costly to deploy, motivating extensive research on model pruning. However, most existing studies focus on instruction-following LLMs, leaving it unclear whether established pruning strategies transfer to reasoning-augmented models that explicitly generate long intermediate reasoning traces. In this work, we conduct a controlled study of pruning for both instruction-following ($\textbf{LLM-instruct}$) and reasoning-augmented ($\textbf{LLM-think}$) models. To isolate the effects of pruning, we align pruning calibration and post-pruning recovery data with each model's original training distribution, which we show yields more stable and reliable pruning behavior. We evaluate static depth pruning, static width pruning, and dynamic pruning across 17 tasks spanning classification, generation, and reasoning. Our results reveal clear paradigm-dependent differences: depth pruning outperforms width pruning on classification tasks, while width pruning is more robust for generation and reasoning. Moreover, static pruning better preserves reasoning performance, whereas dynamic pruning excels on classification and generation but remains challenging for long-chain reasoning. These findings underscore the need for pruning strategies that explicitly account for the distinct characteristics of reasoning-augmented LLMs. Our code is publicly available at https://github.com/EIT-NLP/LRM-Pruning.

