---
layout: default
title: WorkflowPerturb: Calibrated Stress Tests for Evaluating Multi-Agent Workflow Metrics
---

# WorkflowPerturb: Calibrated Stress Tests for Evaluating Multi-Agent Workflow Metrics
**arXiv**：[2602.17990v1](https://arxiv.org/abs/2602.17990) · [PDF](https://arxiv.org/pdf/2602.17990.pdf)  
**作者**：Madhav Kanda, Pedro Las-Casas, Alok Gautam Kumbhare, Rodrigo Fonseca, Sharad Agarwal  

**一句话要点**：提出WorkflowPerturb基准，通过受控扰动评估多智能体工作流指标的校准与敏感性。

**关键词**：工作流评估, 指标校准, 多智能体系统, 基准测试, 受控扰动

## 3 点简述
- 核心问题：LLM生成工作流的自动评估指标未校准，分数变化难以反映工作流退化严重程度。
- 方法要点：构建包含4,973个黄金工作流和44,757个扰动变体的基准，应用缺失、压缩和描述变化三类扰动。
- 实验或效果：基准测试多种指标家族，分析其敏感性和校准，支持基于严重程度的工作流评估分数解释。

## 摘要（原文）

> LLM-based systems increasingly generate structured workflows for complex tasks. In practice, automatic evaluation of these workflows is difficult, because metric scores are often not calibrated, and score changes do not directly communicate the severity of workflow degradation. We introduce WorkflowPerturb, a controlled benchmark for studying workflow evaluation metrics. It works by applying realistic, controlled perturbations to golden workflows. WorkflowPerturb contains 4,973 golden workflows and 44,757 perturbed variants across three perturbation types (Missing Steps, Compressed Steps, and Description Changes), each applied at severity levels of 10%, 30%, and 50%. We benchmark multiple metric families and analyze their sensitivity and calibration using expected score trajectories and residuals. Our results characterize systematic differences across metric families and support severity-aware interpretation of workflow evaluation scores. Our dataset will be released upon acceptance.

