---
layout: default
title: Training-Free Distribution Adaptation for Diffusion Models via Maximum Mean Discrepancy Guidance
---

# Training-Free Distribution Adaptation for Diffusion Models via Maximum Mean Discrepancy Guidance
**arXiv**：[2601.08379v1](https://arxiv.org/abs/2601.08379) · [PDF](https://arxiv.org/pdf/2601.08379.pdf)  
**作者**：Matina Mahdizadeh Sani, Nima Jamali, Mohammad Jalali, Farzan Farnia  

**一句话要点**：提出MMD Guidance以解决扩散模型在少样本域适应中的分布偏差问题

**关键词**：扩散模型, 域适应, 最大均值差异, 无训练指导, 潜在扩散模型, 少样本学习

## 3 点简述
- 核心问题：预训练扩散模型输出与目标数据分布不匹配，尤其在少样本域适应中难以重训练
- 方法要点：通过最大均值差异梯度指导反向扩散过程，实现无训练分布对齐，适用于条件生成和潜在扩散模型
- 实验或效果：在合成和真实基准测试中，MMD Guidance能保持样本保真度并实现分布对齐

## 摘要（原文）

> Pre-trained diffusion models have emerged as powerful generative priors for both unconditional and conditional sample generation, yet their outputs often deviate from the characteristics of user-specific target data. Such mismatches are especially problematic in domain adaptation tasks, where only a few reference examples are available and retraining the diffusion model is infeasible. Existing inference-time guidance methods can adjust sampling trajectories, but they typically optimize surrogate objectives such as classifier likelihoods rather than directly aligning with the target distribution. We propose MMD Guidance, a training-free mechanism that augments the reverse diffusion process with gradients of the Maximum Mean Discrepancy (MMD) between generated samples and a reference dataset. MMD provides reliable distributional estimates from limited data, exhibits low variance in practice, and is efficiently differentiable, which makes it particularly well-suited for the guidance task. Our framework naturally extends to prompt-aware adaptation in conditional generation models via product kernels. Also, it can be applied with computational efficiency in latent diffusion models (LDMs), since guidance is applied in the latent space of the LDM. Experiments on synthetic and real-world benchmarks demonstrate that MMD Guidance can achieve distributional alignment while preserving sample fidelity.

