---
layout: default
title: Boosting SAM for Cross-Domain Few-Shot Segmentation via Conditional Point Sparsification
---

# Boosting SAM for Cross-Domain Few-Shot Segmentation via Conditional Point Sparsification
**arXiv**：[2602.05218v1](https://arxiv.org/abs/2602.05218) · [PDF](https://arxiv.org/pdf/2602.05218.pdf)  
**作者**：Jiahao Nie, Yun Xing, Wenbin An, Qingsong Zhao, Jiawei Shao, Yap-Peng Tan, Alex C. Kot, Shijian Lu, Xuelong Li  

**一句话要点**：提出条件点稀疏化方法以提升SAM在跨域少样本分割中的性能

**关键词**：跨域少样本分割, 条件点稀疏化, Segment Anything Model, 无训练方法, 点匹配优化

## 3 点简述
- 核心问题：SAM在跨域少样本分割中，密集点匹配因域偏移导致性能下降
- 方法要点：基于参考样本自适应稀疏化匹配点，优化SAM交互，无需训练
- 实验或效果：在多个跨域数据集上优于现有无训练SAM方法，提升分割准确性

## 摘要（原文）

> Motivated by the success of the Segment Anything Model (SAM) in promptable segmentation, recent studies leverage SAM to develop training-free solutions for few-shot segmentation, which aims to predict object masks in the target image based on a few reference exemplars. These SAM-based methods typically rely on point matching between reference and target images and use the matched dense points as prompts for mask prediction. However, we observe that dense points perform poorly in Cross-Domain Few-Shot Segmentation (CD-FSS), where target images are from medical or satellite domains. We attribute this issue to large domain shifts that disrupt the point-image interactions learned by SAM, and find that point density plays a crucial role under such conditions. To address this challenge, we propose Conditional Point Sparsification (CPS), a training-free approach that adaptively guides SAM interactions for cross-domain images based on reference exemplars. Leveraging ground-truth masks, the reference images provide reliable guidance for adaptively sparsifying dense matched points, enabling more accurate segmentation results. Extensive experiments demonstrate that CPS outperforms existing training-free SAM-based methods across diverse CD-FSS datasets.

