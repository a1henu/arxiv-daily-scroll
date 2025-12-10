---
layout: default
title: OCCDiff: Occupancy Diffusion Model for High-Fidelity 3D Building Reconstruction from Noisy Point Clouds
---

# OCCDiff: Occupancy Diffusion Model for High-Fidelity 3D Building Reconstruction from Noisy Point Clouds
**arXiv**：[2512.08506v1](https://arxiv.org/abs/2512.08506) · [PDF](https://arxiv.org/pdf/2512.08506.pdf)  
**作者**：Jialu Sui, Rui Liu, Hongsheng Zhang  

**一句话要点**：提出OCCDiff，基于占用函数空间的潜在扩散模型，用于从噪声点云高保真重建3D建筑

**关键词**：3D建筑重建, 点云处理, 潜在扩散模型, 占用函数, 噪声鲁棒性, 多任务学习

## 3 点简述
- 核心问题：从LiDAR点云重建建筑时，点密度变化和噪声干扰导致表面捕捉不准确
- 方法要点：结合潜在扩散过程和函数自编码器，在占用函数空间生成连续函数，支持任意位置评估
- 实验或效果：模型生成物理一致样本，高保真度，对噪声数据鲁棒，多任务训练提升特征表示

## 摘要（原文）

> A major challenge in reconstructing buildings from LiDAR point clouds lies in accurately capturing building surfaces under varying point densities and noise interference. To flexibly gather high-quality 3D profiles of the building in diverse resolution, we propose OCCDiff applying latent diffusion in the occupancy function space. Our OCCDiff combines a latent diffusion process with a function autoencoder architecture to generate continuous occupancy functions evaluable at arbitrary locations. Moreover, a point encoder is proposed to provide condition features to diffusion learning, constraint the final occupancy prediction for occupancy decoder, and insert multi-modal features for latent generation to latent encoder. To further enhance the model performance, a multi-task training strategy is employed, ensuring that the point encoder learns diverse and robust feature representations. Empirical results show that our method generates physically consistent samples with high fidelity to the target distribution and exhibits robustness to noisy data.

