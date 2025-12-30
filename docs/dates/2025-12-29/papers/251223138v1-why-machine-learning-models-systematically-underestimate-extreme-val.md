---
layout: default
title: Why Machine Learning Models Systematically Underestimate Extreme Values II: How to Fix It with LatentNN
---

# Why Machine Learning Models Systematically Underestimate Extreme Values II: How to Fix It with LatentNN
**arXiv**：[2512.23138v1](https://arxiv.org/abs/2512.23138) · [PDF](https://arxiv.org/pdf/2512.23138.pdf)  
**作者**：Yuan-Sen Ting  

**一句话要点**：提出LatentNN方法以解决天文数据中神经网络对极端值的系统性低估问题

**关键词**：衰减偏差校正, 潜在变量模型, 神经网络优化, 天文数据分析, 低信噪比推断

## 3 点简述
- 核心问题：神经网络因输入变量测量误差导致回归系数系统性低估，即衰减偏差
- 方法要点：通过联合优化网络参数和潜在输入值，最大化输入和输出的联合似然
- 实验或效果：在一维回归、多变量输入和恒星光谱应用中，LatentNN有效减少衰减偏差

## 摘要（原文）

> Attenuation bias -- the systematic underestimation of regression coefficients due to measurement errors in input variables -- affects astronomical data-driven models. For linear regression, this problem was solved by treating the true input values as latent variables to be estimated alongside model parameters. In this paper, we show that neural networks suffer from the same attenuation bias and that the latent variable solution generalizes directly to neural networks. We introduce LatentNN, a method that jointly optimizes network parameters and latent input values by maximizing the joint likelihood of observing both inputs and outputs. We demonstrate the correction on one-dimensional regression, multivariate inputs with correlated features, and stellar spectroscopy applications. LatentNN reduces attenuation bias across a range of signal-to-noise ratios where standard neural networks show large bias. This provides a framework for improved neural network inference in the low signal-to-noise regime characteristic of astronomical data. This bias correction is most effective when measurement errors are less than roughly half the intrinsic data range; in the regime of very low signal-to-noise and few informative features. Code is available at https://github.com/tingyuansen/LatentNN.

