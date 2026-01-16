---
layout: default
title: Performance of AI agents based on reasoning language models on ALD process optimization tasks
---

# Performance of AI agents based on reasoning language models on ALD process optimization tasks
**arXiv**：[2601.09980v1](https://arxiv.org/abs/2601.09980) · [PDF](https://arxiv.org/pdf/2601.09980.pdf)  
**作者**：Angel Yanguas-Gil  

**一句话要点**：评估基于推理大语言模型的AI代理在原子层沉积工艺优化任务中的性能

**关键词**：原子层沉积优化, 推理大语言模型, AI代理, 工艺优化, 自限过程

## 3 点简述
- 核心问题：AI代理需在无先验知识下优化ALD工艺剂量时间，包括自限性未知。
- 方法要点：代理基于推理LLM，通过两步过程生成推理轨迹并转化为结构化输出。
- 实验或效果：代理在模拟ALD工具中成功优化，但存在运行间变异性，推理逻辑基于自限过程概念。

## 摘要（原文）

> In this work we explore the performance and behavior of reasoning large language models to autonomously optimize atomic layer deposition (ALD) processes. In the ALD process optimization task, an agent built on top of a reasoning LLM has to find optimal dose times for an ALD precursor and a coreactant without any prior knowledge on the process, including whether it is actually self-limited. The agent is meant to interact iteratively with an ALD reactor in a fully unsupervised way. We evaluate this agent using a simple model of an ALD tool that incorporates ALD processes with different self-limited surface reaction pathways as well as a non self-limited component. Our results show that agents based on reasoning models like OpenAI's o3 and GPT5 consistently succeeded at completing this optimization task. However, we observed significant run-to-run variability due to the non deterministic nature of the model's response. In order to understand the logic followed by the reasoning model, the agent uses a two step process in which the model first generates an open response detailing the reasoning process. This response is then transformed into a structured output. An analysis of these reasoning traces showed that the logic of the model was sound and that its reasoning was based on the notions of self-limited process and saturation expected in the case of ALD. However, the agent can sometimes be misled by its own prior choices when exploring the optimization space.

