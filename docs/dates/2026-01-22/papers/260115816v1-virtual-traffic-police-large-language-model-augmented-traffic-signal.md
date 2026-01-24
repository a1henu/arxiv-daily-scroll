---
layout: default
title: Virtual Traffic Police: Large Language Model-Augmented Traffic Signal Control for Unforeseen Incidents
---

# Virtual Traffic Police: Large Language Model-Augmented Traffic Signal Control for Unforeseen Incidents
**arXiv**：[2601.15816v1](https://arxiv.org/abs/2601.15816) · [PDF](https://arxiv.org/pdf/2601.15816.pdf)  
**作者**：Shiqi Wei, Qiqing Wang, Kaidi Yang  

**一句话要点**：提出基于大语言模型的虚拟交通警察框架，以增强现有交通信号控制系统应对突发事故的能力。

**关键词**：交通信号控制, 大语言模型, 虚拟交通警察, 检索增强生成, 自精炼系统, 突发事故处理

## 3 点简述
- 核心问题：传统自适应交通信号控制方法在突发事故（如事故、道路维护）时依赖低效人工干预，现有大语言模型方案存在幻觉和替换成本高的问题。
- 方法要点：设计分层框架，上层虚拟交通警察代理动态微调下层信号控制器参数，结合自精炼交通语言检索系统提升领域可靠性。
- 实验或效果：结果显示大语言模型能作为可信虚拟警察，显著提高应对突发事故的操作效率和可靠性。

## 摘要（原文）

> Adaptive traffic signal control (TSC) has demonstrated strong effectiveness in managing dynamic traffic flows. However, conventional methods often struggle when unforeseen traffic incidents occur (e.g., accidents and road maintenance), which typically require labor-intensive and inefficient manual interventions by traffic police officers. Large Language Models (LLMs) appear to be a promising solution thanks to their remarkable reasoning and generalization capabilities. Nevertheless, existing works often propose to replace existing TSC systems with LLM-based systems, which can be (i) unreliable due to the inherent hallucinations of LLMs and (ii) costly due to the need for system replacement. To address the issues of existing works, we propose a hierarchical framework that augments existing TSC systems with LLMs, whereby a virtual traffic police agent at the upper level dynamically fine-tunes selected parameters of signal controllers at the lower level in response to real-time traffic incidents. To enhance domain-specific reliability in response to unforeseen traffic incidents, we devise a self-refined traffic language retrieval system (TLRS), whereby retrieval-augmented generation is employed to draw knowledge from a tailored traffic language database that encompasses traffic conditions and controller operation principles. Moreover, we devise an LLM-based verifier to update the TLRS continuously over the reasoning process. Our results show that LLMs can serve as trustworthy virtual traffic police officers that can adapt conventional TSC methods to unforeseen traffic incidents with significantly improved operational efficiency and reliability.

