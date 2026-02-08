---
layout: default
title: Transformers Are Born Biased: Structural Inductive Biases at Random Initialization and Their Practical Consequences
---

# Transformers Are Born Biased: Structural Inductive Biases at Random Initialization and Their Practical Consequences
**arXiv**：[2602.05927v1](https://arxiv.org/abs/2602.05927) · [PDF](https://arxiv.org/pdf/2602.05927.pdf)  
**作者**：Siquan Li, Yao Tong, Haonan Wang, Tianyang Hu  

**一句话要点**：揭示Transformer随机初始化时的结构偏置及其对训练与指纹识别的影响

**关键词**：Transformer偏置, 随机初始化, 模型指纹识别, 注意力机制, 表示学习, 结构分析

## 3 点简述
- 核心问题：Transformer在随机初始化时已存在系统性结构偏置，挑战了其行为无结构的假设
- 方法要点：通过分析MLP激活和自注意力机制，解释偏置源于表示收缩和聚合
- 实验或效果：提出SeedPrint指纹方法，能区分仅初始化不同的模型，并解释注意力汇现象

## 摘要（原文）

> Transformers underpin modern large language models (LLMs) and are commonly assumed to be behaviorally unstructured at random initialization, with all meaningful preferences emerging only through large-scale training. We challenge this assumption by showing that randomly initialized transformers already exhibit strong and systematic structural biases. In particular, untrained models display extreme token preferences: across random input sequences, certain tokens are predicted with probabilities orders of magnitude larger.
>   We provide a mechanistic explanation for this phenomenon by dissecting the transformer architecture at initialization. We show that extreme token preference arises from a contraction of token representations along a random seed-dependent direction. This contraction is driven by two interacting forces: (i) asymmetric nonlinear activations in MLP sublayers induce global (inter-sequence) representation concentration, and (ii) self-attention further amplifies this effect through local (intra-sequence) aggregation. Together, these mechanisms align hidden representations along a direction determined solely by the random initialization, producing highly non-uniform next-token predictions.
>   Beyond mechanistic insight, we demonstrate that these initialization-induced biases persist throughout training, forming a stable and intrinsic model identity. Leveraging this property, we introduce SeedPrint, a fingerprinting method that can reliably distinguish models that differ only in their random initialization, even after extensive training and under substantial distribution shift. Finally, we identify a fundamental positional discrepancy inherent to the attention mechanism's intra-sequence contraction that is causally linked to the attention-sink phenomenon. This discovery provides a principled explanation for the emergence of sinks and offers a pathway for their control.

