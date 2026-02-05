---
layout: default
title: Protein Autoregressive Modeling via Multiscale Structure Generation
---

# Protein Autoregressive Modeling via Multiscale Structure Generation
**arXiv**：[2602.04883v1](https://arxiv.org/abs/2602.04883) · [PDF](https://arxiv.org/pdf/2602.04883.pdf)  
**作者**：Yanru Qu, Cheng-Yen Hsieh, Zaixiang Zheng, Ge Liu, Quanquan Gu  

**一句话要点**：提出蛋白质自回归建模框架，通过多尺度结构生成解决蛋白质骨架生成问题。

**关键词**：蛋白质结构生成, 自回归建模, 多尺度表示, Transformer, 流模型, 零样本泛化

## 3 点简述
- 核心问题：蛋白质结构生成需处理多尺度信息，且自回归模型存在暴露偏差影响质量。
- 方法要点：采用多尺度下采样、自回归Transformer和基于流的解码器，结合噪声上下文学习和计划采样。
- 实验或效果：在无条件生成基准上表现优异，支持零样本泛化和条件生成，无需微调。

## 摘要（原文）

> We present protein autoregressive modeling (PAR), the first multi-scale autoregressive framework for protein backbone generation via coarse-to-fine next-scale prediction. Using the hierarchical nature of proteins, PAR generates structures that mimic sculpting a statue, forming a coarse topology and refining structural details over scales. To achieve this, PAR consists of three key components: (i) multi-scale downsampling operations that represent protein structures across multiple scales during training; (ii) an autoregressive transformer that encodes multi-scale information and produces conditional embeddings to guide structure generation; (iii) a flow-based backbone decoder that generates backbone atoms conditioned on these embeddings. Moreover, autoregressive models suffer from exposure bias, caused by the training and the generation procedure mismatch, and substantially degrades structure generation quality. We effectively alleviate this issue by adopting noisy context learning and scheduled sampling, enabling robust backbone generation. Notably, PAR exhibits strong zero-shot generalization, supporting flexible human-prompted conditional generation and motif scaffolding without requiring fine-tuning. On the unconditional generation benchmark, PAR effectively learns protein distributions and produces backbones of high design quality, and exhibits favorable scaling behavior. Together, these properties establish PAR as a promising framework for protein structure generation.

