---
layout: default
title: GAVEL: Towards rule-based safety through activation monitoring
---

# GAVEL: Towards rule-based safety through activation monitoring
**arXiv**：[2601.19768v1](https://arxiv.org/abs/2601.19768) · [PDF](https://arxiv.org/pdf/2601.19768.pdf)  
**作者**：Shir Rozenfeld, Rahul Pankajakshan, Itay Zloczower, Eyal Lenga, Gilad Gressel, Yisroel Mirsky  

**一句话要点**：提出基于规则的激活安全框架GAVEL，以提升大语言模型安全监控的精确性和可解释性。

**关键词**：激活监控, 规则安全, 认知元素, 大语言模型, AI治理, 可解释性

## 3 点简述
- 现有激活安全方法存在精度低、灵活性差和可解释性不足的问题。
- 将激活建模为可组合的认知元素，支持定义谓词规则进行实时违规检测。
- 实验表明该方法提高了精度，支持领域定制，为可扩展AI治理奠定基础。

## 摘要（原文）

> Large language models (LLMs) are increasingly paired with activation-based monitoring to detect and prevent harmful behaviors that may not be apparent at the surface-text level. However, existing activation safety approaches, trained on broad misuse datasets, struggle with poor precision, limited flexibility, and lack of interpretability. This paper introduces a new paradigm: rule-based activation safety, inspired by rule-sharing practices in cybersecurity. We propose modeling activations as cognitive elements (CEs), fine-grained, interpretable factors such as ''making a threat'' and ''payment processing'', that can be composed to capture nuanced, domain-specific behaviors with higher precision. Building on this representation, we present a practical framework that defines predicate rules over CEs and detects violations in real time. This enables practitioners to configure and update safeguards without retraining models or detectors, while supporting transparency and auditability. Our results show that compositional rule-based activation safety improves precision, supports domain customization, and lays the groundwork for scalable, interpretable, and auditable AI governance. We will release GAVEL as an open-source framework and provide an accompanying automated rule creation tool.

