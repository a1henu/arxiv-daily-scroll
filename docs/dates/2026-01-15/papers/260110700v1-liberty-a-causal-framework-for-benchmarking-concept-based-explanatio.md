---
layout: default
title: LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals
---

# LIBERTy: A Causal Framework for Benchmarking Concept-Based Explanations of LLMs with Structural Counterfactuals
**arXiv**：[2601.10700v1](https://arxiv.org/abs/2601.10700) · [PDF](https://arxiv.org/pdf/2601.10700.pdf)  
**作者**：Gilat Toker, Nitay Calderon, Ohad Amosy, Roi Reichart  

**一句话要点**：提出LIBERTy框架，基于结构因果模型生成反事实对，以评估LLM概念解释的忠实性。

**关键词**：概念解释评估, 结构反事实, LLM基准, 忠实性度量, 因果框架

## 3 点简述
- 核心问题：现有基准依赖人工反事实，成本高且不完美，难以评估概念解释的忠实性。
- 方法要点：通过定义文本生成的结构因果模型，干预概念并传播至LLM生成反事实对，构建数据集。
- 实验或效果：评估多种方法，发现概念解释有改进空间，专有LLM对人口统计概念敏感性降低。

## 摘要（原文）

> Concept-based explanations quantify how high-level concepts (e.g., gender or experience) influence model behavior, which is crucial for decision-makers in high-stakes domains. Recent work evaluates the faithfulness of such explanations by comparing them to reference causal effects estimated from counterfactuals. In practice, existing benchmarks rely on costly human-written counterfactuals that serve as an imperfect proxy. To address this, we introduce a framework for constructing datasets containing structural counterfactual pairs: LIBERTy (LLM-based Interventional Benchmark for Explainability with Reference Targets). LIBERTy is grounded in explicitly defined Structured Causal Models (SCMs) of the text generation, interventions on a concept propagate through the SCM until an LLM generates the counterfactual. We introduce three datasets (disease detection, CV screening, and workplace violence prediction) together with a new evaluation metric, order-faithfulness. Using them, we evaluate a wide range of methods across five models and identify substantial headroom for improving concept-based explanations. LIBERTy also enables systematic analysis of model sensitivity to interventions: we find that proprietary LLMs show markedly reduced sensitivity to demographic concepts, likely due to post-training mitigation. Overall, LIBERTy provides a much-needed benchmark for developing faithful explainability methods.

