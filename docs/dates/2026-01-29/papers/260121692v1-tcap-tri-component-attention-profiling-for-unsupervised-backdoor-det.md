---
layout: default
title: TCAP: Tri-Component Attention Profiling for Unsupervised Backdoor Detection in MLLM Fine-Tuning
---

# TCAP: Tri-Component Attention Profiling for Unsupervised Backdoor Detection in MLLM Fine-Tuning
**arXiv**：[2601.21692v1](https://arxiv.org/abs/2601.21692) · [PDF](https://arxiv.org/pdf/2601.21692.pdf)  
**作者**：Mingzu Liu, Hao Fang, Runmin Cong  

**一句话要点**：提出TCAP框架，通过三组件注意力分析实现MLLM微调中的无监督后门检测

**关键词**：多模态大语言模型, 后门检测, 无监督学习, 注意力机制, 微调服务, 跨模态分析

## 3 点简述
- 核心问题：MLLM微调服务中，中毒数据引入后门风险，现有防御方法依赖监督信号或泛化能力不足
- 方法要点：基于注意力分配差异，分解跨模态注意力图为系统指令、视觉输入和用户文本查询三组件，利用GMM统计分析和EM投票聚合检测后门样本
- 实验或效果：在多种MLLM架构和攻击方法上验证，TCAP表现稳定强劲，提供鲁棒实用的后门防御

## 摘要（原文）

> Fine-Tuning-as-a-Service (FTaaS) facilitates the customization of Multimodal Large Language Models (MLLMs) but introduces critical backdoor risks via poisoned data. Existing defenses either rely on supervised signals or fail to generalize across diverse trigger types and modalities. In this work, we uncover a universal backdoor fingerprint-attention allocation divergence-where poisoned samples disrupt the balanced attention distribution across three functional components: system instructions, vision inputs, and user textual queries, regardless of trigger morphology. Motivated by this insight, we propose Tri-Component Attention Profiling (TCAP), an unsupervised defense framework to filter backdoor samples. TCAP decomposes cross-modal attention maps into the three components, identifies trigger-responsive attention heads via Gaussian Mixture Model (GMM) statistical profiling, and isolates poisoned samples through EM-based vote aggregation. Extensive experiments across diverse MLLM architectures and attack methods demonstrate that TCAP achieves consistently strong performance, establishing it as a robust and practical backdoor defense in MLLMs.

