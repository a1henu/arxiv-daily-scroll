---
layout: default
title: Image Compression Using Singular Value Decomposition
---

# Image Compression Using Singular Value Decomposition
**arXiv**：[2512.16226v1](https://arxiv.org/abs/2512.16226) · [PDF](https://arxiv.org/pdf/2512.16226.pdf)  
**作者**：Justin Jiang  

**一句话要点**：研究奇异值分解与低秩矩阵近似用于图像压缩，评估其性能与标准格式的差距。

**关键词**：图像压缩, 奇异值分解, 低秩近似, 压缩比, Frobenius误差, 标准格式比较

## 3 点简述
- 核心问题：图像压缩对减少存储和带宽需求至关重要，需高效方法。
- 方法要点：使用奇异值分解和低秩矩阵近似进行压缩，适用于灰度与多通道图像。
- 实验或效果：在视觉相似度下，压缩效率低于JPEG等标准格式，高误差容忍时可能增大文件。

## 摘要（原文）

> Images are a substantial portion of the internet, making efficient compression important for reducing storage and bandwidth demands. This study investigates the use of Singular Value Decomposition and low-rank matrix approximations for image compression, evaluating performance using relative Frobenius error and compression ratio. The approach is applied to both grayscale and multichannel images to assess its generality. Results show that the low-rank approximations often produce images that appear visually similar to the originals, but the compression efficiency remains consistently worse than established formats such as JPEG, JPEG2000, and WEBP at comparable error levels. At low tolerated error levels, the compressed representation produced by Singular Value Decomposition can even exceed the size of the original image, indicating that this method is not competitive with industry-standard codecs for practical image compression.

