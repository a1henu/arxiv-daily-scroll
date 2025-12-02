---
layout: default
title: Reconstructing Multi-Scale Physical Fields from Extremely Sparse Measurements with an Autoencoder-Diffusion Cascade
---

# Reconstructing Multi-Scale Physical Fields from Extremely Sparse Measurements with an Autoencoder-Diffusion Cascade
**arXiv**：[2512.01572v1](https://arxiv.org/abs/2512.01572) · [PDF](https://arxiv.org/pdf/2512.01572.pdf)  
**作者**：Letian Yi, Tingpeng Zhang, Mingyuan Zhou, Guannan Wang, Quanke Su, Zhilu Lai  

**一句话要点**：提出级联感知框架以解决极稀疏测量下的多尺度物理场重建问题

**关键词**：物理场重建, 稀疏测量, 自编码器, 扩散模型, 级联框架, 贝叶斯采样

## 3 点简述
- 核心问题：从极稀疏随机测量重建全场是长期存在的病态逆问题
- 方法要点：集成神经算子自编码器和条件扩散模型，通过级联结构缓解病态性
- 实验或效果：在仿真和真实数据集上验证了泛化性和鲁棒性，适用于实际部署

## 摘要（原文）

> Reconstructing full fields from extremely sparse and random measurements is a longstanding ill-posed inverse problem. A powerful framework for addressing such challenges is hierarchical probabilistic modeling, where uncertainty is represented by intermediate variables and resolved through marginalization during inference. Inspired by this principle, we propose Cascaded Sensing (Cas-Sensing), a hierarchical reconstruction framework that integrates an autoencoder-diffusion cascade. First, a neural operator-based functional autoencoder reconstructs the dominant structures of the original field - including large-scale components and geometric boundaries - from arbitrary sparse inputs, serving as an intermediate variable. Then, a conditional diffusion model, trained with a mask-cascade strategy, generates fine-scale details conditioned on these large-scale structures. To further enhance fidelity, measurement consistency is enforced via the manifold constrained gradient based on Bayesian posterior sampling during the generation process. This cascaded pipeline substantially alleviates ill-posedness, delivering accurate and robust reconstructions. Experiments on both simulation and real-world datasets demonstrate that Cas-Sensing generalizes well across varying sensor configurations and geometric boundaries, making it a promising tool for practical deployment in scientific and engineering applications.

