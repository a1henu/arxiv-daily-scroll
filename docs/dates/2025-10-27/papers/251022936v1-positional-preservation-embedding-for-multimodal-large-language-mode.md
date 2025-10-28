---
layout: default
title: Positional Preservation Embedding for Multimodal Large Language Models
---

# Positional Preservation Embedding for Multimodal Large Language Models
**arXiv**：[2510.22936v1](https://arxiv.org/abs/2510.22936) · [PDF](https://arxiv.org/pdf/2510.22936.pdf)  
**作者**：Mouxiao Huang, Borui Jiang, Dehua Zheng, Hailin Hu, Kai Han, Xinghao Chen  

**一句话要点**：提出位置保持嵌入以解决多模态大模型中视觉令牌压缩时的空间布局破坏问题

**关键词**：多模态大语言模型, 视觉令牌压缩, 位置保持嵌入, 空间布局保留, 时间连续性, 级联聚类

## 3 点简述
- 核心问题：现有令牌合并方法在减少序列长度时忽略位置关系，破坏空间布局和时间连续性
- 方法要点：PPE通过解耦编码3D位置，使压缩令牌封装多个原始令牌的不同位置
- 实验或效果：在多个基准测试中实现2%~5%性能提升，支持级联聚类策略

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved strong performance on
> vision-language tasks, yet often suffer from inefficiencies due to redundant
> visual tokens. Existing token merging methods reduce sequence length but
> frequently disrupt spatial layouts and temporal continuity by disregarding
> positional relationships. In this work, we propose a novel encoding operator
> dubbed as \textbf{P}ositional \textbf{P}reservation \textbf{E}mbedding
> (\textbf{PPE}), which has the main hallmark of preservation of spatiotemporal
> structure during visual token compression. PPE explicitly introduces the
> disentangled encoding of 3D positions in the token dimension, enabling each
> compressed token to encapsulate different positions from multiple original
> tokens. Furthermore, we show that PPE can effectively support cascade
> clustering -- a progressive token compression strategy that leads to better
> performance retention. PPE is a parameter-free and generic operator that can be
> seamlessly integrated into existing token merging methods without any
> adjustments. Applied to state-of-the-art token merging framework, PPE achieves
> consistent improvements of $2\%\sim5\%$ across multiple vision-language
> benchmarks, including MMBench (general vision understanding), TextVQA (layout
> understanding) and VideoMME (temporal understanding). These results demonstrate
> that preserving positional cues is critical for efficient and effective MLLM
> reasoning.

