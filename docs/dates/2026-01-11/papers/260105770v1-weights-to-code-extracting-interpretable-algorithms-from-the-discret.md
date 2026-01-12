---
layout: default
title: Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer
---

# Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer
**arXiv**：[2601.05770v1](https://arxiv.org/abs/2601.05770) · [PDF](https://arxiv.org/pdf/2601.05770.pdf)  
**作者**：Yifan Zhang, Wei Bi, Kechi Zhang, Dongming Jin, Jie Fu, Zhi Jin  

**一句话要点**：提出离散Transformer以解决Transformer中算法提取因特征纠缠而受阻的问题

**关键词**：算法提取, Transformer可解释性, 功能解耦, 离散化, 符号逻辑, 温度退火

## 3 点简述
- 核心问题：Transformer因特征纠缠（叠加）阻碍从连续表示提取符号算法
- 方法要点：通过功能解耦（数值注意力路由、数值MLP算术）和温度退火采样实现离散化
- 实验或效果：性能媲美RNN基线，扩展可解释性至连续变量域，支持程序细粒度控制

## 摘要（原文）

> Algorithm extraction aims to synthesize executable programs directly from models trained on specific algorithmic tasks, enabling de novo algorithm discovery without relying on human-written code. However, extending this paradigm to Transformer is hindered by superposition, where entangled features encoded in overlapping directions obstruct the extraction of symbolic expressions. In this work, we propose the Discrete Transformer, an architecture explicitly engineered to bridge the gap between continuous representations and discrete symbolic logic. By enforcing a strict functional disentanglement, which constrains Numerical Attention to information routing and Numerical MLP to element-wise arithmetic, and employing temperature-annealed sampling, our method effectively facilitates the extraction of human-readable programs. Empirically, the Discrete Transformer not only achieves performance comparable to RNN-based baselines but crucially extends interpretability to continuous variable domains. Moreover, our analysis of the annealing process shows that the efficient discrete search undergoes a clear phase transition from exploration to exploitation. We further demonstrate that our method enables fine-grained control over synthesized programs by imposing inductive biases. Collectively, these findings establish the Discrete Transformer as a robust framework for demonstration-free algorithm discovery, offering a rigorous pathway toward Transformer interpretability.

