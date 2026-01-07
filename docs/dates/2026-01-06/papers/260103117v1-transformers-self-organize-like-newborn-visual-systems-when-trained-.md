---
layout: default
title: Transformers self-organize like newborn visual systems when trained in prenatal worlds
---

# Transformers self-organize like newborn visual systems when trained in prenatal worlds
**arXiv**：[2601.03117v1](https://arxiv.org/abs/2601.03117) · [PDF](https://arxiv.org/pdf/2601.03117.pdf)  
**作者**：Lalit Pandey, Samantha M. W. Wood, Justin N. Wood  

**一句话要点**：提出使用视网膜波训练Transformer，使其自发形成与新生儿视觉系统相似的结构。

**关键词**：Transformer学习, 视网膜波, 自监督学习, 视觉系统发育, 生物启发模型

## 3 点简述
- 核心问题：Transformer是否像大脑一样学习，关键在于训练数据的生物合理性差异。
- 方法要点：通过视网膜波生成器模拟产前视觉输入，采用自监督时间学习训练Transformer。
- 实验或效果：训练后Transformer早期层对边缘敏感，后期层对形状敏感，感受野逐层增大，与新生儿视觉系统一致。

## 摘要（原文）

> Do transformers learn like brains? A key challenge in addressing this question is that transformers and brains are trained on fundamentally different data. Brains are initially "trained" on prenatal sensory experiences (e.g., retinal waves), whereas transformers are typically trained on large datasets that are not biologically plausible. We reasoned that if transformers learn like brains, then they should develop the same structure as newborn brains when exposed to the same prenatal data. To test this prediction, we simulated prenatal visual input using a retinal wave generator. Then, using self-supervised temporal learning, we trained transformers to adapt to those retinal waves. During training, the transformers spontaneously developed the same structure as newborn visual systems: (1) early layers became sensitive to edges, (2) later layers became sensitive to shapes, and (3) the models developed larger receptive fields across layers. The organization of newborn visual systems emerges spontaneously when transformers adapt to a prenatal visual world. This developmental convergence suggests that brains and transformers learn in common ways and follow the same general fitting principles.

