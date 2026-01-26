---
layout: default
title: Dual-Prototype Disentanglement: A Context-Aware Enhancement Framework for Time Series Forecasting
---

# Dual-Prototype Disentanglement: A Context-Aware Enhancement Framework for Time Series Forecasting
**arXiv**：[2601.16632v1](https://arxiv.org/abs/2601.16632) · [PDF](https://arxiv.org/pdf/2601.16632.pdf)  
**作者**：Haonan Yang, Jianchao Tang, Zhuo Li  

**一句话要点**：提出双原型自适应解缠框架以增强时间序列预测的上下文感知能力

**关键词**：时间序列预测, 模式解缠, 上下文感知, 原型学习, 自适应增强

## 3 点简述
- 核心问题：现有方法难以动态解缠和利用时间序列中复杂交织的时序模式，导致学习静态平均表示，缺乏上下文感知能力。
- 方法要点：构建动态双原型库，包括捕捉趋势或季节模式的常见模式库和动态记忆关键罕见事件的罕见模式库，通过双路径上下文感知路由机制选择性检索模式表示以增强输出。
- 实验或效果：综合实验表明，该框架能一致提升多种先进模型在真实世界基准上的预测性能和可靠性。

## 摘要（原文）

> Time series forecasting has witnessed significant progress with deep learning. While prevailing approaches enhance forecasting performance by modifying architectures or introducing novel enhancement strategies, they often fail to dynamically disentangle and leverage the complex, intertwined temporal patterns inherent in time series, thus resulting in the learning of static, averaged representations that lack context-aware capabilities. To address this, we propose the Dual-Prototype Adaptive Disentanglement framework (DPAD), a model-agnostic auxiliary method that equips forecasting models with the ability of pattern disentanglement and context-aware adaptation. Specifically, we construct a Dynamic Dual-Prototype bank (DDP), comprising a common pattern bank with strong temporal priors to capture prevailing trend or seasonal patterns, and a rare pattern bank dynamically memorizing critical yet infrequent events, and then an Dual-Path Context-aware routing (DPC) mechanism is proposed to enhance outputs with selectively retrieved context-specific pattern representations from the DDP. Additionally, we introduce a Disentanglement-Guided Loss (DGLoss) to ensure that each prototype bank specializes in its designated role while maintaining comprehensive coverage. Comprehensive experiments demonstrate that DPAD consistently improves forecasting performance and reliability of state-of-the-art models across diverse real-world benchmarks.

