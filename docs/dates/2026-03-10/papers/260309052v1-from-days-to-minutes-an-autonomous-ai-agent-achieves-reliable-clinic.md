---
layout: default
title: From Days to Minutes: An Autonomous AI Agent Achieves Reliable Clinical Triage in Remote Patient Monitoring
---

# From Days to Minutes: An Autonomous AI Agent Achieves Reliable Clinical Triage in Remote Patient Monitoring
**arXiv**：[2603.09052v1](https://arxiv.org/abs/2603.09052) · [PDF](https://arxiv.org/pdf/2603.09052.pdf)  
**作者**：Seunghwan Kim, Tiffany H. Kung, Heena Verma, Dilan Edirisinghe, Kaveh Sedehi, Johanna Alvarez, Diane Shilling, Audra Lisa Doyle, Ajit Chary, William Borden, Ming Jack Po  

**一句话要点**：提出Sentinel自主AI代理，通过上下文分诊解决远程患者监测数据过载问题

**关键词**：远程患者监测, 自主AI代理, 临床分诊, 模型上下文协议, 多步推理

## 3 点简述
- 核心问题：远程患者监测数据量大，传统方法成本高且不可扩展，导致临床试验失败
- 方法要点：使用模型上下文协议和多步推理，结合21个临床工具进行自主上下文分诊
- 实验或效果：在紧急敏感性和可操作警报敏感性上超越个体临床医生，成本低至每次分诊0.34美元

## 摘要（原文）

> Background: Remote patient monitoring (RPM) generates vast data, yet landmark trials (Tele-HF, BEAT-HF) failed because data volume overwhelmed clinical staff. While TIM-HF2 showed 24/7 physician-led monitoring reduces mortality by 30%, this model remains prohibitively expensive and unscalable.
>   Methods: We developed Sentinel, an autonomous AI agent using Model Context Protocol (MCP) for contextual triage of RPM vitals via 21 clinical tools and multi-step reasoning. Evaluation included: (1) self-consistency (100 readings x 5 runs); (2) comparison against rule-based thresholds; and (3) validation against 6 clinicians (3 physicians, 3 NPs) using a connected matrix design. A leave-one-out (LOO) analysis compared the agent against individual clinicians; severe overtriage cases underwent independent physician adjudication.
>   Results: Against a human majority-vote standard (N=467), the agent achieved 95.8% emergency sensitivity and 88.5% sensitivity for all actionable alerts (85.7% specificity). Four-level exact accuracy was 69.4% (quadratic-weighted kappa=0.778); 95.9% of classifications were within one severity level. In LOO analysis, the agent outperformed every clinician in emergency sensitivity (97.5% vs. 60.0% aggregate) and actionable sensitivity (90.9% vs. 69.5%). While disagreements skewed toward overtriage (22.5%), independent adjudication of severe gaps (>=2 levels) validated agent escalation in 88-94% of cases; consensus resolution validated 100%. The agent showed near-perfect self-consistency (kappa=0.850). Median cost was $0.34/triage.
>   Conclusions: Sentinel triages RPM vitals with sensitivity exceeding individual clinicians. By automating systematic context synthesis, Sentinel addresses the core limitation of prior RPM trials, offering a scalable path toward the intensive monitoring shown to reduce mortality while maintaining a clinically defensible overtriage profile.

