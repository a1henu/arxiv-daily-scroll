---
layout: default
title: EasyV2V: A High-quality Instruction-based Video Editing Framework
---

# EasyV2V: A High-quality Instruction-based Video Editing Framework
**arXiv**：[2512.16920v1](https://arxiv.org/abs/2512.16920) · [PDF](https://arxiv.org/pdf/2512.16920.pdf)  
**作者**：Jinjie Mai, Chaoyang Wang, Guocheng Gordon Qian, Willi Menapace, Sergey Tulyakov, Bernard Ghanem, Peter Wonka, Ashkan Mirzaei  

**一句话要点**：提出EasyV2V框架以解决基于指令的视频编辑在一致性、控制和泛化方面的挑战。

**关键词**：视频编辑, 指令驱动, 数据增强, 轻量微调, 时空控制, 参考图像

## 3 点简述
- 核心问题：视频编辑面临一致性、控制和泛化不足的挑战，相比图像编辑进展缓慢。
- 方法要点：通过数据构建、简化架构和统一控制机制，实现高质量指令视频编辑。
- 实验或效果：在灵活输入下达到先进水平，超越同期和商业系统。

## 摘要（原文）

> While image editing has advanced rapidly, video editing remains less explored, facing challenges in consistency, control, and generalization. We study the design space of data, architecture, and control, and introduce \emph{EasyV2V}, a simple and effective framework for instruction-based video editing. On the data side, we compose existing experts with fast inverses to build diverse video pairs, lift image edit pairs into videos via single-frame supervision and pseudo pairs with shared affine motion, mine dense-captioned clips for video pairs, and add transition supervision to teach how edits unfold. On the model side, we observe that pretrained text-to-video models possess editing capability, motivating a simplified design. Simple sequence concatenation for conditioning with light LoRA fine-tuning suffices to train a strong model. For control, we unify spatiotemporal control via a single mask mechanism and support optional reference images. Overall, EasyV2V works with flexible inputs, e.g., video+text, video+mask+text, video+mask+reference+text, and achieves state-of-the-art video editing results, surpassing concurrent and commercial systems. Project page: https://snap-research.github.io/easyv2v/

