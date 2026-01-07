---
layout: default
title: DIP: Dynamic In-Context Planner For Diffusion Language Models
---

# DIP: Dynamic In-Context Planner For Diffusion Language Models
**arXiv**：[2601.03199v1](https://arxiv.org/abs/2601.03199) · [PDF](https://arxiv.org/pdf/2601.03199.pdf)  
**作者**：Yang Li, Han Meng, Chenan Wang, Haipeng Chen  

**一句话要点**：提出动态上下文规划器以解决扩散语言模型上下文计算成本高的问题

**关键词**：扩散语言模型, 上下文优化, 推理加速, 动态规划, 计算效率, 自然语言处理

## 3 点简述
- 核心问题：扩散语言模型因双向注意力机制，上下文长度增加时计算成本显著上升
- 方法要点：基于扩散生成范式允许动态调整上下文，提出动态选择与插入示例的优化方法
- 实验或效果：在保持生成质量的同时，推理速度最高提升12.9倍

## 摘要（原文）

> Diffusion language models (DLMs) have shown strong potential for general natural language tasks with in-context examples. However, due to the bidirectional attention mechanism, DLMs incur substantial computational cost as context length increases. This work addresses this issue with a key discovery: unlike the sequential generation in autoregressive language models (ARLMs), the diffusion generation paradigm in DLMs allows \textit{efficient dynamic adjustment of the context} during generation. Building on this insight, we propose \textbf{D}ynamic \textbf{I}n-Context \textbf{P}lanner (DIP), a context-optimization method that dynamically selects and inserts in-context examples during generation, rather than providing all examples in the prompt upfront. Results show DIP maintains generation quality while achieving up to 12.9$\times$ inference speedup over standard inference and 1.17$\times$ over KV cache-enhanced inference.

