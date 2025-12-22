---
layout: default
title: DeepShare: Sharing ReLU Across Channels and Layers for Efficient Private Inference
---

# DeepShare: Sharing ReLU Across Channels and Layers for Efficient Private Inference
**arXiv**：[2512.17398v1](https://arxiv.org/abs/2512.17398) · [PDF](https://arxiv.org/pdf/2512.17398.pdf)  
**作者**：Yonathan Bornfeld, Shai Avidan  

**一句话要点**：提出DeepShare方法，通过跨通道和层共享DReLU以减少私有推理中的计算瓶颈。

**关键词**：私有推理, ReLU优化, 跨层共享, 计算效率, 图像分类, 图像分割

## 3 点简述
- 私有推理中ReLU计算是主要瓶颈，需减少其数量。
- 设计新激活模块，在原型通道执行DReLU，复制通道复用结果。
- 在ResNet类网络中大幅减少DReLU操作，提升分类和分割性能。

## 摘要（原文）

> Private Inference (PI) uses cryptographic primitives to perform privacy preserving machine learning. In this setting, the owner of the network runs inference on the data of the client without learning anything about the data and without revealing any information about the model. It has been observed that a major computational bottleneck of PI is the calculation of the gate (i.e., ReLU), so a considerable amount of effort have been devoted to reducing the number of ReLUs in a given network.
>   We focus on the DReLU, which is the non-linear step function of the ReLU and show that one DReLU can serve many ReLU operations. We suggest a new activation module where the DReLU operation is only performed on a subset of the channels (Prototype channels), while the rest of the channels (replicate channels) replicates the DReLU of each of their neurons from the corresponding neurons in one of the prototype channels. We then extend this idea to work across different layers.
>   We show that this formulation can drastically reduce the number of DReLU operations in resnet type network. Furthermore, our theoretical analysis shows that this new formulation can solve an extended version of the XOR problem, using just one non-linearity and two neurons, something that traditional formulations and some PI specific methods cannot achieve. We achieve new SOTA results on several classification setups, and achieve SOTA results on image segmentation.

