---
layout: default
title: Uniform error bounds for quantized dynamical models
---

# Uniform error bounds for quantized dynamical models
**arXiv**：[2602.15586v1](https://arxiv.org/abs/2602.15586) · [PDF](https://arxiv.org/pdf/2602.15586.pdf)  
**作者**：Abdelkader Metakalard, Fabien Lauer, Kevin Colin, Marion Gilson  

**一句话要点**：提出量化动态模型的均匀误差界，以解决依赖数据序列学习中的统计保证问题。

**关键词**：量化模型, 动态系统识别, 误差界, 统计保证, 依赖数据, 系统识别

## 3 点简述
- 核心问题：从依赖数据序列学习动态模型时，缺乏量化模型和不完美优化算法的统计准确性保证。
- 方法要点：通过块分解和间距点策略，开发慢速和快速、方差自适应的均匀误差界。
- 实验或效果：误差界随模型编码所需比特数缩放，将硬件约束转化为可解释的统计复杂度。

## 摘要（原文）

> This paper provides statistical guarantees on the accuracy of dynamical models learned from dependent data sequences. Specifically, we develop uniform error bounds that apply to quantized models and imperfect optimization algorithms commonly used in practical contexts for system identification, and in particular hybrid system identification. Two families of bounds are obtained: slow-rate bounds via a block decomposition and fast-rate, variance-adaptive, bounds via a novel spaced-point strategy. The bounds scale with the number of bits required to encode the model and thus translate hardware constraints into interpretable statistical complexities.

