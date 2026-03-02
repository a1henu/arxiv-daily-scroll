---
layout: default
title: The Auton Agentic AI Framework
---

# The Auton Agentic AI Framework
**arXiv**：[2602.23720v1](https://arxiv.org/abs/2602.23720) · [PDF](https://arxiv.org/pdf/2602.23720.pdf)  
**作者**：Sheng Cao, Zhao Chang, Chang Li, Hannan Li, Liyao Fu, Ji Tang  

**一句话要点**：提出Auton框架以解决LLM输出与后端基础设施间的架构不匹配问题

**关键词**：自主代理系统, 认知蓝图, 运行时引擎, 模型上下文协议, 部分可观察马尔可夫决策过程, 安全约束

## 3 点简述
- 核心问题：LLM的随机非结构化输出与后端确定性需求不匹配
- 方法要点：分离认知蓝图与运行时引擎，支持跨语言可移植性和形式化审计
- 实验或效果：未知

## 摘要（原文）

> The field of Artificial Intelligence is undergoing a transition from Generative AI -- probabilistic generation of text and images -- to Agentic AI, in which autonomous systems execute actions within external environments on behalf of users. This transition exposes a fundamental architectural mismatch: Large Language Models (LLMs) produce stochastic, unstructured outputs, whereas the backend infrastructure they must control -- databases, APIs, cloud services -- requires deterministic, schema-conformant inputs. The present paper describes the Auton Agentic AI Framework, a principled architecture for standardizing the creation, execution, and governance of autonomous agent systems. The framework is organized around a strict separation between the Cognitive Blueprint, a declarative, language-agnostic specification of agent identity and capabilities, and the Runtime Engine, the platform-specific execution substrate that instantiates and runs the agent. This separation enables cross-language portability, formal auditability, and modular tool integration via the Model Context Protocol (MCP). The paper formalizes the agent execution model as an augmented Partially Observable Markov Decision Process (POMDP) with a latent reasoning space, introduces a hierarchical memory consolidation architecture inspired by biological episodic memory systems, defines a constraint manifold formalism for safety enforcement via policy projection rather than post-hoc filtering, presents a three-level self-evolution framework spanning in-context adaptation through reinforcement learning, and describes runtime optimizations -- including parallel graph execution, speculative inference, and dynamic context pruning -- that reduce end-to-end latency for multi-step agent workflows.

