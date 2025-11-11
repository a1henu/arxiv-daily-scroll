---
layout: default
title: RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion
---

# RaLD: Generating High-Resolution 3D Radar Point Clouds with Latent Diffusion
**arXiv**：[2511.07067v1](https://arxiv.org/abs/2511.07067) · [PDF](https://arxiv.org/pdf/2511.07067.pdf)  
**作者**：Ruijie Zhang, Bixin Zeng, Shengpeng Wang, Fuhui Zhou, Wei Wang  

**一句话要点**：提出RaLD框架，通过潜在扩散模型生成高分辨率3D雷达点云，以提升恶劣环境下的感知能力。

**关键词**：3D雷达点云生成, 潜在扩散模型, 毫米波雷达感知, 自动驾驶, LiDAR自动编码

## 3 点简述
- 毫米波雷达点云稀疏低分辨率，限制其在自动驾驶等任务中的应用。
- 采用潜在扩散模型，结合LiDAR自动编码和雷达频谱条件，实现紧凑生成。
- 实验显示，能从原始雷达频谱生成密集准确3D点云，增强鲁棒感知。

## 摘要（原文）

> Millimeter-wave radar offers a promising sensing modality for autonomous
> systems thanks to its robustness in adverse conditions and low cost. However,
> its utility is significantly limited by the sparsity and low resolution of
> radar point clouds, which poses challenges for tasks requiring dense and
> accurate 3D perception. Despite that recent efforts have shown great potential
> by exploring generative approaches to address this issue, they often rely on
> dense voxel representations that are inefficient and struggle to preserve
> structural detail. To fill this gap, we make the key observation that latent
> diffusion models (LDMs), though successful in other modalities, have not been
> effectively leveraged for radar-based 3D generation due to a lack of compatible
> representations and conditioning strategies. We introduce RaLD, a framework
> that bridges this gap by integrating scene-level frustum-based LiDAR
> autoencoding, order-invariant latent representations, and direct radar spectrum
> conditioning. These insights lead to a more compact and expressive generation
> process. Experiments show that RaLD produces dense and accurate 3D point clouds
> from raw radar spectrums, offering a promising solution for robust perception
> in challenging environments.

