---
layout: default
title: Lookahead Anchoring: Preserving Character Identity in Audio-Driven Human Animation
---

# Lookahead Anchoring: Preserving Character Identity in Audio-Driven Human Animation
**arXiv**：[2510.23581v1](https://arxiv.org/abs/2510.23581) · [PDF](https://arxiv.org/pdf/2510.23581.pdf)  
**作者**：Junyoung Seo, Rodrigo Mira, Alexandros Haliassos, Stella Bounareli, Honglie Chen, Linh Tran, Seungryong Kim, Zoe Landgraf, Jie Shen  

**一句话要点**：提出前瞻锚定方法以解决音频驱动人体动画中的身份漂移问题

**关键词**：音频驱动动画, 身份保持, 时序建模, 关键帧引导, 自回归生成

## 3 点简述
- 核心问题：时序自回归生成中角色身份随时间逐渐漂移
- 方法要点：利用未来时间步的关键帧作为方向性引导，无需额外关键帧生成
- 实验或效果：在多个模型上提升唇同步、身份保持和视觉质量

## 摘要（原文）

> Audio-driven human animation models often suffer from identity drift during
> temporal autoregressive generation, where characters gradually lose their
> identity over time. One solution is to generate keyframes as intermediate
> temporal anchors that prevent degradation, but this requires an additional
> keyframe generation stage and can restrict natural motion dynamics. To address
> this, we propose Lookahead Anchoring, which leverages keyframes from future
> timesteps ahead of the current generation window, rather than within it. This
> transforms keyframes from fixed boundaries into directional beacons: the model
> continuously pursues these future anchors while responding to immediate audio
> cues, maintaining consistent identity through persistent guidance. This also
> enables self-keyframing, where the reference image serves as the lookahead
> target, eliminating the need for keyframe generation entirely. We find that the
> temporal lookahead distance naturally controls the balance between expressivity
> and consistency: larger distances allow for greater motion freedom, while
> smaller ones strengthen identity adherence. When applied to three recent human
> animation models, Lookahead Anchoring achieves superior lip synchronization,
> identity preservation, and visual quality, demonstrating improved temporal
> conditioning across several different architectures. Video results are
> available at the following link: https://lookahead-anchoring.github.io.

