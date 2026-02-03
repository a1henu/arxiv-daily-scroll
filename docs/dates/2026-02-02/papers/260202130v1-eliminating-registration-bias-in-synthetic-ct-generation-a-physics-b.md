---
layout: default
title: Eliminating Registration Bias in Synthetic CT Generation: A Physics-Based Simulation Framework
---

# Eliminating Registration Bias in Synthetic CT Generation: A Physics-Based Simulation Framework
**arXiv**：[2602.02130v1](https://arxiv.org/abs/2602.02130) · [PDF](https://arxiv.org/pdf/2602.02130.pdf)  
**作者**：Lukas Zimmermann, Michael Rauter, Maximilian Schmid, Dietmar Georg, Barbara Knäusl  

**一句话要点**：提出基于物理的CBCT模拟框架以消除合成CT生成中的配准偏差

**关键词**：合成CT生成, 配准偏差消除, CBCT模拟, 几何对齐评估, 医学影像处理

## 3 点简述
- 核心问题：监督式合成CT生成依赖配准训练对，但配准偏差会污染模型和评估指标。
- 方法要点：通过物理模拟构建几何对齐的训练对，并使用几何对齐指标而非强度指标进行评估。
- 实验或效果：在盆腔数据集上，合成数据训练的模型几何对齐更优，临床观察者偏好率达87%。

## 摘要（原文）

> Supervised synthetic CT generation from CBCT requires registered training pairs, yet perfect registration between separately acquired scans remains unattainable. This registration bias propagates into trained models and corrupts standard evaluation metrics. This may suggest that superior benchmark performance indicates better reproduction of registration artifacts rather than anatomical fidelity. We propose physics-based CBCT simulation to provide geometrically aligned training pairs by construction, combined with evaluation using geometric alignment metrics against input CBCT rather than biased ground truth. On two independent pelvic datasets, models trained on synthetic data achieved superior geometric alignment (Normalized Mutual Information: 0.31 vs 0.22) despite lower conventional intensity scores. Intensity metrics showed inverted correlations with clinical assessment for deformably registered data, while Normalized Mutual Information consistently predicted observer preference across registration methodologies (rho = 0.31, p < 0.001). Clinical observers preferred synthetic-trained outputs in 87% of cases, demonstrating that geometric fidelity, not intensity agreement with biased ground truth, aligns with clinical requirements.

