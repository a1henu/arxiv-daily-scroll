---
layout: default
title: ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection
---

# ManifoldKV: Training-Free KV Cache Compression via Euclidean Outlier Detection
**arXiv**：[2602.08343v1](https://arxiv.org/abs/2602.08343) · [PDF](https://arxiv.org/pdf/2602.08343.pdf)  
**作者**：Debajyoti Datta, Trishala Neeraj, Bibek Paudel, Vyom Sharma, Subhabrata Mukherjee  

**一句话要点**：提出ManifoldKV，通过欧氏距离检测异常值，实现无需训练的KV缓存压缩以支持长上下文推理。

**关键词**：KV缓存压缩, 长上下文推理, 欧氏距离评分, 无需训练方法, 异常值检测

## 3 点简述
- 核心问题：长上下文推理中KV缓存内存线性增长，压缩需可靠选择保留的过去令牌。
- 方法要点：使用欧氏距离而非余弦相似度评分令牌，捕获角度和径向偏差，提升语义区分能力。
- 实验效果：在RULER基准上，20%压缩下达到95.7%准确率，并在多键检索和长上下文场景中优于基线。

## 摘要（原文）

> Long-context inference is constrained by KV-cache memory, which grows linearly with sequence length; KV-cache compression therefore hinges on reliably selecting which past tokens to retain. Most geometry-based eviction methods score keys by cosine similarity to a global centroid, but cosine is scale-invariant and can discard magnitude cues that distinguish semantically salient tokens. We propose ManifoldKV, a training-free scorer that ranks tokens by Euclidean distance to the key centroid, capturing both angular and radial deviations.
>   On the RULER benchmark, ManifoldKV achieves 95.7% accuracy at 4K-16K contexts with 20% compression; matching the best geometric baseline while improving robustness in two regimes where cosine scoring fails. First, on multi-key retrieval, ManifoldKV reduces directional collisions, achieving 92.4% vs KeyDiff's 77.0% (+15.4 points) on 3-key NIAH at 50% compression. Second, to address dilution and performance collapse of global centroids at 64K context, we introduce WindowedManifoldKV, which restores accuracy to 84.3% at 25% compression, a 49-point recovery over global L2 and +3.2 points over KeyDiff. The method requires only 3 lines of code and works across 4 architectures without tuning.

