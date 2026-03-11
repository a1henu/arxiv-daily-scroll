---
layout: default
title: A comprehensive study of time-of-flight non-line-of-sight imaging
---

# A comprehensive study of time-of-flight non-line-of-sight imaging
**arXiv**：[2603.09548v1](https://arxiv.org/abs/2603.09548) · [PDF](https://arxiv.org/pdf/2603.09548.pdf)  
**作者**：Julio Marco, Adrian Jarabo, Ji Hyun Nam, Alberto Tosi, Diego Gutierrez, Andreas Velten  

**一句话要点**：系统比较飞行时间非视距成像方法，在统一框架下评估性能与局限性

**关键词**：飞行时间成像, 非视距成像, Radon变换, 虚拟视距成像, 性能评估

## 3 点简述
- 核心问题：多种飞行时间非视距成像方法公式和硬件实现各异，难以客观评估理论与实验性能
- 方法要点：基于通用前向模型统一表述代表性方法，分析其与Radon变换及频域虚拟视距成像的关系
- 实验或效果：在相同硬件设置和光子计数下测试，显示方法在分辨率、可见性和噪声敏感性方面有相似局限性

## 摘要（原文）

> Time-of-Flight non-line-of-sight (ToF NLOS) imaging techniques provide state-of-the-art reconstructions of scenes hidden around corners by inverting the optical path of indirect photons scattered by visible surfaces and measured by picosecond resolution sensors. The emergence of a wide range of ToF NLOS imaging methods with heterogeneous formulae and hardware implementations obscures the assessment of both their theoretical and experimental aspects. We present a comprehensive study of a representative set of ToF NLOS imaging methods by discussing their similarities and differences under common formulation and hardware. We first outline the problem statement under a common general forward model for ToF NLOS measurements, and the typical assumptions that yield tractable inverse models. We discuss the relationship of the resulting simplified forward and inverse models to a family of Radon transforms, and how migrating these to the frequency domain relates to recent phasor-based virtual line-of-sight imaging models for NLOS imaging that obey the constraints of conventional lens-based imaging systems. We then evaluate performance of the selected methods on hidden scenes captured under the same hardware setup and similar photon counts. Our experiments show that existing methods share similar limitations on spatial resolution, visibility, and sensitivity to noise when operating under equal hardware constraints, with particular differences that stem from method-specific parameters. We expect our methodology to become a reference in future research on ToF NLOS imaging to obtain objective comparisons of existing and new methods.

