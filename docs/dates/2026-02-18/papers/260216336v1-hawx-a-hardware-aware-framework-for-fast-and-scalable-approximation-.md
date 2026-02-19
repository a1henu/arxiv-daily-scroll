---
layout: default
title: HAWX: A Hardware-Aware FrameWork for Fast and Scalable ApproXimation of DNNs
---

# HAWX: A Hardware-Aware FrameWork for Fast and Scalable ApproXimation of DNNs
**arXiv**：[2602.16336v1](https://arxiv.org/abs/2602.16336) · [PDF](https://arxiv.org/pdf/2602.16336.pdf)  
**作者**：Samira Nazari, Mohammad Saeed Almasi, Mahdi Taheri, Ali Azarpeyvand, Ali Mokhtari, Ali Mahani, Christian Herglotz  

**一句话要点**：提出HAWX框架，通过硬件感知多级敏感度评分指导近似计算块集成，加速DNN近似配置搜索。

**关键词**：硬件感知框架, 近似计算, DNN加速, 多级敏感度评分, 配置搜索优化

## 3 点简述
- 核心问题：DNN近似计算配置搜索耗时，需平衡精度、功耗和面积。
- 方法要点：在算子、滤波器、层和模型级别进行多级敏感度评分，支持预测模型加速评估。
- 实验或效果：在VGG-11等基准上实现指数级加速，保持精度接近穷举搜索。

## 摘要（原文）

> This work presents HAWX, a hardware-aware scalable exploration framework that employs multi-level sensitivity scoring at different DNN abstraction levels (operator, filter, layer, and model) to guide selective integration of heterogeneous AxC blocks. Supported by predictive models for accuracy, power, and area, HAWX accelerates the evaluation of candidate configurations, achieving over 23* speedup in a layer-level search with two candidate approximate blocks and more than (3*106)* speedup at the filter-level search only for LeNet-5, while maintaining accuracy comparable to exhaustive search. Experiments across state-of-the-art DNN benchmarks such as VGG-11, ResNet-18, and EfficientNetLite demonstrate that the efficiency benefits of HAWX scale exponentially with network size. The HAWX hardware-aware search algorithm supports both spatial and temporal accelerator architectures, leveraging either off-the-shelf approximate components or customized designs.

