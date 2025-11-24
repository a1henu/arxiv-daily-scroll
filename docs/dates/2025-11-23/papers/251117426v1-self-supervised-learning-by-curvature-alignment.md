---
layout: default
title: Self-Supervised Learning by Curvature Alignment
---

# Self-Supervised Learning by Curvature Alignment
**arXiv**：[2511.17426v1](https://arxiv.org/abs/2511.17426) · [PDF](https://arxiv.org/pdf/2511.17426.pdf)  
**作者**：Benyamin Ghojogh, M. Hadi Sepanj, Paul Fieguth  

**一句话要点**：提出曲率对齐自监督学习框架以增强数据局部几何建模

**关键词**：自监督学习, 曲率正则化, 数据流形, 冗余减少, 局部几何, 图像分类

## 3 点简述
- 自监督学习忽略数据流形局部几何，仅关注统计特征
- 引入曲率正则化，基于近邻余弦交互计算曲率并跨视图对齐
- 在MNIST和CIFAR-10上实验，性能优于Barlow Twins和VICReg

## 摘要（原文）

> Self-supervised learning (SSL) has recently advanced through non-contrastive methods that couple an invariance term with variance, covariance, or redundancy-reduction penalties. While such objectives shape first- and second-order statistics of the representation, they largely ignore the local geometry of the underlying data manifold. In this paper, we introduce CurvSSL, a curvature-regularized self-supervised learning framework, and its RKHS extension, kernel CurvSSL. Our approach retains a standard two-view encoder-projector architecture with a Barlow Twins-style redundancy-reduction loss on projected features, but augments it with a curvature-based regularizer. Each embedding is treated as a vertex whose $k$ nearest neighbors define a discrete curvature score via cosine interactions on the unit hypersphere; in the kernel variant, curvature is computed from a normalized local Gram matrix in an RKHS. These scores are aligned and decorrelated across augmentations by a Barlow-style loss on a curvature-derived matrix, encouraging both view invariance and consistency of local manifold bending. Experiments on MNIST and CIFAR-10 datasets with a ResNet-18 backbone show that curvature-regularized SSL yields competitive or improved linear evaluation performance compared to Barlow Twins and VICReg. Our results indicate that explicitly shaping local geometry is a simple and effective complement to purely statistical SSL regularizers.

