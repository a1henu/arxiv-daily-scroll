---
layout: default
title: Toward Explaining Large Language Models in Software Engineering Tasks
---

# Toward Explaining Large Language Models in Software Engineering Tasks
**arXiv**：[2512.20328v1](https://arxiv.org/abs/2512.20328) · [PDF](https://arxiv.org/pdf/2512.20328.pdf)  
**作者**：Antonio Vitale, Khai-Nguyen Nguyen, Denys Poshyvanyk, Rocco Oliveto, Simone Scalabrino, Antonio Mastropaolo  

**一句话要点**：提出FeatureSHAP框架以解决软件工程中大语言模型的可解释性问题

**关键词**：大语言模型, 软件工程, 可解释人工智能, Shapley值, 代码生成, 代码总结

## 3 点简述
- 核心问题：大语言模型在软件工程任务中缺乏领域特定的可解释性，阻碍其在安全关键领域的应用。
- 方法要点：基于Shapley值，通过输入扰动和任务相似性比较，自动化生成模型无关的解释。
- 实验或效果：在代码生成和总结任务中，FeatureSHAP比基线方法更准确，用户调查显示其提升决策理解。

## 摘要（原文）

> Recent progress in Large Language Models (LLMs) has substantially advanced the automation of software engineering (SE) tasks, enabling complex activities such as code generation and code summarization. However, the black-box nature of LLMs remains a major barrier to their adoption in high-stakes and safety-critical domains, where explainability and transparency are vital for trust, accountability, and effective human supervision. Despite increasing interest in explainable AI for software engineering, existing methods lack domain-specific explanations aligned with how practitioners reason about SE artifacts. To address this gap, we introduce FeatureSHAP, the first fully automated, model-agnostic explainability framework tailored to software engineering tasks. Based on Shapley values, FeatureSHAP attributes model outputs to high-level input features through systematic input perturbation and task-specific similarity comparisons, while remaining compatible with both open-source and proprietary LLMs. We evaluate FeatureSHAP on two bi-modal SE tasks: code generation and code summarization. The results show that FeatureSHAP assigns less importance to irrelevant input features and produces explanations with higher fidelity than baseline methods. A practitioner survey involving 37 participants shows that FeatureSHAP helps practitioners better interpret model outputs and make more informed decisions. Collectively, FeatureSHAP represents a meaningful step toward practical explainable AI in software engineering. FeatureSHAP is available at https://github.com/deviserlab/FeatureSHAP.

