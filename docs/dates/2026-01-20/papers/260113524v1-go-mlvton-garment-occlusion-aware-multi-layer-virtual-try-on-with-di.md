---
layout: default
title: GO-MLVTON: Garment Occlusion-Aware Multi-Layer Virtual Try-On with Diffusion Models
---

# GO-MLVTON: Garment Occlusion-Aware Multi-Layer Virtual Try-On with Diffusion Models
**arXiv**：[2601.13524v1](https://arxiv.org/abs/2601.13524) · [PDF](https://arxiv.org/pdf/2601.13524.pdf)  
**作者**：Yang Yu, Yunze Deng, Yige Zhang, Yanjie Xiao, Youkun Ou, Wenhao Hu, Mingchao Li, Bin Feng, Wenyu Liu, Dandan Zheng, Jingdong Chen  

**一句话要点**：提出GO-MLVTON以解决多层虚拟试穿中的遮挡关系建模问题

**关键词**：多层虚拟试穿, 遮挡关系学习, 扩散模型, 衣物变形拟合, 数据集构建

## 3 点简述
- 核心问题：现有方法忽略多层虚拟试穿，难以准确处理内外衣物间的遮挡关系。
- 方法要点：引入Garment Occlusion Learning模块学习遮挡关系，基于StableDiffusion变形和拟合衣物。
- 实验或效果：提出MLG数据集和LACD评估指标，实验显示达到先进性能。

## 摘要（原文）

> Existing Image-based virtual try-on (VTON) methods primarily focus on single-layer or multi-garment VTON, neglecting multi-layer VTON (ML-VTON), which involves dressing multiple layers of garments onto the human body with realistic deformation and layering to generate visually plausible outcomes. The main challenge lies in accurately modeling occlusion relationships between inner and outer garments to reduce interference from redundant inner garment features. To address this, we propose GO-MLVTON, the first multi-layer VTON method, introducing the Garment Occlusion Learning module to learn occlusion relationships and the StableDiffusion-based Garment Morphing & Fitting module to deform and fit garments onto the human body, producing high-quality multi-layer try-on results. Additionally, we present the MLG dataset for this task and propose a new metric named Layered Appearance Coherence Difference (LACD) for evaluation. Extensive experiments demonstrate the state-of-the-art performance of GO-MLVTON. Project page: https://upyuyang.github.io/go-mlvton/.

