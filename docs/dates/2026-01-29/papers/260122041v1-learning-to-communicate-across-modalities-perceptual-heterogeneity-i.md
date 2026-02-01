---
layout: default
title: Learning to Communicate Across Modalities: Perceptual Heterogeneity in Multi-Agent Systems
---

# Learning to Communicate Across Modalities: Perceptual Heterogeneity in Multi-Agent Systems
**arXiv**：[2601.22041v1](https://arxiv.org/abs/2601.22041) · [PDF](https://arxiv.org/pdf/2601.22041.pdf)  
**作者**：Naomi Pitzer, Daniela Mihai  

**一句话要点**：研究多智能体系统中跨模态通信，揭示感知异构下的表征学习与通信效率差异

**关键词**：涌现通信, 多智能体系统, 感知异构, 跨模态学习, 表征对齐, 通信效率

## 3 点简述
- 核心问题：现有研究忽视真实世界感知异构性，假设模态同质或表征对齐，导致通信机制不切实际
- 方法要点：设计异构多步二元通信游戏，分析多模态与单模态系统在感知未对齐下的通信行为与表征形成
- 实验或效果：多模态系统收敛于基于感知输入的类一致消息，但通信效率低于单模态系统；比特扰动实验表明意义以分布方式编码

## 摘要（原文）

> Emergent communication offers insight into how agents develop shared structured representations, yet most research assumes homogeneous modalities or aligned representational spaces, overlooking the perceptual heterogeneity of real-world settings. We study a heterogeneous multi-step binary communication game where agents differ in modality and lack perceptual grounding. Despite perceptual misalignment, multimodal systems converge to class-consistent messages grounded in perceptual input. Unimodal systems communicate more efficiently, using fewer bits and achieving lower classification entropy, while multimodal agents require greater information exchange and exhibit higher uncertainty. Bit perturbation experiments provide strong evidence that meaning is encoded in a distributional rather than compositional manner, as each bit's contribution depends on its surrounding pattern. Finally, interoperability analyses show that systems trained in different perceptual worlds fail to directly communicate, but limited fine-tuning enables successful cross-system communication. This work positions emergent communication as a framework for studying how agents adapt and transfer representations across heterogeneous modalities, opening new directions for both theory and experimentation.

