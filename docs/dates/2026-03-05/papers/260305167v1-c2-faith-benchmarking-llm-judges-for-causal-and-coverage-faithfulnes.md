---
layout: default
title: C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning
---

# C2-Faith: Benchmarking LLM Judges for Causal and Coverage Faithfulness in Chain-of-Thought Reasoning
**arXiv**：[2603.05167v1](https://arxiv.org/abs/2603.05167) · [PDF](https://arxiv.org/pdf/2603.05167.pdf)  
**作者**：Avni Mittal, Rauno Arike  

**一句话要点**：提出C2-Faith基准，评估大语言模型在链式思维推理中因果与覆盖忠实性的判断能力

**关键词**：链式思维推理, 忠实性评估, 大语言模型评判, 因果检测, 覆盖评分, 基准测试

## 3 点简述
- 核心问题：大语言模型作为链式思维推理的评判者，能否可靠评估过程忠实性而非仅答案合理性
- 方法要点：基于PRM800K构建基准，通过控制扰动创建因果错误和覆盖缺失的示例
- 实验或效果：评估前沿模型在因果检测、定位和覆盖评分任务中的表现，发现模型表现依赖任务框架且存在显著差距

## 摘要（原文）

> Large language models (LLMs) are increasingly used as judges of chain-of-thought (CoT) reasoning, but it remains unclear whether they can reliably assess process faithfulness rather than just answer plausibility. We introduce C2-Faith, a benchmark built from PRM800K that targets two complementary dimensions of faithfulness: causality (does each step logically follow from prior context?) and coverage (are essential intermediate inferences present?). Using controlled perturbations, we create examples with known causal error positions by replacing a single step with an acausal variant, and with controlled coverage deletions at varying deletion rates (scored against reference labels). We evaluate three frontier judges under three tasks: binary causal detection, causal step localization, and coverage scoring. The results show that model rankings depend strongly on task framing, with no single judge dominating all settings; all judges exhibit a substantial gap between detecting an error and localizing it; and coverage judgments are systematically inflated for incomplete reasoning. These findings clarify when LLM judges are dependable and where they fail, and provide practical guidance for selecting judges in process-level evaluation

