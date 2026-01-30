---
layout: default
title: Learning to Communicate Across Modalities: Perceptual Heterogeneity in Multi-Agent Systems
---

# Learning to Communicate Across Modalities: Perceptual Heterogeneity in Multi-Agent Systems
**arXiv**：[2601.22041v1](https://arxiv.org/abs/2601.22041) · [PDF](https://arxiv.org/pdf/2601.22041.pdf)  
**作者**：Naomi Pitzer, Daniela Mihai  

**一句话要点**：研究多智能体系统中跨模态通信，揭示感知异构下涌现通信的分布编码与可迁移性

**关键词**：涌现通信, 多智能体系统, 感知异构, 跨模态学习, 分布编码, 表示迁移

## 3 点简述
- 核心问题：现有研究忽略真实世界感知异构性，假设模态同质或表示空间对齐，导致通信效率受限
- 方法要点：设计异构多步二元通信游戏，分析单模态与多模态系统在感知未对齐下的通信行为与表示形成
- 实验或效果：单模态系统通信更高效，多模态系统需更多信息交换；比特扰动实验支持分布编码，微调实现跨系统通信

## 摘要（原文）

> Emergent communication offers insight into how agents develop shared structured representations, yet most research assumes homogeneous modalities or aligned representational spaces, overlooking the perceptual heterogeneity of real-world settings. We study a heterogeneous multi-step binary communication game where agents differ in modality and lack perceptual grounding. Despite perceptual misalignment, multimodal systems converge to class-consistent messages grounded in perceptual input. Unimodal systems communicate more efficiently, using fewer bits and achieving lower classification entropy, while multimodal agents require greater information exchange and exhibit higher uncertainty. Bit perturbation experiments provide strong evidence that meaning is encoded in a distributional rather than compositional manner, as each bit's contribution depends on its surrounding pattern. Finally, interoperability analyses show that systems trained in different perceptual worlds fail to directly communicate, but limited fine-tuning enables successful cross-system communication. This work positions emergent communication as a framework for studying how agents adapt and transfer representations across heterogeneous modalities, opening new directions for both theory and experimentation.

