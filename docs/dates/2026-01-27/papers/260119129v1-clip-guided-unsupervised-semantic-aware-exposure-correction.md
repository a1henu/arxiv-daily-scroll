---
layout: default
title: CLIP-Guided Unsupervised Semantic-Aware Exposure Correction
---

# CLIP-Guided Unsupervised Semantic-Aware Exposure Correction
**arXiv**：[2601.19129v1](https://arxiv.org/abs/2601.19129) · [PDF](https://arxiv.org/pdf/2601.19129.pdf)  
**作者**：Puzhen Wu, Han Weng, Quan Zheng, Yi Zhan, Hewei Wang, Yiming Li, Jiahui Han, Rui Xu  

**一句话要点**：提出基于CLIP引导的无监督语义感知曝光校正网络，以解决真实世界曝光图像校正中的语义忽略和标签缺失问题。

**关键词**：曝光校正, 无监督学习, 语义感知, CLIP引导, FastSAM, 伪标签生成

## 3 点简述
- 核心问题：曝光不当导致细节丢失和颜色失真，且真实图像缺乏标注，手动编辑成本高。
- 方法要点：结合FastSAM提取语义信息，通过自适应融合模块和多尺度残差空间Mamba组进行校正，并利用CLIP引导生成伪标签进行无监督训练。
- 实验或效果：在真实世界曝光图像上有效校正，数值和视觉上优于现有无监督方法。

## 摘要（原文）

> Improper exposure often leads to severe loss of details, color distortion, and reduced contrast. Exposure correction still faces two critical challenges: (1) the ignorance of object-wise regional semantic information causes the color shift artifacts; (2) real-world exposure images generally have no ground-truth labels, and its labeling entails massive manual editing. To tackle the challenges, we propose a new unsupervised semantic-aware exposure correction network. It contains an adaptive semantic-aware fusion module, which effectively fuses the semantic information extracted from a pre-trained Fast Segment Anything Model into a shared image feature space. Then the fused features are used by our multi-scale residual spatial mamba group to restore the details and adjust the exposure. To avoid manual editing, we propose a pseudo-ground truth generator guided by CLIP, which is fine-tuned to automatically identify exposure situations and instruct the tailored corrections. Also, we leverage the rich priors from the FastSAM and CLIP to develop a semantic-prompt consistency loss to enforce semantic consistency and image-prompt alignment for unsupervised training. Comprehensive experimental results illustrate the effectiveness of our method in correcting real-world exposure images and outperforms state-of-the-art unsupervised methods both numerically and visually.

