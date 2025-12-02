---
layout: default
title: Does Flatness imply Generalization for Logistic Loss in Univariate Two-Layer ReLU Network?
---

# Does Flatness imply Generalization for Logistic Loss in Univariate Two-Layer ReLU Network?
**arXiv**：[2512.01473v1](https://arxiv.org/abs/2512.01473) · [PDF](https://arxiv.org/pdf/2512.01473.pdf)  
**作者**：Dan Qiao, Yu-Xiang Wang  

**一句话要点**：探究单变量两层ReLU网络中平坦解在逻辑损失下的泛化性，揭示其局限性

**关键词**：平坦解, 逻辑损失, ReLU网络, 泛化性, 过拟合, 单变量输入

## 3 点简述
- 研究平坦解在逻辑损失下是否保证泛化，针对过参数化单变量ReLU网络
- 证明平坦解在特定不确定集内具有近最优泛化界，但存在无限平坦的过拟合解
- 通过模拟实验验证理论预测，展示平坦性与泛化关系的复杂性

## 摘要（原文）

> We consider the problem of generalization of arbitrarily overparameterized two-layer ReLU Neural Networks with univariate input. Recent work showed that under square loss, flat solutions (motivated by flat / stable minima and Edge of Stability phenomenon) provably cannot overfit, but it remains unclear whether the same phenomenon holds for logistic loss. This is a puzzling open problem because existing work on logistic loss shows that gradient descent with increasing step size converges to interpolating solutions (at infinity, for the margin-separable cases). In this paper, we prove that the \emph{flatness implied generalization} is more delicate under logistic loss. On the positive side, we show that flat solutions enjoy near-optimal generalization bounds within a region between the left-most and right-most \emph{uncertain} sets determined by each candidate solution. On the negative side, we show that there exist arbitrarily flat yet overfitting solutions at infinity that are (falsely) certain everywhere, thus certifying that flatness alone is insufficient for generalization in general. We demonstrate the effects predicted by our theory in a well-controlled simulation study.

