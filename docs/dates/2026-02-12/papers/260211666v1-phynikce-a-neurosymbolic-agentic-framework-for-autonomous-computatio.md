---
layout: default
title: PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics
---

# PhyNiKCE: A Neurosymbolic Agentic Framework for Autonomous Computational Fluid Dynamics
**arXiv**：[2602.11666v1](https://arxiv.org/abs/2602.11666) · [PDF](https://arxiv.org/pdf/2602.11666.pdf)  
**作者**：E Fan, Lisong Shi, Zhengtong Li, Chih-yung Wen  

**一句话要点**：提出PhyNiKCE框架以解决CFD中LLM因概率性导致的物理约束失效问题

**关键词**：神经符号框架, 计算流体动力学, 约束满足问题, 检索增强生成, 自主代理, 可信人工智能

## 3 点简述
- 核心问题：LLM在CFD中因概率性无法保证物理守恒和数值稳定性，语义RAG易导致物理无效配置
- 方法要点：采用神经符号框架，分离神经规划与符号验证，通过符号知识引擎将仿真设置建模为约束满足问题
- 实验或效果：在OpenFOAM实验中，相对基线提升96%，减少59%自校正循环和17%LLM令牌消耗

## 摘要（原文）

> The deployment of autonomous agents for Computational Fluid Dynamics (CFD), is critically limited by the probabilistic nature of Large Language Models (LLMs), which struggle to enforce the strict conservation laws and numerical stability required for physics-based simulations. Reliance on purely semantic Retrieval Augmented Generation (RAG) often leads to "context poisoning," where agents generate linguistically plausible but physically invalid configurations due to a fundamental Semantic-Physical Disconnect. To bridge this gap, this work introduces PhyNiKCE (Physical and Numerical Knowledgeable Context Engineering), a neurosymbolic agentic framework for trustworthy engineering. Unlike standard black-box agents, PhyNiKCE decouples neural planning from symbolic validation. It employs a Symbolic Knowledge Engine that treats simulation setup as a Constraint Satisfaction Problem, rigidly enforcing physical constraints via a Deterministic RAG Engine with specialized retrieval strategies for solvers, turbulence models, and boundary conditions. Validated through rigorous OpenFOAM experiments on practical, non-tutorial CFD tasks using Gemini-2.5-Pro/Flash, PhyNiKCE demonstrates a 96% relative improvement over state-of-the-art baselines. Furthermore, by replacing trial-and-error with knowledge-driven initialization, the framework reduced autonomous self-correction loops by 59% while simultaneously lowering LLM token consumption by 17%. These results demonstrate that decoupling neural generation from symbolic constraint enforcement significantly enhances robustness and efficiency. While validated on CFD, this architecture offers a scalable, auditable paradigm for Trustworthy Artificial Intelligence in broader industrial automation.

