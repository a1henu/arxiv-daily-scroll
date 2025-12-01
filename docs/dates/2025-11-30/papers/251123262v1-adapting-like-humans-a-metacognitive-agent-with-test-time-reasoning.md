---
layout: default
title: Adapting Like Humans: A Metacognitive Agent with Test-time Reasoning
---

# Adapting Like Humans: A Metacognitive Agent with Test-time Reasoning
**arXiv**：[2511.23262v1](https://arxiv.org/abs/2511.23262) · [PDF](https://arxiv.org/pdf/2511.23262.pdf)  
**作者**：Yang Li, Zhiyuan He, Yuxuan Huang, Zhuhanling Xiao, Chao Yu, Meng Fang, Kun Shao, Jun Wang  

**一句话要点**：提出元认知测试时推理框架，以提升视觉语言模型在测试时对新任务的适应能力。

**关键词**：元认知推理, 测试时适应, 视觉语言模型, 分层记忆系统, 强化学习, Atari游戏

## 3 点简述
- 核心问题：视觉语言模型在测试时面对新任务时适应效率低，缺乏人类元认知的持续策略优化能力。
- 方法要点：设计元级和对象级推理模块，结合记忆系统进行分层自适应推理，通过元认知测试时强化学习更新策略。
- 实验或效果：在45个Atari游戏中评估，在12个未见游戏中取得9项最佳结果，显示稳健的测试时适应能力。

## 摘要（原文）

> Recent Vision-Language Models (VLMs) exhibit strong perceptual reasoning abilities, yet they often struggle to adapt efficiently when encountering novel tasks at test time. In contrast, humans leverage the metacognitive model with memory, enabling continuous strategy refinement through metacognitive control when faced with new challenges. To bridge this gap, we propose metacognitive test-time reasoning (MCTR), a framework that equips models with the ability to learn, adapt, and improve during test time through metacognitive self-updating. Inspired by the dual structure of human metacognition, MCTR comprises meta-level and object-level VLM reasoning modules, each equipped with dedicated memory systems for hierarchical adaptive reasoning. Specifically, MCTR consists of (1) a meta-reasoning module which incrementally builds a structured memory by discovering and storing task-relevant rules, environmental patterns, and action-outcome relationships from test-time observations as natural language descriptions; and (2) an action-reasoning module that determines optimal actions through context-aware perception and strategic reasoning by dynamically retrieving and integrating knowledge from memory. The action-reasoning module continuously updates its policy through proposed metacognitive test-time reinforcement learning, adapting as knowledge memory evolves. We evaluate MCTR on 45 Atari games (33 seen, 12 unseen). MCTR demonstrates robust test-time adaptation, achieving 9/12 top-1 results on unseen games compared with baselines. Analyses through ablations, learning dynamics, and case studies reveal the complementary contributions of both components and show meta-reasoning evolving toward human-like adaptation strategies.

