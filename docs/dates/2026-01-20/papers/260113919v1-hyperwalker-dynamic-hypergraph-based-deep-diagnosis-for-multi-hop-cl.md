---
layout: default
title: HyperWalker: Dynamic Hypergraph-Based Deep Diagnosis for Multi-Hop Clinical Modeling across EHR and X-Ray in Medical VLMs
---

# HyperWalker: Dynamic Hypergraph-Based Deep Diagnosis for Multi-Hop Clinical Modeling across EHR and X-Ray in Medical VLMs
**arXiv**：[2601.13919v1](https://arxiv.org/abs/2601.13919) · [PDF](https://arxiv.org/pdf/2601.13919.pdf)  
**作者**：Yuezhe Yang, Hao Wang, Yige Peng, Jinman Kim, Lei Bi  

**一句话要点**：提出HyperWalker框架，通过动态超图和多跳检索解决医疗多模态诊断中样本孤立推理的局限性。

**关键词**：医疗视觉语言模型, 动态超图, 多跳临床推理, 电子健康记录, 强化学习诊断

## 3 点简述
- 核心问题：现有医疗视觉语言模型在诊断时独立处理样本，忽略电子健康记录和外部证据，限制推理准确性。
- 方法要点：构建动态超图iBrochure建模异构数据，结合强化学习Walker和多跳检索机制优化诊断路径。
- 实验或效果：在MIMIC和EHRXQA数据集上实现医疗报告生成和视觉问答的先进性能。

## 摘要（原文）

> Automated clinical diagnosis remains a core challenge in medical AI, which usually requires models to integrate multi-modal data and reason across complex, case-specific contexts. Although recent methods have advanced medical report generation (MRG) and visual question answering (VQA) with medical vision-language models (VLMs), these methods, however, predominantly operate under a sample-isolated inference paradigm, as such processing cases independently without access to longitudinal electronic health records (EHRs) or structurally related patient examples. This paradigm limits reasoning to image-derived information alone, which ignores external complementary medical evidence for potentially more accurate diagnosis. To overcome this limitation, we propose \textbf{HyperWalker}, a \textit{Deep Diagnosis} framework that reformulates clinical reasoning via dynamic hypergraphs and test-time training. First, we construct a dynamic hypergraph, termed \textbf{iBrochure}, to model the structural heterogeneity of EHR data and implicit high-order associations among multimodal clinical information. Within this hypergraph, a reinforcement learning agent, \textbf{Walker}, navigates to and identifies optimal diagnostic paths. To ensure comprehensive coverage of diverse clinical characteristics in test samples, we incorporate a \textit{linger mechanism}, a multi-hop orthogonal retrieval strategy that iteratively selects clinically complementary neighborhood cases reflecting distinct clinical attributes. Experiments on MRG with MIMIC and medical VQA on EHRXQA demonstrate that HyperWalker achieves state-of-the-art performance. Code is available at: https://github.com/Bean-Young/HyperWalker

