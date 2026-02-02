---
layout: default
title: DAVIS: OOD Detection via Dominant Activations and Variance for Increased Separation
---

# DAVIS: OOD Detection via Dominant Activations and Variance for Increased Separation
**arXiv**：[2601.22703v1](https://arxiv.org/abs/2601.22703) · [PDF](https://arxiv.org/pdf/2601.22703.pdf)  
**作者**：Abid Hassan, Tuan Ngo, Saad Shafiq, Nenad Medvidovic  

**一句话要点**：提出DAVIS方法，通过引入主导激活和方差增强特征，以解决全局平均池化导致的信息损失问题，提升OOD检测性能。

**关键词**：OOD检测, 特征增强, 全局平均池化, 激活统计, 后处理方法, 模型安全

## 3 点简述
- 核心问题：全局平均池化在OOD检测中丢弃了激活图的分布统计信息，导致特征表示不充分。
- 方法要点：DAVIS在特征向量中融入通道级方差和最大激活值，以保留关键统计信息，增强OOD判别能力。
- 实验或效果：在多种架构上显著降低FPR95，如在CIFAR-10上使用ResNet-18改进48.26%，验证了方法的有效性。

## 摘要（原文）

> Detecting out-of-distribution (OOD) inputs is a critical safeguard for deploying machine learning models in the real world. However, most post-hoc detection methods operate on penultimate feature representations derived from global average pooling (GAP) -- a lossy operation that discards valuable distributional statistics from activation maps prior to global average pooling. We contend that these overlooked statistics, particularly channel-wise variance and dominant (maximum) activations, are highly discriminative for OOD detection. We introduce DAVIS, a simple and broadly applicable post-hoc technique that enriches feature vectors by incorporating these crucial statistics, directly addressing the information loss from GAP. Extensive evaluations show DAVIS sets a new benchmark across diverse architectures, including ResNet, DenseNet, and EfficientNet. It achieves significant reductions in the false positive rate (FPR95), with improvements of 48.26\% on CIFAR-10 using ResNet-18, 38.13\% on CIFAR-100 using ResNet-34, and 26.83\% on ImageNet-1k benchmarks using MobileNet-v2. Our analysis reveals the underlying mechanism for this improvement, providing a principled basis for moving beyond the mean in OOD detection.

