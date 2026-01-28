---
layout: default
title: RHSIA: Real-time Hemodynamics Surrogation for Non-idealized Intracranial Aneurysms
---

# RHSIA: Real-time Hemodynamics Surrogation for Non-idealized Intracranial Aneurysms
**arXiv**：[2601.19876v1](https://arxiv.org/abs/2601.19876) · [PDF](https://arxiv.org/pdf/2601.19876.pdf)  
**作者**：Yiying Sheng, Wenhao Ding, Dylan Roi, Leonard Leong Litt Yeo, Hwa Liang Leo, Choon Hwai Yap  

**一句话要点**：提出图变换器模型RHSIA，实时预测颅内动脉瘤血流动力学参数以替代计算流体动力学。

**关键词**：颅内动脉瘤, 血流动力学预测, 图变换器, 实时计算, 数据增强, 深度学习模型

## 3 点简述
- 核心问题：计算流体动力学在颅内动脉瘤风险评估中临床转化困难，因耗时且需专业知识。
- 方法要点：使用图变换器模型，结合时间信息，从动脉瘤表面网格预测心动周期内的壁面剪切应力。
- 实验或效果：模型在结构相似性指数达0.981，相对L2误差2.8%，并通过稳态数据增强提升小样本性能。

## 摘要（原文）

> Extensive studies suggested that fluid mechanical markers of intracranial aneurysms (IAs) derived from Computational Fluid Dynamics (CFD) can indicate disease progression risks, but to date this has not been translated clinically. This is because CFD requires specialized expertise and is time-consuming and low throughput, making it difficult to support clinical trials. A deep learning model that maps IA morphology to biomechanical markers can address this, enabling physicians to obtain these markers in real time without performing CFD. Here, we show that a Graph Transformer model that incorporates temporal information, which is supervised by large CFD data, can accurately predict Wall Shear Stress (WSS) across the cardiac cycle from IA surface meshes. The model effectively captures the temporal variations of the WSS pattern, achieving a Structural Similarity Index (SSIM) of up to 0.981 and a maximum-based relative L2 error of 2.8%. Ablation studies and SOTA comparison confirmed its optimality. Further, as pulsatile CFD data is computationally expensive to generate and sample sizes are limited, we engaged a strategy of injecting a large amount of steady-state CFD data, which are extremely low-cost to generate, as augmentation. This approach enhances network performance substantially when pulsatile CFD data sample size is small. Our study provides a proof of concept that temporal sequences cardiovascular fluid mechanical parameters can be computed in real time using a deep learning model from the geometric mesh, and this is achievable even with small pulsatile CFD sample size. Our approach is likely applicable to other cardiovascular scenarios.

