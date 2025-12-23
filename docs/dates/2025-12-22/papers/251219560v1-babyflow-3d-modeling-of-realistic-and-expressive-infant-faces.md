---
layout: default
title: BabyFlow: 3D modeling of realistic and expressive infant faces
---

# BabyFlow: 3D modeling of realistic and expressive infant faces
**arXiv**：[2512.19560v1](https://arxiv.org/abs/2512.19560) · [PDF](https://arxiv.org/pdf/2512.19560.pdf)  
**作者**：Antonia Alomar, Mireia Masias, Marius George Linguraru, Federico M. Sukno, Gemma Piella  

**一句话要点**：提出BabyFlow模型以解决婴儿面部建模中身份与表情分离的挑战，支持3D重建与表达控制。

**关键词**：婴儿面部建模, 归一化流, 表情迁移, 3D重建, 生成模型, 数据增强

## 3 点简述
- 核心问题：婴儿面部建模因数据稀缺和自发表情多变而困难，影响发育障碍的早期检测。
- 方法要点：使用归一化流学习概率表示，通过跨年龄表情迁移从成人扫描数据丰富婴儿数据集。
- 实验或效果：提高3D重建精度，尤其在嘴、眼、鼻区域，并支持身份保持的表情合成与修改。

## 摘要（原文）

> Early detection of developmental disorders can be aided by analyzing infant craniofacial morphology, but modeling infant faces is challenging due to limited data and frequent spontaneous expressions. We introduce BabyFlow, a generative AI model that disentangles facial identity and expression, enabling independent control over both. Using normalizing flows, BabyFlow learns flexible, probabilistic representations that capture the complex, non-linear variability of expressive infant faces without restrictive linear assumptions. To address scarce and uncontrolled expressive data, we perform cross-age expression transfer, adapting expressions from adult 3D scans to enrich infant datasets with realistic and systematic expressive variants. As a result, BabyFlow improves 3D reconstruction accuracy, particularly in highly expressive regions such as the mouth, eyes, and nose, and supports synthesis and modification of infant expressions while preserving identity. Additionally, by integrating with diffusion models, BabyFlow generates high-fidelity 2D infant images with consistent 3D geometry, providing powerful tools for data augmentation and early facial analysis.

