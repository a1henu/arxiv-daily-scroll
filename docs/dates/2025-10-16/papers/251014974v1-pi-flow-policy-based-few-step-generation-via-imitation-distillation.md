---
layout: default
title: pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation
---

# pi-Flow: Policy-Based Few-Step Generation via Imitation Distillation
**arXiv**：[2510.14974v1](https://arxiv.org/abs/2510.14974) · [PDF](https://arxiv.org/pdf/2510.14974.pdf)  
**作者**：Hansheng Chen, Kai Zhang, Hao Tan, Leonidas Guibas, Gordon Wetzstein, Sai Bi  

**一句话要点**：提出π-Flow策略模型以解决少步生成中的质量-多样性权衡问题

**关键词**：少步生成模型, 策略蒸馏, 流匹配, ODE积分, 质量-多样性权衡, 模仿学习

## 3 点简述
- 核心问题：少步扩散或流模型蒸馏中格式不匹配导致复杂蒸馏和质量-多样性权衡
- 方法要点：修改学生模型输出层为无网络策略，预测动态流速实现快速ODE积分
- 实验或效果：在ImageNet 256²上1-NFE FID达2.85，优于MeanFlow，4 NFEs下保持教师质量并提升多样性

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

