---
layout: default
title: Personalized Image Generation via Human-in-the-loop Bayesian Optimization
---

# Personalized Image Generation via Human-in-the-loop Bayesian Optimization
**arXiv**：[2602.02388v1](https://arxiv.org/abs/2602.02388) · [PDF](https://arxiv.org/pdf/2602.02388.pdf)  
**作者**：Rajalaxmi Rajagopalan, Debottam Dutta, Yu-Lin Wei, Romit Roy Choudhury  

**一句话要点**：提出多选择偏好贝叶斯优化以通过人类反馈提升个性化图像生成精度

**关键词**：个性化图像生成, 人类反馈, 贝叶斯优化, 扩散模型, 偏好学习

## 3 点简述
- 核心问题：语言提示在个性化图像生成中难以精确匹配用户心中图像，存在剩余差距。
- 方法要点：基于用户偏好反馈，设计MultiBO算法迭代生成多图像并优化扩散模型。
- 实验或效果：通过30名用户评估和5个基线比较，显示在有限反馈轮次内能显著接近目标图像。

## 摘要（原文）

> Imagine Alice has a specific image $x^\ast$ in her mind, say, the view of the street in which she grew up during her childhood. To generate that exact image, she guides a generative model with multiple rounds of prompting and arrives at an image $x^{p*}$. Although $x^{p*}$ is reasonably close to $x^\ast$, Alice finds it difficult to close that gap using language prompts. This paper aims to narrow this gap by observing that even after language has reached its limits, humans can still tell when a new image $x^+$ is closer to $x^\ast$ than $x^{p*}$. Leveraging this observation, we develop MultiBO (Multi-Choice Preferential Bayesian Optimization) that carefully generates $K$ new images as a function of $x^{p*}$, gets preferential feedback from the user, uses the feedback to guide the diffusion model, and ultimately generates a new set of $K$ images. We show that within $B$ rounds of user feedback, it is possible to arrive much closer to $x^\ast$, even though the generative model has no information about $x^\ast$. Qualitative scores from $30$ users, combined with quantitative metrics compared across $5$ baselines, show promising results, suggesting that multi-choice feedback from humans can be effectively harnessed for personalized image generation.

