---
layout: default
title: Well Log-Guided Synthesis of Subsurface Images from Sparse Petrography Data Using cGANs
---

# Well Log-Guided Synthesis of Subsurface Images from Sparse Petrography Data Using cGANs
**arXiv**：[2603.09651v1](https://arxiv.org/abs/2603.09651) · [PDF](https://arxiv.org/pdf/2603.09651.pdf)  
**作者**：Ali Sadeghkhani, A. Assadi, B. Bennett, A. Rabbani  

**一句话要点**：提出基于cGAN的井测数据引导合成方法，以解决碳酸盐岩孔隙尺度成像稀疏问题。

**关键词**：条件生成对抗网络, 孔隙尺度成像, 碳酸盐岩合成, 井测数据集成, 储层表征

## 3 点简述
- 核心问题：地下孔隙尺度成像成本高且深度离散，导致储层表征存在显著间隙。
- 方法要点：使用条件生成对抗网络，以井测孔隙度值为条件合成碳酸盐岩薄片图像。
- 实验或效果：在1992-2000米深度区间训练，合成图像孔隙度范围0.004-0.745，目标孔隙度10%误差内准确率达81%。

## 摘要（原文）

> Pore-scale imaging of subsurface formations is costly and limited to discrete depths, creating significant gaps in reservoir characterization. To address this, we present a conditional Generative Adversarial Network (cGAN) framework for synthesizing realistic thin section images of carbonate rock formations, conditioned on porosity values derived from well logs. The model is trained on 5,000 sub-images extracted from 15 petrography samples over a depth interval of 1992-2000m, the model generates geologically consistent images across a wide porosity range (0.004-0.745), achieving 81% accuracy within a 10\% margin of target porosity values. The successful integration of well log data with the trained generator enables continuous pore-scale visualization along the wellbore, bridging gaps between discrete core sampling points and providing valuable insights for reservoir characterization and energy transition applications such as carbon capture and underground hydrogen storage.

