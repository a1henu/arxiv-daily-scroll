---
layout: default
title: Vision Transformer Finetuning Benefits from Non-Smooth Components
---

# Vision Transformer Finetuning Benefits from Non-Smooth Components
**arXiv**：[2602.06883v1](https://arxiv.org/abs/2602.06883) · [PDF](https://arxiv.org/pdf/2602.06883.pdf)  
**作者**：Ambroise Odonnat, Laetitia Chapel, Romain Tavenard, Ievgen Redko  

**一句话要点**：分析视觉Transformer组件塑性以指导微调，发现高塑性模块提升性能

**关键词**：视觉Transformer, 微调策略, 组件塑性, 迁移学习, 注意力机制, 前馈网络

## 3 点简述
- 研究视觉Transformer在迁移学习中组件塑性（输出对输入变化的适应能力）的作用，挑战平滑性假设
- 通过理论分析和实验证明，注意力模块和前馈层的高塑性（低平滑性）有利于微调性能
- 提供基于塑性的组件选择原则，代码开源，为实践者提供新视角

## 摘要（原文）

> The smoothness of the transformer architecture has been extensively studied in the context of generalization, training stability, and adversarial robustness. However, its role in transfer learning remains poorly understood. In this paper, we analyze the ability of vision transformer components to adapt their outputs to changes in inputs, or, in other words, their plasticity. Defined as an average rate of change, it captures the sensitivity to input perturbation; in particular, a high plasticity implies low smoothness. We demonstrate through theoretical analysis and comprehensive experiments that this perspective provides principled guidance in choosing the components to prioritize during adaptation. A key takeaway for practitioners is that the high plasticity of the attention modules and feedforward layers consistently leads to better finetuning performance. Our findings depart from the prevailing assumption that smoothness is desirable, offering a novel perspective on the functional properties of transformers. The code is available at https://github.com/ambroiseodt/vit-plasticity.

