---
layout: default
title: Calibration without Ground Truth
---

# Calibration without Ground Truth
**arXiv**：[2601.19862v1](https://arxiv.org/abs/2601.19862) · [PDF](https://arxiv.org/pdf/2601.19862.pdf)  
**作者**：Yuqing Kong, Mingyu Song, Yizhou Wang, Yifan Wu  

**一句话要点**：提出无标签后处理框架，利用弱校准参考模型改进强但未校准模型

**关键词**：模型校准, 无标签学习, 后处理框架, Bregman投影, 损失函数优化, 大语言模型

## 3 点简述
- 核心问题：公开人类文本将耗尽，需无标签改进模型校准
- 方法要点：基于互不校准条件，开发Bregman投影算法保证损失降低
- 实验或效果：在多种规模LLM上显著减少校准误差，性能媲美监督基线

## 摘要（原文）

> Villalobos et al. [2024] predict that publicly available human text will be exhausted within the next decade. Thus, improving models without access to ground-truth labels becomes increasingly important. We propose a label-free post-processing framework that improves a strong but miscalibrated model using a weaker yet better-calibrated reference. Our framework guarantees a strict performance improvement under any proper loss. Our approach is based on a characterization of when strict improvement is possible: when the strong and reference models are not mutually calibrated. We formalize this condition, connect it to arbitrage and no-trade results from economics, and develop an efficient Bregman projection algorithm that guarantees worst-case loss reduction without labels. Experiments on representative LLMs across varying scales demonstrate that our label-free method significantly reduces proper losses and calibration errors, achieving performance competitive with supervised baselines.

