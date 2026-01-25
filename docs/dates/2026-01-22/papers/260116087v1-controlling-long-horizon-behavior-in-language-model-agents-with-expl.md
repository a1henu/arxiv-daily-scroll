---
layout: default
title: Controlling Long-Horizon Behavior in Language Model Agents with Explicit State Dynamics
---

# Controlling Long-Horizon Behavior in Language Model Agents with Explicit State Dynamics
**arXiv**：[2601.16087v1](https://arxiv.org/abs/2601.16087) · [PDF](https://arxiv.org/pdf/2601.16087.pdf)  
**作者**：Sukesh Subaharan  

**一句话要点**：提出基于显式情感动态的VAD子系统以控制语言模型代理在长程对话中的行为一致性

**关键词**：语言模型代理, 情感动态, 长程对话, VAD状态, 行为控制, 状态持久性

## 3 点简述
- 核心问题：LLM代理在长程交互中缺乏显式状态动态，导致行为突变和一致性差
- 方法要点：引入外部情感子系统，通过一阶和二阶更新规则维持VAD状态，并注入生成过程
- 实验或效果：在25轮对话中，二阶动态增强稳定性和恢复能力，但需权衡响应性

## 摘要（原文）

> Large language model (LLM) agents often exhibit abrupt shifts in tone and persona during extended interaction, reflecting the absence of explicit temporal structure governing agent-level state. While prior work emphasizes turn-local sentiment or static emotion classification, the role of explicit affective dynamics in shaping long-horizon agent behavior remains underexplored. This work investigates whether imposing dynamical structure on an external affective state can induce temporal coherence and controlled recovery in multi-turn dialogue. We introduce an agent-level affective subsystem that maintains a continuous Valence-Arousal-Dominance (VAD) state external to the language model and governed by first- and second-order update rules. Instantaneous affective signals are extracted using a fixed, memoryless estimator and integrated over time via exponential smoothing or momentum-based dynamics. The resulting affective state is injected back into generation without modifying model parameters. Using a fixed 25-turn dialogue protocol, we compare stateless, first-order, and second-order affective dynamics. Stateless agents fail to exhibit coherent trajectories or recovery, while state persistence enables delayed responses and reliable recovery. Second-order dynamics introduce affective inertia and hysteresis that increase with momentum, revealing a trade-off between stability and responsiveness.

