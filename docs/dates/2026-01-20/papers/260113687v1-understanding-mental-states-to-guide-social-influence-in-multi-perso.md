---
layout: default
title: Understanding Mental States to Guide Social Influence in Multi-Person Group Dialogue
---

# Understanding Mental States to Guide Social Influence in Multi-Person Group Dialogue
**arXiv**：[2601.13687v1](https://arxiv.org/abs/2601.13687) · [PDF](https://arxiv.org/pdf/2601.13687.pdf)  
**作者**：Zhichao Liang, Satoshi Nakamura  

**一句话要点**：提出SocialMindChange基准，从追踪心智转向在多人对话中改变心智以引导社会影响

**关键词**：心智理论基准, 社会影响建模, 多人对话生成, 长链交互评估, 高阶心智状态

## 3 点简述
- 核心问题：现有动态心智理论基准多让模型被动追踪心智状态，缺乏主动改变他人心智以达成目标的能力
- 方法要点：构建包含4角色和5场景的社交上下文，模型扮演角色生成对话，使用结构化四步框架确保真实性和质量
- 实验或效果：评估10个先进大语言模型，平均性能比人类低54.2%，显示在长链交互中维持和改变心智表示仍具挑战

## 摘要（原文）

> Existing dynamic Theory of Mind (ToM) benchmarks mostly place language models in a passive role: the model reads a sequence of connected scenarios and reports what people believe, feel, intend, and do as these states change. In real social interaction, ToM is also used for action: a speaker plans what to say in order to shift another person's mental-state trajectory toward a goal. We introduce SocialMindChange, a benchmark that moves from tracking minds to changing minds in social interaction. Each instance defines a social context with 4 characters and five connected scenes. The model plays one character and generates dialogue across the five scenes to reach the target while remaining consistent with the evolving states of all participants. SocialMindChange also includes selected higher-order states. Using a structured four-step framework, we construct 1,200 social contexts, covering 6000 scenarios and over 90,000 questions, each validated for realism and quality. Evaluations on ten state-of-the-art LLMs show that their average performance is 54.2% below human performance. This gap suggests that current LLMs still struggle to maintain and change mental-state representations across long, linked interactions.

