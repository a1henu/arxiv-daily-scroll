---
layout: default
title: QFlowNet: Fast, Diverse, and Efficient Unitary Synthesis with Generative Flow Networks
---

# QFlowNet: Fast, Diverse, and Efficient Unitary Synthesis with Generative Flow Networks
**arXiv**：[2603.03045v1](https://arxiv.org/abs/2603.03045) · [PDF](https://arxiv.org/pdf/2603.03045.pdf)  
**作者**：Inhoe Koo, Hyunho Cha, Jungwoo Lee  

**一句话要点**：提出QFlowNet以解决量子编译中酉合成的高效与多样性问题

**关键词**：酉合成, 生成流网络, 量子编译, Transformer, 策略多样性, 稀疏奖励

## 3 点简述
- 核心问题：酉合成中强化学习面临稀疏奖励和单一策略限制，影响效率和多样性。
- 方法要点：结合生成流网络和Transformer，学习多样策略并压缩高维状态表示。
- 实验或效果：在3量子比特基准上达到99.7%成功率，生成紧凑且多样的量子电路。

## 摘要（原文）

> Unitary Synthesis, the decomposition of a unitary matrix into a sequence of quantum gates, is a fundamental challenge in quantum compilation. Prevailing reinforcement learning(RL) approaches are often hampered by sparse reward signals, which necessitate complex reward shaping or long training times, and typically converge to a single policy, lacking solution diversity. In this work, we propose QFlowNet, a novel framework that learns efficiently from sparse signals by pairing a Generative Flow Network (GFlowNet) with Transformers. Our approach addresses two key challenges. First, the GFlowNet framework is fundamentally designed to learn a diverse policy that samples solutions proportional to their reward, overcoming the single-solution limitation of RL while offering faster inference than other generative models like diffusion. Second, the Transformers act as a powerful encoder, capturing the non-local structure of unitary matrices and compressing a high-dimensional state into a dense latent representation for the policy network. Our agent achieves an overall success rate of 99.7% on a 3-qubit benchmark(lengths 1-12) and discovers a diverse set of compact circuits, establishing QFlowNet as an efficient and diverse paradigm for unitary synthesis.

