---
layout: default
title: MagicFuse: Single Image Fusion for Visual and Semantic Reinforcement
---

# MagicFuse: Single Image Fusion for Visual and Semantic Reinforcement
**arXiv**：[2602.01760v1](https://arxiv.org/abs/2602.01760) · [PDF](https://arxiv.org/pdf/2602.01760.pdf)  
**作者**：Hao Zhang, Yanping Zha, Zizhuo Li, Meiqi Gong, Jiayi Ma  

**一句话要点**：提出MagicFuse单图像融合框架，从单张低质量可见光图像生成跨光谱场景表示，以在恶劣条件下替代多模态输入。

**关键词**：单图像融合, 扩散模型, 跨光谱表示, 视觉语义约束, 知识级融合, 低质量图像增强

## 3 点简述
- 核心问题：在仅可用可见光传感器时，如何从单张低质量图像实现多模态融合的视觉和语义优势。
- 方法要点：基于扩散模型，设计分支挖掘可见光谱隐藏信息并生成红外光谱模式，通过融合噪声获得跨光谱表示。
- 实验或效果：实验显示，仅用单张退化可见光图像，视觉和语义性能媲美或优于多模态输入的先进融合方法。

## 摘要（原文）

> This paper focuses on a highly practical scenario: how to continue benefiting from the advantages of multi-modal image fusion under harsh conditions when only visible imaging sensors are available. To achieve this goal, we propose a novel concept of single-image fusion, which extends conventional data-level fusion to the knowledge level. Specifically, we develop MagicFuse, a novel single image fusion framework capable of deriving a comprehensive cross-spectral scene representation from a single low-quality visible image. MagicFuse first introduces an intra-spectral knowledge reinforcement branch and a cross-spectral knowledge generation branch based on the diffusion models. They mine scene information obscured in the visible spectrum and learn thermal radiation distribution patterns transferred to the infrared spectrum, respectively. Building on them, we design a multi-domain knowledge fusion branch that integrates the probabilistic noise from the diffusion streams of these two branches, from which a cross-spectral scene representation can be obtained through successive sampling. Then, we impose both visual and semantic constraints to ensure that this scene representation can satisfy human observation while supporting downstream semantic decision-making. Extensive experiments show that our MagicFuse achieves visual and semantic representation performance comparable to or even better than state-of-the-art fusion methods with multi-modal inputs, despite relying solely on a single degraded visible image.

