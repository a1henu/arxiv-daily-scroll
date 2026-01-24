---
layout: default
title: Learning to Discover at Test Time
---

# Learning to Discover at Test Time
**arXiv**：[2601.16175v1](https://arxiv.org/abs/2601.16175) · [PDF](https://arxiv.org/pdf/2601.16175.pdf)  
**作者**：Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun  

**一句话要点**：提出TTT-Discover方法，通过测试时强化学习在连续奖励问题中发现最优解。

**关键词**：测试时训练, 强化学习, 连续奖励优化, 科学发现, 开源模型

## 3 点简述
- 核心问题：如何在测试时利用AI发现科学问题的新最优解，而非依赖预训练模型。
- 方法要点：采用强化学习在测试时持续训练LLM，优先探索最有希望的解决方案。
- 实验效果：在数学、GPU工程、算法设计和生物学等多个领域设置新最优记录，使用开源模型实现可复现性。

## 摘要（原文）

> How can we use AI to discover a new state of the art for a scientific problem? Prior work in test-time scaling, such as AlphaEvolve, performs search by prompting a frozen LLM. We perform reinforcement learning at test time, so the LLM can continue to train, but now with experience specific to the test problem. This form of continual learning is quite special, because its goal is to produce one great solution rather than many good ones on average, and to solve this very problem rather than generalize to other problems. Therefore, our learning objective and search subroutine are designed to prioritize the most promising solutions. We call this method Test-Time Training to Discover (TTT-Discover). Following prior work, we focus on problems with continuous rewards. We report results for every problem we attempted, across mathematics, GPU kernel engineering, algorithm design, and biology. TTT-Discover sets the new state of the art in almost all of them: (i) Erdős' minimum overlap problem and an autocorrelation inequality; (ii) a GPUMode kernel competition (up to $2\times$ faster than prior art); (iii) past AtCoder algorithm competitions; and (iv) denoising problem in single-cell analysis. Our solutions are reviewed by experts or the organizers. All our results are achieved with an open model, OpenAI gpt-oss-120b, and can be reproduced with our publicly available code, in contrast to previous best results that required closed frontier models. Our test-time training runs are performed using Tinker, an API by Thinking Machines, with a cost of only a few hundred dollars per problem.

