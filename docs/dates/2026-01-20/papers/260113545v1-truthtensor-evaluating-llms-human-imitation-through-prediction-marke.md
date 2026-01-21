---
layout: default
title: TruthTensor: Evaluating LLMs Human Imitation through Prediction Market Drift and Holistic Reasoning
---

# TruthTensor: Evaluating LLMs Human Imitation through Prediction Market Drift and Holistic Reasoning
**arXiv**：[2601.13545v1](https://arxiv.org/abs/2601.13545) · [PDF](https://arxiv.org/pdf/2601.13545.pdf)  
**作者**：Shirin Shahabi, Spencer Graham, Haruna Isah  

**一句话要点**：提出TruthTensor评估范式，通过预测市场漂移和整体推理评估LLMs在真实世界决策中的人类模仿能力。

**关键词**：语言模型评估, 预测市场, 人类模仿系统, 整体推理, 漂移诊断, 可重复性评估

## 3 点简述
- 核心问题：静态基准无法捕捉真实世界不确定性、分布偏移及任务准确性与人类对齐决策的差距。
- 方法要点：基于前瞻性、无污染任务，结合预测市场和概率评分，提供模型行为的整体视图。
- 实验或效果：在500+真实市场实验中，显示模型在准确性、校准和风险敏感性等方面存在显著差异。

## 摘要（原文）

> Evaluating language models and AI agents remains fundamentally challenging because static benchmarks fail to capture real-world uncertainty, distribution shift, and the gap between isolated task accuracy and human-aligned decision-making under evolving conditions. This paper introduces TruthTensor, a novel, reproducible evaluation paradigm that measures Large Language Models (LLMs) not only as prediction engines but as human-imitation systems operating in socially-grounded, high-entropy environments. Building on forward-looking, contamination-free tasks, our framework anchors evaluation to live prediction markets and combines probabilistic scoring to provide a holistic view of model behavior. TruthTensor complements traditional correctness metrics with drift-centric diagnostics and explicit robustness checks for reproducibility. It specify human vs. automated evaluation roles, annotation protocols, and statistical testing procedures to ensure interpretability and replicability of results. In experiments across 500+ real markets (political, economic, cultural, technological), TruthTensor demonstrates that models with similar forecast accuracy can diverge markedly in calibration, drift, and risk-sensitivity, underscoring the need to evaluate models along multiple axes (accuracy, calibration, narrative stability, cost, and resource efficiency). TruthTensor therefore operationalizes modern evaluation best practices, clear hypothesis framing, careful metric selection, transparent compute/cost reporting, human-in-the-loop validation, and open, versioned evaluation contracts, to produce defensible assessments of LLMs in real-world decision contexts. We publicly release TruthTensor at https://truthtensor.com

