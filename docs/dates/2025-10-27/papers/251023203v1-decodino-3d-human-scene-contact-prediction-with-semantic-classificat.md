---
layout: default
title: DecoDINO: 3D Human-Scene Contact Prediction with Semantic Classification
---

# DecoDINO: 3D Human-Scene Contact Prediction with Semantic Classification
**arXiv**：[2510.23203v1](https://arxiv.org/abs/2510.23203) · [PDF](https://arxiv.org/pdf/2510.23203.pdf)  
**作者**：Lukas Bierling, Davide Pasero, Fleur Dolmans, Helia Ghasemi, Angelo Broere  

**一句话要点**：提出DecoDINO以改进人-场景接触预测，提升精度与语义分类能力

**关键词**：3D人-场景接触预测, 语义分类, DINOv2编码器, 补丁级交叉注意力, LoRA微调, DAMON基准

## 3 点简述
- 核心问题：现有方法在软表面、遮挡等场景下接触预测精度不足，且缺乏语义信息
- 方法要点：基于DECO框架，采用双DINOv2编码器与补丁级交叉注意力，优化局部推理
- 实验或效果：在DAMON基准上，F1分数提升7%，测地误差减半，并添加对象级语义标签

## 摘要（原文）

> Accurate vertex-level contact prediction between humans and surrounding
> objects is a prerequisite for high fidelity human object interaction models
> used in robotics, AR/VR, and behavioral simulation. DECO was the first in the
> wild estimator for this task but is limited to binary contact maps and
> struggles with soft surfaces, occlusions, children, and false-positive foot
> contacts. We address these issues and introduce DecoDINO, a three-branch
> network based on DECO's framework. It uses two DINOv2 ViT-g/14 encoders,
> class-balanced loss weighting to reduce bias, and patch-level cross-attention
> for improved local reasoning. Vertex features are finally passed through a
> lightweight MLP with a softmax to assign semantic contact labels. We also
> tested a vision-language model (VLM) to integrate text features, but the
> simpler architecture performed better and was used instead. On the DAMON
> benchmark, DecoDINO (i) raises the binary-contact F1 score by 7$\%$, (ii)
> halves the geodesic error, and (iii) augments predictions with object-level
> semantic labels. Ablation studies show that LoRA fine-tuning and the dual
> encoders are key to these improvements. DecoDINO outperformed the challenge
> baseline in both tasks of the DAMON Challenge. Our code is available at
> https://github.com/DavidePasero/deco/tree/main.

