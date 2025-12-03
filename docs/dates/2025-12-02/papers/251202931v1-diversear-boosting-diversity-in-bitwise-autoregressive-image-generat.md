---
layout: default
title: DiverseAR: Boosting Diversity in Bitwise Autoregressive Image Generation
---

# DiverseAR: Boosting Diversity in Bitwise Autoregressive Image Generation
**arXiv**：[2512.02931v1](https://arxiv.org/abs/2512.02931) · [PDF](https://arxiv.org/pdf/2512.02931.pdf)  
**作者**：Ying Yang, Zhengyao Lv, Tianlin Pan, Haofan Wang, Binxin Yang, Hubery Yin, Chen Li, Chenyang Si  

**一句话要点**：提出DiverseAR以提升比特自回归图像生成的样本多样性

**关键词**：比特自回归模型, 样本多样性, 对数分布缩放, 生成路径搜索, 图像生成

## 3 点简述
- 核心问题：比特自回归模型因二元分类和尖锐对数分布导致样本多样性受限
- 方法要点：引入自适应对数分布缩放和基于能量的生成路径搜索以平衡多样性与质量
- 实验或效果：实验显示DiverseAR显著提升多样性且保持视觉质量

## 摘要（原文）

> In this paper, we investigate the underexplored challenge of sample diversity in autoregressive (AR) generative models with bitwise visual tokenizers. We first analyze the factors that limit diversity in bitwise AR models and identify two key issues: (1) the binary classification nature of bitwise modeling, which restricts the prediction space, and (2) the overly sharp logits distribution, which causes sampling collapse and reduces diversity. Building on these insights, we propose DiverseAR, a principled and effective method that enhances image diversity without sacrificing visual quality. Specifically, we introduce an adaptive logits distribution scaling mechanism that dynamically adjusts the sharpness of the binary output distribution during sampling, resulting in smoother predictions and greater diversity. To mitigate potential fidelity loss caused by distribution smoothing, we further develop an energy-based generation path search algorithm that avoids sampling low-confidence tokens, thereby preserving high visual quality. Extensive experiments demonstrate that DiverseAR substantially improves sample diversity in bitwise autoregressive image generation.

