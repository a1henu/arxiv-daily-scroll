---
layout: default
title: CSF-Net: Context-Semantic Fusion Network for Large Mask Inpainting
---

# CSF-Net: Context-Semantic Fusion Network for Large Mask Inpainting
**arXiv**：[2511.07987v1](https://arxiv.org/abs/2511.07987) · [PDF](https://arxiv.org/pdf/2511.07987.pdf)  
**作者**：Chae-Yeon Heo, Yeong-Jun Cho  

**一句话要点**：提出CSF-Net以解决大掩码图像修复中语义一致性问题

**关键词**：图像修复, 语义引导, transformer融合, 大掩码处理, 结构一致性

## 3 点简述
- 核心问题：大掩码图像修复中视觉内容缺失和上下文线索有限。
- 方法要点：利用预训练AC模型生成语义先验，通过transformer融合上下文特征。
- 实验或效果：在Places365和COCOA数据集上减少物体幻觉，提升视觉真实感。

## 摘要（原文）

> In this paper, we propose a semantic-guided framework to address the challenging problem of large-mask image inpainting, where essential visual content is missing and contextual cues are limited. To compensate for the limited context, we leverage a pretrained Amodal Completion (AC) model to generate structure-aware candidates that serve as semantic priors for the missing regions. We introduce Context-Semantic Fusion Network (CSF-Net), a transformer-based fusion framework that fuses these candidates with contextual features to produce a semantic guidance image for image inpainting. This guidance improves inpainting quality by promoting structural accuracy and semantic consistency. CSF-Net can be seamlessly integrated into existing inpainting models without architectural changes and consistently enhances performance across diverse masking conditions. Extensive experiments on the Places365 and COCOA datasets demonstrate that CSF-Net effectively reduces object hallucination while enhancing visual realism and semantic alignment. The code for CSF-Net is available at https://github.com/chaeyeonheo/CSF-Net.

