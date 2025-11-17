---
layout: default
title: S2D-ALIGN: Shallow-to-Deep Auxiliary Learning for Anatomically-Grounded Radiology Report Generation
---

# S2D-ALIGN: Shallow-to-Deep Auxiliary Learning for Anatomically-Grounded Radiology Report Generation
**arXiv**：[2511.11066v1](https://arxiv.org/abs/2511.11066) · [PDF](https://arxiv.org/pdf/2511.11066.pdf)  
**作者**：Jiechao Gao, Chang Liu, Yuangang Li  

**一句话要点**：提出S2D-ALIGN方法，通过浅到深辅助学习解决放射学报告生成中解剖基础对齐不足的问题。

**关键词**：放射学报告生成, 多模态大语言模型, 监督微调, 解剖基础对齐, 辅助学习, 记忆适配器

## 3 点简述
- 核心问题：标准监督微调在放射学报告生成中缺乏解剖基础对齐，导致生成质量不佳。
- 方法要点：采用浅到深策略，从粗到细引入辅助信号，并使用记忆适配器整合特征。
- 实验或效果：在MIMIC-CXR和IU X-Ray基准上实现最优性能，消融研究验证多阶段方法的有效性。

## 摘要（原文）

> Radiology Report Generation (RRG) aims to automatically generate diagnostic reports from radiology images. To achieve this, existing methods have leveraged the powerful cross-modal generation capabilities of Multimodal Large Language Models (MLLMs), primarily focusing on optimizing cross-modal alignment between radiographs and reports through Supervised Fine-Tuning (SFT). However, by only performing instance-level alignment with the image-text pairs, the standard SFT paradigm fails to establish anatomically-grounded alignment, where the templated nature of reports often leads to sub-optimal generation quality. To address this, we propose \textsc{S2D-Align}, a novel SFT paradigm that establishes anatomically-grounded alignment by leveraging auxiliary signals of varying granularities. \textsc{S2D-Align} implements a shallow-to-deep strategy, progressively enriching the alignment process: it begins with the coarse radiograph-report pairing, then introduces reference reports for instance-level guidance, and ultimately utilizes key phrases to ground the generation in specific anatomical details. To bridge the different alignment stages, we introduce a memory-based adapter that empowers feature sharing, thereby integrating coarse and fine-grained guidance. For evaluation, we conduct experiments on the public \textsc{MIMIC-CXR} and \textsc{IU X-Ray} benchmarks, where \textsc{S2D-Align} achieves state-of-the-art performance compared to existing methods. Ablation studies validate the effectiveness of our multi-stage, auxiliary-guided approach, highlighting a promising direction for enhancing grounding capabilities in complex, multi-modal generation tasks.

