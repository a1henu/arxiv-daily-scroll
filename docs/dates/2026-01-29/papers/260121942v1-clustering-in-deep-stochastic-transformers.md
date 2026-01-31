---
layout: default
title: Clustering in Deep Stochastic Transformers
---

# Clustering in Deep Stochastic Transformers
**arXiv**：[2601.21942v1](https://arxiv.org/abs/2601.21942) · [PDF](https://arxiv.org/pdf/2601.21942.pdf)  
**作者**：Lev Fedorov, Michaël E. Sander, Romuald Elie, Pierre Marion, Mathieu Laurière  

**一句话要点**：分析深度Transformer随机初始化噪声，揭示其防止token坍缩并诱导相变

**关键词**：Transformer理论分析, 随机初始化, token动态, 相变, 交互粒子系统

## 3 点简述
- 核心问题：确定性理论预测token会坍缩至单点，但未考虑标准随机初始化噪声的影响
- 方法要点：在扩散缩放和RMS归一化下，证明token动态收敛于球面上的交互粒子系统
- 实验效果：数值实验证实相变存在，抑制噪声会降低模型准确率

## 摘要（原文）

> Transformers have revolutionized deep learning across various domains but understanding the precise token dynamics remains a theoretical challenge. Existing theories of deep Transformers with layer normalization typically predict that tokens cluster to a single point; however, these results rely on deterministic weight assumptions, which fail to capture the standard initialization scheme in Transformers. In this work, we show that accounting for the intrinsic stochasticity of random initialization alters this picture. More precisely, we analyze deep Transformers where noise arises from the random initialization of value matrices. Under diffusion scaling and token-wise RMS normalization, we prove that, as the number of Transformer layers goes to infinity, the discrete token dynamics converge to an interacting-particle system on the sphere where tokens are driven by a \emph{common} matrix-valued Brownian noise. In this limit, we show that initialization noise prevents the collapse to a single cluster predicted by deterministic models. For two tokens, we prove a phase transition governed by the interaction strength and the token dimension: unlike deterministic attention flows, antipodal configurations become attracting with positive probability. Numerical experiments confirm the predicted transition, reveal that antipodal formations persist for more than two tokens, and demonstrate that suppressing the intrinsic noise degrades accuracy.

