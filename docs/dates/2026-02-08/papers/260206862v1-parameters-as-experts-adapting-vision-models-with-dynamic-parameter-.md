---
layout: default
title: Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing
---

# Parameters as Experts: Adapting Vision Models with Dynamic Parameter Routing
**arXiv**：[2602.06862v1](https://arxiv.org/abs/2602.06862) · [PDF](https://arxiv.org/pdf/2602.06862.pdf)  
**作者**：Meng Lou, Stanley Yu, Yizhou Yu  

**一句话要点**：提出AdaRoute，通过动态参数路由实现视觉模型参数高效微调，提升密集预测任务性能。

**关键词**：参数高效微调, 动态参数路由, 混合专家, 密集预测, 视觉模型适应

## 3 点简述
- 核心问题：现有参数高效微调方法在密集预测任务中存在输入无关建模和跨层表示冗余的局限性。
- 方法要点：采用混合专家架构，通过动态参数路由机制为每个模块生成输入依赖的低秩适应权重矩阵。
- 实验或效果：在语义分割、目标检测和全景分割等任务上验证了AdaRoute的优越性。

## 摘要（原文）

> Adapting pre-trained vision models using parameter-efficient fine-tuning (PEFT) remains challenging, as it aims to achieve performance comparable to full fine-tuning using a minimal number of trainable parameters. When applied to complex dense prediction tasks, existing methods exhibit limitations, including input-agnostic modeling and redundant cross-layer representations. To this end, we propose AdaRoute, a new adapter-style method featuring a simple mixture-of-experts (MoE) architecture. Specifically, we introduce shared expert centers, where each expert is a trainable parameter matrix. During a feedforward pass, each AdaRoute module in the network dynamically generates weight matrices tailored for the current module via a simple dynamic parameter routing mechanism, which selectively aggregates parameter matrices in the corresponding expert center. Dynamic weight matrices in AdaRoute modules facilitate low-rank adaptation in an input-dependent manner, thus generating more customized and powerful feature representations. Moreover, since AdaRoute modules across multiple network layers share the same expert center, they improve feature diversity by promoting implicit cross-layer feature interaction. Extensive experiments demonstrate the superiority of AdaRoute on diverse vision tasks, including semantic segmentation, object detection and instance segmentation, and panoptic segmentation. Code will be available at: https://bit.ly/3NZcr0H.

