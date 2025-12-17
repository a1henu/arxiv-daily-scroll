---
layout: default
title: RePo: Language Models with Context Re-Positioning
---

# RePo: Language Models with Context Re-Positioning
**arXiv**：[2512.14391v1](https://arxiv.org/abs/2512.14391) · [PDF](https://arxiv.org/pdf/2512.14391.pdf)  
**作者**：Huayang Li, Tianyu Zhao, Richard Sproat  

**一句话要点**：提出RePo机制，通过上下文重定位减少大语言模型中的额外认知负荷。

**关键词**：上下文学习, 位置编码, 认知负荷理论, 大语言模型, 可微分模块

## 3 点简述
- 核心问题：现有大语言模型采用固定位置索引，增加额外认知负荷，影响深度推理。
- 方法要点：引入可微分模块fφ动态分配token位置，捕捉上下文依赖关系。
- 实验或效果：在OLMo-2 1B上持续预训练，提升噪声上下文、结构化数据和长上下文任务性能。

## 摘要（原文）

> In-context learning is fundamental to modern Large Language Models (LLMs); however, prevailing architectures impose a rigid and fixed contextual structure by assigning linear or constant positional indices. Drawing on Cognitive Load Theory (CLT), we argue that this uninformative structure increases extraneous cognitive load, consuming finite working memory capacity that should be allocated to deep reasoning and attention allocation. To address this, we propose RePo, a novel mechanism that reduces extraneous load via context re-positioning. Unlike standard approaches, RePo utilizes a differentiable module, $f_φ$, to assign token positions that capture contextual dependencies, rather than replying on pre-defined integer range. By continually pre-training on the OLMo-2 1B backbone, we demonstrate that RePo significantly enhances performance on tasks involving noisy contexts, structured data, and longer context length, while maintaining competitive performance on general short-context tasks. Detailed analysis reveals that RePo successfully allocate higher attention to distant but relevant information, assign positions in dense and non-linear space, and capture the intrinsic structure of the input context. Our code is available at https://github.com/SakanaAI/repo.

