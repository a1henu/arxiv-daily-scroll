---
layout: default
title: FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis
---

# FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis
**arXiv**：[2603.09733v1](https://arxiv.org/abs/2603.09733) · [PDF](https://arxiv.org/pdf/2603.09733.pdf)  
**作者**：Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  

**一句话要点**：提出FetalAgents多智能体系统，以解决胎儿超声图像与视频分析中任务准确性与端到端临床工作流需求间的平衡问题。

**关键词**：多智能体系统, 胎儿超声分析, 端到端工作流, 视频流摘要, 临床报告生成, 多中心评估

## 3 点简述
- 核心问题：现有胎儿超声自动分析工具难以兼顾任务特定准确性和支持端到端临床工作流的全流程多功能性。
- 方法要点：通过轻量级智能体协调框架，动态编排专业视觉专家，优化诊断、测量和分割性能，并支持视频流摘要生成。
- 实验或效果：多中心外部评估显示，FetalAgents在八项临床任务中表现稳健准确，优于专业模型和多模态大语言模型。

## 摘要（原文）

> Fetal ultrasound (US) is the primary imaging modality for prenatal screening, yet its interpretation relies heavily on the expertise of the clinician. Despite advances in deep learning and foundation models, existing automated tools for fetal US analysis struggle to balance task-specific accuracy with the whole-process versatility required to support end-to-end clinical workflows. To address these limitations, we propose FetalAgents, the first multi-agent system for comprehensive fetal US analysis. Through a lightweight, agentic coordination framework, FetalAgents dynamically orchestrates specialized vision experts to maximize performance across diagnosis, measurement, and segmentation. Furthermore, FetalAgents advances beyond static image analysis by supporting end-to-end video stream summarization, where keyframes are automatically identified across multiple anatomical planes, analyzed by coordinated experts, and synthesized with patient metadata into a structured clinical report. Extensive multi-center external evaluations across eight clinical tasks demonstrate that FetalAgents consistently delivers the most robust and accurate performance when compared against specialized models and multimodal large language models (MLLMs), ultimately providing an auditable, workflow-aligned solution for fetal ultrasound analysis and reporting.

