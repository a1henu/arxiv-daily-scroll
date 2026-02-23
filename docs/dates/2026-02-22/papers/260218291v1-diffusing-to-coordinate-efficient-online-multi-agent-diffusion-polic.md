---
layout: default
title: Diffusing to Coordinate: Efficient Online Multi-Agent Diffusion Policies
---

# Diffusing to Coordinate: Efficient Online Multi-Agent Diffusion Policies
**arXiv**：[2602.18291v1](https://arxiv.org/abs/2602.18291) · [PDF](https://arxiv.org/pdf/2602.18291.pdf)  
**作者**：Zhuoran Li, Hai Zhong, Xun Wang, Qingxin Xia, Lihua Zhang, Longbo Huang  

**一句话要点**：提出在线多智能体扩散策略框架以解决扩散模型在在线强化学习中探索与协调的难题

**关键词**：在线多智能体强化学习, 扩散模型, 策略表达性, 联合熵探索, 去中心化执行, 样本效率

## 3 点简述
- 核心问题：扩散模型在在线多智能体强化学习中因似然不可处理而阻碍基于熵的探索与协调
- 方法要点：设计松弛策略目标最大化缩放联合熵，并利用联合分布值函数优化去中心化扩散策略
- 实验或效果：在MPE和MAMuJoCo的10个任务中实现样本效率2.5倍至5倍提升，达到新最优性能

## 摘要（原文）

> Online Multi-Agent Reinforcement Learning (MARL) is a prominent framework for efficient agent coordination. Crucially, enhancing policy expressiveness is pivotal for achieving superior performance. Diffusion-based generative models are well-positioned to meet this demand, having demonstrated remarkable expressiveness and multimodal representation in image generation and offline settings. Yet, their potential in online MARL remains largely under-explored. A major obstacle is that the intractable likelihoods of diffusion models impede entropy-based exploration and coordination. To tackle this challenge, we propose among the first \underline{O}nline off-policy \underline{MA}RL framework using \underline{D}iffusion policies (\textbf{OMAD}) to orchestrate coordination. Our key innovation is a relaxed policy objective that maximizes scaled joint entropy, facilitating effective exploration without relying on tractable likelihood. Complementing this, within the centralized training with decentralized execution (CTDE) paradigm, we employ a joint distributional value function to optimize decentralized diffusion policies. It leverages tractable entropy-augmented targets to guide the simultaneous updates of diffusion policies, thereby ensuring stable coordination. Extensive evaluations on MPE and MAMuJoCo establish our method as the new state-of-the-art across $10$ diverse tasks, demonstrating a remarkable $2.5\times$ to $5\times$ improvement in sample efficiency.

