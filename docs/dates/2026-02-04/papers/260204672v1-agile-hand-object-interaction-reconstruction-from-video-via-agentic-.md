---
layout: default
title: AGILE: Hand-Object Interaction Reconstruction from Video via Agentic Generation
---

# AGILE: Hand-Object Interaction Reconstruction from Video via Agentic Generation
**arXiv**：[2602.04672v1](https://arxiv.org/abs/2602.04672) · [PDF](https://arxiv.org/pdf/2602.04672.pdf)  
**作者**：Jin-Chuan Shi, Binhong Ye, Tao Liu, Junzhe He, Yangjinhui Xu, Xiaoyang Liu, Zeju Li, Hao Chen, Chunhua Shen  

**一句话要点**：提出AGILE框架，通过代理生成从单目视频重建手-物交互，提升鲁棒性与几何完整性。

**关键词**：手-物交互重建, 代理生成, 单目视频, 物理合理性, 仿真就绪资产, 鲁棒跟踪

## 3 点简述
- 核心问题：现有方法依赖神经渲染导致几何破碎，且基于SfM初始化在野外视频中易失败。
- 方法要点：使用VLM引导生成完整物体网格，并采用锚定跟踪策略绕过SfM，结合接触感知优化确保物理合理性。
- 实验或效果：在HO3D等数据集上优于基线，在挑战性序列中展现高鲁棒性，生成仿真就绪资产。

## 摘要（原文）

> Reconstructing dynamic hand-object interactions from monocular videos is critical for dexterous manipulation data collection and creating realistic digital twins for robotics and VR. However, current methods face two prohibitive barriers: (1) reliance on neural rendering often yields fragmented, non-simulation-ready geometries under heavy occlusion, and (2) dependence on brittle Structure-from-Motion (SfM) initialization leads to frequent failures on in-the-wild footage. To overcome these limitations, we introduce AGILE, a robust framework that shifts the paradigm from reconstruction to agentic generation for interaction learning. First, we employ an agentic pipeline where a Vision-Language Model (VLM) guides a generative model to synthesize a complete, watertight object mesh with high-fidelity texture, independent of video occlusions. Second, bypassing fragile SfM entirely, we propose a robust anchor-and-track strategy. We initialize the object pose at a single interaction onset frame using a foundation model and propagate it temporally by leveraging the strong visual similarity between our generated asset and video observations. Finally, a contact-aware optimization integrates semantic, geometric, and interaction stability constraints to enforce physical plausibility. Extensive experiments on HO3D, DexYCB, and in-the-wild videos reveal that AGILE outperforms baselines in global geometric accuracy while demonstrating exceptional robustness on challenging sequences where prior art frequently collapses. By prioritizing physical validity, our method produces simulation-ready assets validated via real-to-sim retargeting for robotic applications.

