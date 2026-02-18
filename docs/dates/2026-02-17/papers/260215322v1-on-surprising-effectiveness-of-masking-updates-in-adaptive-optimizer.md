---
layout: default
title: On Surprising Effectiveness of Masking Updates in Adaptive Optimizers
---

# On Surprising Effectiveness of Masking Updates in Adaptive Optimizers
**arXiv**：[2602.15322v1](https://arxiv.org/abs/2602.15322) · [PDF](https://arxiv.org/pdf/2602.15322.pdf)  
**作者**：Taejong Joo, Wenhan Xia, Cheolmin Kim, Ming Zhang, Eugene Ie  

**一句话要点**：提出随机掩码更新方法Magma，提升大语言模型训练效果

**关键词**：自适应优化器, 大语言模型训练, 梯度掩码, 几何正则化, 动量对齐

## 3 点简述
- 挑战密集自适应优化器主导地位，展示随机掩码更新的有效性
- 分析掩码诱导几何正则化，提出动量对齐梯度掩码方法Magma
- 实验显示Magma在1B模型上显著降低困惑度，计算开销可忽略

## 摘要（原文）

> Training large language models (LLMs) relies almost exclusively on dense adaptive optimizers with increasingly sophisticated preconditioners. We challenge this by showing that randomly masking parameter updates can be highly effective, with a masked variant of RMSProp consistently outperforming recent state-of-the-art optimizers. Our analysis reveals that the random masking induces a curvature-dependent geometric regularization that smooths the optimization trajectory. Motivated by this finding, we introduce Momentum-aligned gradient masking (Magma), which modulates the masked updates using momentum-gradient alignment. Extensive LLM pre-training experiments show that Magma is a simple drop-in replacement for adaptive optimizers with consistent gains and negligible computational overhead. Notably, for the 1B model size, Magma reduces perplexity by over 19\% and 9\% compared to Adam and Muon, respectively.

