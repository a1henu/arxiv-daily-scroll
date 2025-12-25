---
layout: default
title: PUFM++: Point Cloud Upsampling via Enhanced Flow Matching
---

# PUFM++: Point Cloud Upsampling via Enhanced Flow Matching
**arXiv**：[2512.20988v1](https://arxiv.org/abs/2512.20988) · [PDF](https://arxiv.org/pdf/2512.20988.pdf)  
**作者**：Zhi-Song Liu, Chenhang He, Roland Maier, Andreas Rupp  

**一句话要点**：提出PUFM++，通过增强流匹配从稀疏噪声点云重建密集准确点云。

**关键词**：点云上采样, 流匹配, 几何重建, 鲁棒性增强, 表面一致性

## 3 点简述
- 核心问题：从稀疏、噪声、部分点云重建密集准确点云，提升几何保真度、鲁棒性和下游任务一致性。
- 方法要点：采用两阶段流匹配策略，结合自适应时间调度器和流形约束，并引入循环接口网络增强特征交互。
- 实验或效果：在合成基准和真实扫描上实现最先进性能，提供优越的视觉保真度和定量准确性。

## 摘要（原文）

> Recent advances in generative modeling have demonstrated strong promise for high-quality point cloud upsampling. In this work, we present PUFM++, an enhanced flow-matching framework for reconstructing dense and accurate point clouds from sparse, noisy, and partial observations. PUFM++ improves flow matching along three key axes: (i) geometric fidelity, (ii) robustness to imperfect input, and (iii) consistency with downstream surface-based tasks. We introduce a two-stage flow-matching strategy that first learns a direct, straight-path flow from sparse inputs to dense targets, and then refines it using noise-perturbed samples to approximate the terminal marginal distribution better. To accelerate and stabilize inference, we propose a data-driven adaptive time scheduler that improves sampling efficiency based on interpolation behavior. We further impose on-manifold constraints during sampling to ensure that generated points remain aligned with the underlying surface. Finally, we incorporate a recurrent interface network~(RIN) to strengthen hierarchical feature interactions and boost reconstruction quality. Extensive experiments on synthetic benchmarks and real-world scans show that PUFM++ sets a new state of the art in point cloud upsampling, delivering superior visual fidelity and quantitative accuracy across a wide range of tasks. Code and pretrained models are publicly available at https://github.com/Holmes-Alan/Enhanced_PUFM.

