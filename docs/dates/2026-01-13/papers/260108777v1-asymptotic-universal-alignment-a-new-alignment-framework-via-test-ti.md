---
layout: default
title: Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling
---

# Asymptotic Universal Alignment: A New Alignment Framework via Test-Time Scaling
**arXiv**：[2601.08777v1](https://arxiv.org/abs/2601.08777) · [PDF](https://arxiv.org/pdf/2601.08777.pdf)  
**作者**：Yang Cai, Weiqiang Zheng  

**一句话要点**：提出渐近通用对齐框架，通过测试时缩放实现个性化大语言模型对齐

**关键词**：大语言模型对齐, 测试时缩放, 渐近通用对齐, 纳什均衡, 输出多样性, 多玩家游戏

## 3 点简述
- 核心问题：大语言模型对齐需满足用户异质偏好，现有方法缺乏输出多样性，导致测试时缩放效益不足。
- 方法要点：引入(k,f(k))-鲁棒对齐和渐近通用对齐概念，构建对称多玩家对齐游戏，其纳什均衡策略达到最优收敛率。
- 实验或效果：理论证明最优收敛率为f(k)=k/(k+1)，并扩展至对手也生成多响应场景，提供自学习动态收敛保证。

## 摘要（原文）

> Aligning large language models (LLMs) to serve users with heterogeneous and potentially conflicting preferences is a central challenge for personalized and trustworthy AI. We formalize an ideal notion of universal alignment through test-time scaling: for each prompt, the model produces $k\ge 1$ candidate responses and a user selects their preferred one. We introduce $(k,f(k))$-robust alignment, which requires the $k$-output model to have win rate $f(k)$ against any other single-output model, and asymptotic universal alignment (U-alignment), which requires $f(k)\to 1$ as $k\to\infty$. Our main result characterizes the optimal convergence rate: there exists a family of single-output policies whose $k$-sample product policies achieve U-alignment at rate $f(k)=\frac{k}{k+1}$, and no method can achieve a faster rate in general.
>   We show that popular post-training methods, including Nash learning from human feedback (NLHF), can fundamentally underutilize the benefits of test-time scaling. Even though NLHF is optimal for $k=1$, sampling from the resulting (often deterministic) policy cannot guarantee win rates above $\tfrac{1}{2}$ except for an arbitrarily small slack. This stems from a lack of output diversity: existing alignment methods can collapse to a single majority-preferred response, making additional samples redundant. In contrast, our approach preserves output diversity and achieves the optimal test-time scaling rate. In particular, we propose a family of symmetric multi-player alignment games and prove that any symmetric Nash equilibrium policy of the $(k+1)$-player alignment game achieves the optimal $(k,\frac{k}{k+1})$-robust alignment. Finally, we provide theoretical convergence guarantees for self-play learning dynamics in these games and extend the framework to opponents that also generate multiple responses.

