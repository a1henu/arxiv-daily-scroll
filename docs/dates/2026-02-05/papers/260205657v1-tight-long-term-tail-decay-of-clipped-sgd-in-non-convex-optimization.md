---
layout: default
title: Tight Long-Term Tail Decay of (Clipped) SGD in Non-Convex Optimization
---

# Tight Long-Term Tail Decay of (Clipped) SGD in Non-Convex Optimization
**arXiv**：[2602.05657v1](https://arxiv.org/abs/2602.05657) · [PDF](https://arxiv.org/pdf/2602.05657.pdf)  
**作者**：Aleksandar Armacki, Dragana Bajović, Dušan Jakovetić, Soummya Kar, Ali H. Sayed  

**一句话要点**：提出基于大偏差理论的SGD长尾衰减分析，为非凸优化提供紧致长期尾概率界。

**关键词**：随机梯度下降, 非凸优化, 大偏差理论, 尾概率分析, 重尾噪声, 长期收敛

## 3 点简述
- 研究SGD算法在非凸优化中的长期尾衰减，填补现有有限时间分析的不足。
- 针对有界噪声和重尾噪声，分别给出SGD和c-SGD的梯度范数平方尾概率上界。
- 证明衰减率紧致性，相比现有工作展示更快长期衰减，增强个体运行保证。

## 摘要（原文）

> The study of tail behaviour of SGD-induced processes has been attracting a lot of interest, due to offering strong guarantees with respect to individual runs of an algorithm. While many works provide high-probability guarantees, quantifying the error rate for a fixed probability threshold, there is a lack of work directly studying the probability of failure, i.e., quantifying the tail decay rate for a fixed error threshold. Moreover, existing results are of finite-time nature, limiting their ability to capture the true long-term tail decay which is more informative for modern learning models, typically trained for millions of iterations. Our work closes these gaps, by studying the long-term tail decay of SGD-based methods through the lens of large deviations theory, establishing several strong results in the process. First, we provide an upper bound on the tails of the gradient norm-squared of the best iterate produced by (vanilla) SGD, for non-convex costs and bounded noise, with long-term decay at rate $e^{-t/\log(t)}$. Next, we relax the noise assumption by considering clipped SGD (c-SGD) under heavy-tailed noise with bounded moment of order $p \in (1,2]$, showing an upper bound with long-term decay at rate $e^{-t^{β_p}/\log(t)}$, where $β_p = \frac{4(p-1)}{3p-2}$ for $p \in (1,2)$ and $e^{-t/\log^2(t)}$ for $p = 2$. Finally, we provide lower bounds on the tail decay, at rate $e^{-t}$, showing that our rates for both SGD and c-SGD are tight, up to poly-logarithmic factors. Notably, our results demonstrate an order of magnitude faster long-term tail decay compared to existing work based on finite-time bounds, which show rates $e^{-\sqrt{t}}$ and $e^{-t^{β_p/2}}$, $p \in (1,2]$, for SGD and c-SGD, respectively. As such, we uncover regimes where the tails decay much faster than previously known, providing stronger long-term guarantees for individual runs.

