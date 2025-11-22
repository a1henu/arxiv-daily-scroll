---
layout: default
title: SurvAgent: Hierarchical CoT-Enhanced Case Banking and Dichotomy-Based Multi-Agent System for Multimodal Survival Prediction
---

# SurvAgent: Hierarchical CoT-Enhanced Case Banking and Dichotomy-Based Multi-Agent System for Multimodal Survival Prediction
**arXiv**：[2511.16635v1](https://arxiv.org/abs/2511.16635) · [PDF](https://arxiv.org/pdf/2511.16635.pdf)  
**作者**：Guolin Huang, Wenting Chen, Jiaqi Yang, Xinheng Lyu, Xiaoling Luo, Sen Yang, Xiaohan Xing, Linlin Shen  

**一句话要点**：提出SurvAgent分层CoT增强多智能体系统，用于多模态生存预测以提升可解释性。

**关键词**：生存预测, 多智能体系统, 链式思维, 多模态数据, 可解释AI, 精准肿瘤学

## 3 点简述
- 现有生存分析方法缺乏透明度，难以整合多模态数据和利用历史案例经验。
- 方法包括WSI-Gene CoT增强案例库构建和二分法多专家智能体推理。
- 在五个TCGA队列实验中优于传统方法、专有MLLM和医疗智能体。

## 摘要（原文）

> Survival analysis is critical for cancer prognosis and treatment planning, yet existing methods lack the transparency essential for clinical adoption. While recent pathology agents have demonstrated explainability in diagnostic tasks, they face three limitations for survival prediction: inability to integrate multimodal data, ineffective region-of-interest exploration, and failure to leverage experiential learning from historical cases. We introduce SurvAgent, the first hierarchical chain-of-thought (CoT)-enhanced multi-agent system for multimodal survival prediction. SurvAgent consists of two stages: (1) WSI-Gene CoT-Enhanced Case Bank Construction employs hierarchical analysis through Low-Magnification Screening, Cross-Modal Similarity-Aware Patch Mining, and Confidence-Aware Patch Mining for pathology images, while Gene-Stratified analysis processes six functional gene categories. Both generate structured reports with CoT reasoning, storing complete analytical processes for experiential learning. (2) Dichotomy-Based Multi-Expert Agent Inference retrieves similar cases via RAG and integrates multimodal reports with expert predictions through progressive interval refinement. Extensive experiments on five TCGA cohorts demonstrate SurvAgent's superority over conventional methods, proprietary MLLMs, and medical agents, establishing a new paradigm for explainable AI-driven survival prediction in precision oncology.

