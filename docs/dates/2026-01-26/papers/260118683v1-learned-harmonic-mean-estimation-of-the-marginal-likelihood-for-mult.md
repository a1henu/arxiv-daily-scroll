---
layout: default
title: Learned harmonic mean estimation of the marginal likelihood for multimodal posteriors with flow matching
---

# Learned harmonic mean estimation of the marginal likelihood for multimodal posteriors with flow matching
**arXiv**：[2601.18683v1](https://arxiv.org/abs/2601.18683) · [PDF](https://arxiv.org/pdf/2601.18683.pdf)  
**作者**：Alicja Polanska, Jason D. McEwen  

**一句话要点**：提出基于流匹配的连续归一化流以改进学习调和平均估计器，处理多模态后验的边际似然计算

**关键词**：边际似然估计, 学习调和平均, 流匹配, 连续归一化流, 多模态后验, 贝叶斯模型比较

## 3 点简述
- 核心问题：学习调和平均估计器在处理多模态后验时内部密度估计可能失效
- 方法要点：引入流匹配连续归一化流作为内部密度估计架构，提升对复杂后验的适应性
- 实验或效果：在20维参数示例中展示处理挑战性多模态后验的能力，无需微调或启发式修改

## 摘要（原文）

> The marginal likelihood, or Bayesian evidence, is a crucial quantity for Bayesian model comparison but its computation can be challenging for complex models, even in parameters space of moderate dimension. The learned harmonic mean estimator has been shown to provide accurate and robust estimates of the marginal likelihood simply using posterior samples. It is agnostic to the sampling strategy, meaning that the samples can be obtained using any method. This enables marginal likelihood calculation and model comparison with whatever sampling is most suitable for the task. However, the internal density estimators considered previously for the learned harmonic mean can struggle with highly multimodal posteriors. In this work we introduce flow matching-based continuous normalizing flows as a powerful architecture for the internal density estimation of the learned harmonic mean. We demonstrate the ability to handle challenging multimodal posteriors, including an example in 20 parameter dimensions, showcasing the method's ability to handle complex posteriors without the need for fine-tuning or heuristic modifications to the base distribution.

