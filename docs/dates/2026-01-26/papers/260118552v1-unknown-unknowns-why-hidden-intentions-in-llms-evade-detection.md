---
layout: default
title: Unknown Unknowns: Why Hidden Intentions in LLMs Evade Detection
---

# Unknown Unknowns: Why Hidden Intentions in LLMs Evade Detection
**arXiv**：[2601.18552v1](https://arxiv.org/abs/2601.18552) · [PDF](https://arxiv.org/pdf/2601.18552.pdf)  
**作者**：Devansh Srivastav, David Pape, Lea Schönherr  

**一句话要点**：提出隐藏意图分类法，分析大语言模型在开放世界中的检测失败问题。

**关键词**：隐藏意图检测, 大语言模型安全, 开放世界评估, 分类法构建, 检测失败分析

## 3 点简述
- 核心问题：大语言模型输出中可能编码难以检测的隐藏意图，影响用户决策。
- 方法要点：基于社会科学研究，构建十类隐藏意图分类法，涵盖意图、机制、上下文和影响。
- 实验或效果：在开放世界设置下，检测方法失效，尤其在低流行率条件下，假阳性或假阴性导致风险。

## 摘要（原文）

> LLMs are increasingly embedded in everyday decision-making, yet their outputs can encode subtle, unintended behaviours that shape user beliefs and actions. We refer to these covert, goal-directed behaviours as hidden intentions, which may arise from training and optimisation artefacts, or be deliberately induced by an adversarial developer, yet remain difficult to detect in practice. We introduce a taxonomy of ten categories of hidden intentions, grounded in social science research and organised by intent, mechanism, context, and impact, shifting attention from surface-level behaviours to design-level strategies of influence. We show how hidden intentions can be easily induced in controlled models, providing both testbeds for evaluation and demonstrations of potential misuse. We systematically assess detection methods, including reasoning and non-reasoning LLM judges, and find that detection collapses in realistic open-world settings, particularly under low-prevalence conditions, where false positives overwhelm precision and false negatives conceal true risks. Stress tests on precision-prevalence and precision-FNR trade-offs reveal why auditing fails without vanishingly small false positive rates or strong priors on manipulation types. Finally, a qualitative case study shows that all ten categories manifest in deployed, state-of-the-art LLMs, emphasising the urgent need for robust frameworks. Our work provides the first systematic analysis of detectability failures of hidden intentions in LLMs under open-world settings, offering a foundation for understanding, inducing, and stress-testing such behaviours, and establishing a flexible taxonomy for anticipating evolving threats and informing governance.

