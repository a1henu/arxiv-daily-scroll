---
layout: default
title: Deterministic Preprocessing and Interpretable Fuzzy Banding for Cost-per-Student Reporting from Extracted Records
---

# Deterministic Preprocessing and Interpretable Fuzzy Banding for Cost-per-Student Reporting from Extracted Records
**arXiv**：[2603.04905v1](https://arxiv.org/abs/2603.04905) · [PDF](https://arxiv.org/pdf/2603.04905.pdf)  
**作者**：Shane Lee, Stella Ng  

**一句话要点**：提出确定性预处理与可解释模糊分带方法，用于从提取记录生成生均成本报告

**关键词**：确定性预处理, 模糊分带, 生均成本报告, 行政数据转换, 可解释性, 工作流自动化

## 3 点简述
- 核心问题：行政提取数据常以电子表格形式交换，需可靠转换以支持预算和治理决策
- 方法要点：实现基于规则的确定性工作流，聚合成本与学生数，并添加模糊分带层进行解释
- 实验或效果：提供可复现计算示例，包括处理摘要、趋势分析和模糊分带工作表，支持快照匹配重算

## 摘要（原文）

> Administrative extracts are often exchanged as spreadsheets and may be read as reports in their own right during budgeting, workload review, and governance discussions. When an exported workbook becomes the reference snapshot for such decisions, the transformation can be checked by recomputation against a clearly identified input.
>   A deterministic, rule-governed, file-based workflow is implemented in cad_processor.py. The script ingests a Casual Academic Database (CAD) export workbook and aggregates inclusive on-costs and student counts into subject-year and school-year totals, from which it derives cost-per-student ratios. It writes a processed workbook with four sheets: Processing Summary (run record and counters), Trend Analysis (schoolyear cost-per-student matrix), Report (wide subject-level table), and Fuzzy Bands (per-year anchors, membership weights, and band labels). The run record includes a SHA-256 hash of the input workbook bytes to support snapshot-matched recomputation.
>   For within-year interpretation, the workflow adds a simple fuzzy banding layer that labels finite, positive school-year cost-per-student values as Low, Medium, or High. The per-year anchors are the minimum, median, and maximum of the finite, positive ratios. Membership weights are computed using left-shoulder, triangular, and right-shoulder functions, with deterministic tie-breaking in a fixed priority order (Medium, then Low, then High). These weights are treated as decision-support signals rather than probabilities.
>   A worked example provides a reproducible calculation of a band assignment from the reported anchors and ratios. Supplementary material includes a claim-to-evidence matrix, a reproducibility note, and a short glossary that links selected statements to code and workbook artefacts.

