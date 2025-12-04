---
layout: default
title: Scalable Decision Focused Learning via Online Trainable Surrogates
---

# Scalable Decision Focused Learning via Online Trainable Surrogates
**arXiv**：[2512.03861v1](https://arxiv.org/abs/2512.03861) · [PDF](https://arxiv.org/pdf/2512.03861.pdf)  
**作者**：Gaetano Signorelli, Michele Lombardi  

**一句话要点**：提出在线可训练代理方法以解决决策聚焦学习中的可扩展性问题

**关键词**：决策聚焦学习, 代理模型, 可扩展优化, 黑盒优化, 在线训练

## 3 点简述
- 核心问题：传统参数估计导致决策次优，决策聚焦学习训练时计算成本高
- 方法要点：使用无偏代理替代昂贵损失评估，支持黑盒设置并允许回退机制
- 实验或效果：减少求解器调用，解质量与先进技术相当

## 摘要（原文）

> Decision support systems often rely on solving complex optimization problems that may require to estimate uncertain parameters beforehand. Recent studies have shown how using traditionally trained estimators for this task can lead to suboptimal solutions. Using the actual decision cost as a loss function (called Decision Focused Learning) can address this issue, but with a severe loss of scalability at training time. To address this issue, we propose an acceleration method based on replacing costly loss function evaluations with an efficient surrogate. Unlike previously defined surrogates, our approach relies on unbiased estimators reducing the risk of spurious local optima and can provide information on its local confidence allowing one to switch to a fallback method when needed. Furthermore, the surrogate is designed for a black-box setting, which enables compensating for simplifications in the optimization model and account- ing for recourse actions during cost computation. In our results, the method reduces costly inner solver calls, with a solution quality comparable to other state-of-the-art techniques.

