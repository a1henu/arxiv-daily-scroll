---
layout: default
title: Online identification of nonlinear time-varying systems with uncertain information
---

# Online identification of nonlinear time-varying systems with uncertain information
**arXiv**：[2601.10379v1](https://arxiv.org/abs/2601.10379) · [PDF](https://arxiv.org/pdf/2601.10379.pdf)  
**作者**：He Ren, Gaowei Yan, Hang Liu, Lifeng Cao, Zhijun Zhao, Gang Dang  

**一句话要点**：提出贝叶斯回归符号学习框架，以解决数字孪生中非线性时变系统在线识别与不确定性量化问题。

**关键词**：数字孪生, 非线性系统识别, 贝叶斯推断, 在线学习, 不确定性量化, 符号回归

## 3 点简述
- 核心问题：现有方法难以同时满足数字孪生对高精度、可解释性和在线适应性的需求。
- 方法要点：将在线符号发现建模为概率状态空间模型，结合稀疏先验实现贝叶斯推断与不确定性量化。
- 实验或效果：案例研究验证了框架在可解释概率预测和在线学习方面的有效性，并提供了收敛性分析。

## 摘要（原文）

> Digital twins (DTs), serving as the core enablers for real-time monitoring and predictive maintenance of complex cyber-physical systems, impose critical requirements on their virtual models: high predictive accuracy, strong interpretability, and online adaptive capability. However, existing techniques struggle to meet these demands simultaneously: Bayesian methods excel in uncertainty quantification but lack model interpretability, while interpretable symbolic identification methods (e.g., SINDy) are constrained by their offline, batch-processing nature, which make real-time updates challenging. To bridge this semantic and computational gap, this paper proposes a novel Bayesian Regression-based Symbolic Learning (BRSL) framework. The framework formulates online symbolic discovery as a unified probabilistic state-space model. By incorporating sparse horseshoe priors, model selection is transformed into a Bayesian inference task, enabling simultaneous system identification and uncertainty quantification. Furthermore, we derive an online recursive algorithm with a forgetting factor and establish precise recursive conditions that guarantee the well-posedness of the posterior distribution. These conditions also function as real-time monitors for data utility, enhancing algorithmic robustness. Additionally, a rigorous convergence analysis is provided, demonstrating the convergence of parameter estimates under persistent excitation conditions. Case studies validate the effectiveness of the proposed framework in achieving interpretable, probabilistic prediction and online learning.

