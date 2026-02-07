---
layout: default
title: NeVStereo: A NeRF-Driven NVS-Stereo Architecture for High-Fidelity 3D Tasks
---

# NeVStereo: A NeRF-Driven NVS-Stereo Architecture for High-Fidelity 3D Tasks
**arXiv**：[2602.05423v1](https://arxiv.org/abs/2602.05423) · [PDF](https://arxiv.org/pdf/2602.05423.pdf)  
**作者**：Pengcheng Chen, Yue Hu, Wenhao Li, Nicole M Gunderson, Andrew Feng, Zhenglong Sun, Peter Beerel, Eric J Seibel  

**一句话要点**：提出NeVStereo架构，结合NeRF与立体视觉，从多视角RGB输入联合优化相机位姿、深度、新视角合成与表面重建。

**关键词**：神经辐射场, 多视角立体视觉, 相机位姿估计, 新视角合成, 表面重建, 零样本学习

## 3 点简述
- 核心问题：现有方法难以从随意拍摄图像中同时获得准确位姿、可靠深度、高质量渲染和精确3D表面。
- 方法要点：结合NeRF新视角合成生成立体友好渲染，置信度引导多视角深度估计，NeRF耦合光束法平差优化位姿，迭代细化提升几何一致性。
- 实验或效果：在室内外等基准测试中，零样本性能强，深度误差降低达36%，位姿精度提升10.4%，新视角合成保真度提高4.5%，网格质量达先进水平。

## 摘要（原文）

> In modern dense 3D reconstruction, feed-forward systems (e.g., VGGT, pi3) focus on end-to-end matching and geometry prediction but do not explicitly output the novel view synthesis (NVS). Neural rendering-based approaches offer high-fidelity NVS and detailed geometry from posed images, yet they typically assume fixed camera poses and can be sensitive to pose errors. As a result, it remains non-trivial to obtain a single framework that can offer accurate poses, reliable depth, high-quality rendering, and accurate 3D surfaces from casually captured views. We present NeVStereo, a NeRF-driven NVS-stereo architecture that aims to jointly deliver camera poses, multi-view depth, novel view synthesis, and surface reconstruction from multi-view RGB-only inputs. NeVStereo combines NeRF-based NVS for stereo-friendly renderings, confidence-guided multi-view depth estimation, NeRF-coupled bundle adjustment for pose refinement, and an iterative refinement stage that updates both depth and the radiance field to improve geometric consistency. This design mitigated the common NeRF-based issues such as surface stacking, artifacts, and pose-depth coupling. Across indoor, outdoor, tabletop, and aerial benchmarks, our experiments indicate that NeVStereo achieves consistently strong zero-shot performance, with up to 36% lower depth error, 10.4% improved pose accuracy, 4.5% higher NVS fidelity, and state-of-the-art mesh quality (F1 91.93%, Chamfer 4.35 mm) compared to existing prestigious methods.

