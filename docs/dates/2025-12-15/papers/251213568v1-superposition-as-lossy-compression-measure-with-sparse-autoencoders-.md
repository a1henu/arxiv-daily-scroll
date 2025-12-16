---
layout: default
title: Superposition as Lossy Compression: Measure with Sparse Autoencoders and Connect to Adversarial Vulnerability
---

# Superposition as Lossy Compression: Measure with Sparse Autoencoders and Connect to Adversarial Vulnerability
**arXiv**：[2512.13568v1](https://arxiv.org/abs/2512.13568) · [PDF](https://arxiv.org/pdf/2512.13568.pdf)  
**作者**：Leonard Bereska, Zoe Tzifa-Kratira, Reza Samavi, Efstratios Gavves  

**一句话要点**：提出基于稀疏自编码器的信息论框架，以测量神经网络中的叠加现象及其与对抗鲁棒性的关系。

**关键词**：叠加现象, 稀疏自编码器, 信息论测量, 对抗鲁棒性, 特征压缩, 神经网络可解释性

## 3 点简述
- 核心问题：缺乏量化神经网络中特征叠加现象的原则性方法，影响可解释性。
- 方法要点：应用香农熵于稀疏自编码器激活，计算有效特征数作为无干扰编码所需最小神经元数。
- 实验或效果：在玩具模型中验证相关性，揭示对抗训练可增加有效特征，挑战叠加导致脆弱性的假设。

## 摘要（原文）

> Neural networks achieve remarkable performance through superposition: encoding multiple features as overlapping directions in activation space rather than dedicating individual neurons to each feature. This challenges interpretability, yet we lack principled methods to measure superposition. We present an information-theoretic framework measuring a neural representation's effective degrees of freedom. We apply Shannon entropy to sparse autoencoder activations to compute the number of effective features as the minimum neurons needed for interference-free encoding. Equivalently, this measures how many "virtual neurons" the network simulates through superposition. When networks encode more effective features than actual neurons, they must accept interference as the price of compression. Our metric strongly correlates with ground truth in toy models, detects minimal superposition in algorithmic tasks, and reveals systematic reduction under dropout. Layer-wise patterns mirror intrinsic dimensionality studies on Pythia-70M. The metric also captures developmental dynamics, detecting sharp feature consolidation during grokking. Surprisingly, adversarial training can increase effective features while improving robustness, contradicting the hypothesis that superposition causes vulnerability. Instead, the effect depends on task complexity and network capacity: simple tasks with ample capacity allow feature expansion (abundance regime), while complex tasks or limited capacity force reduction (scarcity regime). By defining superposition as lossy compression, this work enables principled measurement of how neural networks organize information under computational constraints, connecting superposition to adversarial robustness.

