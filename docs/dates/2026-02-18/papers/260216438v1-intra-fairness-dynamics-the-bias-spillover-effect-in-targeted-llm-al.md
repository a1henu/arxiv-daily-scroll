---
layout: default
title: Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment
---

# Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment
**arXiv**：[2602.16438v1](https://arxiv.org/abs/2602.16438) · [PDF](https://arxiv.org/pdf/2602.16438.pdf)  
**作者**：Eva Paraschou, Line Harder Clemmensen, Sneha Das  

**一句话要点**：揭示目标对齐中的偏见溢出效应，强调多属性公平评估的必要性

**关键词**：偏见溢出, 多属性公平, LLM对齐, 上下文感知评估, DPO优化, BBQ基准

## 3 点简述
- 核心问题：传统LLM公平对齐聚焦单一敏感属性，忽视多维公平，导致偏见溢出风险
- 方法要点：使用DPO和BBQ基准，评估三个先进LLM在目标性别对齐下的多属性公平性
- 实验或效果：发现模糊语境下偏见显著恶化，如外貌、性取向和残疾状态，需上下文感知评估

## 摘要（原文）

> Conventional large language model (LLM) fairness alignment largely focuses on mitigating bias along single sensitive attributes, overlooking fairness as an inherently multidimensional and context-specific value. This approach risks creating systems that achieve narrow fairness metrics while exacerbating disparities along untargeted attributes, a phenomenon known as bias spillover. While extensively studied in machine learning, bias spillover remains critically underexplored in LLM alignment. In this work, we investigate how targeted gender alignment affects fairness across nine sensitive attributes in three state-of-the-art LLMs (Mistral 7B, Llama 3.1 8B, Qwen 2.5 7B). Using Direct Preference Optimization and the BBQ benchmark, we evaluate fairness under ambiguous and disambiguous contexts. Our findings reveal noticeable bias spillover: while aggregate results show improvements, context-aware analysis exposes significant degradations in ambiguous contexts, particularly for physical appearance ($p< 0.001$ across all models), sexual orientation, and disability status. We demonstrate that improving fairness along one attribute can inadvertently worsen disparities in others under uncertainty, highlighting the necessity of context-aware, multi-attribute fairness evaluation frameworks.

