---
layout: default
title: SpeechMedAssist: Efficiently and Effectively Adapting Speech Language Models for Medical Consultation
---

# SpeechMedAssist: Efficiently and Effectively Adapting Speech Language Models for Medical Consultation
**arXiv**：[2601.04638v1](https://arxiv.org/abs/2601.04638) · [PDF](https://arxiv.org/pdf/2601.04638.pdf)  
**作者**：Sirry Chen, Jieyi Wang, Wei Chen, Zhongyu Wei  

**一句话要点**：提出SpeechMedAssist，通过两阶段训练高效适应语音语言模型于医疗咨询场景。

**关键词**：语音语言模型, 医疗咨询, 两阶段训练, 模态对齐, 合成语音数据, 多轮交互

## 3 点简述
- 核心问题：医疗语音数据稀缺，直接微调语音语言模型效率低，阻碍其在医疗咨询中的应用。
- 方法要点：利用语音语言模型架构特性，将训练分为知识注入和模态对齐两阶段，仅需少量合成语音数据。
- 实验或效果：在单轮问答和多轮交互基准测试中，模型在多数设置下优于基线，展现高效性和鲁棒性。

## 摘要（原文）

> Medical consultations are intrinsically speech-centric. However, most prior works focus on long-text-based interactions, which are cumbersome and patient-unfriendly. Recent advances in speech language models (SpeechLMs) have enabled more natural speech-based interaction, yet the scarcity of medical speech data and the inefficiency of directly fine-tuning on speech data jointly hinder the adoption of SpeechLMs in medical consultation. In this paper, we propose SpeechMedAssist, a SpeechLM natively capable of conducting speech-based multi-turn interactions with patients. By exploiting the architectural properties of SpeechLMs, we decouple the conventional one-stage training into a two-stage paradigm consisting of (1) Knowledge & Capability Injection via Text and (2) Modality Re-alignment with Limited Speech Data, thereby reducing the requirement for medical speech data to only 10k synthesized samples. To evaluate SpeechLMs for medical consultation scenarios, we design a benchmark comprising both single-turn question answering and multi-turn simulated interactions. Experimental results show that our model outperforms all baselines in both effectiveness and robustness in most evaluation settings.

