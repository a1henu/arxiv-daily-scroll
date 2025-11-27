---
layout: default
title: Mechanisms of Non-Monotonic Scaling in Vision Transformers
---

# Mechanisms of Non-Monotonic Scaling in Vision Transformers
**arXiv**：[2511.21635v1](https://arxiv.org/abs/2511.21635) · [PDF](https://arxiv.org/pdf/2511.21635.pdf)  
**作者**：Anantha Padmanaban Krishna Kumar  

**一句话要点**：提出信息扰乱指数以解释ViT深度非单调缩放机制，优化架构设计。

**关键词**：视觉Transformer, 深度缩放, 信息扰乱指数, 表示演化, 架构优化

## 3 点简述
- 核心问题：深层ViT性能下降，挑战传统缩放假设。
- 方法要点：分析表示演化模式，量化信息混合与[CLS]令牌边缘化。
- 实验或效果：在ImageNet上验证Cliff-Plateau-Climb模式，指导深度校准。

## 摘要（原文）

> Deeper Vision Transformers often perform worse than shallower ones, which challenges common scaling assumptions. Through a systematic empirical analysis of ViT-S, ViT-B, and ViT-L on ImageNet, we identify a consistent three-phase Cliff-Plateau-Climb pattern that governs how representations evolve with depth. We observe that better performance is associated with progressive marginalization of the [CLS] token, originally designed as a global aggregation hub, in favor of distributed consensus among patch tokens. We quantify patterns of information mixing with an Information Scrambling Index, and show that in ViT-L the information-task tradeoff emerges roughly 10 layers later than in ViT-B, and that these additional layers correlate with increased information diffusion rather than improved task performance. Taken together, these results suggest that transformer architectures in this regime may benefit more from carefully calibrated depth that executes clean phase transitions than from simply increasing parameter count. The Information Scrambling Index provides a useful diagnostic for existing models and suggests a potential design target for future architectures. All code is available at: https://github.com/AnanthaPadmanaban-KrishnaKumar/Cliff-Plateau-Climb.

