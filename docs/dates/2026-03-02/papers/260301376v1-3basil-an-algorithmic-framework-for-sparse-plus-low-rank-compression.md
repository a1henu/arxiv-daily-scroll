---
layout: default
title: 3BASiL: An Algorithmic Framework for Sparse plus Low-Rank Compression of LLMs
---

# 3BASiL: An Algorithmic Framework for Sparse plus Low-Rank Compression of LLMs
**arXiv**：[2603.01376v1](https://arxiv.org/abs/2603.01376) · [PDF](https://arxiv.org/pdf/2603.01376.pdf)  
**作者**：Mehdi Makni, Xiang Meng, Rahul Mazumder  

**一句话要点**：提出3BASiL-TM框架，用于大语言模型的稀疏加低秩压缩以减少性能损失。

**关键词**：大语言模型压缩, 稀疏加低秩分解, 交替方向乘子法, Transformer匹配, 后训练优化, 模型加速

## 3 点简述
- 现有稀疏加低秩分解方法常导致大语言模型性能显著下降。
- 引入3BASiL算法最小化层重构误差，并设计Transformer匹配步骤联合优化组件。
- 实验显示在特定配置下，WikiText2困惑度差距减少超30%，压缩速度提升超2.5倍。

## 摘要（原文）

> Sparse plus Low-Rank $(\mathbf{S} + \mathbf{LR})$ decomposition of Large Language Models (LLMs) has emerged as a promising direction in model compression, aiming to decompose pre-trained model weights into a sum of sparse and low-rank matrices $(\mathbf{W} \approx \mathbf{S} + \mathbf{LR})$. Despite recent progress, existing methods often suffer from substantial performance degradation compared to dense models. In this work, we introduce 3BASiL-TM, an efficient one-shot post-training method for $(\mathbf{S} + \mathbf{LR})$ decomposition of LLMs that addresses this gap. Our approach first introduces a novel 3-Block Alternating Direction Method of Multipliers (ADMM) method, termed 3BASiL, to minimize the layer-wise reconstruction error with convergence guarantees. We then design an efficient transformer-matching (TM) refinement step that jointly optimizes the sparse and low-rank components across transformer layers. This step minimizes a novel memory-efficient loss that aligns outputs at the transformer level. Notably, the TM procedure is universal as it can enhance any $(\mathbf{S} + \mathbf{LR})$ decomposition, including pure sparsity. Our numerical experiments show that 3BASiL-TM reduces the WikiText2 perplexity gap relative to dense LLaMA-8B model by over 30% under a (2:4 Sparse + 64 LR) configuration, compared to prior methods. Moreover, our method achieves over 2.5x faster compression runtime on an A100 GPU compared to SOTA $(\mathbf{S} + \mathbf{LR})$ method. Our code is available at https://github.com/mazumder-lab/3BASiL.

