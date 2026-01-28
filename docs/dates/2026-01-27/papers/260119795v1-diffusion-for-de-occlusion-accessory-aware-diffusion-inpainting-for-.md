---
layout: default
title: Diffusion for De-Occlusion: Accessory-Aware Diffusion Inpainting for Robust Ear Biometric Recognition
---

# Diffusion for De-Occlusion: Accessory-Aware Diffusion Inpainting for Robust Ear Biometric Recognition
**arXiv**：[2601.19795v1](https://arxiv.org/abs/2601.19795) · [PDF](https://arxiv.org/pdf/2601.19795.pdf)  
**作者**：Deeksha Arun, Kevin W. Bowyer, Patrick Flynn  

**一句话要点**：提出基于扩散模型的耳部修复方法，以缓解耳饰遮挡对耳部生物识别系统的影响

**关键词**：耳部生物识别, 扩散模型, 图像修复, 遮挡处理, Transformer识别

## 3 点简述
- 核心问题：耳饰（如耳环、耳机）遮挡在非约束成像条件下会降低耳部生物识别系统的性能
- 方法要点：利用扩散模型，根据输入图像和自动生成的遮挡掩码，合成缺失像素以重建解剖学合理的耳部区域
- 实验或效果：在多个基准数据集上评估，扩散修复作为预处理辅助能提升基于Transformer的耳部识别性能

## 摘要（原文）

> Ear occlusions (arising from the presence of ear accessories such as earrings and earphones) can negatively impact performance in ear-based biometric recognition systems, especially in unconstrained imaging circumstances. In this study, we assess the effectiveness of a diffusion-based ear inpainting technique as a pre-processing aid to mitigate the issues of ear accessory occlusions in transformer-based ear recognition systems. Given an input ear image and an automatically derived accessory mask, the inpainting model reconstructs clean and anatomically plausible ear regions by synthesizing missing pixels while preserving local geometric coherence along key ear structures, including the helix, antihelix, concha, and lobule. We evaluate the effectiveness of this pre-processing aid in transformer-based recognition systems for several vision transformer models and different patch sizes for a range of benchmark datasets. Experiments show that diffusion-based inpainting can be a useful pre-processing aid to alleviate ear accessory occlusions to improve overall recognition performance.

