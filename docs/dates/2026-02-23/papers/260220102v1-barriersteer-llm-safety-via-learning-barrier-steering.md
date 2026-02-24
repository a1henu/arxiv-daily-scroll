---
layout: default
title: BarrierSteer: LLM Safety via Learning Barrier Steering
---

# BarrierSteer: LLM Safety via Learning Barrier Steering
**arXiv**：[2602.20102v1](https://arxiv.org/abs/2602.20102) · [PDF](https://arxiv.org/pdf/2602.20102.pdf)  
**作者**：Thanh Q. Tran, Arun Verma, Kiwan Wong, Bryan Kian Hsiang Low, Daniela Rus, Wei Xiao  

**一句话要点**：提出BarrierSteer框架，通过控制屏障函数在潜在空间嵌入安全约束，以解决LLM对抗攻击和不安全内容生成问题。

**关键词**：大语言模型安全, 控制屏障函数, 潜在空间约束, 对抗攻击防御, 安全机制

## 3 点简述
- 核心问题：LLM易受对抗攻击，生成不安全内容，阻碍高风险部署。
- 方法要点：基于控制屏障函数，在潜在空间嵌入非线性安全约束，无需修改模型参数。
- 实验或效果：实验显示显著降低对抗成功率，减少不安全生成，优于现有方法。

## 摘要（原文）

> Despite the state-of-the-art performance of large language models (LLMs) across diverse tasks, their susceptibility to adversarial attacks and unsafe content generation remains a major obstacle to deployment, particularly in high-stakes settings. Addressing this challenge requires safety mechanisms that are both practically effective and supported by rigorous theory. We introduce BarrierSteer, a novel framework that formalizes response safety by embedding learned non-linear safety constraints directly into the model's latent representation space. BarrierSteer employs a steering mechanism based on Control Barrier Functions (CBFs) to efficiently detect and prevent unsafe response trajectories during inference with high precision. By enforcing multiple safety constraints through efficient constraint merging, without modifying the underlying LLM parameters, BarrierSteer preserves the model's original capabilities and performance. We provide theoretical results establishing that applying CBFs in latent space offers a principled and computationally efficient approach to enforcing safety. Our experiments across multiple models and datasets show that BarrierSteer substantially reduces adversarial success rates, decreases unsafe generations, and outperforms existing methods.

