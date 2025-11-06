---
layout: default
title: Unified Long Video Inpainting and Outpainting via Overlapping High-Order Co-Denoising
---

# Unified Long Video Inpainting and Outpainting via Overlapping High-Order Co-Denoising
**arXiv**：[2511.03272v1](https://arxiv.org/abs/2511.03272) · [PDF](https://arxiv.org/pdf/2511.03272.pdf)  
**作者**：Shuangquan Lyu, Steven Mao, Yue Ma  

**一句话要点**：提出统一长视频修复与外延方法，通过重叠高阶协同去噪实现高保真编辑

**关键词**：长视频修复, 视频外延, 扩散模型, 协同去噪, LoRA微调, 视频编辑

## 3 点简述
- 核心问题：长视频生成与可控修复/外延困难，现有方法存在固定长度限制或拼接伪影
- 方法要点：基于LoRA微调预训练视频扩散模型，采用重叠混合高阶协同去噪策略
- 实验或效果：在数百帧任务中优于基线，质量与感知真实度指标提升，参数高效

## 摘要（原文）

> Generating long videos remains a fundamental challenge, and achieving high
> controllability in video inpainting and outpainting is particularly demanding.
> To address both of these challenges simultaneously and achieve controllable
> video inpainting and outpainting for long video clips, we introduce a novel and
> unified approach for long video inpainting and outpainting that extends
> text-to-video diffusion models to generate arbitrarily long, spatially edited
> videos with high fidelity. Our method leverages LoRA to efficiently fine-tune a
> large pre-trained video diffusion model like Alibaba's Wan 2.1 for masked
> region video synthesis, and employs an overlap-and-blend temporal co-denoising
> strategy with high-order solvers to maintain consistency across long sequences.
> In contrast to prior work that struggles with fixed-length clips or exhibits
> stitching artifacts, our system enables arbitrarily long video generation and
> editing without noticeable seams or drift. We validate our approach on
> challenging inpainting/outpainting tasks including editing or adding objects
> over hundreds of frames and demonstrate superior performance to baseline
> methods like Wan 2.1 model and VACE in terms of quality (PSNR/SSIM), and
> perceptual realism (LPIPS). Our method enables practical long-range video
> editing with minimal overhead, achieved a balance between parameter efficient
> and superior performance.

