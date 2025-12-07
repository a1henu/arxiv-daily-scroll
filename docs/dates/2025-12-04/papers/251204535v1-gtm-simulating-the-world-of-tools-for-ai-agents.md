---
layout: default
title: GTM: Simulating the World of Tools for AI Agents
---

# GTM: Simulating the World of Tools for AI Agents
**arXiv**：[2512.04535v1](https://arxiv.org/abs/2512.04535) · [PDF](https://arxiv.org/pdf/2512.04535.pdf)  
**作者**：Zhenzhen Ren, Xinpeng Zhang, Zhenxing Qian, Yan Gao, Yu Shi, Shuxin Zheng, Jiyan He  

**一句话要点**：提出通用工具模型GTM，以模拟工具执行解决LLM代理训练成本高的问题

**关键词**：工具模拟, LLM代理训练, 上下文感知响应生成, 多领域工具, 强化学习, 成本优化

## 3 点简述
- 核心问题：LLM代理直接交互工具训练成本高、速度慢且维护开销大
- 方法要点：通过CARG管道合成多领域数据，训练GTM作为通用工具模拟器
- 实验或效果：GTM输出质量高、模拟速度快，在强化学习场景中表现优异

## 摘要（原文）

> The integration of external tools is pivotal for empowering Large Language Model (LLM) agents with real-world capabilities. However, training these agents through direct, continuous interaction with diverse tools is often prohibitively expensive, slow, and introduces additional development and maintenance overhead. To address this challenge, we introduce the Generalist Tool Model (GTM), a 1.5-billion-parameter model that learns to act as a universal tool simulator. With only prompt-level configuration, GTM accesses tool functionalities along with input arguments and generates outputs that faithfully mimic real tool execution, providing a fast and cost-effective solution that eliminates development overhead. To build GTM, we propose the Context-Aware Response Generation (CARG) pipeline, which synthesizes comprehensive training data covering over 20,000 tools across 300 domains including physics, medicine, robotics, and finance. Through this pipeline, GTM learns to produce not only syntactically correct outputs but also logically coherent and contextually appropriate responses. Experiments demonstrate that GTM produces high-quality outputs with strong consistency and reliability. Besides when used in real reinforcement learning scenarios for agent training, GTM exhibits significantly faster simulation speed compared to real tools while maintaining comparable output quality, along with remarkable generalization and domain adaptability. Our results establish GTM as a foundational component for developing future AI agents, enabling efficient and scalable training of tool-augmented systems.

