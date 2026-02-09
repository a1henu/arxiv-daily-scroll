---
layout: default
title: Infinite-dimensional generative diffusions via Doob's h-transform
---

# Infinite-dimensional generative diffusions via Doob's h-transform
**arXiv**：[2602.06621v1](https://arxiv.org/abs/2602.06621) · [PDF](https://arxiv.org/pdf/2602.06621.pdf)  
**作者**：Thorben Pieper-Sethmacher, Daniel Paulin  

**一句话要点**：提出基于Doob's h-transform的无限维生成扩散框架，以增强模型灵活性。

**关键词**：无限维扩散模型, Doob's h-transform, 指数测度变换, 生成建模, 分数匹配, 概率框架

## 3 点简述
- 核心问题：传统扩散模型在无限维设置中难以定义和推广。
- 方法要点：通过指数测度变换强制参考扩散朝向目标分布，避免时间反转。
- 实验或效果：在合成和真实数据上验证方法，并建立目标测度边界。

## 摘要（原文）

> This paper introduces a rigorous framework for defining generative diffusion models in infinite dimensions via Doob's h-transform. Rather than relying on time reversal of a noising process, a reference diffusion is forced towards the target distribution by an exponential change of measure. Compared to existing methodology, this approach readily generalises to the infinite-dimensional setting, hence offering greater flexibility in the diffusion model. The construction is derived rigorously under verifiable conditions, and bounds with respect to the target measure are established. We show that the forced process under the changed measure can be approximated by minimising a score-matching objective and validate our method on both synthetic and real data.

