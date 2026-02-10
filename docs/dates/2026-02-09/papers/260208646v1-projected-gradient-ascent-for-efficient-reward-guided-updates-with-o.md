---
layout: default
title: Projected Gradient Ascent for Efficient Reward-Guided Updates with One-Step Generative Models
---

# Projected Gradient Ascent for Efficient Reward-Guided Updates with One-Step Generative Models
**arXiv**：[2602.08646v1](https://arxiv.org/abs/2602.08646) · [PDF](https://arxiv.org/pdf/2602.08646.pdf)  
**作者**：Jisung Hwang, Minhyuk Sung  

**一句话要点**：提出投影梯度上升方法，以高效可靠地实现基于奖励引导的生成模型更新。

**关键词**：奖励引导生成, 潜在优化, 投影梯度上升, 白高斯噪声约束, 测试时优化

## 3 点简述
- 核心问题：测试时潜在优化易导致奖励黑客和效率低下，影响生成质量。
- 方法要点：用硬白高斯噪声约束替换软正则化，通过投影梯度上升保持噪声特性。
- 实验或效果：在仅需30%时间下达到可比美学分数，防止奖励黑客。

## 摘要（原文）

> We propose a constrained latent optimization method for reward-guided generation that preserves white Gaussian noise characteristics with negligible overhead. Test-time latent optimization can unlock substantially better reward-guided generations from pretrained generative models, but it is prone to reward hacking that degrades quality and also too slow for practical use. In this work, we make test-time optimization both efficient and reliable by replacing soft regularization with hard white Gaussian noise constraints enforced via projected gradient ascent. Our method applies a closed-form projection after each update to keep the latent vector explicitly noise-like throughout optimization, preventing the drift that leads to unrealistic artifacts. This enforcement adds minimal cost: the projection matches the $O(N \log N)$ complexity of standard algorithms such as sorting or FFT and does not practically increase wall-clock time. In experiments, our approach reaches a comparable Aesthetic Score using only 30% of the wall-clock time required by the SOTA regularization-based method, while preventing reward hacking.

