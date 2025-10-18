---
layout: default
title: pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation
---

# pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation
**arXiv**：[2510.14974v1](https://arxiv.org/abs/2510.14974) · [PDF](https://arxiv.org/pdf/2510.14974.pdf)  
**作者**：Hansheng Chen, Kai Zhang, Hao Tan, Leonidas Guibas, Gordon Wetzstein, Sai Bi  

**一句话要点**：提出π-Flow策略模型，通过模仿蒸馏解决少步生成中的质量-多样性权衡问题

**关键词**：少步生成模型, 模仿蒸馏, 策略预测, ODE积分, 质量-多样性权衡, 流匹配损失

## 3 点简述
- 核心问题：少步生成模型蒸馏过程复杂，常面临质量与多样性权衡。
- 方法要点：修改学生模型输出层为策略，预测动态流速，实现高效ODE积分。
- 实验效果：在ImageNet等数据集上，以少步数实现高FID和多样性，超越现有方法。

## 摘要（原文）

> Few-step diffusion or flow-based generative models typically distill a
> velocity-predicting teacher into a student that predicts a shortcut towards
> denoised data. This format mismatch has led to complex distillation procedures
> that often suffer from a quality-diversity trade-off. To address this, we
> propose policy-based flow models ($\pi$-Flow). $\pi$-Flow modifies the output
> layer of a student flow model to predict a network-free policy at one timestep.
> The policy then produces dynamic flow velocities at future substeps with
> negligible overhead, enabling fast and accurate ODE integration on these
> substeps without extra network evaluations. To match the policy's ODE
> trajectory to the teacher's, we introduce a novel imitation distillation
> approach, which matches the policy's velocity to the teacher's along the
> policy's trajectory using a standard $\ell_2$ flow matching loss. By simply
> mimicking the teacher's behavior, $\pi$-Flow enables stable and scalable
> training and avoids the quality-diversity trade-off. On ImageNet 256$^2$, it
> attains a 1-NFE FID of 2.85, outperforming MeanFlow of the same DiT
> architecture. On FLUX.1-12B and Qwen-Image-20B at 4 NFEs, $\pi$-Flow achieves
> substantially better diversity than state-of-the-art few-step methods, while
> maintaining teacher-level quality.

