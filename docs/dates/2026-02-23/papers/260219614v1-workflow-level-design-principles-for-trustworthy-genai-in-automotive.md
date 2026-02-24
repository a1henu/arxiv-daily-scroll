---
layout: default
title: Workflow-Level Design Principles for Trustworthy GenAI in Automotive System Engineering
---

# Workflow-Level Design Principles for Trustworthy GenAI in Automotive System Engineering
**arXiv**：[2602.19614v1](https://arxiv.org/abs/2602.19614) · [PDF](https://arxiv.org/pdf/2602.19614.pdf)  
**作者**：Chih-Hong Cheng, Brian Hsuan-Cheng Liao, Adam Molin, Hasan Esen  

**一句话要点**：提出工作流级设计原则，以提升汽车系统工程中可信生成式AI的集成

**关键词**：可信生成式AI, 汽车系统工程, 工作流设计原则, 需求变更识别, SysML v2模型更新, 回归测试生成

## 3 点简述
- 核心问题：大型语言模型在安全关键系统工程中应用受限于可信度、可追溯性和验证实践对齐。
- 方法要点：采用分段分解、多样性采样和轻量NLP检查，改进需求变更识别的完整性和正确性。
- 实验或效果：通过端到端汽车管道演示，从需求变更识别到SysML v2架构更新和回归测试验证。

## 摘要（原文）

> The adoption of large language models in safety-critical system engineering is constrained by trustworthiness, traceability, and alignment with established verification practices. We propose workflow-level design principles for trustworthy GenAI integration and demonstrate them in an end-to-end automotive pipeline, from requirement delta identification to SysML v2 architecture update and re-testing. First, we show that monolithic ("big-bang") prompting misses critical changes in large specifications, while section-wise decomposition with diversity sampling and lightweight NLP sanity checks improves completeness and correctness. Then, we propagate requirement deltas into SysML v2 models and validate updates via compilation and static analysis. Additionally, we ensure traceable regression testing by generating test cases through explicit mappings from specification variables to architectural ports and states, providing practical safeguards for GenAI used in safety-critical automotive engineering.

