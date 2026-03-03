---
layout: default
title: NeuroSymb-MRG: Differentiable Abductive Reasoning with Active Uncertainty Minimization for Radiology Report Generation
---

# NeuroSymb-MRG: Differentiable Abductive Reasoning with Active Uncertainty Minimization for Radiology Report Generation
**arXiv**：[2603.01756v1](https://arxiv.org/abs/2603.01756) · [PDF](https://arxiv.org/pdf/2603.01756.pdf)  
**作者**：Rong Fu, Yiqing Lyu, Chunlei Meng, Muge Qi, Yabin Jin, Qi Zhao, Li Bao, Juntao Gao, Fuqian Shi, Nilanjan Dey, Wei Luo, Simon Fong  

**一句话要点**：提出NeuroSymb-MRG框架，通过神经符号归纳推理与主动不确定性最小化，提升放射学报告生成的临床一致性与推理能力。

**关键词**：放射学报告生成, 神经符号推理, 不确定性最小化, 临床推理, 检索增强生成

## 3 点简述
- 核心问题：现有方法存在视觉-语言偏差、事实不一致和缺乏显式多跳临床推理。
- 方法要点：集成神经符号归纳推理，包括概率概念映射、可微分逻辑推理链和检索增强语言模型编辑。
- 实验或效果：在标准基准测试中，相比基线方法，在事实一致性和语言指标上取得一致改进。

## 摘要（原文）

> Automatic generation of radiology reports seeks to reduce clinician workload while improving documentation consistency. Existing methods that adopt encoder-decoder or retrieval-augmented pipelines achieve progress in fluency but remain vulnerable to visual-linguistic biases, factual inconsistency, and lack of explicit multi-hop clinical reasoning. We present NeuroSymb-MRG, a unified framework that integrates NeuroSymbolic abductive reasoning with active uncertainty minimization to produce structured, clinically grounded reports. The system maps image features to probabilistic clinical concepts, composes differentiable logic-based reasoning chains, decodes those chains into templated clauses, and refines the textual output via retrieval and constrained language-model editing. An active sampling loop driven by rule-level uncertainty and diversity guides clinician-in-the-loop adjudication and promptbook refinement. Experiments on standard benchmarks demonstrate consistent improvements in factual consistency and standard language metrics compared to representative baselines.

