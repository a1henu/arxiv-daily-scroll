---
layout: default
title: PG-ControlNet: A Physics-Guided ControlNet for Generative Spatially Varying Image Deblurring
---

# PG-ControlNet: A Physics-Guided ControlNet for Generative Spatially Varying Image Deblurring
**arXiv**：[2511.21043v1](https://arxiv.org/abs/2511.21043) · [PDF](https://arxiv.org/pdf/2511.21043.pdf)  
**作者**：Hakki Motorcu, Mujdat Cetin  

**一句话要点**：提出PG-ControlNet以解决空间变化图像去模糊问题，结合物理约束与生成模型

**关键词**：图像去模糊, 空间变化模糊, 物理引导生成, ControlNet, 扩散模型, 深度学习

## 3 点简述
- 核心问题：空间变化图像去模糊是病态问题，尤其在噪声和复杂模糊下，现有方法易产生伪影或幻觉细节
- 方法要点：建模密集连续模糊核，通过ControlNet架构强引导扩散采样，融合物理约束与生成先验
- 实验或效果：在严重模糊场景中，优于基于模型和生成基线方法，平衡物理准确性与感知真实感

## 摘要（原文）

> Spatially varying image deblurring remains a fundamentally ill-posed problem, especially when degradations arise from complex mixtures of motion and other forms of blur under significant noise. State-of-the-art learning-based approaches generally fall into two paradigms: model-based deep unrolling methods that enforce physical constraints by modeling the degradations, but often produce over-smoothed, artifact-laden textures, and generative models that achieve superior perceptual quality yet hallucinate details due to weak physical constraints. In this paper, we propose a novel framework that uniquely reconciles these paradigms by taming a powerful generative prior with explicit, dense physical constraints. Rather than oversimplifying the degradation field, we model it as a dense continuum of high-dimensional compressed kernels, ensuring that minute variations in motion and other degradation patterns are captured. We leverage this rich descriptor field to condition a ControlNet architecture, strongly guiding the diffusion sampling process. Extensive experiments demonstrate that our method effectively bridges the gap between physical accuracy and perceptual realism, outperforming state-of-the-art model-based methods as well as generative baselines in challenging, severely blurred scenarios.

