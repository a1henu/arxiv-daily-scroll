---
layout: default
title: Active Context Compression: Autonomous Memory Management in LLM Agents
---

# Active Context Compression: Autonomous Memory Management in LLM Agents
**arXiv**：[2601.07190v1](https://arxiv.org/abs/2601.07190) · [PDF](https://arxiv.org/pdf/2601.07190.pdf)  
**作者**：Nikhil Verma  

**一句话要点**：提出Focus架构以解决LLM代理在长时程软件工程任务中的上下文膨胀问题

**关键词**：上下文管理, 自主压缩, LLM代理, 软件工程任务, 成本优化

## 3 点简述
- 核心问题：LLM代理面临上下文膨胀，导致计算成本高、延迟增加和推理能力下降
- 方法要点：受黏菌探索策略启发，代理自主管理上下文，压缩关键学习到知识块并修剪原始历史
- 实验或效果：在SWE-bench Lite上测试，实现22.7%令牌减少，保持60%准确率，平均每任务6.0次自主压缩

## 摘要（原文）

> Large Language Model (LLM) agents struggle with long-horizon software engineering tasks due to "Context Bloat." As interaction history grows, computational costs explode, latency increases, and reasoning capabilities degrade due to distraction by irrelevant past errors. Existing solutions often rely on passive, external summarization mechanisms that the agent cannot control. This paper proposes Focus, an agent-centric architecture inspired by the biological exploration strategies of Physarum polycephalum (slime mold). The Focus Agent autonomously decides when to consolidate key learnings into a persistent "Knowledge" block and actively withdraws (prunes) the raw interaction history. Using an optimized scaffold matching industry best practices (persistent bash + string-replacement editor), we evaluated Focus on N=5 context-intensive instances from SWE-bench Lite using Claude Haiku 4.5. With aggressive prompting that encourages frequent compression, Focus achieves 22.7% token reduction (14.9M -> 11.5M tokens) while maintaining identical accuracy (3/5 = 60% for both agents). Focus performed 6.0 autonomous compressions per task on average, with token savings up to 57% on individual instances. We demonstrate that capable models can autonomously self-regulate their context when given appropriate tools and prompting, opening pathways for cost-aware agentic systems without sacrificing task performance.

