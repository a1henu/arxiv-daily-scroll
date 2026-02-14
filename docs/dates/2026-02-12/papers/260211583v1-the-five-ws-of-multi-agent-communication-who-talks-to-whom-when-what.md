---
layout: default
title: The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs
---

# The Five Ws of Multi-Agent Communication: Who Talks to Whom, When, What, and Why -- A Survey from MARL to Emergent Language and LLMs
**arXiv**：[2602.11583v1](https://arxiv.org/abs/2602.11583) · [PDF](https://arxiv.org/pdf/2602.11583.pdf)  
**作者**：Jingdi Chen, Hanqing Yang, Zongjun Liu, Carlee Joe-Wong  

**一句话要点**：综述多智能体通信的五大要素，连接MARL、涌现语言与LLMs研究脉络

**关键词**：多智能体通信, 多智能体强化学习, 涌现语言, 大语言模型, 协作AI, 通信协议

## 3 点简述
- 核心问题：动态部分可观测环境中，通信如何减少不确定性并促进协作
- 方法要点：以五大要素框架梳理MARL、涌现语言和LLMs的通信设计演变
- 实验或效果：提炼设计模式与开放挑战，支持未来混合系统开发

## 摘要（原文）

> Multi-agent sequential decision-making powers many real-world systems, from autonomous vehicles and robotics to collaborative AI assistants. In dynamic, partially observable environments, communication is often what reduces uncertainty and makes collaboration possible. This survey reviews multi-agent communication (MA-Comm) through the Five Ws: who communicates with whom, what is communicated, when communication occurs, and why communication is beneficial. This framing offers a clean way to connect ideas across otherwise separate research threads. We trace how communication approaches have evolved across three major paradigms. In Multi-Agent Reinforcement Learning (MARL), early methods used hand-designed or implicit protocols, followed by end-to-end learned communication optimized for reward and control. While successful, these protocols are frequently task-specific and hard to interpret, motivating work on Emergent Language (EL), where agents can develop more structured or symbolic communication through interaction. EL methods, however, still struggle with grounding, generalization, and scalability, which has fueled recent interest in large language models (LLMs) that bring natural language priors for reasoning, planning, and collaboration in more open-ended settings. Across MARL, EL, and LLM-based systems, we highlight how different choices shape communication design, where the main trade-offs lie, and what remains unsolved. We distill practical design patterns and open challenges to support future hybrid systems that combine learning, language, and control for scalable and interpretable multi-agent collaboration.

