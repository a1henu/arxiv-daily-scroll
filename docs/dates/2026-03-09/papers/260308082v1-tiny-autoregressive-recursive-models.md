---
layout: default
title: Tiny Autoregressive Recursive Models
---

# Tiny Autoregressive Recursive Models
**arXiv**：[2603.08082v1](https://arxiv.org/abs/2603.08082) · [PDF](https://arxiv.org/pdf/2603.08082.pdf)  
**作者**：Paulius Rauba, Claudio Fanconi, Mihaela van der Schaar  

**一句话要点**：提出自回归TRM以评估小模型在字符级任务中的两步精炼机制效果

**关键词**：自回归模型, 两步精炼机制, 字符级算法任务, 小模型性能, 受控实验设计, TRM架构

## 3 点简述
- 核心问题：TRM机制能否有效应用于自回归模型以提升性能
- 方法要点：通过受控实验逐步将标准Transformer转换为自回归TRM，固定块设计、令牌流和下一令牌目标
- 实验或效果：在计算匹配实验中，未发现自回归TRM带来可靠性能增益，但两步精炼基线表现良好

## 摘要（原文）

> Tiny Recursive Models (TRMs) have recently demonstrated remarkable performance on ARC-AGI, showing that very small models can compete against large foundation models through a two-step refinement mechanism that updates an internal reasoning state $z$ and the predicted output $y$. Naturally, such refinement is of interest for any predictor; it is therefore natural to wonder whether the TRM mechanism could be effectively re-adopted in autoregressive models. However, TRMs cannot be simply compared to standard models because they lack causal predictive structures and contain persistent latent states that make it difficult to isolate specific performance gains. In this paper, we propose the Autoregressive TRM and evaluate it on small autoregressive tasks. To understand its efficacy, we propose a suite of models that gradually transform a standard Transformer to a Tiny Autoregressive Recursive Model in a controlled setting that fixes the block design, token stream, and next-token objective. Across compute-matched experiments on character-level algorithmic tasks, we surprisingly find that there are some two-level refinement baselines that show strong performance. Contrary to expectations, we find no reliable performance gains from the full Autoregressive TRM architecture. These results offer potential promise for two-step refinement mechanisms more broadly but caution against investing in the autoregressive TRM-specific model as a fruitful research direction.

