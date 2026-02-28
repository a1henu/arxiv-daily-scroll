---
layout: default
title: A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring
---

# A Decision-Theoretic Formalisation of Steganography With Applications to LLM Monitoring
**arXiv**：[2602.23163v1](https://arxiv.org/abs/2602.23163) · [PDF](https://arxiv.org/pdf/2602.23163.pdf)  
**作者**：Usman Anwar, Julianna Piskorz, David D. Baek, David Africa, Jim Weatherall, Max Tegmark, Christian Schroeder de Witt, Mihaela van der Schaar, David Krueger  

**一句话要点**：提出基于决策论的隐写术形式化框架，用于检测和量化大型语言模型中的隐写推理。

**关键词**：隐写术检测, 决策论框架, 大型语言模型监控, 信息不对称, 广义V-信息, 隐写间隙

## 3 点简述
- 核心问题：大型语言模型展现隐写能力，可能逃避监管，但传统检测方法因缺乏参考分布而不适用。
- 方法要点：引入决策论视角，定义广义V-信息和隐写间隙，通过代理行为推断信息不对称性。
- 实验或效果：经验验证框架有效性，能检测、量化和缓解模型中的隐写推理行为。

## 摘要（原文）

> Large language models are beginning to show steganographic capabilities. Such capabilities could allow misaligned models to evade oversight mechanisms. Yet principled methods to detect and quantify such behaviours are lacking. Classical definitions of steganography, and detection methods based on them, require a known reference distribution of non-steganographic signals. For the case of steganographic reasoning in LLMs, knowing such a reference distribution is not feasible; this renders these approaches inapplicable. We propose an alternative, \textbf{decision-theoretic view of steganography}. Our central insight is that steganography creates an asymmetry in usable information between agents who can and cannot decode the hidden content (present within a steganographic signal), and this otherwise latent asymmetry can be inferred from the agents' observable actions. To formalise this perspective, we introduce generalised $\mathcal{V}$-information: a utilitarian framework for measuring the amount of usable information within some input. We use this to define the \textbf{steganographic gap} -- a measure that quantifies steganography by comparing the downstream utility of the steganographic signal to agents that can and cannot decode the hidden content. We empirically validate our formalism, and show that it can be used to detect, quantify, and mitigate steganographic reasoning in LLMs.

