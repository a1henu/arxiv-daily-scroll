---
layout: default
title: Token Sample Complexity of Attention
---

# Token Sample Complexity of Attention
**arXiv**：[2512.10656v1](https://arxiv.org/abs/2512.10656) · [PDF](https://arxiv.org/pdf/2512.10656.pdf)  
**作者**：Léa Bohbot, Cyril Letrouit, Gabriel Peyré, François-Xavier Vialard  

**一句话要点**：提出令牌样本复杂度以刻画注意力在长序列中的收敛行为

**关键词**：注意力机制, 样本复杂度, 收敛分析, 长序列建模, 软最大函数

## 3 点简述
- 核心问题：注意力机制在极端序列长度下的收敛速率未知
- 方法要点：分析注意力图点一致收敛和变换令牌分布矩的收敛界
- 实验或效果：在合成高斯数据和真实BERT模型上验证理论预测

## 摘要（原文）

> As context windows in large language models continue to expand, it is essential to characterize how attention behaves at extreme sequence lengths. We introduce token-sample complexity: the rate at which attention computed on $n$ tokens converges to its infinite-token limit. We estimate finite-$n$ convergence bounds at two levels: pointwise uniform convergence of the attention map, and convergence of moments for the transformed token distribution. For compactly supported (and more generally sub-Gaussian) distributions, our first result shows that the attention map converges uniformly on a ball of radius $R$ at rate $C(R)/\sqrt{n}$, where $C(R)$ grows exponentially with $R$. For large $R$, this estimate loses practical value, and our second result addresses this issue by establishing convergence rates for the moments of the transformed distribution (the token output of the attention layer). In this case, the rate is $C'(R)/n^β$ with $β<\tfrac{1}{2}$, and $C'(R)$ depends polynomially on the size of the support of the distribution. The exponent $β$ depends on the attention geometry and the spectral properties of the tokens distribution. We also examine the regime in which the attention parameter tends to infinity and the softmax approaches a hardmax, and in this setting, we establish a logarithmic rate of convergence. Experiments on synthetic Gaussian data and real BERT models on Wikipedia text confirm our predictions.

