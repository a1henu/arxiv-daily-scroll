---
layout: default
title: StructBiHOI: Structured Articulation Modeling for Long--Horizon Bimanual Hand--Object Interaction Generation
---

# StructBiHOI: Structured Articulation Modeling for Long--Horizon Bimanual Hand--Object Interaction Generation
**arXiv**：[2603.08390v1](https://arxiv.org/abs/2603.08390) · [PDF](https://arxiv.org/pdf/2603.08390.pdf)  
**作者**：Zhi Wang, Liu Liu, Ruonan Liu, Dan Guo, Meng Wang  

**一句话要点**：提出StructBiHOI框架，通过结构化建模解决长时程双手-物体交互生成中的协调与稳定性问题。

**关键词**：双手-物体交互生成, 结构化建模, 长时程规划, 扩散模型, Mamba架构, 关节演化

## 3 点简述
- 核心问题：现有方法在长时程双手交互生成中难以同时保证时间一致性、物理合理性和语义对齐。
- 方法要点：采用分层设计，联合VAE建模长期关节演化，操作VAE细化单帧手部姿态，并基于Mamba的扩散去噪器提升长序列生成效率。
- 实验或效果：在双手操作和单手握持基准测试中，相比基线方法，在长时程稳定性、运动真实性和计算效率方面表现更优。

## 摘要（原文）

> Recent progress in 3D hand--object interaction (HOI) generation has primarily focused on single--hand grasp synthesis, while bimanual manipulation remains significantly more challenging. Long--horizon planning instability, fine--grained joint articulation, and complex cross--hand coordination make coherent bimanual generation difficult, especially under multimodal conditions. Existing approaches often struggle to simultaneously ensure temporal consistency, physical plausibility, and semantic alignment over extended sequences. We propose StructBiHOI, a Structured articulation modeling framework for long-horizon Bimanual HOI generation. Our key insight is to structurally disentangle temporal joint planning from frame--level manipulation refinement. Specifically, a jointVAE models long-term joint evolution conditioned on object geometry and task semantics, while a maniVAE refines fine-grained hand poses at the single--frame level. To enable stable and efficient long--sequence generation, we incorporate a state--space--inspired diffusion denoiser based on Mamba, which models long--range dependencies with linear complexity. This hierarchical design facilitates coherent dual-hand coordination and articulated object interaction. Extensive experiments on bimanual manipulation and single-hand grasping benchmarks demonstrate that our method achieves superior long--horizon stability, motion realism, and computational efficiency compared to strong baselines.

