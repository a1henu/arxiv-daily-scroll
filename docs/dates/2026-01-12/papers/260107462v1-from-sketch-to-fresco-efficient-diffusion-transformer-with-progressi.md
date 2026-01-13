---
layout: default
title: From Sketch to Fresco: Efficient Diffusion Transformer with Progressive Resolution
---

# From Sketch to Fresco: Efficient Diffusion Transformer with Progressive Resolution
**arXiv**：[2601.07462v1](https://arxiv.org/abs/2601.07462) · [PDF](https://arxiv.org/pdf/2601.07462.pdf)  
**作者**：Shikang Zheng, Guantao Chen, Lixuan He, Jiacheng Liu, Yuqi Lin, Chang Zou, Linfeng Zhang  

**一句话要点**：提出Fresco框架以解决扩散Transformer动态分辨率采样中的噪声注入和全局结构破坏问题

**关键词**：扩散Transformer, 动态分辨率采样, 渐进上采样, 加速技术, 生成模型, 跨阶段一致性

## 3 点简述
- 核心问题：现有动态分辨率方法依赖启发式重噪声，破坏跨阶段一致性并导致模型需重新学习全局结构
- 方法要点：Fresco统一重噪声和全局结构，采用渐进上采样，保持低分辨率草稿效率和高分辨率细化保真度
- 实验或效果：在FLUX和HunyuanVideo上分别实现10倍和5倍加速，结合蒸馏模型可达22倍，保持近无损质量

## 摘要（原文）

> Diffusion Transformers achieve impressive generative quality but remain computationally expensive due to iterative sampling. Recently, dynamic resolution sampling has emerged as a promising acceleration technique by reducing the resolution of early sampling steps. However, existing methods rely on heuristic re-noising at every resolution transition, injecting noise that breaks cross-stage consistency and forces the model to relearn global structure. In addition, these methods indiscriminately upsample the entire latent space at once without checking which regions have actually converged, causing accumulated errors, and visible artifacts. Therefore, we propose \textbf{Fresco}, a dynamic resolution framework that unifies re-noise and global structure across stages with progressive upsampling, preserving both the efficiency of low-resolution drafting and the fidelity of high-resolution refinement, with all stages aligned toward the same final target. Fresco achieves near-lossless acceleration across diverse domains and models, including 10$\times$ speedup on FLUX, and 5$\times$ on HunyuanVideo, while remaining orthogonal to distillation, quantization and feature caching, reaching 22$\times$ speedup when combined with distilled models. Our code is in supplementary material and will be released on Github.

