---
layout: default
title: Diffusion-SDPO: Safeguarded Direct Preference Optimization for Diffusion Models
---

# Diffusion-SDPO: Safeguarded Direct Preference Optimization for Diffusion Models
**arXiv**：[2511.03317v1](https://arxiv.org/abs/2511.03317) · [PDF](https://arxiv.org/pdf/2511.03317.pdf)  
**作者**：Minghao Fu, Guo-Hua Wang, Tianyu Cui, Qing-Guo Chen, Zhao Xu, Weihua Luo, Kaifu Zhang  

**一句话要点**：提出Diffusion-SDPO以解决扩散模型偏好优化中的生成质量退化问题

**关键词**：扩散模型, 偏好优化, 梯度缩放, 文本到图像生成, 对齐框架

## 3 点简述
- 核心问题：标准Diffusion-DPO扩大偏好间隔可能导致胜败分支重建误差增加，影响生成质量
- 方法要点：引入自适应缩放败者梯度的保护更新规则，确保胜者输出误差非增
- 实验或效果：在文本到图像基准测试中，偏好、美学和提示对齐指标优于基线

## 摘要（原文）

> Text-to-image diffusion models deliver high-quality images, yet aligning them
> with human preferences remains challenging. We revisit diffusion-based Direct
> Preference Optimization (DPO) for these models and identify a critical
> pathology: enlarging the preference margin does not necessarily improve
> generation quality. In particular, the standard Diffusion-DPO objective can
> increase the reconstruction error of both winner and loser branches.
> Consequently, degradation of the less-preferred outputs can become sufficiently
> severe that the preferred branch is also adversely affected even as the margin
> grows. To address this, we introduce Diffusion-SDPO, a safeguarded update rule
> that preserves the winner by adaptively scaling the loser gradient according to
> its alignment with the winner gradient. A first-order analysis yields a
> closed-form scaling coefficient that guarantees the error of the preferred
> output is non-increasing at each optimization step. Our method is simple,
> model-agnostic, broadly compatible with existing DPO-style alignment frameworks
> and adds only marginal computational overhead. Across standard text-to-image
> benchmarks, Diffusion-SDPO delivers consistent gains over preference-learning
> baselines on automated preference, aesthetic, and prompt alignment metrics.
> Code is publicly available at https://github.com/AIDC-AI/Diffusion-SDPO.

