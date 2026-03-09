---
layout: default
title: DEX-AR: A Dynamic Explainability Method for Autoregressive Vision-Language Models
---

# DEX-AR: A Dynamic Explainability Method for Autoregressive Vision-Language Models
**arXiv**：[2603.06302v1](https://arxiv.org/abs/2603.06302) · [PDF](https://arxiv.org/pdf/2603.06302.pdf)  
**作者**：Walid Bousselham, Angie Boggust, Hendrik Strobelt, Hilde Kuehne  

**一句话要点**：提出DEX-AR方法以解决自回归视觉语言模型的可解释性挑战

**关键词**：自回归视觉语言模型, 可解释性方法, 梯度计算, 热图生成, 多模态交互, 评估指标

## 3 点简述
- 核心问题：传统可解释性方法难以处理自回归VLMs的逐令牌生成和多模态交互复杂性。
- 方法要点：通过计算逐层梯度生成每令牌和序列级热图，并引入动态头过滤和序列级过滤机制。
- 实验或效果：在ImageNet等数据集上评估，基于扰动和分割的指标均显示一致改进。

## 摘要（原文）

> As Vision-Language Models (VLMs) become increasingly sophisticated and widely used, it becomes more and more crucial to understand their decision-making process. Traditional explainability methods, designed for classification tasks, struggle with modern autoregressive VLMs due to their complex token-by-token generation process and intricate interactions between visual and textual modalities. We present DEX-AR (Dynamic Explainability for AutoRegressive models), a novel explainability method designed to address these challenges by generating both per-token and sequence-level 2D heatmaps highlighting image regions crucial for the model's textual responses. The proposed method offers to interpret autoregressive VLMs-including varying importance of layers and generated tokens-by computing layer-wise gradients with respect to attention maps during the token-by-token generation process. DEX-AR introduces two key innovations: a dynamic head filtering mechanism that identifies attention heads focused on visual information, and a sequence-level filtering approach that aggregates per-token explanations while distinguishing between visually-grounded and purely linguistic tokens. Our evaluation on ImageNet, VQAv2, and PascalVOC, shows a consistent improvement in both perturbation-based metrics, using a novel normalized perplexity measure, as well as segmentation-based metrics.

