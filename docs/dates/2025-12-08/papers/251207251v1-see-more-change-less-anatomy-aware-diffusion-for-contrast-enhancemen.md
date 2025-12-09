---
layout: default
title: See More, Change Less: Anatomy-Aware Diffusion for Contrast Enhancement
---

# See More, Change Less: Anatomy-Aware Diffusion for Contrast Enhancement
**arXiv**：[2512.07251v1](https://arxiv.org/abs/2512.07251) · [PDF](https://arxiv.org/pdf/2512.07251.pdf)  
**作者**：Junqi Liu, Zejun Wu, Pedro R. A. S. Bassi, Xinze Zhou, Wenxuan Li, Ibrahim E. Hamamci, Sezgin Er, Tianyu Lin, Yi Luo, Szymon Płotka, Bjoern Menze, Daguang Xu, Kai Ding, Kang Wang, Yang Yang, Yucheng Tang, Alan L. Yuille, Zongwei Zhou  

**一句话要点**：提出SMILE解剖感知扩散模型，以解决医学图像增强中过度编辑导致解剖失真和临床误判的问题。

**关键词**：医学图像增强, 解剖感知扩散模型, 对比度增强, 免配准学习, 临床决策支持

## 3 点简述
- 核心问题：现有医学图像增强模型因缺乏解剖和对比度动态理解，常过度编辑，导致器官失真、假阳性或漏检小肿瘤。
- 方法要点：SMILE通过结构感知监督、免配准学习和统一推理，实现仅增强临床相关区域，保持解剖准确性。
- 实验或效果：在六个外部数据集上，SMILE在图像质量和临床有用性上优于现有方法，提升癌症检测F1分数达10%。

## 摘要（原文）

> Image enhancement improves visual quality and helps reveal details that are hard to see in the original image. In medical imaging, it can support clinical decision-making, but current models often over-edit. This can distort organs, create false findings, and miss small tumors because these models do not understand anatomy or contrast dynamics. We propose SMILE, an anatomy-aware diffusion model that learns how organs are shaped and how they take up contrast. It enhances only clinically relevant regions while leaving all other areas unchanged. SMILE introduces three key ideas: (1) structure-aware supervision that follows true organ boundaries and contrast patterns; (2) registration-free learning that works directly with unaligned multi-phase CT scans; (3) unified inference that provides fast and consistent enhancement across all contrast phases. Across six external datasets, SMILE outperforms existing methods in image quality (14.2% higher SSIM, 20.6% higher PSNR, 50% better FID) and in clinical usefulness by producing anatomically accurate and diagnostically meaningful images. SMILE also improves cancer detection from non-contrast CT, raising the F1 score by up to 10 percent.

