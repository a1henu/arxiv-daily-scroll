---
layout: default
title: RamanSeg: Interpretability-driven Deep Learning on Raman Spectra for Cancer Diagnosis
---

# RamanSeg: Interpretability-driven Deep Learning on Raman Spectra for Cancer Diagnosis
**arXiv**：[2602.18119v1](https://arxiv.org/abs/2602.18119) · [PDF](https://arxiv.org/pdf/2602.18119.pdf)  
**作者**：Chris Tomy, Mo Vali, David Pertzborn, Tammam Alamatouri, Anna Mühlig, Orlando Guntinas-Lichius, Anna Xylander, Eric Michele Fantuzzi, Matteo Negro, Francesco Crisafi, Pietro Lio, Tiago Azevedo  

**一句话要点**：提出RamanSeg原型架构，基于拉曼光谱实现可解释的癌症诊断分割。

**关键词**：拉曼光谱, 癌症诊断, 图像分割, 可解释性, 原型学习, nnU-Net

## 3 点简述
- 核心问题：传统组织病理学癌症诊断耗时且依赖专家，需无染色替代方法。
- 方法要点：使用nnU-Net训练分割模型，并设计原型驱动的RamanSeg架构提升可解释性。
- 实验或效果：RamanSeg无投影版本在平均前景Dice得分上优于U-Net基线，达67.3%。

## 摘要（原文）

> Histopathology, the current gold standard for cancer diagnosis, involves the manual examination of tissue samples after chemical staining, a time-consuming process requiring expert analysis. Raman spectroscopy is an alternative, stain-free method of extracting information from samples. Using nnU-Net, we trained a segmentation model on a novel dataset of spatial Raman spectra aligned with tumour annotations, achieving a mean foreground Dice score of 80.9%, surpassing previous work. Furthermore, we propose a novel, interpretable, prototype-based architecture called RamanSeg. RamanSeg classifies pixels based on discovered regions of the training set, generating a segmentation mask. Two variants of RamanSeg allow a trade-off between interpretability and performance: one with prototype projection and another projection-free version. The projection-free RamanSeg outperformed a U-Net baseline with a mean foreground Dice score of 67.3%, offering a meaningful improvement over a black-box training approach.

