---
layout: default
title: AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration
---

# AXIOM: Benchmarking LLM-as-a-Judge for Code via Rule-Based Perturbation and Multisource Quality Calibration
**arXiv**：[2512.20159v1](https://arxiv.org/abs/2512.20159) · [PDF](https://arxiv.org/pdf/2512.20159.pdf)  
**作者**：Ruiqi Wang, Xinchen Wang, Cuiyun Gao, Chun Yong Chong, Xin Xia, Qing Liao  

**一句话要点**：提出AXIOM框架，通过规则扰动和多源校准构建代码评估基准，以解决现有基准的局限性。

**关键词**：代码评估基准, LLM-as-a-judge, 规则扰动, 质量校准, 程序合成, 软件工程

## 3 点简述
- 现有代码评估基准存在标签粗糙、标准主观或分布不平衡等问题，影响LLM-as-a-judge指标的可靠性。
- AXIOM采用规则引导的扰动方法，精确控制程序质量分数，实现平衡分布；结合多源质量校准优化人工标注。
- 未知具体实验效果，但框架旨在提升基准多样性和评估准确性，适用于代码生成场景。

## 摘要（原文）

> Large language models (LLMs) have been increasingly deployed in real-world software engineering, fostering the development of code evaluation metrics to study the quality of LLM-generated code. Conventional rule-based metrics merely score programs based on their surface-level similarities with reference programs instead of analyzing functionality and code quality in depth. To address this limitation, researchers have developed LLM-as-a-judge metrics, prompting LLMs to evaluate and score code, and curated various code evaluation benchmarks to validate their effectiveness. However, these benchmarks suffer from critical limitations, hindering reliable assessments of evaluation capability: Some feature coarse-grained binary labels, which reduce rich code behavior to a single bit of information, obscuring subtle errors. Others propose fine-grained but subjective, vaguely-defined evaluation criteria, introducing unreliability in manually-annotated scores, which is the ground-truth they rely on. Furthermore, they often use uncontrolled data synthesis methods, leading to unbalanced score distributions that poorly represent real-world code generation scenarios.
>   To curate a diverse benchmark with programs of well-balanced distributions across various quality levels and streamline the manual annotation procedure, we propose AXIOM, a novel perturbation-based framework for synthesizing code evaluation benchmarks at scale. It reframes program scores as the refinement effort needed for deployment, consisting of two stages: (1) Rule-guided perturbation, which prompts LLMs to apply sequences of predefined perturbation rules to existing high-quality programs to modify their functionality and code quality, enabling us to precisely control each program's target score to achieve balanced score distributions. (2) Multisource quality calibration, which first selects a subset of...

