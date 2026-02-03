---
layout: default
title: Rethinking Genomic Modeling Through Optical Character Recognition
---

# Rethinking Genomic Modeling Through Optical Character Recognition
**arXiv**：[2602.02014v1](https://arxiv.org/abs/2602.02014) · [PDF](https://arxiv.org/pdf/2602.02014.pdf)  
**作者**：Hongxin Xiang, Pengsen Ma, Yunkang Cao, Di Yu, Haowen Chen, Xinyu Yang, Xiangxiang Zeng  

**一句话要点**：提出OpticalDNA框架，通过OCR式视觉建模解决基因组序列计算效率低的问题。

**关键词**：基因组建模, 光学字符识别, 视觉-语言模型, 序列压缩, 长上下文处理

## 3 点简述
- 核心问题：现有基因组模型将DNA视为一维序列，导致计算浪费在低信息背景上，难以压缩长上下文。
- 方法要点：将DNA渲染为结构化视觉布局，训练视觉-语言模型，实现高保真压缩和布局感知表示。
- 实验或效果：在多个基准测试中表现优异，以更少有效token和可训练参数超越基线模型。

## 摘要（原文）

> Recent genomic foundation models largely adopt large language model architectures that treat DNA as a one-dimensional token sequence. However, exhaustive sequential reading is structurally misaligned with sparse and discontinuous genomic semantics, leading to wasted computation on low-information background and preventing understanding-driven compression for long contexts. Here, we present OpticalDNA, a vision-based framework that reframes genomic modeling as Optical Character Recognition (OCR)-style document understanding. OpticalDNA renders DNA into structured visual layouts and trains an OCR-capable vision--language model with a \emph{visual DNA encoder} and a \emph{document decoder}, where the encoder produces compact, reconstructible visual tokens for high-fidelity compression. Building on this representation, OpticalDNA defines prompt-conditioned objectives over core genomic primitives-reading, region grounding, subsequence retrieval, and masked span completion-thereby learning layout-aware DNA representations that retain fine-grained genomic information under a reduced effective token budget. Across diverse genomic benchmarks, OpticalDNA consistently outperforms recent baselines; on sequences up to 450k bases, it achieves the best overall performance with nearly $20\times$ fewer effective tokens, and surpasses models with up to $985\times$ more activated parameters while tuning only 256k \emph{trainable} parameters.

