---
layout: default
title: Equivariant Multiscale Learned Invertible Reconstruction for Cone Beam CT: From Simulated to Real Data
---

# Equivariant Multiscale Learned Invertible Reconstruction for Cone Beam CT: From Simulated to Real Data
**arXiv**：[2512.21180v1](https://arxiv.org/abs/2512.21180) · [PDF](https://arxiv.org/pdf/2512.21180.pdf)  
**作者**：Nikita Moriakov, Efstratios Gavves, Jonathan H. Mason, Carmen Seller-Oria, Jonas Teuwen, Jan-Jakob Sonke  

**一句话要点**：提出LIRE++，一种旋转等变多尺度可逆学习重建方法，用于快速高效锥束CT重建。

**关键词**：锥束CT重建, 旋转等变性, 多尺度学习, 可逆网络, 深度学习, 医学成像

## 3 点简述
- 锥束CT图像质量低，深度学习重建面临缺乏真实数据、内存限制和快速推理挑战。
- LIRE++结合旋转等变性和多尺度可逆对偶方案，提升参数效率和内存优化。
- 在合成数据上PSNR平均提高1 dB，在真实临床数据上MAE比现有方法降低10 HU。

## 摘要（原文）

> Cone Beam CT (CBCT) is an important imaging modality nowadays, however lower image quality of CBCT compared to more conventional Computed Tomography (CT) remains a limiting factor in CBCT applications. Deep learning reconstruction methods are a promising alternative to classical analytical and iterative reconstruction methods, but applying such methods to CBCT is often difficult due to the lack of ground truth data, memory limitations and the need for fast inference at clinically-relevant resolutions. In this work we propose LIRE++, an end-to-end rotationally-equivariant multiscale learned invertible primal-dual scheme for fast and memory-efficient CBCT reconstruction. Memory optimizations and multiscale reconstruction allow for fast training and inference, while rotational equivariance improves parameter efficiency. LIRE++ was trained on simulated projection data from a fast quasi-Monte Carlo CBCT projection simulator that we developed as well. Evaluated on synthetic data, LIRE++ gave an average improvement of 1 dB in Peak Signal-to-Noise Ratio over alternative deep learning baselines. On real clinical data, LIRE++ improved the average Mean Absolute Error between the reconstruction and the corresponding planning CT by 10 Hounsfield Units with respect to current proprietary state-of-the-art hybrid deep-learning/iterative method.

