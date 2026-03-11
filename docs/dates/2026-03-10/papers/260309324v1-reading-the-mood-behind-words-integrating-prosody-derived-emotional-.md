---
layout: default
title: Reading the Mood Behind Words: Integrating Prosody-Derived Emotional Context into Socially Responsive VR Agents
---

# Reading the Mood Behind Words: Integrating Prosody-Derived Emotional Context into Socially Responsive VR Agents
**arXiv**：[2603.09324v1](https://arxiv.org/abs/2603.09324) · [PDF](https://arxiv.org/pdf/2603.09324.pdf)  
**作者**：SangYeop Jeong, Yeongseo Na, Seung Gyu Jeong, Jin-Woo Jeong, Seong-Eun Kim  

**一句话要点**：提出基于韵律情感识别的VR对话代理，以提升情感一致性与交互质量。

**关键词**：语音情感识别, VR对话代理, 韵律分析, 情感上下文, LLM集成

## 3 点简述
- 问题：VR代理依赖语音转文本，忽略韵律线索，导致情感响应不匹配。
- 方法：实时语音情感识别模型提取用户情感，作为上下文注入LLM对话代理。
- 效果：用户研究显示对话质量、自然度、参与度等显著提升，93.3%参与者偏好情感感知代理。

## 摘要（原文）

> In VR interactions with embodied conversational agents, users' emotional intent is often conveyed more by how something is said than by what is said. However, most VR agent pipelines rely on speech-to-text processing, discarding prosodic cues and often producing emotionally incongruent responses despite correct semantics. We propose an emotion-context-aware VR interaction pipeline that treats vocal emotion as explicit dialogue context in an LLM-based conversational agent. A real-time speech emotion recognition model infers users' emotional states from prosody, and the resulting emotion labels are injected into the agent's dialogue context to shape response tone and style. Results from a within-subjects VR study (N=30) show significant improvements in dialogue quality, naturalness, engagement, rapport, and human-likeness, with 93.3% of participants preferring the emotion-aware agent.

