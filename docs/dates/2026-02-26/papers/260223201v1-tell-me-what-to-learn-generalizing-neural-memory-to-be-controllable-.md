---
layout: default
title: Tell Me What To Learn: Generalizing Neural Memory to be Controllable in Natural Language
---

# Tell Me What To Learn: Generalizing Neural Memory to be Controllable in Natural Language
**arXiv**：[2602.23201v1](https://arxiv.org/abs/2602.23201) · [PDF](https://arxiv.org/pdf/2602.23201.pdf)  
**作者**：Max S. Bennett, Thomas P. Zollo, Richard Zemel  

**一句话要点**：提出基于自然语言指令的可控神经记忆系统，以支持异构信息源下的选择性学习。

**关键词**：神经记忆, 自然语言指令, 选择性学习, 异构信息源, 持续学习

## 3 点简述
- 核心问题：现有神经记忆模型假设固定目标和同质信息流，缺乏用户对记忆内容的控制。
- 方法要点：设计通用神经记忆系统，通过自然语言指令灵活更新记忆，实现选择性学习。
- 实验或效果：适用于医疗和客服等场景，支持轻量级更新和最小遗忘，提升适应性。

## 摘要（原文）

> Modern machine learning models are deployed in diverse, non-stationary environments where they must continually adapt to new tasks and evolving knowledge. Continual fine-tuning and in-context learning are costly and brittle, whereas neural memory methods promise lightweight updates with minimal forgetting. However, existing neural memory models typically assume a single fixed objective and homogeneous information streams, leaving users with no control over what the model remembers or ignores over time. To address this challenge, we propose a generalized neural memory system that performs flexible updates based on learning instructions specified in natural language. Our approach enables adaptive agents to learn selectively from heterogeneous information sources, supporting settings, such as healthcare and customer service, where fixed-objective memory updates are insufficient.

