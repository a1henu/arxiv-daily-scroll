---
layout: default
title: Twinning Complex Networked Systems: Data-Driven Calibration of the mABCD Synthetic Graph Generator
---

# Twinning Complex Networked Systems: Data-Driven Calibration of the mABCD Synthetic Graph Generator
**arXiv**：[2602.02044v1](https://arxiv.org/abs/2602.02044) · [PDF](https://arxiv.org/pdf/2602.02044.pdf)  
**作者**：Piotr Bródka, Michał Czuba, Bogumił Kamiński, Łukasz Kraiński, Katarzyna Musial, Paweł Prałat, Mateusz Stolarski  

**一句话要点**：提出数据驱动方法校准mABCD多层网络生成器，以创建真实系统的数字孪生网络。

**关键词**：多层网络, 图生成器, 数字孪生, 参数校准, 数据驱动方法, 网络分析

## 3 点简述
- 核心问题：多层网络分析因大规模实证数据稀缺而受限，现有图生成器引入系统偏差。
- 方法要点：从真实系统推断mABCD生成器的配置参数，采用联合预测而非独立估计以应对参数强依赖。
- 实验或效果：任务非平凡，需量化误差，验证合成网络能作为原始结构的数字孪生。

## 摘要（原文）

> The increasing availability of relational data has contributed to a growing reliance on network-based representations of complex systems. Over time, these models have evolved to capture more nuanced properties, such as the heterogeneity of relationships, leading to the concept of multilayer networks. However, the analysis and evaluation of methods for these structures is often hindered by the limited availability of large-scale empirical data. As a result, graph generators are commonly used as a workaround, albeit at the cost of introducing systematic biases. In this paper, we address the inverse-generator problem by inferring the configuration parameters of a multilayer network generator, mABCD, from a real-world system. Our goal is to identify parameter settings that enable the generator to produce synthetic networks that act as digital twins of the original structure. We propose a method for estimating matching configurations and for quantifying the associated error. Our results demonstrate that this task is non-trivial, as strong interdependencies between configuration parameters weaken independent estimation and instead favour a joint-prediction approach.

