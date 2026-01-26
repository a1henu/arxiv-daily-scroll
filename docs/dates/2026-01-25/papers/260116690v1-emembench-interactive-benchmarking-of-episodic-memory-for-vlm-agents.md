---
layout: default
title: EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents
---

# EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents
**arXiv**：[2601.16690v1](https://arxiv.org/abs/2601.16690) · [PDF](https://arxiv.org/pdf/2601.16690.pdf)  
**作者**：Xinze Li, Ziyue Zhu, Siyuan Liu, Yubo Ma, Yuhang Zang, Yixin Cao, Aixin Sun  

**一句话要点**：提出EMemBench基准，通过交互游戏评估智能体的长时记忆能力。

**关键词**：长时记忆评估, 交互式基准, 视觉语言模型, 记忆技能, 游戏环境, 可验证真值

## 3 点简述
- 核心问题：评估智能体在文本和视觉游戏中的长时记忆，包括多技能推理。
- 方法要点：基于智能体轨迹生成问题，使用模板计算可验证真值，覆盖多种记忆技能。
- 实验或效果：测试强LM/VLM智能体，结果显示诱导和空间推理是瓶颈，视觉记忆挑战大。

## 摘要（原文）

> We introduce EMemBench, a programmatic benchmark for evaluating long-term memory of agents through interactive games. Rather than using a fixed set of questions, EMemBench generates questions from each agent's own trajectory, covering both text and visual game environments. Each template computes verifiable ground truth from underlying game signals, with controlled answerability and balanced coverage over memory skills: single/multi-hop recall, induction, temporal, spatial, logical, and adversarial. We evaluate memory agents with strong LMs/VLMs as backbones, using in-context prompting as baselines. Across 15 text games and multiple visual seeds, results are far from saturated: induction and spatial reasoning are persistent bottlenecks, especially in visual setting. Persistent memory yields clear gains for open backbones on text games, but improvements are less consistent for VLM agents, suggesting that visually grounded episodic memory remains an open challenge. A human study further confirms the difficulty of EMemBench.

