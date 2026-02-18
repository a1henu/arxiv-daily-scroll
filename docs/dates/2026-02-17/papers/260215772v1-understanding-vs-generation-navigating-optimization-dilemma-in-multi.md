---
layout: default
title: Understanding vs. Generation: Navigating Optimization Dilemma in Multimodal Models
---

# Understanding vs. Generation: Navigating Optimization Dilemma in Multimodal Models
**arXiv**：[2602.15772v1](https://arxiv.org/abs/2602.15772) · [PDF](https://arxiv.org/pdf/2602.15772.pdf)  
**作者**：Sen Ye, Mengde Xu, Shuyang Gu, Di He, Liwei Wang, Han Hu  

**一句话要点**：提出Reason-Reflect-Refine框架以解决多模态模型中生成与理解的优化困境

**关键词**：多模态模型, 优化困境, 生成与理解权衡, Reason-Reflect-Refine框架, 多步生成

## 3 点简述
- 核心问题：多模态模型中生成与理解能力存在权衡，增强一方可能削弱另一方
- 方法要点：将单步生成重构为“生成-理解-再生成”的多步过程，利用理解能力优化生成
- 实验或效果：缓解优化困境，提升生成结果和与生成过程相关的理解能力

## 摘要（原文）

> Current research in multimodal models faces a key challenge where enhancing generative capabilities often comes at the expense of understanding, and vice versa. We analyzed this trade-off and identify the primary cause might be the potential conflict between generation and understanding, which creates a competitive dynamic within the model. To address this, we propose the Reason-Reflect-Refine (R3) framework. This innovative algorithm re-frames the single-step generation task into a multi-step process of "generate-understand-regenerate". By explicitly leveraging the model's understanding capability during generation, we successfully mitigate the optimization dilemma, achieved stronger generation results and improved understanding ability which are related to the generation process. This offers valuable insights for designing next-generation unified multimodal models. Code is available at https://github.com/sen-ye/R3.

