---
layout: default
title: From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing
---

# From Inpainting to Editing: A Self-Bootstrapping Framework for Context-Rich Visual Dubbing
**arXiv**：[2512.25066v1](https://arxiv.org/abs/2512.25066) · [PDF](https://arxiv.org/pdf/2512.25066.pdf)  
**作者**：Xu He, Haoxian Zhang, Hejia Chen, Changyuan Zheng, Liyang Chen, Songlin Tang, Jiehui Huang, Xiaoqiang Liu, Pengfei Wan, Zhiyong Wu  

**一句话要点**：提出自引导框架，将视觉配音从修复任务重构为编辑问题，以提升唇部同步和身份保持。

**关键词**：视觉配音, 扩散变换器, 视频编辑, 唇部同步, 自引导框架, 基准数据集

## 3 点简述
- 核心问题：现有基于掩码修复的方法因视觉条件不完整，导致唇部同步差、视觉伪影和身份漂移。
- 方法要点：使用扩散变换器生成理想训练数据，形成视觉对齐的视频对，训练音频驱动编辑器进行精确唇部修改。
- 实验或效果：引入时间步自适应多阶段学习策略和ContextDubBench基准，在野外场景中实现高精度唇部同步和鲁棒性。

## 摘要（原文）

> Audio-driven visual dubbing aims to synchronize a video's lip movements with new speech, but is fundamentally challenged by the lack of ideal training data: paired videos where only a subject's lip movements differ while all other visual conditions are identical. Existing methods circumvent this with a mask-based inpainting paradigm, where an incomplete visual conditioning forces models to simultaneously hallucinate missing content and sync lips, leading to visual artifacts, identity drift, and poor synchronization. In this work, we propose a novel self-bootstrapping framework that reframes visual dubbing from an ill-posed inpainting task into a well-conditioned video-to-video editing problem. Our approach employs a Diffusion Transformer, first as a data generator, to synthesize ideal training data: a lip-altered companion video for each real sample, forming visually aligned video pairs. A DiT-based audio-driven editor is then trained on these pairs end-to-end, leveraging the complete and aligned input video frames to focus solely on precise, audio-driven lip modifications. This complete, frame-aligned input conditioning forms a rich visual context for the editor, providing it with complete identity cues, scene interactions, and continuous spatiotemporal dynamics. Leveraging this rich context fundamentally enables our method to achieve highly accurate lip sync, faithful identity preservation, and exceptional robustness against challenging in-the-wild scenarios. We further introduce a timestep-adaptive multi-phase learning strategy as a necessary component to disentangle conflicting editing objectives across diffusion timesteps, thereby facilitating stable training and yielding enhanced lip synchronization and visual fidelity. Additionally, we propose ContextDubBench, a comprehensive benchmark dataset for robust evaluation in diverse and challenging practical application scenarios.

