---
layout: default
title: Learning to bin: differentiable and Bayesian optimization for multi-dimensional discriminants in high-energy physics
---

# Learning to bin: differentiable and Bayesian optimization for multi-dimensional discriminants in high-energy physics
**arXiv**：[2601.07756v1](https://arxiv.org/abs/2601.07756) · [PDF](https://arxiv.org/pdf/2601.07756.pdf)  
**作者**：Johannes Erdmann, Nitish Kumar Kasaraguppe, Florian Mausolf  

**一句话要点**：提出基于高斯混合模型和优化策略的多维判别量分箱方法，以提升高能物理信号灵敏度。

**关键词**：高能物理分析, 多维分箱优化, 高斯混合模型, 可微分优化, 贝叶斯优化, 信号显著性

## 3 点简述
- 核心问题：高能物理分析中，事件分类常依赖手动选择分箱边界，导致信号灵敏度受限。
- 方法要点：使用高斯混合模型定义多维分箱形状，结合可微分和贝叶斯优化策略直接优化信号显著性。
- 实验或效果：在二元和三元分类任务中，方法优于等距分箱和一维投影，尤其在信号可分离性有限时表现突出。

## 摘要（原文）

> Categorizing events using discriminant observables is central to many high-energy physics analyses. Yet, bin boundaries are often chosen by hand. A simple, popular choice is to apply argmax projections of multi-class scores and equidistant binning of one-dimensional discriminants. We propose a binning optimization for signal significance directly in multi-dimensional discriminants. We use a Gaussian Mixture Model (GMM) to define flexible bin boundary shapes for multi-class scores, while in one dimension (binary classification) we move bin boundaries directly. On this binning model, we study two optimization strategies: a differentiable and a Bayesian optimization approach. We study two toy setups: a binary classification and a three-class problem with two signals and backgrounds. In the one-dimensional case, both approaches achieve similar gains in signal sensitivity compared to equidistant binnings for a given number of bins. In the multi-dimensional case, the GMM-based binning defines sensitive categories as well, with the differentiable approach performing best. We show that, in particular for limited separability of the signal processes, our approach outperforms argmax classification even with optimized binning in the one-dimensional projections. Both methods are released as lightweight Python plugins intended for straightforward integration into existing analyses.

