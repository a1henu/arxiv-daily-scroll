---
layout: default
title: Learning to Communicate Across Modalities: Perceptual Heterogeneity in Multi-Agent Systems
---

# Learning to Communicate Across Modalities: Perceptual Heterogeneity in Multi-Agent Systems
**arXiv**：[2601.22041v1](https://arxiv.org/abs/2601.22041) · [PDF](https://arxiv.org/pdf/2601.22041.pdf)  
**作者**：Naomi Pitzer, Daniela Mihai  

**一句话要点**：研究异构多智能体系统中跨模态涌现通信，揭示分布编码与可互操作性

**关键词**：涌现通信, 多智能体系统, 跨模态学习, 感知异构性, 分布编码, 可互操作性

## 3 点简述
- 核心问题：真实世界智能体感知异构性被忽视，缺乏对齐表示空间
- 方法要点：设计异构多步二元通信游戏，分析模态差异下的消息收敛与编码方式
- 实验或效果：单模态系统更高效，多模态系统需更多信息交换，分布编码证据强

## 摘要（原文）

> Emergent communication offers insight into how agents develop shared structured representations, yet most research assumes homogeneous modalities or aligned representational spaces, overlooking the perceptual heterogeneity of real-world settings. We study a heterogeneous multi-step binary communication game where agents differ in modality and lack perceptual grounding. Despite perceptual misalignment, multimodal systems converge to class-consistent messages grounded in perceptual input. Unimodal systems communicate more efficiently, using fewer bits and achieving lower classification entropy, while multimodal agents require greater information exchange and exhibit higher uncertainty. Bit perturbation experiments provide strong evidence that meaning is encoded in a distributional rather than compositional manner, as each bit's contribution depends on its surrounding pattern. Finally, interoperability analyses show that systems trained in different perceptual worlds fail to directly communicate, but limited fine-tuning enables successful cross-system communication. This work positions emergent communication as a framework for studying how agents adapt and transfer representations across heterogeneous modalities, opening new directions for both theory and experimentation.

