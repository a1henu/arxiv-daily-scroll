---
layout: default
title: Adaptive Structured Pruning of Convolutional Neural Networks for Time Series Classification
---

# Adaptive Structured Pruning of Convolutional Neural Networks for Time Series Classification
**arXiv**：[2602.12744v1](https://arxiv.org/abs/2602.12744) · [PDF](https://arxiv.org/pdf/2602.12744.pdf)  
**作者**：Javidan Abdullayev, Maxime Devanne, Cyril Meyer, Ali Ismail-Fawaz, Jonathan Weber, Germain Forestier  

**一句话要点**：提出动态结构化剪枝框架以自动压缩时间序列分类模型，适用于资源受限设备部署。

**关键词**：时间序列分类, 结构化剪枝, 模型压缩, 卷积神经网络, 资源受限设备, 自适应剪枝

## 3 点简述
- 核心问题：时间序列分类模型计算和内存需求高，现有结构化剪枝方法依赖手动调参，限制可扩展性。
- 方法要点：引入实例级稀疏损失诱导通道稀疏，通过全局激活分析自动识别并剪枝冗余滤波器，无需预设剪枝比例。
- 实验或效果：在128个UCR数据集上验证，对LITETime和InceptionTime架构分别实现平均58%和75%压缩，保持分类准确率。

## 摘要（原文）

> Deep learning models for Time Series Classification (TSC) have achieved strong predictive performance but their high computational and memory requirements often limit deployment on resource-constrained devices. While structured pruning can address these issues by removing redundant filters, existing methods typically rely on manually tuned hyperparameters such as pruning ratios which limit scalability and generalization across datasets. In this work, we propose Dynamic Structured Pruning (DSP), a fully automatic, structured pruning framework for convolution-based TSC models. DSP introduces an instance-wise sparsity loss during training to induce channel-level sparsity, followed by a global activation analysis to identify and prune redundant filters without needing any predefined pruning ratio. This work tackles computational bottlenecks of deep TSC models for deployment on resource-constrained devices. We validate DSP on 128 UCR datasets using two different deep state-of-the-art architectures: LITETime and InceptionTime. Our approach achieves an average compression of 58% for LITETime and 75% for InceptionTime architectures while maintaining classification accuracy. Redundancy analyses confirm that DSP produces compact and informative representations, offering a practical path for scalable and efficient deep TSC deployment.

