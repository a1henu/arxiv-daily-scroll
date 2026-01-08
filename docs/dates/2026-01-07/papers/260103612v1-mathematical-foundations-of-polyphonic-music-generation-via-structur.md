---
layout: default
title: Mathematical Foundations of Polyphonic Music Generation via Structural Inductive Bias
---

# Mathematical Foundations of Polyphonic Music Generation via Structural Inductive Bias
**arXiv**：[2601.03612v1](https://arxiv.org/abs/2601.03612) · [PDF](https://arxiv.org/pdf/2601.03612.pdf)  
**作者**：Joonwon Seo  

**一句话要点**：提出基于结构归纳偏置的多声部音乐生成方法，以解决'缺失中间层'问题。

**关键词**：多声部音乐生成, 结构归纳偏置, 信息论证明, 智能嵌入架构, 泛化能力提升, 数学基础

## 3 点简述
- 核心问题：多声部音乐生成中存在'缺失中间层'问题，影响模型稳定性和泛化能力。
- 方法要点：引入结构归纳偏置，通过智能嵌入架构减少参数，并利用信息论和范畴论提供数学证明。
- 实验或效果：在贝多芬钢琴奏鸣曲案例中，验证音高和手部属性独立性，实现验证损失降低9.47%，参数减少48.30%。

## 摘要（原文）

> This monograph introduces a novel approach to polyphonic music generation by addressing the "Missing Middle" problem through structural inductive bias. Focusing on Beethoven's piano sonatas as a case study, we empirically verify the independence of pitch and hand attributes using normalized mutual information (NMI=0.167) and propose the Smart Embedding architecture, achieving a 48.30% reduction in parameters. We provide rigorous mathematical proofs using information theory (negligible loss bounded at 0.153 bits), Rademacher complexity (28.09% tighter generalization bound), and category theory to demonstrate improved stability and generalization. Empirical results show a 9.47% reduction in validation loss, confirmed by SVD analysis and an expert listening study (N=53). This dual theoretical and applied framework bridges gaps in AI music generation, offering verifiable insights for mathematically grounded deep learning.

