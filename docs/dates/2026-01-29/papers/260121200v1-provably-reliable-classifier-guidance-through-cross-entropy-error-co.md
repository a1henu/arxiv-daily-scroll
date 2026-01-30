---
layout: default
title: Provably Reliable Classifier Guidance through Cross-entropy Error Control
---

# Provably Reliable Classifier Guidance through Cross-entropy Error Control
**arXiv**：[2601.21200v1](https://arxiv.org/abs/2601.21200) · [PDF](https://arxiv.org/pdf/2601.21200.pdf)  
**作者**：Sharan Sahu, Arisina Banerjee, Yuchen Wu  

**一句话要点**：提出基于交叉熵误差控制的分类器引导方法，确保扩散模型采样可靠性

**关键词**：扩散模型, 分类器引导, 交叉熵误差, 采样误差, 理论分析, 条件生成

## 3 点简述
- 核心问题：标准分类器训练是否保证扩散模型引导向量的有效性未知
- 方法要点：在分类器平滑假设下，控制交叉熵误差可量化引导向量误差
- 实验或效果：理论证明引导向量误差上界，并构造反例强调平滑假设必要性

## 摘要（原文）

> Classifier-guided diffusion models generate conditional samples by augmenting the reverse-time score with the gradient of a learned classifier, yet it remains unclear whether standard classifier training procedures yield effective diffusion guidance. We address this gap by showing that, under mild smoothness assumptions on the classifiers, controlling the cross-entropy error at each diffusion step also controls the error of the resulting guidance vectors: classifiers achieving conditional KL divergence $\varepsilon^2$ from the ground-truth conditional label probabilities induce guidance vectors with mean squared error $\widetilde{O}(d \varepsilon )$. Our result yields an upper bound on the sampling error under classifier guidance and bears resemblance to a reverse log-Sobolev-type inequality. Moreover, we show that the classifier smoothness assumption is essential, by constructing simple counterexamples demonstrating that, without it, control of the guidance vector can fail for almost all distributions. To our knowledge, our work establishes the first quantitative link between classifier training and guidance alignment, yielding both a theoretical foundation for classifier guidance and principled guidelines for classifier selection.

