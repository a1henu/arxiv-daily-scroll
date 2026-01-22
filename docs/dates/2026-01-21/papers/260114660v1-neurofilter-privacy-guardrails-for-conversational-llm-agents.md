---
layout: default
title: NeuroFilter: Privacy Guardrails for Conversational LLM Agents
---

# NeuroFilter: Privacy Guardrails for Conversational LLM Agents
**arXiv**：[2601.14660v1](https://arxiv.org/abs/2601.14660) · [PDF](https://arxiv.org/pdf/2601.14660.pdf)  
**作者**：Saswat Das, Ferdinando Fioretto  

**一句话要点**：提出NeuroFilter隐私护栏框架，基于激活空间线性结构检测对话LLM代理中的隐私违规意图。

**关键词**：隐私保护, 对话LLM代理, 激活空间分析, 上下文完整性, 线性可分离性, 计算效率

## 3 点简述
- 核心问题：现有LLM代理隐私防御依赖LLM检查，导致高延迟、成本，且在多轮对话中易被绕过。
- 方法要点：利用隐私违规意图在模型激活空间中的线性可分离性，映射违规到简单方向，并引入激活速度概念捕获长对话威胁。
- 实验或效果：在超15万次交互和7B至70B参数模型上评估，NeuroFilter检测隐私攻击性能强，良性提示零误报，计算成本降低多个数量级。

## 摘要（原文）

> This work addresses the computational challenge of enforcing privacy for agentic Large Language Models (LLMs), where privacy is governed by the contextual integrity framework. Indeed, existing defenses rely on LLM-mediated checking stages that add substantial latency and cost, and that can be undermined in multi-turn interactions through manipulation or benign-looking conversational scaffolding. Contrasting this background, this paper makes a key observation: internal representations associated with privacy-violating intent can be separated from benign requests using linear structure. Using this insight, the paper proposes NeuroFilter, a guardrail framework that operationalizes contextual integrity by mapping norm violations to simple directions in the model's activation space, enabling detection even when semantic filters are bypassed. The proposed filter is also extended to capture threats arising during long conversations using the concept of activation velocity, which measures cumulative drift in internal representations across turns. A comprehensive evaluation across over 150,000 interactions and covering models from 7B to 70B parameters, illustrates the strong performance of NeuroFilter in detecting privacy attacks while maintaining zero false positives on benign prompts, all while reducing the computational inference cost by several orders of magnitude when compared to LLM-based agentic privacy defenses.

