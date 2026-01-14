---
layout: default
title: Incentivizing Cardiologist-Like Reasoning in MLLMs for Interpretable Echocardiographic Diagnosis
---

# Incentivizing Cardiologist-Like Reasoning in MLLMs for Interpretable Echocardiographic Diagnosis
**arXiv**：[2601.08440v1](https://arxiv.org/abs/2601.08440) · [PDF](https://arxiv.org/pdf/2601.08440.pdf)  
**作者**：Yi Qin, Lehan Wang, Chenxu Zhao, Alex P. W. Lee, Xiaomeng Li  

**一句话要点**：提出CardiacMind方法以激励MLLMs在超声心动图诊断中模拟心脏科医生推理

**关键词**：超声心动图诊断, 多模态大语言模型, 强化学习, 医学推理, 心脏科医生思维, 诊断模板

## 3 点简述
- 核心问题：现有超声心动图基础模型难以关联定量测量与临床表现，MLLMs推理路径构建成本高且缺乏先验知识整合。
- 方法要点：引入心脏科医生思维，通过Cardiac Reasoning Template提供标准化诊断流程，结合强化学习奖励机制优化推理。
- 实验或效果：在15种复杂心脏病多视图诊断中提升48%，用户研究显示93.33%临床医生认可其推理逻辑。

## 摘要（原文）

> Echocardiographic diagnosis is vital for cardiac screening yet remains challenging. Existing echocardiography foundation models do not effectively capture the relationships between quantitative measurements and clinical manifestations, whereas medical reasoning multimodal large language models (MLLMs) require costly construction of detailed reasoning paths and remain ineffective at directly incorporating such echocardiographic priors into their reasoning. To address these limitations, we propose a novel approach comprising Cardiac Reasoning Template (CRT) and CardiacMind to enhance MLLM's echocardiographic reasoning by introducing cardiologist-like mindset. Specifically, CRT provides stepwise canonical diagnostic procedures for complex cardiac diseases to streamline reasoning path construction without the need for costly case-by-case verification. To incentivize reasoning MLLM under CRT, we develop CardiacMind, a new reinforcement learning scheme with three novel rewards: Procedural Quantity Reward (PQtR), Procedural Quality Reward (PQlR), and Echocardiographic Semantic Reward (ESR). PQtR promotes detailed reasoning; PQlR promotes integration of evidence across views and modalities, while ESR grounds stepwise descriptions in visual content. Our methods show a 48% improvement in multiview echocardiographic diagnosis for 15 complex cardiac diseases and a 5% improvement on CardiacNet-PAH over prior methods. The user study on our method's reasoning outputs shows 93.33% clinician agreement with cardiologist-like reasoning logic. Our code will be available.

