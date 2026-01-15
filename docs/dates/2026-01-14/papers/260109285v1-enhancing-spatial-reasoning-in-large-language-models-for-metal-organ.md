---
layout: default
title: Enhancing Spatial Reasoning in Large Language Models for Metal-Organic Frameworks Structure Prediction
---

# Enhancing Spatial Reasoning in Large Language Models for Metal-Organic Frameworks Structure Prediction
**arXiv**：[2601.09285v1](https://arxiv.org/abs/2601.09285) · [PDF](https://arxiv.org/pdf/2601.09285.pdf)  
**作者**：Mianzhi Pan, JianFei Li, Peishuo Liu, Botian Wang, Yawen Ouyang, Yiming Rong, Hao Zhou, Jianbing Zhang  

**一句话要点**：提出MOF-LLM框架，通过块级预测增强大语言模型空间推理能力，用于金属有机框架结构预测。

**关键词**：金属有机框架预测, 大语言模型应用, 空间推理增强, 块级结构生成, 强化学习优化

## 3 点简述
- 核心问题：金属有机框架（MOFs）结构预测因原子复杂性高而困难，现有大语言模型应用受限。
- 方法要点：引入块级预测框架MOF-LLM，结合空间感知持续预训练、结构监督微调和匹配驱动强化学习。
- 实验或效果：MOF-LLM在实验中超越现有方法，表现出更高的采样效率和预测准确性。

## 摘要（原文）

> Metal-organic frameworks (MOFs) are porous crystalline materials with broad applications such as carbon capture and drug delivery, yet accurately predicting their 3D structures remains a significant challenge. While Large Language Models (LLMs) have shown promise in generating crystals, their application to MOFs is hindered by MOFs' high atomic complexity. Inspired by the success of block-wise paradigms in deep generative models, we pioneer the use of LLMs in this domain by introducing MOF-LLM, the first LLM framework specifically adapted for block-level MOF structure prediction. To effectively harness LLMs for this modular assembly task, our training paradigm integrates spatial-aware continual pre-training (CPT), structural supervised fine-tuning (SFT), and matching-driven reinforcement learning (RL). By incorporating explicit spatial priors and optimizing structural stability via Soft Adaptive Policy Optimization (SAPO), our approach substantially enhances the spatial reasoning capability of a Qwen-3 8B model for accurate MOF structure prediction. Comprehensive experiments demonstrate that MOF-LLM outperforms state-of-the-art denoising-based and LLM-based methods while exhibiting superior sampling efficiency.

