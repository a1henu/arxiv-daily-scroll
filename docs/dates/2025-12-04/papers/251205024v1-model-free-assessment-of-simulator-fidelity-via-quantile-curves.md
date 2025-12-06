---
layout: default
title: Model-Free Assessment of Simulator Fidelity via Quantile Curves
---

# Model-Free Assessment of Simulator Fidelity via Quantile Curves
**arXiv**：[2512.05024v1](https://arxiv.org/abs/2512.05024) · [PDF](https://arxiv.org/pdf/2512.05024.pdf)  
**作者**：Garud Iyengar, Yu-Shiou Willy Lin, Kaizheng Wang  

**一句话要点**：提出基于分位数曲线的无模型方法，评估复杂系统模拟器与真实数据的差异。

**关键词**：模拟器保真度评估, 分位数曲线, 无模型方法, 黑盒模拟, 机器学习系统, 风险度量

## 3 点简述
- 核心问题：复杂机器学习系统模拟器与真实数据差异难以量化，传统方法受限。
- 方法要点：无模型估计模拟与真实结果分布差异的分位数函数，支持黑盒模拟器。
- 实验或效果：应用于LLM模拟保真度评估，展示在WorldValueBench数据集上的实用性。

## 摘要（原文）

> Simulation of complex systems originated in manufacturing and queuing applications. It is now widely used for large-scale, ML-based systems in research, education, and consumer surveys. However, characterizing the discrepancy between simulators and ground truth remains challenging for increasingly complex, machine-learning-based systems. We propose a computationally tractable method to estimate the quantile function of the discrepancy between the simulated and ground-truth outcome distributions. Our approach focuses on output uncertainty and treats the simulator as a black box, imposing no modeling assumptions on its internals, and hence applies broadly across many parameter families, from Bernoulli and multinomial models to continuous, vector-valued settings. The resulting quantile curve supports confidence interval construction for unseen scenarios, risk-aware summaries of sim-to-real discrepancy (e.g., VaR/CVaR), and comparison of simulators' performance. We demonstrate our methodology in an application assessing LLM simulation fidelity on the WorldValueBench dataset spanning four LLMs.

