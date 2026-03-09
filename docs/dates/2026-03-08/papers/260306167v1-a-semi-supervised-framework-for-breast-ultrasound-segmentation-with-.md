---
layout: default
title: A Semi-Supervised Framework for Breast Ultrasound Segmentation with Training-Free Pseudo-Label Generation and Label Refinement
---

# A Semi-Supervised Framework for Breast Ultrasound Segmentation with Training-Free Pseudo-Label Generation and Label Refinement
**arXiv**：[2603.06167v1](https://arxiv.org/abs/2603.06167) · [PDF](https://arxiv.org/pdf/2603.06167.pdf)  
**作者**：Ruili Li, Jiayi Ding, Ruiyu Li, Yilun Jin, Shiwen Ge, Yuwen Zeng, Xiaoyong Zhang, Eichi Takaya, Jan Vrba, Noriyasu Homma  

**一句话要点**：提出基于训练无关伪标签生成与标签精炼的半监督框架，以解决乳腺超声图像分割中标注有限导致的伪标签不稳定问题。

**关键词**：半监督学习, 乳腺超声分割, 伪标签生成, 标签精炼, 跨域迁移, 医学图像分析

## 3 点简述
- 核心问题：半监督学习在乳腺超声图像分割中因标注极少导致伪标签不稳定，影响性能。
- 方法要点：利用外观描述实现跨域结构迁移，生成伪标签，结合静态教师与指数移动平均教师进行标签精炼。
- 实验或效果：在四个数据集上，仅用2.5%标注数据即达到全监督模型可比性能，优于现有半监督方法。

## 摘要（原文）

> Semi-supervised learning (SSL) has emerged as a promising paradigm for breast ultrasound (BUS) image segmentation, but it often suffers from unstable pseudo labels under extremely limited annotations, leading to inaccurate supervision and degraded performance. Recent vision-language models (VLMs) provide a new opportunity for pseudo-label generation, yet their effectiveness on BUS images remains limited because domain-specific prompts are difficult to transfer.
>   To address this issue, we propose a semi-supervised framework with training-free pseudo-label generation and label refinement. By leveraging simple appearance-based descriptions (e.g., dark oval), our method enables cross-domain structural transfer between natural and medical images, allowing VLMs to generate structurally consistent pseudo labels. These pseudo labels are used to warm up a static teacher that captures global structural priors of breast lesions. Combined with an exponential moving average teacher, we further introduce uncertainty entropy weighted fusion and adaptive uncertainty-guided reverse contrastive learning to improve boundary discrimination.
>   Experiments on four BUS datasets demonstrate that our method achieves performance comparable to fully supervised models even with only 2.5% labeled data, significantly outperforming existing SSL approaches. Moreover, the proposed paradigm is readily extensible: for other imaging modalities or diseases, only a global appearance description is required to obtain reliable pseudo supervision, enabling scalable semi-supervised medical image segmentation under limited annotations.

