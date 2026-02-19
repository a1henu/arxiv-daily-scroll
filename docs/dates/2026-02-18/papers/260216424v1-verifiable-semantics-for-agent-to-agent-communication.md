---
layout: default
title: Verifiable Semantics for Agent-to-Agent Communication
---

# Verifiable Semantics for Agent-to-Agent Communication
**arXiv**：[2602.16424v1](https://arxiv.org/abs/2602.16424) · [PDF](https://arxiv.org/pdf/2602.16424.pdf)  
**作者**：Philipp Schoenegger, Matt Carlson, Chris Schneider, Chris Daly  

**一句话要点**：提出基于刺激-意义模型的认证协议，以解决多智能体系统中语义一致性的验证问题。

**关键词**：多智能体通信, 语义验证, 认证协议, 核心防护推理, 语义漂移检测, 词汇重协商

## 3 点简述
- 核心问题：多智能体通信中缺乏验证术语共享理解的方法，自然语言易漂移，学习协议不透明。
- 方法要点：通过共享可观测事件测试智能体，若经验分歧低于统计阈值则认证术语，实现核心防护推理以限制分歧。
- 实验或效果：模拟中核心防护减少分歧72-96%，微调语言模型验证中减少分歧51%。

## 摘要（原文）

> Multiagent AI systems require consistent communication, but we lack methods to verify that agents share the same understanding of the terms used. Natural language is interpretable but vulnerable to semantic drift, while learned protocols are efficient but opaque. We propose a certification protocol based on the stimulus-meaning model, where agents are tested on shared observable events and terms are certified if empirical disagreement falls below a statistical threshold. In this protocol, agents restricting their reasoning to certified terms ("core-guarded reasoning") achieve provably bounded disagreement. We also outline mechanisms for detecting drift (recertification) and recovering shared vocabulary (renegotiation). In simulations with varying degrees of semantic divergence, core-guarding reduces disagreement by 72-96%. In a validation with fine-tuned language models, disagreement is reduced by 51%. Our framework provides a first step towards verifiable agent-to-agent communication.

