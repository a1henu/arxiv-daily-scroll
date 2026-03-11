---
layout: default
title: MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems
---

# MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems
**arXiv**：[2603.09909v1](https://arxiv.org/abs/2603.09909) · [PDF](https://arxiv.org/pdf/2603.09909.pdf)  
**作者**：Yunhang Qian, Xiaobin Hu, Jiaquan Yu, Siyang Xin, Xiaokun Chen, Jiangning Zhang, Peng-Tao Jiang, Jiawei Liu, Hongwei Bran Li  

**一句话要点**：提出MedMASLab统一框架以解决多模态医疗多智能体系统标准化与评估难题

**关键词**：多智能体系统, 医疗多模态, 临床决策支持, 标准化框架, 自动化评估, 跨专科基准

## 3 点简述
- 核心问题：医疗多智能体系统存在架构碎片化、多模态集成缺乏标准、跨专科评估不足。
- 方法要点：引入标准化多模态通信协议、自动化临床推理评估器及广泛基准数据集。
- 实验或效果：系统评估揭示领域特定性能差距，为未来自主临床系统建立技术基线。

## 摘要（原文）

> While Multi-Agent Systems (MAS) show potential for complex clinical decision support, the field remains hindered by architectural fragmentation and the lack of standardized multimodal integration. Current medical MAS research suffers from non-uniform data ingestion pipelines, inconsistent visual-reasoning evaluation, and a lack of cross-specialty benchmarking. To address these challenges, we present MedMASLab, a unified framework and benchmarking platform for multimodal medical multi-agent systems. MedMASLab introduces: (1) A standardized multimodal agent communication protocol that enables seamless integration of 11 heterogeneous MAS architectures across 24 medical modalities. (2) An automated clinical reasoning evaluator, a zero-shot semantic evaluation paradigm that overcomes the limitations of lexical string-matching by leveraging large vision-language models to verify diagnostic logic and visual grounding. (3) The most extensive benchmark to date, spanning 11 organ systems and 473 diseases, standardizing data from 11 clinical benchmarks. Our systematic evaluation reveals a critical domain-specific performance gap: while MAS improves reasoning depth, current architectures exhibit significant fragility when transitioning between specialized medical sub-domains. We provide a rigorous ablation of interaction mechanisms and cost-performance trade-offs, establishing a new technical baseline for future autonomous clinical systems. The source code and data is publicly available at: https://github.com/NUS-Project/MedMASLab/

