---
layout: default
title: CoME: Empowering Channel-of-Mobile-Experts with Informative Hybrid-Capabilities Reasoning
---

# CoME: Empowering Channel-of-Mobile-Experts with Informative Hybrid-Capabilities Reasoning
**arXiv**：[2602.24142v1](https://arxiv.org/abs/2602.24142) · [PDF](https://arxiv.org/pdf/2602.24142.pdf)  
**作者**：Yuxuan Liu, Weikai Xu, Kun Huang, Changyu Chen, Jiankun Zhao, Pengzhi Gao, Wei Liu, Jian Luan, Shuo Shang, Bo Du, Ji-Rong Wen, Rui Yan  

**一句话要点**：提出CoME架构以解决移动代理在混合能力推理中解耦增强与平衡整合的挑战。

**关键词**：移动代理, 混合能力推理, 专家架构, 渐进训练, 信息增益优化

## 3 点简述
- 现有移动代理在屏幕摘要、子任务规划等混合能力推理中难以实现解耦增强与平衡整合。
- CoME采用四专家架构和输出导向激活，通过渐进训练策略提升各专家能力与协作。
- 在AITZ和AMEX数据集上，CoME优于密集移动代理和MoE方法。

## 摘要（原文）

> Mobile Agents can autonomously execute user instructions, which requires hybrid-capabilities reasoning, including screen summary, subtask planning, action decision and action function. However, existing agents struggle to achieve both decoupled enhancement and balanced integration of these capabilities. To address these challenges, we propose Channel-of-Mobile-Experts (CoME), a novel agent architecture consisting of four distinct experts, each aligned with a specific reasoning stage, CoME activates the corresponding expert to generate output tokens in each reasoning stage via output-oriented activation. To empower CoME with hybrid-capabilities reasoning, we introduce a progressive training strategy: Expert-FT enables decoupling and enhancement of different experts' capability; Router-FT aligns expert activation with the different reasoning stage; CoT-FT facilitates seamless collaboration and balanced optimization across multiple capabilities. To mitigate error propagation in hybrid-capabilities reasoning, we propose InfoGain-Driven DPO (Info-DPO), which uses information gain to evaluate the contribution of each intermediate step, thereby guiding CoME toward more informative reasoning. Comprehensive experiments show that CoME outperforms dense mobile agents and MoE methods on both AITZ and AMEX datasets.

