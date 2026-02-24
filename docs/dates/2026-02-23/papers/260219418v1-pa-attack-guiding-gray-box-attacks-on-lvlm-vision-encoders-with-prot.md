---
layout: default
title: PA-Attack: Guiding Gray-Box Attacks on LVLM Vision Encoders with Prototypes and Attention
---

# PA-Attack: Guiding Gray-Box Attacks on LVLM Vision Encoders with Prototypes and Attention
**arXiv**：[2602.19418v1](https://arxiv.org/abs/2602.19418) · [PDF](https://arxiv.org/pdf/2602.19418.pdf)  
**作者**：Hefei Mei, Zirui Wang, Chang Xu, Jianyuan Guo, Minjing Dong  

**一句话要点**：提出PA-Attack，通过原型锚定和注意力增强引导灰盒攻击LVLM视觉编码器

**关键词**：大视觉语言模型, 灰盒攻击, 原型锚定, 注意力机制, 对抗攻击, 视觉编码器

## 3 点简述
- 针对LVLM视觉编码器的灰盒攻击，解决白盒攻击任务泛化差和黑盒攻击效率低的问题
- 采用原型锚定引导攻击方向，结合两阶段注意力机制聚焦关键视觉令牌并动态调整权重
- 实验显示在多种下游任务和LVLM架构中平均得分降低率达75.1%，攻击有效且泛化性强

## 摘要（原文）

> Large Vision-Language Models (LVLMs) are foundational to modern multimodal applications, yet their susceptibility to adversarial attacks remains a critical concern. Prior white-box attacks rarely generalize across tasks, and black-box methods depend on expensive transfer, which limits efficiency. The vision encoder, standardized and often shared across LVLMs, provides a stable gray-box pivot with strong cross-model transfer. Building on this premise, we introduce PA-Attack (Prototype-Anchored Attentive Attack). PA-Attack begins with a prototype-anchored guidance that provides a stable attack direction towards a general and dissimilar prototype, tackling the attribute-restricted issue and limited task generalization of vanilla attacks. Building on this, we propose a two-stage attention enhancement mechanism: (i) leverage token-level attention scores to concentrate perturbations on critical visual tokens, and (ii) adaptively recalibrate attention weights to track the evolving attention during the adversarial process. Extensive experiments across diverse downstream tasks and LVLM architectures show that PA-Attack achieves an average 75.1% score reduction rate (SRR), demonstrating strong attack effectiveness, efficiency, and task generalization in LVLMs. Code is available at https://github.com/hefeimei06/PA-Attack.

