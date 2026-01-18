---
layout: default
title: Discrete Feynman-Kac Correctors
---

# Discrete Feynman-Kac Correctors
**arXiv**：[2601.10403v1](https://arxiv.org/abs/2601.10403) · [PDF](https://arxiv.org/pdf/2601.10403.pdf)  
**作者**：Mohsin Hasan, Viktor Ohanesian, Artem Gazizov, Yoshua Bengio, Alán Aspuru-Guzik, Roberto Bondesan, Marta Skreta, Kirill Neklyudov  

**一句话要点**：提出离散Feynman-Kac校正器框架，以在推理时控制离散掩码扩散模型的生成分布

**关键词**：离散扩散模型, 序列蒙特卡洛, 推理控制, 退火采样, 奖励加权采样, 蛋白质序列生成

## 3 点简述
- 核心问题：离散扩散模型缺乏对生成样本分布的灵活控制，限制了应用范围。
- 方法要点：基于序列蒙特卡洛算法，无需额外训练，实现退火、多过程乘积和奖励函数加权采样。
- 实验或效果：应用于伊辛模型退火采样、代码生成性能提升和奖励导向的蛋白质序列生成。

## 摘要（原文）

> Discrete diffusion models have recently emerged as a promising alternative to the autoregressive approach for generating discrete sequences. Sample generation via gradual denoising or demasking processes allows them to capture hierarchical non-sequential interdependencies in the data. These custom processes, however, do not assume a flexible control over the distribution of generated samples. We propose Discrete Feynman-Kac Correctors, a framework that allows for controlling the generated distribution of discrete masked diffusion models at inference time. We derive Sequential Monte Carlo (SMC) algorithms that, given a trained discrete diffusion model, control the temperature of the sampled distribution (i.e. perform annealing), sample from the product of marginals of several diffusion processes (e.g. differently conditioned processes), and sample from the product of the marginal with an external reward function, producing likely samples from the target distribution that also have high reward. Notably, our framework does not require any training of additional models or fine-tuning of the original model. We illustrate the utility of our framework in several applications including: efficient sampling from the annealed Boltzmann distribution of the Ising model, improving the performance of language models for code generation and amortized learning, as well as reward-tilted protein sequence generation.

