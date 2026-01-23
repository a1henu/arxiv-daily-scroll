---
layout: default
title: AgentSM: Semantic Memory for Agentic Text-to-SQL
---

# AgentSM: Semantic Memory for Agentic Text-to-SQL
**arXiv**：[2601.15709v1](https://arxiv.org/abs/2601.15709) · [PDF](https://arxiv.org/pdf/2601.15709.pdf)  
**作者**：Asim Biswal, Chuan Lei, Xiao Qin, Aodong Li, Balakrishnan Narayanaswamy, Tim Kraska  

**一句话要点**：提出AgentSM框架，利用语义记忆解决企业环境中Text-to-SQL的扩展与效率问题。

**关键词**：Text-to-SQL, 语义记忆, 代理框架, 执行轨迹, 推理效率

## 3 点简述
- 核心问题：现有LLM-based Text-to-SQL系统在企业大规模复杂场景下扩展困难，效率低且不稳定。
- 方法要点：构建可解释的语义记忆，通过结构化程序捕获或合成执行轨迹，指导未来推理。
- 实验或效果：在Spider 2.0基准上，平均token使用和轨迹长度分别减少25%和35%，执行准确率提升。

## 摘要（原文）

> Recent advances in LLM-based Text-to-SQL have achieved remarkable gains on public benchmarks such as BIRD and Spider. Yet, these systems struggle to scale in realistic enterprise settings with large, complex schemas, diverse SQL dialects, and expensive multi-step reasoning. Emerging agentic approaches show potential for adaptive reasoning but often suffer from inefficiency and instability-repeating interactions with databases, producing inconsistent outputs, and occasionally failing to generate valid answers. To address these challenges, we introduce Agent Semantic Memory (AgentSM), an agentic framework for Text-to-SQL that builds and leverages interpretable semantic memory. Instead of relying on raw scratchpads or vector retrieval, AgentSM captures prior execution traces-or synthesizes curated ones-as structured programs that directly guide future reasoning. This design enables systematic reuse of reasoning paths, which allows agents to scale to larger schemas, more complex questions, and longer trajectories efficiently and reliably. Compared to state-of-the-art systems, AgentSM achieves higher efficiency by reducing average token usage and trajectory length by 25% and 35%, respectively, on the Spider 2.0 benchmark. It also improves execution accuracy, reaching a state-of-the-art accuracy of 44.8% on the Spider 2.0 Lite benchmark.

