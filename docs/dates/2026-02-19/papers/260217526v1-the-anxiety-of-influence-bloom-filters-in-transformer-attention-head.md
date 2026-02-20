---
layout: default
title: The Anxiety of Influence: Bloom Filters in Transformer Attention Heads
---

# The Anxiety of Influence: Bloom Filters in Transformer Attention Heads
**arXiv**：[2602.17526v1](https://arxiv.org/abs/2602.17526) · [PDF](https://arxiv.org/pdf/2602.17526.pdf)  
**作者**：Peter Balogh  

**一句话要点**：发现Transformer注意力头作为成员测试器，形成多分辨率系统，提升重复令牌处理能力。

**关键词**：Transformer注意力头, 成员测试, Bloom过滤器, 语言模型分析, 重复令牌处理, 混淆控制

## 3 点简述
- 核心问题：Transformer注意力头是否执行成员测试，即检测令牌在上下文中是否重复出现。
- 方法要点：在四个语言模型中识别成员测试头，分析其策略，包括高精度过滤器和经典Bloom过滤器行为。
- 实验或效果：通过混淆控制验证头功能，显示这些头对重复令牌处理有贡献，并具有广泛泛化能力。

## 摘要（原文）

> Some transformer attention heads appear to function as membership testers, dedicating themselves to answering the question "has this token appeared before in the context?" We identify these heads across four language models (GPT-2 small, medium, and large; Pythia-160M) and show that they form a spectrum of membership-testing strategies. Two heads (L0H1 and L0H5 in GPT-2 small) function as high-precision membership filters with false positive rates of 0-4\% even at 180 unique context tokens -- well above the $d_\text{head} = 64$ bit capacity of a classical Bloom filter. A third head (L1H11) shows the classic Bloom filter capacity curve: its false positive rate follows the theoretical formula $p \approx (1 - e^{-kn/m})^k$ with $R^2 = 1.0$ and fitted capacity $m \approx 5$ bits, saturating by $n \approx 20$ unique tokens. A fourth head initially identified as a Bloom filter (L3H0) was reclassified as a general prefix-attention head after confound controls revealed its apparent capacity curve was a sequence-length artifact. Together, the three genuine membership-testing heads form a multi-resolution system concentrated in early layers (0-1), taxonomically distinct from induction and previous-token heads, with false positive rates that decay monotonically with embedding distance -- consistent with distance-sensitive Bloom filters. These heads generalize broadly: they respond to any repeated token type, not just repeated names, with 43\% higher generalization than duplicate-token-only heads. Ablation reveals these heads contribute to both repeated and novel token processing, indicating that membership testing coexists with broader computational roles. The reclassification of L3H0 through confound controls strengthens rather than weakens the case: the surviving heads withstand the scrutiny that eliminated a false positive in our own analysis.

