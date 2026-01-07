---
layout: default
title: MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents
---

# MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents
**arXiv**：[2601.03236v1](https://arxiv.org/abs/2601.03236) · [PDF](https://arxiv.org/pdf/2601.03236.pdf)  
**作者**：Dongming Jiang, Yi Li, Guanpeng Li, Bingzhe Li  

**一句话要点**：提出多图代理记忆架构MAGMA，以提升长时推理任务中的准确性和可解释性。

**关键词**：记忆增强生成, 多图表示, 代理记忆架构, 长时推理, 策略引导检索

## 3 点简述
- 现有记忆增强生成方法依赖单一语义相似度，混淆时间、因果和实体信息，限制推理准确性。
- MAGMA通过正交语义、时间、因果和实体图表示记忆，实现策略引导的查询自适应检索。
- 在LoCoMo和LongMemEval基准测试中，MAGMA优于现有代理记忆系统，验证其有效性。

## 摘要（原文）

> Memory-Augmented Generation (MAG) extends Large Language Models with external memory to support long-context reasoning, but existing approaches largely rely on semantic similarity over monolithic memory stores, entangling temporal, causal, and entity information. This design limits interpretability and alignment between query intent and retrieved evidence, leading to suboptimal reasoning accuracy. In this paper, we propose MAGMA, a multi-graph agentic memory architecture that represents each memory item across orthogonal semantic, temporal, causal, and entity graphs. MAGMA formulates retrieval as policy-guided traversal over these relational views, enabling query-adaptive selection and structured context construction. By decoupling memory representation from retrieval logic, MAGMA provides transparent reasoning paths and fine-grained control over retrieval. Experiments on LoCoMo and LongMemEval demonstrate that MAGMA consistently outperforms state-of-the-art agentic memory systems in long-horizon reasoning tasks.

