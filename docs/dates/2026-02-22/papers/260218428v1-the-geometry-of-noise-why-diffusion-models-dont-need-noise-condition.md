---
layout: default
title: The Geometry of Noise: Why Diffusion Models Don't Need Noise Conditioning
---

# The Geometry of Noise: Why Diffusion Models Don't Need Noise Conditioning
**arXiv**：[2602.18428v1](https://arxiv.org/abs/2602.18428) · [PDF](https://arxiv.org/pdf/2602.18428.pdf)  
**作者**：Mojtaba Sahraee-Ardakan, Mauricio Delbracio, Peyman Milanfar  

**一句话要点**：提出边际能量框架以解释无噪声条件扩散模型的几何稳定性

**关键词**：扩散模型, 无噪声条件, 几何优化, 边际能量, 黎曼梯度流, 参数化稳定性

## 3 点简述
- 核心问题：无噪声条件模型在数据流形附近梯度发散，如何保持稳定？
- 方法要点：形式化边际能量，证明模型是黎曼梯度流，隐式抵消几何奇点。
- 实验或效果：识别参数化稳定性条件，速度参数化因有界增益而稳定。

## 摘要（原文）

> Autonomous (noise-agnostic) generative models, such as Equilibrium Matching and blind diffusion, challenge the standard paradigm by learning a single, time-invariant vector field that operates without explicit noise-level conditioning. While recent work suggests that high-dimensional concentration allows these models to implicitly estimate noise levels from corrupted observations, a fundamental paradox remains: what is the underlying landscape being optimized when the noise level is treated as a random variable, and how can a bounded, noise-agnostic network remain stable near the data manifold where gradients typically diverge? We resolve this paradox by formalizing Marginal Energy, $E_{\text{marg}}(\mathbf{u}) = -\log p(\mathbf{u})$, where $p(\mathbf{u}) = \int p(\mathbf{u}\|t)p(t)dt$ is the marginal density of the noisy data integrated over a prior distribution of unknown noise levels. We prove that generation using autonomous models is not merely blind denoising, but a specific form of Riemannian gradient flow on this Marginal Energy. Through a novel relative energy decomposition, we demonstrate that while the raw Marginal Energy landscape possesses a $1/t^p$ singularity normal to the data manifold, the learned time-invariant field implicitly incorporates a local conformal metric that perfectly counteracts the geometric singularity, converting an infinitely deep potential well into a stable attractor. We also establish the structural stability conditions for sampling with autonomous models. We identify a ``Jensen Gap'' in noise-prediction parameterizations that acts as a high-gain amplifier for estimation errors, explaining the catastrophic failure observed in deterministic blind models. Conversely, we prove that velocity-based parameterizations are inherently stable because they satisfy a bounded-gain condition that absorbs posterior uncertainty into a smooth geometric drift.

