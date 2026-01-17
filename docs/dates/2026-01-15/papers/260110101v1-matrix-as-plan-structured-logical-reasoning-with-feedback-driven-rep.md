---
layout: default
title: MATRIX AS PLAN: Structured Logical Reasoning with Feedback-Driven Replanning
---

# MATRIX AS PLAN: Structured Logical Reasoning with Feedback-Driven Replanning
**arXiv**：[2601.10101v1](https://arxiv.org/abs/2601.10101) · [PDF](https://arxiv.org/pdf/2601.10101.pdf)  
**作者**：Ke Chen, Jiandian Zeng, Zihao Peng, Guo Li, Guangxue Zhang, Tian Wang  

**一句话要点**：提出MatrixCoT框架，通过矩阵规划和反馈重规划增强LLMs在复杂符号推理任务中的鲁棒性和可解释性。

**关键词**：逻辑推理, 矩阵规划, 反馈重规划, 结构化思维链, 符号推理增强, LLM鲁棒性

## 3 点简述
- 核心问题：现有CoT提示在依赖符号表达式和严格演绎规则的逻辑推理任务中表现不足，神经符号方法易受格式敏感性影响，LLM驱动方法缺乏结构化表示和错误纠正机制。
- 方法要点：引入矩阵化规划方法，规范化自然语言表达式并添加引用字段，以矩阵形式保留步骤间全局关系，并集成反馈驱动的重规划机制进行验证和优化。
- 实验或效果：在五个逻辑推理基准和五个LLMs上测试，MatrixCoT在不依赖外部求解器的情况下，提升了鲁棒性和可解释性，同时保持竞争力性能。

## 摘要（原文）

> As knowledge and semantics on the web grow increasingly complex, enhancing Large Language Models (LLMs) comprehension and reasoning capabilities has become particularly important. Chain-of-Thought (CoT) prompting has been shown to enhance the reasoning capabilities of LLMs. However, it still falls short on logical reasoning tasks that rely on symbolic expressions and strict deductive rules. Neuro-symbolic methods address this gap by enforcing formal correctness through external solvers. Yet these solvers are highly format-sensitive, and small instabilities in model outputs can lead to frequent processing failures. LLM-driven approaches avoid parsing brittleness, but they lack structured representations and process-level error-correction mechanisms. To further enhance the logical reasoning capabilities of LLMs, we propose MatrixCoT, a structured CoT framework with a matrix-based plan. Specifically, we normalize and type natural language expressions, attach explicit citation fields, and introduce a matrix-based planning method to preserve global relations among steps. The plan becomes a verifiable artifact, making execution more stable. For verification, we also add a feedback-driven replanning mechanism. Under semantic-equivalence constraints, it identifies omissions and defects, rewrites and compresses the dependency matrix, and produces a more trustworthy final answer. Experiments on five logical-reasoning benchmarks and five LLMs show that, without relying on external solvers, MatrixCoT enhances both robustness and interpretability when tackling complex symbolic reasoning tasks, while maintaining competitive performance.

