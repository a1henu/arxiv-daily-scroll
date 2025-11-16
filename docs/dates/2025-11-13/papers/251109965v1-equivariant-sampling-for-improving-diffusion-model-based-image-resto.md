---
layout: default
title: Equivariant Sampling for Improving Diffusion Model-based Image Restoration
---

# Equivariant Sampling for Improving Diffusion Model-based Image Restoration
**arXiv**：[2511.09965v1](https://arxiv.org/abs/2511.09965) · [PDF](https://arxiv.org/pdf/2511.09965.pdf)  
**作者**：Chenxu Wu, Qingpeng Kong, Peiang Zhao, Wendi Yang, Wenxin Ma, Fenghe Tang, Zihang Jiang, S. Kevin Zhou  

**一句话要点**：提出EquS方法以改进扩散模型图像修复，通过双采样轨迹增强先验利用。

**关键词**：扩散模型, 图像修复, 等变采样, 双采样轨迹, 时间步感知调度

## 3 点简述
- 问题：现有扩散模型图像修复方法未能充分利用扩散先验，导致性能不佳。
- 方法：引入EquS，使用双采样轨迹施加等变信息，并添加TAS提升效率。
- 效果：实验显示兼容现有方法，显著提升性能且不增加计算成本。

## 摘要（原文）

> Recent advances in generative models, especially diffusion models, have significantly improved image restoration (IR) performance. However, existing problem-agnostic diffusion model-based image restoration (DMIR) methods face challenges in fully leveraging diffusion priors, resulting in suboptimal performance. In this paper, we address the limitations of current problem-agnostic DMIR methods by analyzing their sampling process and providing effective solutions. We introduce EquS, a DMIR method that imposes equivariant information through dual sampling trajectories. To further boost EquS, we propose the Timestep-Aware Schedule (TAS) and introduce EquS$^+$. TAS prioritizes deterministic steps to enhance certainty and sampling efficiency. Extensive experiments on benchmarks demonstrate that our method is compatible with previous problem-agnostic DMIR methods and significantly boosts their performance without increasing computational costs. Our code is available at https://github.com/FouierL/EquS.

