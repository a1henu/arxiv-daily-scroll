---
layout: default
title: Rethinking Attention Output Projection: Structured Hadamard Transforms for Efficient Transformers
---

# Rethinking Attention Output Projection: Structured Hadamard Transforms for Efficient Transformers
**arXiv**：[2603.08343v1](https://arxiv.org/abs/2603.08343) · [PDF](https://arxiv.org/pdf/2603.08343.pdf)  
**作者**：Shubham Aggarwal, Lokendra Kumar  

**一句话要点**：提出结构化哈达玛变换替代多头注意力中的密集输出投影，以提升Transformer效率。

**关键词**：Transformer效率, 结构化变换, 参数减少, 多头注意力, 哈达玛变换, 计算优化

## 3 点简述
- 核心问题：多头注意力中的密集输出投影导致参数和计算成本随模型维度二次增长。
- 方法要点：用固定、无参数的Walsh哈达玛变换和轻量可学习仿射缩放替换投影，保持正交性和范数。
- 实验或效果：在标准基准上保持或略优性能，实现参数减少、内存节省和吞吐量提升，效率随模型规模增加。

## 摘要（原文）

> The dense output projection in multi-head attention scales quadratically with model dimension, contributing significantly to parameter count, memory footprint, and inference cost. We propose replacing this projection with a fixed, parameter-free Walsh Hadamard Transform followed by a lightweight learnable affine rescaling, eliminating approximately 25 percent of attention parameters per block while preserving global cross head interaction through an orthogonal, norm-preserving transformation. Across different model sizes, we demonstrate that this structured substitution maintains comparable or slightly superior downstream task performance on standard benchmarks, while achieving up to 7 percent aggregate parameter reduction, 8.9 percent peak memory savings, and 6.6 percent throughput improvement at scale, with efficiency gains growing monotonically with model size, batch size, and sequence length. Interestingly, we observe that structured Hadamard-based models exhibit a steeper validation loss curve relative to training FLOPs compared to their dense counterparts, suggesting more favorable compute utilization during training.

