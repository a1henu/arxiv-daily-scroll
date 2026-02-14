---
layout: default
title: External Division of Two Bregman Proximity Operators for Poisson Inverse Problems
---

# External Division of Two Bregman Proximity Operators for Poisson Inverse Problems
**arXiv**：[2602.11482v1](https://arxiv.org/abs/2602.11482) · [PDF](https://arxiv.org/pdf/2602.11482.pdf)  
**作者**：Kazuki Haishima, Kyohei Suzuki, Konstantinos Slavakis  

**一句话要点**：提出外部除法Bregman邻近算子以解决泊松噪声下的稀疏向量恢复问题

**关键词**：泊松逆问题, 稀疏恢复, Bregman邻近算子, 外部除法, 图像恢复, NoLips算法

## 3 点简述
- 核心问题：从泊松噪声污染的线性模型中恢复稀疏向量，传统ℓ₁正则化存在估计偏差
- 方法要点：引入外部除法Bregman邻近算子促进稀疏解，并嵌入NoLips算法以替代标准算子
- 实验或效果：数值测试显示方法比传统KL方法收敛更稳定，在合成数据和图像恢复中性能显著提升

## 摘要（原文）

> This paper presents a novel method for recovering sparse vectors from linear models corrupted by Poisson noise. The contribution is twofold. First, an operator defined via the external division of two Bregman proximity operators is introduced to promote sparse solutions while mitigating the estimation bias induced by classical $\ell_1$-norm regularization. This operator is then embedded into the already established NoLips algorithm, replacing the standard Bregman proximity operator in a plug-and-play manner. Second, the geometric structure of the proposed external-division operator is elucidated through two complementary reformulations, which provide clear interpretations in terms of the primal and dual spaces of the Poisson inverse problem. Numerical tests show that the proposed method exhibits more stable convergence behavior than conventional Kullback-Leibler (KL)-based approaches and achieves significantly superior performance on synthetic data and an image restoration problem.

