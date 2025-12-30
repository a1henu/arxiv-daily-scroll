---
layout: default
title: Adaptive Fusion Graph Network for 3D Strain Field Prediction in Solid Rocket Motor Grains
---

# Adaptive Fusion Graph Network for 3D Strain Field Prediction in Solid Rocket Motor Grains
**arXiv**：[2512.23443v1](https://arxiv.org/abs/2512.23443) · [PDF](https://arxiv.org/pdf/2512.23443.pdf)  
**作者**：Jiada Huang, Hao Ma, Zhibin Shen, Yizhou Qiao, Haiyang Li  

**一句话要点**：提出自适应融合图网络GrainGNet以预测固体火箭发动机药柱的3D应变场

**关键词**：图神经网络, 应变场预测, 固体火箭发动机, 自适应池化, 特征融合, 计算效率

## 3 点简述
- 核心问题：传统数值模拟计算成本高，现有代理模型难以显式建模几何并准确捕捉高应变区域。
- 方法要点：采用自适应池化动态节点选择机制保留关键力学特征，结合特征融合增强模型表示能力。
- 实验或效果：在联合预测任务中，相比基线图U-Net模型，均方误差降低62.8%，训练效率提升约7倍。

## 摘要（原文）

> Local high strain in solid rocket motor grains is a primary cause of structural failure. However, traditional numerical simulations are computationally expensive, and existing surrogate models cannot explicitly establish geometric models and accurately capture high-strain regions. Therefore, this paper proposes an adaptive graph network, GrainGNet, which employs an adaptive pooling dynamic node selection mechanism to effectively preserve the key mechanical features of structurally critical regions, while concurrently utilising feature fusion to transmit deep features and enhance the model's representational capacity. In the joint prediction task involving four sequential conditions--curing and cooling, storage, overloading, and ignition--GrainGNet reduces the mean squared error by 62.8% compared to the baseline graph U-Net model, with only a 5.2% increase in parameter count and an approximately sevenfold improvement in training efficiency. Furthermore, in the high-strain regions of debonding seams, the prediction error is further reduced by 33% compared to the second-best method, offering a computationally efficient and high-fidelity approach to evaluate motor structural safety.

