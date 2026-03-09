---
layout: default
title: EffectMaker: Unifying Reasoning and Generation for Customized Visual Effect Creation
---

# EffectMaker: Unifying Reasoning and Generation for Customized Visual Effect Creation
**arXiv**：[2603.06014v1](https://arxiv.org/abs/2603.06014) · [PDF](https://arxiv.org/pdf/2603.06014.pdf)  
**作者**：Shiyuan Yang, Ruihuang Li, Jiale Tao, Shuai Shao, Qinglin Lu, Jing Liao  

**一句话要点**：提出EffectMaker框架，通过统一推理与生成实现基于参考的自定义视觉特效创建。

**关键词**：视觉特效生成, 多模态推理, 扩散变换器, 上下文学习, 语义-视觉引导, 合成数据集

## 3 点简述
- 核心问题：现有AIGC系统因特效数据稀缺和建模困难，难以生成高质量视觉特效，且需逐特效微调，限制可扩展性。
- 方法要点：采用多模态大语言模型推理特效语义，结合扩散变换器通过上下文学习捕获参考视频的细粒度视觉线索，实现语义-视觉双路径引导。
- 实验或效果：构建EffectData数据集，包含130k视频和3k特效类别；实验显示EffectMaker在视觉质量和特效一致性上优于基线，无需逐特效微调。

## 摘要（原文）

> Visual effects (VFX) are essential for enhancing the expressiveness and creativity of video content, yet producing high-quality effects typically requires expert knowledge and costly production pipelines. Existing AIGC systems face significant challenges in VFX generation due to the scarcity of effect-specific data and the inherent difficulty of modeling supernatural or stylized effects. Moreover, these approaches often require per-effect fine-tuning, which severely limits their scalability and generalization to novel VFX. In this work, we present EffectMaker, a unified reasoning-generation framework that enables reference-based VFX customization. EffectMaker employs a multimodal large language model to interpret high-level effect semantics and reason about how they should adapt to a target subject, while a diffusion transformer leverages in-context learning to capture fine-grained visual cues from reference videos. These two components form a semantic-visual dual-path guidance mechanism that enables accurate, controllable, and effect-consistent synthesis without per-effect fine-tuning. Furthermore, we construct EffectData, the largest high-quality synthetic dataset containing 130k videos across 3k VFX categories, to improve generalization and scalability. Experiments show that EffectMaker achieves superior visual quality and effect consistency over state-of-the-art baselines, offering a scalable and flexible paradigm for customized VFX generation. Project page: https://effectmaker.github.io

