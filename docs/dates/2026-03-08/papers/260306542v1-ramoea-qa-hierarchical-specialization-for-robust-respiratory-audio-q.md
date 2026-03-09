---
layout: default
title: RAMoEA-QA: Hierarchical Specialization for Robust Respiratory Audio Question Answering
---

# RAMoEA-QA: Hierarchical Specialization for Robust Respiratory Audio Question Answering
**arXiv**：[2603.06542v1](https://arxiv.org/abs/2603.06542) · [PDF](https://arxiv.org/pdf/2603.06542.pdf)  
**作者**：Gaia A. Bertolino, Yuwei Zhang, Tong Xia, Domenico Talia, Cecilia Mascolo  

**一句话要点**：提出RAMoEA-QA，通过分层专业化解决呼吸音频问答中的异质性问题。

**关键词**：呼吸音频问答, 分层专业化, 专家混合, LoRA适配器, 多模态生成模型, 泛化能力

## 3 点简述
- 核心问题：呼吸音频问答面临设备、环境和查询意图的异质性挑战，现有系统缺乏专业化机制。
- 方法要点：采用两阶段条件专业化，音频专家混合路由音频编码器，语言适配器混合选择LoRA适配器以匹配查询。
- 实验或效果：在领域内测试准确率提升至0.72，在领域、模态和任务偏移下展现最强泛化能力。

## 摘要（原文）

> Conversational generative AI is rapidly entering healthcare, where general-purpose models must integrate heterogeneous patient signals and support diverse interaction styles while producing clinically meaningful outputs. In respiratory care, non-invasive audio, such as recordings captured via mobile microphones, enables scalable screening and longitudinal monitoring, but the heterogeneity challenge is particularly acute: recordings vary widely across devices, environments, and acquisition protocols, and questions span multiple intents and question formats. Existing biomedical audio-language QA systems are typically monolithic, without any specialization mechanisms for tackling diverse respiratory corpora and query intents. They are also only validated in limited settings, leaving it unclear how reliably they handle the shifts encountered in real-world settings.
>   To address these limitations, we introduce RAMoEA-QA, a hierarchically routed generative model for respiratory audio question answering that unifies multiple question types and supports both discrete and continuous targets within a single multimodal system. RAMoEA-QA applies two-stage conditional specialization: an Audio Mixture-of-Experts routes each recording to a suitable pre-trained audio encoder, and a Language Mixture-of-Adapters selects a LoRA adapter on a shared frozen LLM to match the query intent and answer format. By specializing both acoustic representations and generation behaviour per example, RAMoEA-QA consistently outperforms strong baselines and routing ablations with minimal parameter overhead, improving in-domain test accuracy to 0.72 (vs. 0.61 and 0.67 for state-of-the-art baselines) and exhibiting the strongest generalization for diagnosis under domain, modality, and task shifts.

