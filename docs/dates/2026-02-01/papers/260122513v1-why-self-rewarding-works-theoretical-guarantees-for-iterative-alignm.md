---
layout: default
title: Why Self-Rewarding Works: Theoretical Guarantees for Iterative Alignment of Language Models
---

# Why Self-Rewarding Works: Theoretical Guarantees for Iterative Alignment of Language Models
**arXiv**：[2601.22513v1](https://arxiv.org/abs/2601.22513) · [PDF](https://arxiv.org/pdf/2601.22513.pdf)  
**作者**：Shi Fu, Yingjie Wang, Shengchao Hu, Peng Wang, Dacheng Tao  

**一句话要点**：为自奖励语言模型提供首个理论保证，解释其迭代对齐机制

**关键词**：自奖励语言模型, 理论保证, 迭代对齐, 误差界, 模型初始化, 线性softmax模型

## 3 点简述
- 核心问题：自奖励语言模型缺乏理论解释，机制未明
- 方法要点：建立单步更新下界和全迭代误差界，揭示指数衰减依赖
- 实验或效果：在线性softmax模型类中实例化，连接理论到实践

## 摘要（原文）

> Self-Rewarding Language Models (SRLMs) achieve notable success in iteratively improving alignment without external feedback. Yet, despite their striking empirical progress, the core mechanisms driving their capabilities remain unelucidated, leaving a critical gap in theoretical understanding. This paper provides the first rigorous theoretical guarantees for SRLMs. We first establish a lower bound that characterizes the fundamental limits of a single update step, revealing a critical dependence on the quality of the initial model. We then derive finite-sample error bounds for the full iterative paradigm, showing that performance improves at a rate of $\widetilde{\mathcal{O}}\left(1/\sqrt{n}\right)$ with sample size $n$. Crucially, our analysis reveals that the dependence on the initial model decays exponentially with the number of iterations $T$. This provides a formal explanation for why self-rewarding succeeds: it robustly overcomes poor initialization by steering the dynamics toward internal stability and consistency. Finally, we instantiate our theoretical framework for the linear softmax model class, yielding tailored guarantees that connect our high-level insights to practical model architectures.

