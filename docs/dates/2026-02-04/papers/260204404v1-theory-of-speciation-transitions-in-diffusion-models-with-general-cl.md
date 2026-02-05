---
layout: default
title: Theory of Speciation Transitions in Diffusion Models with General Class Structure
---

# Theory of Speciation Transitions in Diffusion Models with General Class Structure
**arXiv**：[2602.04404v1](https://arxiv.org/abs/2602.04404) · [PDF](https://arxiv.org/pdf/2602.04404.pdf)  
**作者**：Beatrice Achilli, Marco Benedetti, Giulio Biroli, Marc Mézard  

**一句话要点**：提出扩散模型中物种形成转变的通用理论，适用于任意类结构的目标分布。

**关键词**：扩散模型, 物种形成转变, 贝叶斯分类, 自由熵差, 伊辛模型, 高斯混合

## 3 点简述
- 核心问题：现有理论局限于类可通过一阶矩识别，如高斯混合模型，无法处理高阶或集体特征差异的类。
- 方法要点：基于贝叶斯分类形式化类结构，用类间自由熵差表征物种形成时间，扩展至任意目标分布。
- 实验或效果：在可解析的一维伊辛模型和零均值高斯混合上验证理论，预测多类和连续细化类承诺。

## 摘要（原文）

> Diffusion Models generate data by reversing a stochastic diffusion process, progressively transforming noise into structured samples drawn from a target distribution. Recent theoretical work has shown that this backward dynamics can undergo sharp qualitative transitions, known as speciation transitions, during which trajectories become dynamically committed to data classes. Existing theoretical analyses, however, are limited to settings where classes are identifiable through first moments, such as mixtures of Gaussians with well-separated means. In this work, we develop a general theory of speciation in diffusion models that applies to arbitrary target distributions admitting well-defined classes. We formalize the notion of class structure through Bayes classification and characterize speciation times in terms of free-entropy difference between classes. This criterion recovers known results in previously studied Gaussian-mixture models, while extending to situations in which classes are not distinguishable by first moments and may instead differ through higher-order or collective features. Our framework also accommodates multiple classes and predicts the existence of successive speciation times associated with increasingly fine-grained class commitment. We illustrate the theory on two analytically tractable examples: mixtures of one-dimensional Ising models at different temperatures and mixtures of zero-mean Gaussians with distinct covariance structures. In the Ising case, we obtain explicit expressions for speciation times by mapping the problem onto a random-field Ising model and solving it via the replica method. Our results provide a unified and broadly applicable description of speciation transitions in diffusion-based generative models.

