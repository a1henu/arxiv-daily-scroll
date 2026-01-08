---
layout: default
title: Bayes-PD: Exploring a Sequence to Binding Bayesian Neural Network model trained on Phage Display data
---

# Bayes-PD: Exploring a Sequence to Binding Bayesian Neural Network model trained on Phage Display data
**arXiv**：[2601.03930v1](https://arxiv.org/abs/2601.03930) · [PDF](https://arxiv.org/pdf/2601.03930.pdf)  
**作者**：Ilann Amiaud-Plachy, Michael Blank, Oliver Bent, Sebastien Boyer  

**一句话要点**：提出基于噬菌体展示数据的序列到结合贝叶斯神经网络模型，以模拟实验噪声并提升模型可靠性。

**关键词**：噬菌体展示, 贝叶斯神经网络, 蛋白质设计, 实验噪声模拟, 结合亲和力预测

## 3 点简述
- 核心问题：噬菌体展示数据在深度学习蛋白质设计中未充分利用，因高噪声、预处理复杂和结果解释困难。
- 方法要点：采用贝叶斯神经网络在训练循环中模拟噬菌体展示实验及其噪声，以理解实验噪声和模型不确定性。
- 实验或效果：使用实际结合亲和力测量验证方法，而非仅依赖噬菌体展示轮次的代理值，以可靠解释实验。

## 摘要（原文）

> Phage display is a powerful laboratory technique used to study the interactions between proteins and other molecules, whether other proteins, peptides, DNA or RNA. The under-utilisation of this data in conjunction with deep learning models for protein design may be attributed to; high experimental noise levels; the complex nature of data pre-processing; and difficulty interpreting these experimental results. In this work, we propose a novel approach utilising a Bayesian Neural Network within a training loop, in order to simulate the phage display experiment and its associated noise. Our goal is to investigate how understanding the experimental noise and model uncertainty can enable the reliable application of such models to reliably interpret phage display experiments. We validate our approach using actual binding affinity measurements instead of relying solely on proxy values derived from 'held-out' phage display rounds.

