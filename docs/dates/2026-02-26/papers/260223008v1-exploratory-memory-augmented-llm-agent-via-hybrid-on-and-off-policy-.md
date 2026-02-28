---
layout: default
title: Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization
---

# Exploratory Memory-Augmented LLM Agent via Hybrid On- and Off-Policy Optimization
**arXiv**：[2602.23008v1](https://arxiv.org/abs/2602.23008) · [PDF](https://arxiv.org/pdf/2602.23008.pdf)  
**作者**：Zeyuan Liu, Jeonghye Kim, Xufang Luo, Dongsheng Li, Yuqing Yang  

**一句话要点**：提出EMPO²混合强化学习框架，通过记忆增强探索，解决LLM代理在需发现新状态环境中的探索瓶颈。

**关键词**：LLM代理, 强化学习, 探索策略, 记忆增强, 混合优化, 分布外泛化

## 3 点简述
- 核心问题：LLM代理在强化学习中探索不足，尤其在需发现新状态的环境下表现不佳。
- 方法要点：结合记忆机制进行探索，并融合在线与离线策略优化，提升代理在有记忆和无记忆时的性能。
- 实验或效果：在ScienceWorld和WebShop上分别比GRPO提升128.6%和11.3%，并在分布外测试中展示出强适应性。

## 摘要（原文）

> Exploration remains the key bottleneck for large language model agents trained with reinforcement learning. While prior methods exploit pretrained knowledge, they fail in environments requiring the discovery of novel states. We propose Exploratory Memory-Augmented On- and Off-Policy Optimization (EMPO$^2$), a hybrid RL framework that leverages memory for exploration and combines on- and off-policy updates to make LLMs perform well with memory while also ensuring robustness without it. On ScienceWorld and WebShop, EMPO$^2$ achieves 128.6% and 11.3% improvements over GRPO, respectively. Moreover, in out-of-distribution tests, EMPO$^2$ demonstrates superior adaptability to new tasks, requiring only a few trials with memory and no parameter updates. These results highlight EMPO$^2$ as a promising framework for building more exploratory and generalizable LLM-based agents.

