---
layout: default
title: Optimizing 3D Gaussian Splattering for Mobile GPUs
---

# Optimizing 3D Gaussian Splattering for Mobile GPUs
**arXiv**：[2511.16298v1](https://arxiv.org/abs/2511.16298) · [PDF](https://arxiv.org/pdf/2511.16298.pdf)  
**作者**：Md Musfiqur Rahman Sanim, Zhihao Shu, Bahram Afsharmanesh, AmirAli Mirian, Jiexiong Guan, Wei Niu, Bin Ren, Gagan Agrawal  

**一句话要点**：提出Texture3dgs以优化3D高斯泼溅在移动GPU上的性能

**关键词**：3D高斯泼溅, 移动GPU优化, 纹理缓存, 排序算法, 3D场景重建

## 3 点简述
- 核心问题：移动GPU上3D高斯泼溅的二维纹理缓存优化不足，导致计算效率低。
- 方法要点：设计新型排序算法，优化数据处理和内存布局，针对纹理缓存进行加速。
- 实验或效果：排序速度提升4.1倍，整体重建加速1.7倍，内存使用减少1.6倍。

## 摘要（原文）

> Image-based 3D scene reconstruction, which transforms multi-view images into a structured 3D representation of the surrounding environment, is a common task across many modern applications. 3D Gaussian Splatting (3DGS) is a new paradigm to address this problem and offers considerable efficiency as compared to the previous methods. Motivated by this, and considering various benefits of mobile device deployment (data privacy, operating without internet connectivity, and potentially faster responses), this paper develops Texture3dgs, an optimized mapping of 3DGS for a mobile GPU. A critical challenge in this area turns out to be optimizing for the two-dimensional (2D) texture cache, which needs to be exploited for faster executions on mobile GPUs. As a sorting method dominates the computations in 3DGS on mobile platforms, the core of Texture3dgs is a novel sorting algorithm where the processing, data movement, and placement are highly optimized for 2D memory. The properties of this algorithm are analyzed in view of a cost model for the texture cache. In addition, we accelerate other steps of the 3DGS algorithm through improved variable layout design and other optimizations. End-to-end evaluation shows that Texture3dgs delivers up to 4.1$\times$ and 1.7$\times$ speedup for the sorting and overall 3D scene reconstruction, respectively -- while also reducing memory usage by up to 1.6$\times$ -- demonstrating the effectiveness of our design for efficient mobile 3D scene reconstruction.

