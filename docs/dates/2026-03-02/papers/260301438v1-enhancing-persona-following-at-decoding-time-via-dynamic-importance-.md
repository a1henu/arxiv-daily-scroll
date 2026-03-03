---
layout: default
title: Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents
---

# Enhancing Persona Following at Decoding Time via Dynamic Importance Estimation for Role-Playing Agents
**arXiv**：[2603.01438v1](https://arxiv.org/abs/2603.01438) · [PDF](https://arxiv.org/pdf/2603.01438.pdf)  
**作者**：Yuxin Liu, Mingye Zhu, Siyuan Liu, Bo Hu, Lei Zhang  

**一句话要点**：提出动态重要性估计的PDD框架，以增强角色扮演代理在解码时对动态场景中人物设定的遵循能力。

**关键词**：角色扮演代理, 动态重要性估计, 推理时对齐, 加权解码, 人物设定遵循, 社会模拟

## 3 点简述
- 核心问题：现有角色扮演代理方法无法适应动态场景，导致人物设定遵循不足，影响社会模拟的真实性。
- 方法要点：基于心理学理论，设计PIE模块动态估计人物属性重要性，结合PIA范式在推理时通过加权奖励引导解码。
- 实验或效果：实验验证了方法在话语一致性和行为保真度方面的有效性，但具体数据集和基线对比未知。

## 摘要（原文）

> The utility of Role-Playing Language Agents in sociological research is growing alongside the adoption of Large Language Models. For realism in social simulation, these agents must adhere to their personas defined by character profiles, yet existing strategies-static prompt engineering or costly fine-tuning-fail to adapt personas to dynamic scenarios. Psychological theories, such as the Cognitive-Affective Personality Systems, provide a crucial explanation for this failure: a persona's influence on behavior is not static but varies with the scenarios. This context-dependence highlights the critical need for adaptive persona management. To address this gap, we propose a novel, theory-driven method that dynamically estimates context-dependent persona importance and integrates it into weighted reward-guided decoding, enabling inference-time persona following. Specifically, we introduce the Persona Dynamic Decoding (PDD) framework, which consists of two key components: (1) Persona Importance Estimation (PIE) module, which dynamically quantifies the contextual importance of persona attributes without requiring ground-truth supervision; and (2) Persona-Guided Inference-Time Alignment (PIA) paradigm, which leverages these importance scores to construct weighted multi-objective rewards and modulate generation probabilities during inference. Extensive experiments show the effectiveness of our method in utterance consistency and behavioral fidelity.

