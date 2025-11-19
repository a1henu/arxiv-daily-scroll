---
layout: default
title: Masked IRL: LLM-Guided Reward Disambiguation from Demonstrations and Language
---

# Masked IRL: LLM-Guided Reward Disambiguation from Demonstrations and Language
**arXiv**：[2511.14565v1](https://arxiv.org/abs/2511.14565) · [PDF](https://arxiv.org/pdf/2511.14565.pdf)  
**作者**：Minyoung Hwang, Alexandra Forsey-Smerek, Nathaniel Dennler, Andreea Bobu  

**一句话要点**：提出Masked IRL框架，利用LLM结合演示与语言解决奖励函数泛化问题

**关键词**：逆强化学习, 语言指导奖励学习, 状态掩码, LLM推理, 机器人适应

## 3 点简述
- 核心问题：有限演示数据下奖励模型易过拟合，无法泛化到新场景
- 方法要点：使用LLM从语言推断状态相关性掩码，强制对无关状态不变
- 实验或效果：在仿真和真实机器人上，性能提升15%，数据需求减少4.7倍

## 摘要（原文）

> Robots can adapt to user preferences by learning reward functions from demonstrations, but with limited data, reward models often overfit to spurious correlations and fail to generalize. This happens because demonstrations show robots how to do a task but not what matters for that task, causing the model to focus on irrelevant state details. Natural language can more directly specify what the robot should focus on, and, in principle, disambiguate between many reward functions consistent with the demonstrations. However, existing language-conditioned reward learning methods typically treat instructions as simple conditioning signals, without fully exploiting their potential to resolve ambiguity. Moreover, real instructions are often ambiguous themselves, so naive conditioning is unreliable. Our key insight is that these two input types carry complementary information: demonstrations show how to act, while language specifies what is important. We propose Masked Inverse Reinforcement Learning (Masked IRL), a framework that uses large language models (LLMs) to combine the strengths of both input types. Masked IRL infers state-relevance masks from language instructions and enforces invariance to irrelevant state components. When instructions are ambiguous, it uses LLM reasoning to clarify them in the context of the demonstrations. In simulation and on a real robot, Masked IRL outperforms prior language-conditioned IRL methods by up to 15% while using up to 4.7 times less data, demonstrating improved sample-efficiency, generalization, and robustness to ambiguous language. Project page: https://MIT-CLEAR-Lab.github.io/Masked-IRL and Code: https://github.com/MIT-CLEAR-Lab/Masked-IRL

