---
layout: default
title: Nix and Fix: Targeting 1000x Compression of 3D Gaussian Splatting with Diffusion Models
---

# Nix and Fix: Targeting 1000x Compression of 3D Gaussian Splatting with Diffusion Models
**arXiv**：[2602.04549v1](https://arxiv.org/abs/2602.04549) · [PDF](https://arxiv.org/pdf/2602.04549.pdf)  
**作者**：Cem Eteke, Enzo Tartaglione  

**一句话要点**：提出NiFi方法，通过扩散模型实现3D高斯泼溅的极端压缩，以解决低码率下视觉质量下降问题。

**关键词**：3D高斯泼溅压缩, 扩散模型, 一步蒸馏, 伪影感知恢复, 极端压缩率

## 3 点简述
- 核心问题：3D高斯泼溅压缩在低码率时引入伪影，显著降低视觉质量。
- 方法要点：使用基于扩散模型的一步蒸馏，结合伪影感知进行恢复。
- 实验或效果：在极低码率下达到最佳感知质量，压缩率提升近1000倍。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) revolutionized novel view rendering. Instead of inferring from dense spatial points, as implicit representations do, 3DGS uses sparse Gaussians. This enables real-time performance but increases space requirements, hindering applications such as immersive communication. 3DGS compression emerged as a field aimed at alleviating this issue. While impressive progress has been made, at low rates, compression introduces artifacts that degrade visual quality significantly. We introduce NiFi, a method for extreme 3DGS compression through restoration via artifact-aware, diffusion-based one-step distillation. We show that our method achieves state-of-the-art perceptual quality at extremely low rates, down to 0.1 MB, and towards 1000x rate improvement over 3DGS at comparable perceptual performance. The code will be open-sourced upon acceptance.

