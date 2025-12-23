---
layout: default
title: ActAvatar: Temporally-Aware Precise Action Control for Talking Avatars
---

# ActAvatar: Temporally-Aware Precise Action Control for Talking Avatars
**arXiv**：[2512.19546v1](https://arxiv.org/abs/2512.19546) · [PDF](https://arxiv.org/pdf/2512.19546.pdf)  
**作者**：Ziqiao Peng, Yi Chen, Yifeng Ma, Guozhen Zhang, Zhiyao Sun, Zixiang Zhou, Youliang Zhang, Zhengguang Zhou, Zhaoxin Fan, Hongyan Liu, Yuan Zhou, Qinglin Lu, Jun He  

**一句话要点**：提出ActAvatar框架，通过文本引导实现说话头像的精确动作控制，解决动作与音频时序对齐问题。

**关键词**：说话头像生成, 动作控制, 时序对齐, 文本引导, 视听模态, 两阶段训练

## 3 点简述
- 现有方法在文本跟随能力、动作与音频时序对齐方面不足，依赖额外控制信号。
- 引入Phase-Aware Cross-Attention和渐进式视听对齐，实现相位级动作控制和模态防干扰。
- 实验显示在动作控制和视觉质量上显著优于先进方法，保持视听对齐和文本跟随能力。

## 摘要（原文）

> Despite significant advances in talking avatar generation, existing methods face critical challenges: insufficient text-following capability for diverse actions, lack of temporal alignment between actions and audio content, and dependency on additional control signals such as pose skeletons. We present ActAvatar, a framework that achieves phase-level precision in action control through textual guidance by capturing both action semantics and temporal context. Our approach introduces three core innovations: (1) Phase-Aware Cross-Attention (PACA), which decomposes prompts into a global base block and temporally-anchored phase blocks, enabling the model to concentrate on phase-relevant tokens for precise temporal-semantic alignment; (2) Progressive Audio-Visual Alignment, which aligns modality influence with the hierarchical feature learning process-early layers prioritize text for establishing action structure while deeper layers emphasize audio for refining lip movements, preventing modality interference; (3) A two-stage training strategy that first establishes robust audio-visual correspondence on diverse data, then injects action control through fine-tuning on structured annotations, maintaining both audio-visual alignment and the model's text-following capabilities. Extensive experiments demonstrate that ActAvatar significantly outperforms state-of-the-art methods in both action control and visual quality.

