---
layout: default
title: Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization
---

# Unlocking Noisy Real-World Corpora for Foundation Model Pre-Training via Quality-Aware Tokenization
**arXiv**：[2602.06394v1](https://arxiv.org/abs/2602.06394) · [PDF](https://arxiv.org/pdf/2602.06394.pdf)  
**作者**：Arvid E. Gollwitzer, Paridhi Latawa, David de Gruijl, Deepak A. Subramanian, Adrián Noriega de la Colina  

**一句话要点**：提出质量感知分词方法QA-Token，通过联合优化词汇构建与下游性能，提升噪声现实语料在基础模型预训练中的有效性。

**关键词**：质量感知分词, 词汇构建优化, 噪声语料处理, 基础模型预训练, 强化学习策略, 双层优化

## 3 点简述
- 当前分词方法未考虑信号质量，在处理噪声现实语料时效果受限。
- QA-Token采用双层优化、强化学习策略和自适应参数学习机制，将数据可靠性融入词汇构建。
- 实验在基因组学和金融领域显示显著性能提升，并在大规模预训练中实现最优病原检测效果。

## 摘要（原文）

> Current tokenization methods process sequential data without accounting for signal quality, limiting their effectiveness on noisy real-world corpora. We present QA-Token (Quality-Aware Tokenization), which incorporates data reliability directly into vocabulary construction. We make three key contributions: (i) a bilevel optimization formulation that jointly optimizes vocabulary construction and downstream performance, (ii) a reinforcement learning approach that learns merge policies through quality-aware rewards with convergence guarantees, and (iii) an adaptive parameter learning mechanism via Gumbel-Softmax relaxation for end-to-end optimization. Our experimental evaluation demonstrates consistent improvements: genomics (6.7 percentage point F1 gain in variant calling over BPE), finance (30% Sharpe ratio improvement). At foundation scale, we tokenize a pretraining corpus comprising 1.7 trillion base-pairs and achieve state-of-the-art pathogen detection (94.53 MCC) while reducing token count by 15%. We unlock noisy real-world corpora, spanning petabases of genomic sequences and terabytes of financial time series, for foundation model training with zero inference overhead.

