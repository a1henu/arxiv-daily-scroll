---
layout: default
title: Ordinal Diffusion Models for Color Fundus Images
---

# Ordinal Diffusion Models for Color Fundus Images
**arXiv**：[2602.24013v1](https://arxiv.org/abs/2602.24013) · [PDF](https://arxiv.org/pdf/2602.24013.pdf)  
**作者**：Gustav Schmidt, Philipp Berens, Sarah Müller  

**一句话要点**：提出序数潜在扩散模型以解决糖尿病视网膜病变分级中疾病进展连续性与离散标签不匹配问题

**关键词**：序数扩散模型, 彩色眼底图像生成, 糖尿病视网膜病变, 医学成像, 条件生成模型, 疾病进展建模

## 3 点简述
- 核心问题：现有条件扩散模型将疾病阶段视为独立类别，忽略医学成像中疾病进展的连续本质。
- 方法要点：使用标量疾病表示替代分类条件，将有序结构融入生成过程，实现相邻阶段间的平滑过渡。
- 实验或效果：在EyePACS数据集上评估，视觉真实性和临床一致性提升，Fréchet inception距离降低，二次加权κ从0.79增至0.87。

## 摘要（原文）

> It has been suggested that generative image models such as diffusion models can improve performance on clinically relevant tasks by offering deep learning models supplementary training data. However, most conditional diffusion models treat disease stages as independent classes, ignoring the continuous nature of disease progression. This mismatch is problematic in medical imaging because continuous pathological processes are typically only observed through coarse, discrete but ordered labels as in ophthalmology for diabetic retinopathy (DR). We propose an ordinal latent diffusion model for generating color fundus images that explicitly incorporates the ordered structure of DR severity into the generation process. Instead of categorical conditioning, we used a scalar disease representation, enabling a smooth transition between adjacent stages. We evaluated our approach using visual realism metrics and classification-based clinical consistency analysis on the EyePACS dataset. Compared to a standard conditional diffusion model, our model reduced the Fréchet inception distance for four of the five DR stages and increased the quadratic weighted $κ$ from 0.79 to 0.87. Furthermore, interpolation experiments showed that the model captured a continuous spectrum of disease progression learned from ordered, coarse class labels.

