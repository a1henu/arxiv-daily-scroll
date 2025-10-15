---
layout: default
title: Efficient Perceptual Image Super Resolution: AIM 2025 Study and Benchmark
---

# Efficient Perceptual Image Super Resolution: AIM 2025 Study and Benchmark
**arXiv**：[2510.12765v1](https://arxiv.org/abs/2510.12765) · [PDF](https://arxiv.org/pdf/2510.12765.pdf)  
**作者**：Bruno Longarela, Marcos V. Conde, Alvaro Garcia, Radu Timofte  

**一句话要点**：提出高效感知超分辨率方法，在严格效率约束下超越Real-ESRGAN。

**关键词**：高效感知超分辨率, 参数约束优化, 4K图像基准, Real-ESRGAN比较

## 3 点简述
- 核心问题：感知质量导向的超分辨率方法效率低下，需在5M参数和2000 GFLOPs内优化。
- 方法要点：设计高效模型，复制或改进Real-ESRGAN的感知结果，满足资源限制。
- 实验或效果：在500张4K退化图像数据集上评估，最优方法在所有基准中表现更优。

## 摘要（原文）

> This paper presents a comprehensive study and benchmark on Efficient
> Perceptual Super-Resolution (EPSR). While significant progress has been made in
> efficient PSNR-oriented super resolution, approaches focusing on perceptual
> quality metrics remain relatively inefficient. Motivated by this gap, we aim to
> replicate or improve the perceptual results of Real-ESRGAN while meeting strict
> efficiency constraints: a maximum of 5M parameters and 2000 GFLOPs, calculated
> for an input size of 960x540 pixels. The proposed solutions were evaluated on a
> novel dataset consisting of 500 test images of 4K resolution, each degraded
> using multiple degradation types, without providing the original high-quality
> counterparts. This design aims to reflect realistic deployment conditions and
> serves as a diverse and challenging benchmark. The top-performing approach
> manages to outperform Real-ESRGAN across all benchmark datasets, demonstrating
> the potential of efficient methods in the perceptual domain. This paper
> establishes the modern baselines for efficient perceptual super resolution.

