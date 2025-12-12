---
layout: default
title: Mode-Seeking for Inverse Problems with Diffusion Models
---

# Mode-Seeking for Inverse Problems with Diffusion Models
**arXiv**：[2512.10524v1](https://arxiv.org/abs/2512.10524) · [PDF](https://arxiv.org/pdf/2512.10524.pdf)  
**作者**：Sai Bharath Chandra Gutha, Ricardo Vinuesa, Hossein Azizpour  

**一句话要点**：提出变分模式寻求损失以引导扩散模型解决逆问题，无需任务特定训练。

**关键词**：扩散模型, 逆问题求解, 变分推断, 图像恢复, 最大后验估计

## 3 点简述
- 现有方法依赖建模近似且计算成本高，限制了扩散模型在逆问题中的应用。
- 通过最小化扩散后验与测量后验的KL散度，推导出变分模式寻求损失，引导样本至最大后验估计。
- 在线性逆问题中，该方法无需近似，实验验证其在图像恢复任务中性能与效率优于现有方法。

## 摘要（原文）

> A pre-trained unconditional diffusion model, combined with posterior sampling or maximum a posteriori (MAP) estimation techniques, can solve arbitrary inverse problems without task-specific training or fine-tuning. However, existing posterior sampling and MAP estimation methods often rely on modeling approximations and can be computationally demanding. In this work, we propose the variational mode-seeking loss (VML), which, when minimized during each reverse diffusion step, guides the generated sample towards the MAP estimate. VML arises from a novel perspective of minimizing the Kullback-Leibler (KL) divergence between the diffusion posterior $p(\mathbf{x}_0\|\mathbf{x}_t)$ and the measurement posterior $p(\mathbf{x}_0\|\mathbf{y})$, where $\mathbf{y}$ denotes the measurement. Importantly, for linear inverse problems, VML can be analytically derived and need not be approximated. Based on further theoretical insights, we propose VML-MAP, an empirically effective algorithm for solving inverse problems, and validate its efficacy over existing methods in both performance and computational time, through extensive experiments on diverse image-restoration tasks across multiple datasets.

