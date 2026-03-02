---
layout: default
title: SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching
---

# SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching
**arXiv**：[2602.24208v1](https://arxiv.org/abs/2602.24208) · [PDF](https://arxiv.org/pdf/2602.24208.pdf)  
**作者**：Yasaman Haghighi, Alexandre Alahi  

**一句话要点**：提出SenCache，通过敏感性感知缓存加速扩散模型推理

**关键词**：扩散模型, 推理加速, 缓存策略, 敏感性分析, 视频生成

## 3 点简述
- 扩散模型推理因多步去噪计算昂贵，现有缓存方法依赖启发式准则且需调优
- 基于模型输出对去噪输入扰动的敏感性分析，提出动态缓存策略SenCache
- 在多个视频生成模型上实验，SenCache在相同计算预算下视觉质量优于现有方法

## 摘要（原文）

> Diffusion models achieve state-of-the-art video generation quality, but their inference remains expensive due to the large number of sequential denoising steps. This has motivated a growing line of research on accelerating diffusion inference. Among training-free acceleration methods, caching reduces computation by reusing previously computed model outputs across timesteps. Existing caching methods rely on heuristic criteria to choose cache/reuse timesteps and require extensive tuning. We address this limitation with a principled sensitivity-aware caching framework. Specifically, we formalize the caching error through an analysis of the model output sensitivity to perturbations in the denoising inputs, i.e., the noisy latent and the timestep, and show that this sensitivity is a key predictor of caching error. Based on this analysis, we propose Sensitivity-Aware Caching (SenCache), a dynamic caching policy that adaptively selects caching timesteps on a per-sample basis. Our framework provides a theoretical basis for adaptive caching, explains why prior empirical heuristics can be partially effective, and extends them to a dynamic, sample-specific approach. Experiments on Wan 2.1, CogVideoX, and LTX-Video show that SenCache achieves better visual quality than existing caching methods under similar computational budgets.

