---
layout: default
title: Cut Less, Fold More: Model Compression through the Lens of Projection Geometry
---

# Cut Less, Fold More: Model Compression through the Lens of Projection Geometry
**arXiv**：[2602.18116v1](https://arxiv.org/abs/2602.18116) · [PDF](https://arxiv.org/pdf/2602.18116.pdf)  
**作者**：Olga Saukh, Dong Wang, Haris Šikić, Yun Cheng, Lothar Thiele  

**一句话要点**：提出模型折叠作为几何感知的无校准压缩方法，优于结构化剪枝

**关键词**：模型压缩, 投影几何, 结构化剪枝, 模型折叠, 无校准压缩, 神经网络部署

## 3 点简述
- 研究无重训练神经网络压缩，基于投影几何视角分析结构化剪枝与模型折叠
- 形式化两种方法为正交算子，证明折叠在参数重构误差和功能扰动上通常更优
- 大规模实验验证折叠在多种模型和训练设置下通常获得更高压缩后准确率

## 摘要（原文）

> Compressing neural networks without retraining is vital for deployment at scale. We study calibration-free compression through the lens of projection geometry: structured pruning is an axis-aligned projection, whereas model folding performs a low-rank projection via weight clustering. We formalize both as orthogonal operators and show that, within a rank distance of one, folding provably yields smaller parameter reconstruction error, and under mild smoothness assumptions, smaller functional perturbations than pruning. At scale, we evaluate >1000 checkpoints spanning ResNet18, PreActResNet18, ViT-B/32, and CLIP ViT-B/32 on CIFAR-10 and ImageNet-1K, covering diverse training hyperparameters (optimizers, learning rates, augmentations, regularization, sharpness-aware training), as well as multiple LLaMA-family 60M and 130M parameter models trained on C4. We show that folding typically achieves higher post-compression accuracy, with the largest gains at moderate-high compression. The gap narrows and occasionally reverses at specific training setups. Our results position folding as a geometry-aware, calibration-free alternative to pruning that is often superior in practice and principled in theory.

