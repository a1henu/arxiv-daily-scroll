---
layout: default
title: Neural Implicit 3D Cardiac Shape Reconstruction from Sparse CT Angiography Slices Mimicking 2D Transthoracic Echocardiography Views
---

# Neural Implicit 3D Cardiac Shape Reconstruction from Sparse CT Angiography Slices Mimicking 2D Transthoracic Echocardiography Views
**arXiv**：[2602.05884v1](https://arxiv.org/abs/2602.05884) · [PDF](https://arxiv.org/pdf/2602.05884.pdf)  
**作者**：Gino E. Jansen, Carolina Brás, R. Nils Planken, Mark J. Schuuring, Berto J. Bouma, Ivana Išgum  

**一句话要点**：提出基于神经隐式函数的3D心脏形状重建方法，从稀疏CTA切片模拟2D经胸超声心动图视图

**关键词**：神经隐式函数, 3D心脏重建, 稀疏视图重建, 经胸超声心动图, CT血管造影, 形状先验学习

## 3 点简述
- 核心问题：从稀疏的CTA平面分割中重建完整3D心脏形状，以应用于2D经胸超声心动图。
- 方法要点：使用多层感知机学习形状先验，通过联合优化潜在编码和刚性变换，从模拟TTE视图的CTA平面重建3D结构。
- 实验或效果：在保留的CTA分割集上，平均Dice系数为0.86±0.04，左心室和左心房体积误差显著低于临床标准Simpson双平面规则。

## 摘要（原文）

> Accurate 3D representations of cardiac structures allow quantitative analysis of anatomy and function. In this work, we propose a method for reconstructing complete 3D cardiac shapes from segmentations of sparse planes in CT angiography (CTA) for application in 2D transthoracic echocardiography (TTE). Our method uses a neural implicit function to reconstruct the 3D shape of the cardiac chambers and left-ventricle myocardium from sparse CTA planes. To investigate the feasibility of achieving 3D reconstruction from 2D TTE, we select planes that mimic the standard apical 2D TTE views. During training, a multi-layer perceptron learns shape priors from 3D segmentations of the target structures in CTA. At test time, the network reconstructs 3D cardiac shapes from segmentations of TTE-mimicking CTA planes by jointly optimizing the latent code and the rigid transforms that map the observed planes into 3D space. For each heart, we simulate four realistic apical views, and we compare reconstructed multi-class volumes with the reference CTA volumes. On a held-out set of CTA segmentations, our approach achieves an average Dice coefficient of 0.86 $\pm$ 0.04 across all structures. Our method also achieves markedly lower volume errors than the clinical standard, Simpson's biplane rule: 4.88 $\pm$ 4.26 mL vs. 8.14 $\pm$ 6.04 mL, respectively, for the left ventricle; and 6.40 $\pm$ 7.37 mL vs. 37.76 $\pm$ 22.96 mL, respectively, for the left atrium. This suggests that our approach offers a viable route to more accurate 3D chamber quantification in 2D transthoracic echocardiography.

