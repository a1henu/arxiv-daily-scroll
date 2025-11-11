---
layout: default
title: Integrating Reweighted Least Squares with Plug-and-Play Diffusion Priors for Noisy Image Restoration
---

# Integrating Reweighted Least Squares with Plug-and-Play Diffusion Priors for Noisy Image Restoration
**arXiv**：[2511.06823v1](https://arxiv.org/abs/2511.06823) · [PDF](https://arxiv.org/pdf/2511.06823.pdf)  
**作者**：Ji Li, Chao Wang  

**一句话要点**：提出结合重加权最小二乘与扩散先验的即插即用框架，以去除非高斯噪声。

**关键词**：图像恢复, 非高斯噪声, 扩散先验, 重加权最小二乘, 即插即用框架

## 3 点简述
- 现有方法多用于高斯噪声，非高斯噪声如脉冲噪声处理不足。
- 采用广义高斯尺度混合损失和IRLS优化，结合扩散去噪器作为近端算子。
- 在基准数据集上有效去除脉冲噪声，恢复性能优于现有方法。

## 摘要（原文）

> Existing plug-and-play image restoration methods typically employ
> off-the-shelf Gaussian denoisers as proximal operators within classical
> optimization frameworks based on variable splitting. Recently, denoisers
> induced by generative priors have been successfully integrated into regularized
> optimization methods for image restoration under Gaussian noise. However, their
> application to non-Gaussian noise--such as impulse noise--remains largely
> unexplored. In this paper, we propose a plug-and-play image restoration
> framework based on generative diffusion priors for robust removal of general
> noise types, including impulse noise. Within the maximum a posteriori (MAP)
> estimation framework, the data fidelity term is adapted to the specific noise
> model. Departing from the conventional least-squares loss used for Gaussian
> noise, we introduce a generalized Gaussian scale mixture-based loss, which
> approximates a wide range of noise distributions and leads to an $\ell_q$-norm
> ($0<q\leq2$) fidelity term. This optimization problem is addressed using an
> iteratively reweighted least squares (IRLS) approach, wherein the proximal step
> involving the generative prior is efficiently performed via a diffusion-based
> denoiser. Experimental results on benchmark datasets demonstrate that the
> proposed method effectively removes non-Gaussian impulse noise and achieves
> superior restoration performance.

