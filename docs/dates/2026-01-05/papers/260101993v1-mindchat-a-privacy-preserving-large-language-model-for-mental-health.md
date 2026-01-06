---
layout: default
title: MindChat: A Privacy-preserving Large Language Model for Mental Health Support
---

# MindChat: A Privacy-preserving Large Language Model for Mental Health Support
**arXiv**：[2601.01993v1](https://arxiv.org/abs/2601.01993) · [PDF](https://arxiv.org/pdf/2601.01993.pdf)  
**作者**：Dong Xue, Jicheng Tu, Ming Wang, Xin Yan, Fangzhou Liu, Jie Hu  

**一句话要点**：提出MindChat隐私保护大语言模型，通过合成数据集MindCorpus解决心理健康支持中数据稀缺与隐私问题。

**关键词**：心理健康支持, 隐私保护大语言模型, 合成数据集, 联邦学习, 差分隐私优化, 多智能体角色扮演

## 3 点简述
- 核心问题：心理健康支持大语言模型训练受限于真实咨询对话的稀缺性和敏感性。
- 方法要点：使用多智能体角色扮演框架构建合成数据集MindCorpus，并采用联邦学习与差分隐私优化进行隐私保护微调。
- 实验或效果：MindCorpus提升训练效果，MindChat在自动和人工评估中与基线模型竞争，同时减少隐私泄露风险。

## 摘要（原文）

> Large language models (LLMs) have shown promise for mental health support, yet training such models is constrained by the scarcity and sensitivity of real counseling dialogues. In this article, we present MindChat, a privacy-preserving LLM for mental health support, together with MindCorpus, a synthetic multi-turn counseling dataset constructed via a multi-agent role-playing framework. To synthesize high-quality counseling data, the developed dialogue-construction framework employs a dual closed-loop feedback design to integrate psychological expertise and counseling techniques through role-playing: (i) turn-level critique-and-revision to improve coherence and counseling appropriateness within a session, and (ii) session-level strategy refinement to progressively enrich counselor behaviors across sessions. To mitigate privacy risks under decentralized data ownership, we fine-tune the base model using federated learning with parameter-efficient LoRA adapters and incorporate differentially private optimization to reduce membership and memorization risks. Experiments on synthetic-data quality assessment and counseling capability evaluation show that MindCorpus improves training effectiveness and that MindChat is competitive with existing general and counseling-oriented LLM baselines under both automatic LLM-judge and human evaluation protocols, while exhibiting reduced privacy leakage under membership inference attacks.

