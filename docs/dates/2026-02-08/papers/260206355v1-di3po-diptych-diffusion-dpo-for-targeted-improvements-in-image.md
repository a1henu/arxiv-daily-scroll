---
layout: default
title: Di3PO -- Diptych Diffusion DPO for Targeted Improvements in Image
---

# Di3PO -- Diptych Diffusion DPO for Targeted Improvements in Image
**arXiv**：[2602.06355v1](https://arxiv.org/abs/2602.06355) · [PDF](https://arxiv.org/pdf/2602.06355.pdf)  
**作者**：Sanjana Reddy, Ishaan Malhi, Sally Ma, Praneet Dutta  

**一句话要点**：提出Di3PO方法，通过构建区域隔离的正负图像对，提升文本到图像扩散模型的偏好调优效率。

**关键词**：文本到图像扩散模型, 偏好调优, 图像对构建, 文本渲染, 训练效率

## 3 点简述
- 现有方法依赖昂贵生成步骤，导致训练对差异小或像素方差大，降低效率。
- Di3PO构建正负对时隔离目标改进区域，保持图像上下文稳定，以优化偏好调优。
- 应用于文本渲染任务，实验显示优于SFT和DPO基线方法，验证了其有效性。

## 摘要（原文）

> Existing methods for preference tuning of text-to-image (T2I) diffusion models often rely on computationally expensive generation steps to create positive and negative pairs of images. These approaches frequently yield training pairs that either lack meaningful differences, are expensive to sample and filter, or exhibit significant variance in irrelevant pixel regions, thereby degrading training efficiency. To address these limitations, we introduce "Di3PO", a novel method for constructing positive and negative pairs that isolates specific regions targeted for improvement during preference tuning, while keeping the surrounding context in the image stable. We demonstrate the efficacy of our approach by applying it to the challenging task of text rendering in diffusion models, showcasing improvements over baseline methods of SFT and DPO.

