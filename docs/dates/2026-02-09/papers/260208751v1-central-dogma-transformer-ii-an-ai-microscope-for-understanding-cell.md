---
layout: default
title: Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms
---

# Central Dogma Transformer II: An AI Microscope for Understanding Cellular Regulatory Mechanisms
**arXiv**：[2602.08751v1](https://arxiv.org/abs/2602.08751) · [PDF](https://arxiv.org/pdf/2602.08751.pdf)  
**作者**：Nobuyuki Ota  

**一句话要点**：提出CDT-II作为AI显微镜，通过注意力机制直接解释细胞调控结构，以解决生物AI模型缺乏可解释性的问题。

**关键词**：可解释AI, 注意力机制, 细胞调控, 基因组学, 转录控制, 生物信息学

## 3 点简述
- 当前生物AI模型缺乏可解释性，内部表示不直接对应可检验的生物关系。
- CDT-II架构模拟中心法则，注意力机制对应特定生物关系，如DNA自注意力用于基因组关系。
- 在K562 CRISPRi数据中，CDT-II预测扰动效果（平均r=0.84）并恢复GFI1B调控网络（6.6倍富集）。

## 摘要（原文）

> Current biological AI models lack interpretability -- their internal representations do not correspond to biological relationships that
>   researchers can examine. Here we present CDT-II, an "AI microscope" whose attention maps are directly interpretable as regulatory structure.
>   By mirroring the central dogma in its architecture, each attention mechanism corresponds to a specific biological relationship: DNA
>   self-attention for genomic relationships, RNA self-attention for gene co-regulation, and DNA-to-RNA cross-attention for transcriptional
>   control. Using only genomic embeddings and raw per-cell expression, CDT-II enables experimental biologists to observe regulatory networks in
>   their own data. Applied to K562 CRISPRi data, CDT-II predicts perturbation effects (per-gene mean $r = 0.84$) and recovers the GFI1B
>   regulatory network without supervision (6.6-fold enrichment, $P = 3.5 \times 10^{-17}$). Two distinct attention mechanisms converge on an RNA
>   processing module ($P = 1 \times 10^{-16}$). CDT-II establishes mechanism-oriented AI as an alternative to task-oriented approaches, revealing
>   regulatory structure rather than merely optimizing predictions.

