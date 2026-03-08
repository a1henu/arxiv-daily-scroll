---
layout: default
title: A Benchmark Study of Neural Network Compression Methods for Hyperspectral Image Classification
---

# A Benchmark Study of Neural Network Compression Methods for Hyperspectral Image Classification
**arXiv**：[2603.04720v1](https://arxiv.org/abs/2603.04720) · [PDF](https://arxiv.org/pdf/2603.04720.pdf)  
**作者**：Sai Shi  

**一句话要点**：评估神经网络压缩方法在高光谱图像分类中的性能与效率

**关键词**：神经网络压缩, 高光谱图像分类, 剪枝, 量化, 知识蒸馏, 遥感应用

## 3 点简述
- 核心问题：深度神经网络在资源受限平台部署时面临计算和内存挑战
- 方法要点：系统评估剪枝、量化和知识蒸馏三种压缩策略
- 实验或效果：在基准数据集上验证压缩模型能保持分类性能并显著提升效率

## 摘要（原文）

> Deep neural networks have achieved strong performance in image classification tasks due to their ability to learn complex patterns from high-dimensional data. However, their large computational and memory requirements often limit deployment on resource-constrained platforms such as remote sensing devices and edge systems. Network compression techniques have therefore been proposed to reduce model size and computational cost while maintaining predictive performance. In this study, we conduct a systematic evaluation of neural network compression methods for a remote sensing application, namely hyperspectral land cover classification. Specifically, we examine three widely used compression strategies for convolutional neural networks: pruning, quantization, and knowledge distillation. Experiments are conducted on two benchmark hyperspectral datasets, considering classification accuracy, memory consumption, and inference efficiency. Our results demonstrate that compressed models can significantly reduce model size and computational cost while maintaining competitive classification performance. These findings provide insights into the trade-offs between compression ratio, efficiency, and accuracy, and highlight the potential of compression techniques for enabling efficient deep learning deployment in remote sensing applications.

