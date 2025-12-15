---
layout: default
title: MedAI: Evaluating TxAgent's Therapeutic Agentic Reasoning in the NeurIPS CURE-Bench Competition
---

# MedAI: Evaluating TxAgent's Therapeutic Agentic Reasoning in the NeurIPS CURE-Bench Competition
**arXiv**：[2512.11682v1](https://arxiv.org/abs/2512.11682) · [PDF](https://arxiv.org/pdf/2512.11682.pdf)  
**作者**：Tim Cofala, Christian Kalfar, Jingge Xiao, Johanna Schrader, Michelle Tang, Wolfgang Nejdl  

**一句话要点**：提出TxAgent的代理推理方法，在CURE-Bench竞赛中评估医疗决策性能

**关键词**：医疗决策AI, 代理推理, 检索增强生成, 生物医学工具集成, CURE-Bench竞赛

## 3 点简述
- 医疗AI需处理患者、疾病和药物的复杂交互，要求多步推理和可靠知识
- TxAgent基于微调Llama-3.1-8B模型，通过迭代RAG动态调用生物医学工具
- 在CURE-Bench竞赛中分析工具检索质量对性能的影响，获得Open Science Excellence奖

## 摘要（原文）

> Therapeutic decision-making in clinical medicine constitutes a high-stakes domain in which AI guidance interacts with complex interactions among patient characteristics, disease processes, and pharmacological agents. Tasks such as drug recommendation, treatment planning, and adverse-effect prediction demand robust, multi-step reasoning grounded in reliable biomedical knowledge. Agentic AI methods, exemplified by TxAgent, address these challenges through iterative retrieval-augmented generation (RAG). TxAgent employs a fine-tuned Llama-3.1-8B model that dynamically generates and executes function calls to a unified biomedical tool suite (ToolUniverse), integrating FDA Drug API, OpenTargets, and Monarch resources to ensure access to current therapeutic information. In contrast to general-purpose RAG systems, medical applications impose stringent safety constraints, rendering the accuracy of both the reasoning trace and the sequence of tool invocations critical. These considerations motivate evaluation protocols treating token-level reasoning and tool-usage behaviors as explicit supervision signals. This work presents insights derived from our participation in the CURE-Bench NeurIPS 2025 Challenge, which benchmarks therapeutic-reasoning systems using metrics that assess correctness, tool utilization, and reasoning quality. We analyze how retrieval quality for function (tool) calls influences overall model performance and demonstrate performance gains achieved through improved tool-retrieval strategies. Our work was awarded the Excellence Award in Open Science. Complete information can be found at https://curebench.ai/.

