---
layout: default
title: Exploring Deep Learning and Ultra-Widefield Imaging for Diabetic Retinopathy and Macular Edema
---

# Exploring Deep Learning and Ultra-Widefield Imaging for Diabetic Retinopathy and Macular Edema
**arXiv**：[2603.08235v1](https://arxiv.org/abs/2603.08235) · [PDF](https://arxiv.org/pdf/2603.08235.pdf)  
**作者**：Pablo Jimenez-Lizcano, Sergio Romero-Tapiador, Ruben Tolosana, Aythami Morales, Guillermo González de Rivera, Ruben Vera-Rodriguez, Julian Fierrez  

**一句话要点**：探索深度学习与超广角成像在糖尿病视网膜病变和黄斑水肿检测中的应用

**关键词**：糖尿病视网膜病变检测, 超广角成像, 深度学习, 视觉变换器, 特征融合, 频域分析

## 3 点简述
- 核心问题：糖尿病视网膜病变和黄斑水肿是导致可预防失明的主要原因，传统方法依赖标准眼底摄影，但超广角成像提供更广视野。
- 方法要点：使用深度学习模型（包括卷积神经网络、视觉变换器和基础模型）在空间和频域进行基准测试，并探索特征级融合以提高鲁棒性。
- 实验或效果：在UWF4DR挑战数据集上评估，模型表现一致强劲，增强了解释性，验证了视觉变换器和频域表示在超广角分析中的潜力。

## 摘要（原文）

> Diabetic retinopathy (DR) and diabetic macular edema (DME) are leading causes of preventable blindness among working-age adults. Traditional approaches in the literature focus on standard color fundus photography (CFP) for the detection of these conditions. Nevertheless, recent ultra-widefield imaging (UWF) offers a significantly wider field of view in comparison to CFP. Motivated by this, the present study explores state-of-the-art deep learning (DL) methods and UWF imaging on three clinically relevant tasks: i) image quality assessment for UWF, ii) identification of referable diabetic retinopathy (RDR), and iii) identification of DME. Using the publicly available UWF4DR Challenge dataset, released as part of the MICCAI 2024 conference, we benchmark DL models in the spatial (RGB) and frequency domains, including popular convolutional neural networks (CNNs) as well as recent vision transformers (ViTs) and foundation models. In addition, we explore a final feature-level fusion to increase robustness. Finally, we also analyze the decisions of the DL models using Grad-CAM, increasing the explainability. Our proposal achieves consistently strong performance across all architectures, underscoring the competitiveness of emerging ViTs and foundation models and the promise of feature-level fusion and frequency-domain representations for UWF analysis.

