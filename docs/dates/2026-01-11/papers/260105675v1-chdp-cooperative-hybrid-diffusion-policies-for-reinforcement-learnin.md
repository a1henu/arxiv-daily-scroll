---
layout: default
title: CHDP: Cooperative Hybrid Diffusion Policies for Reinforcement Learning in Parameterized Action Space
---

# CHDP: Cooperative Hybrid Diffusion Policies for Reinforcement Learning in Parameterized Action Space
**arXiv**：[2601.05675v1](https://arxiv.org/abs/2601.05675) · [PDF](https://arxiv.org/pdf/2601.05675.pdf)  
**作者**：Bingyi Liu, Jinbo He, Haiyong Shi, Enshu Wang, Weizhen Han, Jingxiang Hao, Peixi Wang, Zhuangzhuang Zhang  

**一句话要点**：提出合作混合扩散策略框架以解决强化学习中参数化动作空间的建模与优化挑战

**关键词**：混合动作空间, 扩散策略, 强化学习, 参数化动作, 合作学习, 低维嵌入

## 3 点简述
- 核心问题：混合动作空间（离散选择与连续参数结合）在机器人控制等领域存在策略表达能力有限和高维可扩展性差的问题
- 方法要点：采用两个合作代理分别处理离散和连续动作，通过扩散策略捕获复杂分布，并引入顺序更新和低维嵌入提升性能
- 实验或效果：在混合动作基准测试中，成功率比现有最优方法提升高达19.3%

## 摘要（原文）

> Hybrid action space, which combines discrete choices and continuous parameters, is prevalent in domains such as robot control and game AI. However, efficiently modeling and optimizing hybrid discrete-continuous action space remains a fundamental challenge, mainly due to limited policy expressiveness and poor scalability in high-dimensional settings. To address this challenge, we view the hybrid action space problem as a fully cooperative game and propose a \textbf{Cooperative Hybrid Diffusion Policies (CHDP)} framework to solve it. CHDP employs two cooperative agents that leverage a discrete and a continuous diffusion policy, respectively. The continuous policy is conditioned on the discrete action's representation, explicitly modeling the dependency between them. This cooperative design allows the diffusion policies to leverage their expressiveness to capture complex distributions in their respective action spaces. To mitigate the update conflicts arising from simultaneous policy updates in this cooperative setting, we employ a sequential update scheme that fosters co-adaptation. Moreover, to improve scalability when learning in high-dimensional discrete action space, we construct a codebook that embeds the action space into a low-dimensional latent space. This mapping enables the discrete policy to learn in a compact, structured space. Finally, we design a Q-function-based guidance mechanism to align the codebook's embeddings with the discrete policy's representation during training. On challenging hybrid action benchmarks, CHDP outperforms the state-of-the-art method by up to $19.3\%$ in success rate.

