---
layout: default
title: Incremental dimension reduction for efficient and accurate visual anomaly detection
---

# Incremental dimension reduction for efficient and accurate visual anomaly detection
**arXiv**：[2602.23595v1](https://arxiv.org/abs/2602.23595) · [PDF](https://arxiv.org/pdf/2602.23595.pdf)  
**作者**：Teng-Yok Lee  

**一句话要点**：提出增量降维算法以解决视觉异常检测中高维特征处理效率低的问题

**关键词**：视觉异常检测, 增量降维, 奇异值分解, 特征处理, 高效训练

## 3 点简述
- 核心问题：视觉异常检测中，深度特征的高维度导致处理大规模图像数据时效率低下。
- 方法要点：通过分批处理特征向量，增量更新截断奇异值分解，降低内存开销并加速训练。
- 实验或效果：算法能加速先进异常检测算法的训练，同时保持接近的准确度。

## 摘要（原文）

> While nowadays visual anomaly detection algorithms use deep neural networks to extract salient features from images, the high dimensionality of extracted features makes it difficult to apply those algorithms to large data with 1000s of images. To address this issue, we present an incremental dimension reduction algorithm to reduce the extracted features. While our algorithm essentially computes truncated singular value decomposition of these features, other than processing all vectors at once, our algorithm groups the vectors into batches. At each batch, our algorithm updates the truncated singular values and vectors that represent all visited vectors, and reduces each batch by its own singular values and vectors so they can be stored in the memory with low overhead. After processing all batches, we re-transform these batch-wise singular vectors to the space spanned by the singular vectors of all features. We show that our algorithm can accelerate the training of state-of-the-art anomaly detection algorithm with close accuracy.

