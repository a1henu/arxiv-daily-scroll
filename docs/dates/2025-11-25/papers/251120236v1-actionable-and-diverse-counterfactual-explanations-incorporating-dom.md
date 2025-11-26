---
layout: default
title: Actionable and diverse counterfactual explanations incorporating domain knowledge and causal constraints
---

# Actionable and diverse counterfactual explanations incorporating domain knowledge and causal constraints
**arXiv**：[2511.20236v1](https://arxiv.org/abs/2511.20236) · [PDF](https://arxiv.org/pdf/2511.20236.pdf)  
**作者**：Szymon Bobek, Łukasz Bałec, Grzegorz J. Nalepa  

**一句话要点**：提出DANCE方法以解决网络安全中反事实解释不现实的问题

**关键词**：反事实解释, 领域知识整合, 因果约束, 机器学习可解释性, 网络安全应用

## 3 点简述
- 核心问题：现有反事实解释忽略特征依赖，导致修改不现实或不实用
- 方法要点：结合领域知识和因果约束，确保反事实的合理性和可行性
- 实验或效果：在140个公共数据集上评估，优于现有方法，生成有意义解释

## 摘要（原文）

> Counterfactual explanations enhance the actionable interpretability of machine learning models by identifying the minimal changes required to achieve a desired outcome of the model. However, existing methods often ignore the complex dependencies in real-world datasets, leading to unrealistic or impractical modifications. Motivated by cybersecurity applications in the email marketing domain, we propose a method for generating Diverse, Actionable, and kNowledge-Constrained Explanations (DANCE), which incorporates feature dependencies and causal constraints to ensure plausibility and real-world feasibility of counterfactuals. Our method learns linear and nonlinear constraints from data or integrates expert-provided dependency graphs, ensuring counterfactuals are plausible and actionable. By maintaining consistency with feature relationships, the method produces explanations that align with real-world constraints. Additionally, it balances plausibility, diversity, and sparsity, effectively addressing key limitations in existing algorithms. The work is developed based on a real-life case study with Freshmail, the largest email marketing company in Poland and supported by a joint R&D project Sendguard. Furthermore, we provide an extensive evaluation using 140 public datasets, which highlights its ability to generate meaningful, domain-relevant counterfactuals that outperform other existing approaches based on widely used metrics. The source code for reproduction of the results can be found in a GitHub repository we provide.

