---
layout: default
title: A Computationally Efficient Multidimensional Vision Transformer
---

# A Computationally Efficient Multidimensional Vision Transformer
**arXiv**：[2602.19982v1](https://arxiv.org/abs/2602.19982) · [PDF](https://arxiv.org/pdf/2602.19982.pdf)  
**作者**：Alaa El Ichi, Khalide Jbilou  

**一句话要点**：提出基于张量余弦积的Vision Transformer，以降低计算和内存成本，适用于图像分类和分割任务。

**关键词**：Vision Transformer, 张量余弦积, 计算效率, 注意力机制, 图像分类, 图像分割

## 3 点简述
- Vision Transformers在计算机视觉任务中性能优越，但计算和内存成本高，限制实际部署。
- 利用张量余弦积，结合图像数据的多线性结构和余弦变换正交性，实现高效注意力机制和结构化特征表示。
- 在标准分类和分割基准测试中，方法实现参数均匀减少1/C，同时保持竞争性准确度。

## 摘要（原文）

> Vision Transformers have achieved state-of-the-art performance in a wide range
>   of computer vision tasks, but their practical deployment is limited by high
>   computational and memory costs. In this paper, we introduce a novel tensor-based
>   framework for Vision Transformers built upon the Tensor Cosine Product
>   (Cproduct). By exploiting multilinear structures inherent in image data and the
>   orthogonality of cosine transforms, the proposed approach enables efficient
>   attention mechanisms and structured feature representations. We develop the
>   theoretical foundations of the tensor cosine product, analyze its algebraic
>   properties, and integrate it into a new Cproduct-based Vision Transformer
>   architecture (TCP-ViT). Numerical experiments on standard classification and
>   segmentation benchmarks demonstrate that the proposed method achieves a uniform
>   1/C parameter reduction (where C is the number of channels) while
>   maintaining competitive accuracy.

