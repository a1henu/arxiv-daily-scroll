---
layout: default
title: FOAM: Blocked State Folding for Memory-Efficient LLM Training
---

# FOAM: Blocked State Folding for Memory-Efficient LLM Training
**arXiv**：[2512.07112v1](https://arxiv.org/abs/2512.07112) · [PDF](https://arxiv.org/pdf/2512.07112.pdf)  
**作者**：Ziqing Wen, Jiahuan Wang, Ping Luo, Dongsheng Li, Tao Sun  

**一句话要点**：提出FOAM方法以解决大语言模型训练中的内存瓶颈问题

**关键词**：大语言模型训练, 内存优化, 优化器压缩, 梯度均值, 残差校正, 收敛加速

## 3 点简述
- 核心问题：大语言模型训练因Adam等优化器状态占用大量内存，导致内存瓶颈
- 方法要点：通过分块梯度均值压缩优化器状态，并引入残差校正恢复信息损失
- 实验或效果：减少总训练内存约50%，消除高达90%优化器状态内存开销，加速收敛

## 摘要（原文）

> Large language models (LLMs) have demonstrated remarkable performance due to their large parameter counts and extensive training data. However, their scale leads to significant memory bottlenecks during training, especially when using memory-intensive optimizers like Adam. Existing memory-efficient approaches often rely on techniques such as singular value decomposition (SVD), projections, or weight freezing, which can introduce substantial computational overhead, require additional memory for projections, or degrade model performance. In this paper, we propose Folded Optimizer with Approximate Moment (FOAM), a method that compresses optimizer states by computing block-wise gradient means and incorporates a residual correction to recover lost information. Theoretically, FOAM achieves convergence rates equivalent to vanilla Adam under standard non-convex optimization settings. Empirically, FOAM reduces total training memory by approximately 50\%, eliminates up to 90\% of optimizer state memory overhead, and accelerates convergence. Furthermore, FOAM is compatible with other memory-efficient optimizers, delivering performance and throughput that match or surpass both full-rank and existing memory-efficient baselines.

