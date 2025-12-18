---
layout: default
title: IC-Effect: Precise and Efficient Video Effects Editing via In-Context Learning
---

# IC-Effect: Precise and Efficient Video Effects Editing via In-Context Learning
**arXiv**：[2512.15635v1](https://arxiv.org/abs/2512.15635) · [PDF](https://arxiv.org/pdf/2512.15635.pdf)  
**作者**：Yuanhang Li, Yiren Song, Junzhe Bai, Xinran Liang, Hu Yang, Libiao Jin, Qi Mao  

**一句话要点**：提出IC-Effect框架，通过上下文学习实现精确高效的视频特效编辑。

**关键词**：视频特效编辑, 上下文学习, DiT模型, 稀疏标记化, 两阶段训练, 时间一致性

## 3 点简述
- 核心问题：视频特效编辑需无缝融合特效、保持背景不变，现有模型难以满足。
- 方法要点：基于DiT模型，利用源视频作为上下文条件，结合两阶段训练和稀疏标记化提升效果与效率。
- 实验或效果：在15种视觉风格数据集上验证，实现高质量、可控且时间一致的特效编辑。

## 摘要（原文）

> We propose \textbf{IC-Effect}, an instruction-guided, DiT-based framework for few-shot video VFX editing that synthesizes complex effects (\eg flames, particles and cartoon characters) while strictly preserving spatial and temporal consistency. Video VFX editing is highly challenging because injected effects must blend seamlessly with the background, the background must remain entirely unchanged, and effect patterns must be learned efficiently from limited paired data. However, existing video editing models fail to satisfy these requirements. IC-Effect leverages the source video as clean contextual conditions, exploiting the contextual learning capability of DiT models to achieve precise background preservation and natural effect injection. A two-stage training strategy, consisting of general editing adaptation followed by effect-specific learning via Effect-LoRA, ensures strong instruction following and robust effect modeling. To further improve efficiency, we introduce spatiotemporal sparse tokenization, enabling high fidelity with substantially reduced computation. We also release a paired VFX editing dataset spanning $15$ high-quality visual styles. Extensive experiments show that IC-Effect delivers high-quality, controllable, and temporally consistent VFX editing, opening new possibilities for video creation.

