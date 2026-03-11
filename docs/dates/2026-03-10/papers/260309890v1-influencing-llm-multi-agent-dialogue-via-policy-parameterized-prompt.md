---
layout: default
title: Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts
---

# Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts
**arXiv**：[2603.09890v1](https://arxiv.org/abs/2603.09890) · [PDF](https://arxiv.org/pdf/2603.09890.pdf)  
**作者**：Hongbo Bo, Jingyu Hu, Weiru Liu  

**一句话要点**：提出基于策略参数化提示的框架，以轻量级方式影响LLM多智能体对话行为。

**关键词**：大语言模型, 多智能体系统, 提示工程, 策略参数化, 对话控制, 社会模拟

## 3 点简述
- 核心问题：现有LLM多智能体研究依赖临时提示，缺乏策略化视角。
- 方法要点：将提示视为动作，通过五组件动态构建参数化策略，无需训练。
- 实验或效果：在公共讨论场景中评估对话指标，显示参数化控制能有效影响对话动态。

## 摘要（原文）

> Large Language Models (LLMs) have emerged as a new paradigm for multi-agent systems. However, existing research on the behaviour of LLM-based multi-agents relies on ad hoc prompts and lacks a principled policy perspective. Different from reinforcement learning, we investigate whether prompt-as-action can be parameterized so as to construct a lightweight policy which consists of a sequence of state-action pairs to influence conversational behaviours without training. Our framework regards prompts as actions executed by LLMs, and dynamically constructs prompts through five components based on the current state of the agent. To test the effectiveness of parameterized control, we evaluated the dialogue flow based on five indicators: responsiveness, rebuttal, evidence usage, non-repetition, and stance shift. We conduct experiments using different LLM-driven agents in two discussion scenarios related to the general public and show that prompt parameterization can influence the dialogue dynamics. This result shows that policy-parameterised prompts offer a simple and effective mechanism to influence the dialogue process, which will help the research of multi-agent systems in the direction of social simulation.

