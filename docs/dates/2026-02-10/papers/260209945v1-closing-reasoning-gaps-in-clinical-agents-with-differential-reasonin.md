---
layout: default
title: Closing Reasoning Gaps in Clinical Agents with Differential Reasoning Learning
---

# Closing Reasoning Gaps in Clinical Agents with Differential Reasoning Learning
**arXiv**：[2602.09945v1](https://arxiv.org/abs/2602.09945) · [PDF](https://arxiv.org/pdf/2602.09945.pdf)  
**作者**：Jinsong Liu, Yuhang Jiang, Ramayya Krishnan, Rema Padman, Yiye Zhang, Jiang Bian  

**一句话要点**：提出差分推理学习框架，通过分析推理差异提升临床决策代理的可靠性和准确性。

**关键词**：临床决策支持, 差分推理学习, 图编辑距离, 检索增强生成, 推理保真度, 医疗问答

## 3 点简述
- 核心问题：临床决策支持需确保推理过程符合临床逻辑，而现有代理存在推理差距。
- 方法要点：从参考推理和代理链式思维中提取有向无环图，基于加权图编辑距离诊断差异，构建知识库并通过检索增强生成补丁推理。
- 实验或效果：在开放医疗问答和内部临床预测任务中验证，提升答案准确性和推理保真度，临床医生评审支持其可靠性。

## 摘要（原文）

> Clinical decision support requires not only correct answers but also clinically valid reasoning. We propose Differential Reasoning Learning (DRL), a framework that improves clinical agents by learning from reasoning discrepancies. From reference reasoning rationales (e.g., physician-authored clinical rationale, clinical guidelines, or outputs from more capable models) and the agent's free-form chain-of-thought (CoT), DRL extracts reasoning graphs as directed acyclic graphs (DAGs) and performs a clinically weighted graph edit distance (GED)-based discrepancy analysis. An LLM-as-a-judge aligns semantically equivalent nodes and diagnoses discrepancies between graphs. These graph-level discrepancy diagnostics are converted into natural-language instructions and stored in a Differential Reasoning Knowledge Base (DR-KB). At inference, we retrieve top-$k$ instructions via Retrieval-Augmented Generation (RAG) to augment the agent prompt and patch likely logic gaps. Evaluation on open medical question answering (QA) benchmarks and a Return Visit Admissions (RVA) prediction task from internal clinical data demonstrates gains over baselines, improving both final-answer accuracy and reasoning fidelity. Ablation studies confirm gains from infusing reference reasoning rationales and the top-$k$ retrieval strategy. Clinicians' review of the output provides further assurance of the approach. Together, results suggest that DRL supports more reliable clinical decision-making in complex reasoning scenarios and offers a practical mechanism for deployment under limited token budgets.

