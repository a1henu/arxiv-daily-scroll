---
layout: default
title: FOZO: Forward-Only Zeroth-Order Prompt Optimization for Test-Time Adaptation
---

# FOZO: Forward-Only Zeroth-Order Prompt Optimization for Test-Time Adaptation
**arXiv**：[2603.04733v1](https://arxiv.org/abs/2603.04733) · [PDF](https://arxiv.org/pdf/2603.04733.pdf)  
**作者**：Xingyu Wang, Tao Wang  

**一句话要点**：提出FOZO方法，通过前向零阶提示优化实现资源受限场景下的测试时适应。

**关键词**：测试时适应, 零阶优化, 前向计算, 提示优化, 资源受限部署

## 3 点简述
- 核心问题：测试时适应中，基于反向传播的方法计算和内存需求高，不适合低端设备；传统无反向传播方法适应能力有限。
- 方法要点：采用内存高效的零阶提示优化，结合中间特征统计和预测熵目标，引入动态衰减扰动尺度确保稳定适应。
- 实验或效果：在ImageNet-C等数据集上表现优异，Top-1准确率达59.52%，优于基于梯度的方法和SOTA前向方法，并适用于量化模型。

## 摘要（原文）

> Test-Time Adaptation (TTA) is essential for enabling deep learning models to handle real-world data distribution shifts. However, current approaches face significant limitations: backpropagation-based methods are not suitable for low-end deployment devices, due to their high computation and memory requirements, as well as their tendency to modify model weights during adaptation; while traditional backpropagation-free techniques exhibit constrained adaptation capabilities. In this work, we propose Forward-Only Zeroth-Order Optimization (FOZO), a novel and practical backpropagation-free paradigm for TTA. FOZO leverages a memory-efficient zeroth-order prompt optimization, which is led by objectives optimizing both intermediate feature statistics and prediction entropy. To ensure efficient and stable adaptation over the out-of-distribution data stream, we introduce a dynamically decaying perturbation scale during zeroth-order gradient estimation and theoretically prove its convergence under the TTA data stream assumption. Extensive continual adaptation experiments on ImageNet-C, ImageNet-R, and ImageNet-Sketch demonstrate FOZO's superior performance, achieving 59.52% Top-1 accuracy on ImageNet-C (5K, level 5) and outperforming main gradient-based methods and SOTA forward-only FOA (58.13%). Furthermore, FOZO exhibits strong generalization on quantized (INT8) models. These findings demonstrate that FOZO is a highly competitive solution for TTA deployment in resource-limited scenarios.

