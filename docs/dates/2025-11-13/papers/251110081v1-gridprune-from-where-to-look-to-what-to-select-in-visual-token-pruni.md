---
layout: default
title: GridPrune: From "Where to Look" to "What to Select" in Visual Token Pruning for MLLMs
---

# GridPrune: From "Where to Look" to "What to Select" in Visual Token Pruning for MLLMs
**arXiv**：[2511.10081v1](https://arxiv.org/abs/2511.10081) · [PDF](https://arxiv.org/pdf/2511.10081.pdf)  
**作者**：Yuxiang Duan, Ao Li, Yingqin Li, Luyu Li, Pengwei Wang  

**一句话要点**：提出GridPrune方法以解决多模态大语言模型中视觉令牌修剪的效率问题

**关键词**：多模态大语言模型, 视觉令牌修剪, 空间分配, 计算效率优化, 两阶段策略

## 3 点简述
- 核心问题：现有视觉令牌修剪方法忽略空间分配，导致计算效率低下和位置偏差。
- 方法要点：采用两阶段策略，先全局分配令牌预算，再局部选择令牌。
- 实验或效果：在LLaVA-NeXT-7B上，使用11.1%令牌保留96.98%性能，优于基线。

## 摘要（原文）

> Multimodal large language models (MLLMs) have shown remarkable capabilities in a wide range of vision-language tasks. However, the large number of visual tokens introduces significant computational overhead. To address this issue, visual token pruning has emerged as a key technique for enhancing the efficiency of MLLMs. In cognitive science, humans tend to first determine which regions of a scene to attend to ("where to look") before deciding which specific elements within those regions to process in detail ("what to select"). This two-stage strategy enables the visual system to efficiently allocate attention at a coarse spatial level before performing fine-grained selection. However, existing pruning methods primarily focus on directly optimizing "what to select", typically using attention scores or similarity metrics. They rarely consider "where to look", which has been shown to lead to inefficient spatial allocation, positional bias, and the retention of irrelevant or redundant tokens. In this paper, we propose GridPrune, a method that replaces the global Top-K mechanism with a "guide-globally, select-locally" zonal selection system. GridPrune splits the pruning process into two steps: first, it uses text-conditional guidance to dynamically allocate a token budget across spatial zones; and then, it performs local selection within each budgeted zone. Experimental results demonstrate that GridPrune achieves superior performance across various MLLM architectures. On LLaVA-NeXT-7B, GridPrune retains 96.98% of the full performance while using 11.1% of the tokens, outperforming the best-performing baseline by 2.34% at the same pruning rate.

