---
layout: default
title: TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents
---

# TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents
**arXiv**：[2601.05899v1](https://arxiv.org/abs/2601.05899) · [PDF](https://arxiv.org/pdf/2601.05899.pdf)  
**作者**：Dawei Wang, Chengming Zhou, Di Zhao, Xinyuan Liu, Marci Chi Ma, Gary Ushaw, Richard Davison  

**一句话要点**：提出TowerMind塔防游戏环境，以轻量多模态设计评估大语言模型作为智能体的规划与决策能力。

**关键词**：塔防游戏环境, 大语言模型评估, 多模态观察, 智能体基准, 规划决策能力, 模型幻觉

## 3 点简述
- 针对现有RTS游戏环境计算需求高或缺乏文本观察支持，限制大语言模型评估的问题。
- 设计轻量多模态塔防环境，支持像素、文本和结构化状态表示，并评估模型幻觉和可定制性。
- 通过基准测试揭示大语言模型与人类专家在能力和幻觉方面的差距，并分析其行为局限性。

## 摘要（原文）

> Recent breakthroughs in Large Language Models (LLMs) have positioned them as a promising paradigm for agents, with long-term planning and decision-making emerging as core general-purpose capabilities for adapting to diverse scenarios and tasks. Real-time strategy (RTS) games serve as an ideal testbed for evaluating these two capabilities, as their inherent gameplay requires both macro-level strategic planning and micro-level tactical adaptation and action execution. Existing RTS game-based environments either suffer from relatively high computational demands or lack support for textual observations, which has constrained the use of RTS games for LLM evaluation. Motivated by this, we present TowerMind, a novel environment grounded in the tower defense (TD) subgenre of RTS games. TowerMind preserves the key evaluation strengths of RTS games for assessing LLMs, while featuring low computational demands and a multimodal observation space, including pixel-based, textual, and structured game-state representations. In addition, TowerMind supports the evaluation of model hallucination and provides a high degree of customizability. We design five benchmark levels to evaluate several widely used LLMs under different multimodal input settings. The results reveal a clear performance gap between LLMs and human experts across both capability and hallucination dimensions. The experiments further highlight key limitations in LLM behavior, such as inadequate planning validation, a lack of multifinality in decision-making, and inefficient action use. We also evaluate two classic reinforcement learning algorithms: Ape-X DQN and PPO. By offering a lightweight and multimodal design, TowerMind complements the existing RTS game-based environment landscape and introduces a new benchmark for the AI agent field. The source code is publicly available on GitHub(https://github.com/tb6147877/TowerMind).

