---
layout: default
title: DiffInf: Influence-Guided Diffusion for Supervision Alignment in Facial Attribute Learning
---

# DiffInf: Influence-Guided Diffusion for Supervision Alignment in Facial Attribute Learning
**arXiv**：[2603.06399v1](https://arxiv.org/abs/2603.06399) · [PDF](https://arxiv.org/pdf/2603.06399.pdf)  
**作者**：Basudha Pal, Rama Chellappa  

**一句话要点**：提出DiffInf框架，通过影响引导扩散缓解人脸属性学习中的标注不一致问题。

**关键词**：人脸属性分类, 标注不一致, 扩散模型, 影响函数, 生成式校正, 监督对齐

## 3 点简述
- 人脸属性分类中，标注不一致源于主观性和视觉混淆因素，导致监督误差。
- DiffInf使用自影响分数识别关键样本，通过潜在扩散自编码器进行生成式校正，对齐图像与标签。
- 实验表明，DiffInf在多类人脸属性分类中提升泛化性能，优于基线方法。

## 摘要（原文）

> Facial attribute classification relies on large-scale annotated datasets in which many traits, such as age and expression, are inherently ambiguous and continuous but are discretized into categorical labels. Annotation inconsistencies arise from subjectivity and visual confounders such as pose, illumination, expression, and demographic variation, creating mismatch between images and assigned labels. These inconsistencies introduce supervision errors that impair representation learning and degrade downstream prediction. We introduce DiffInf, a self-influence--guided diffusion framework for mitigating annotation inconsistencies in facial attribute learning. We first train a baseline classifier and compute sample-wise self-influence scores using a practical first-order approximation to identify training instances that disproportionately destabilize optimization. Instead of discarding these influential samples, we apply targeted generative correction via a latent diffusion autoencoder to better align visual content with assigned labels while preserving identity and realism. To enable differentiable guidance during correction, we train a lightweight predictor of high-influence membership and use it as a surrogate influence regularizer. The edited samples replace the originals, yielding an influence-refined dataset of unchanged size. Across multi-class facial attribute classification, DiffInf consistently improves generalization compared with standard noisy-label training, robust optimization baselines, and influence-based filtering. Our results demonstrate that repairing influential annotation inconsistencies at the image level enhances downstream facial attribute classification without sacrificing distributional coverage.

