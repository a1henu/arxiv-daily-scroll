---
layout: default
title: CHIMERA: Adaptive Cache Injection and Semantic Anchor Prompting for Zero-shot Image Morphing with Morphing-oriented Metrics
---

# CHIMERA: Adaptive Cache Injection and Semantic Anchor Prompting for Zero-shot Image Morphing with Morphing-oriented Metrics
**arXiv**：[2512.07155v1](https://arxiv.org/abs/2512.07155) · [PDF](https://arxiv.org/pdf/2512.07155.pdf)  
**作者**：Dahyeon Kye, Jeahun Sung, MinKyu Jeon, Jihyong Oh  

**一句话要点**：提出CHIMERA框架以解决扩散模型图像变形中的过渡不自然问题

**关键词**：图像变形, 扩散模型, 零样本学习, 语义对齐, 自适应缓存, 视觉语言模型

## 3 点简述
- 核心问题：现有方法在图像变形中常产生突兀过渡或过饱和外观，缺乏自适应结构和语义对齐。
- 方法要点：采用自适应缓存注入和语义锚点提示，通过缓存反转特征和共享提示实现平滑变形。
- 实验或效果：引入全局-局部一致性评分，实验显示CHIMERA在变形平滑度和语义对齐上优于现有方法。

## 摘要（原文）

> Diffusion models exhibit remarkable generative ability, yet achieving smooth and semantically consistent image morphing remains a challenge. Existing approaches often yield abrupt transitions or over-saturated appearances due to the lack of adaptive structural and semantic alignments. We propose CHIMERA, a zero-shot diffusion-based framework that formulates morphing as a cached inversion-guided denoising process. To handle large semantic and appearance disparities, we propose Adaptive Cache Injection and Semantic Anchor Prompting. Adaptive Cache Injection (ACI) caches down, mid, and up blocks features from both inputs during DDIM inversion and re-injects them adaptively during denoising, enabling spatial and semantic alignment in depth- and time-adaptive manners and enabling natural feature fusion and smooth transitions. Semantic Anchor Prompting (SAP) leverages a vision-language model to generate a shared anchor prompt that serves as a semantic anchor, bridging dissimilar inputs and guiding the denoising process toward coherent results. Finally, we introduce the Global-Local Consistency Score (GLCS), a morphing-oriented metric that simultaneously evaluates the global harmonization of the two inputs and the smoothness of the local morphing transition. Extensive experiments and user studies show that CHIMERA achieves smoother and more semantically aligned transitions than existing methods, establishing a new state of the art in image morphing. The code and project page will be publicly released.

