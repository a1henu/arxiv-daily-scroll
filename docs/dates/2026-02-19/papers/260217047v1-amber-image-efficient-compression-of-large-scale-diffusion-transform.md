---
layout: default
title: Amber-Image: Efficient Compression of Large-Scale Diffusion Transformers
---

# Amber-Image: Efficient Compression of Large-Scale Diffusion Transformers
**arXiv**：[2602.17047v1](https://arxiv.org/abs/2602.17047) · [PDF](https://arxiv.org/pdf/2602.17047.pdf)  
**作者**：Chaojie Yang, Tian Li, Yue Zhang, Jun Gao  

**一句话要点**：提出Amber-Image压缩框架，高效压缩大规模扩散Transformer以降低计算成本。

**关键词**：扩散Transformer压缩, 深度剪枝, 混合流架构, 层间蒸馏, 文本到图像生成, 高效训练

## 3 点简述
- 扩散Transformer计算成本高，部署困难，需高效压缩方案。
- 采用时间步敏感深度剪枝和混合流架构，无需从头训练，减少参数70%。
- 在DPG-Bench等基准测试中实现高保真合成和优越文本渲染，匹配更大模型。

## 摘要（原文）

> Diffusion Transformer (DiT) architectures have significantly advanced Text-to-Image (T2I) generation but suffer from prohibitive computational costs and deployment barriers. To address these challenges, we propose an efficient compression framework that transforms the 60-layer dual-stream MMDiT-based Qwen-Image into lightweight models without training from scratch. Leveraging this framework, we introduce Amber-Image, a series of streamlined T2I models. We first derive Amber-Image-10B using a timestep-sensitive depth pruning strategy, where retained layers are reinitialized via local weight averaging and optimized through layer-wise distillation and full-parameter fine-tuning. Building on this, we develop Amber-Image-6B by introducing a hybrid-stream architecture that converts deep-layer dual streams into a single stream initialized from the image branch, further refined via progressive distillation and lightweight fine-tuning. Our approach reduces parameters by 70% and eliminates the need for large-scale data engineering. Notably, the entire compression and training pipeline-from the 10B to the 6B variant-requires fewer than 2,000 GPU hours, demonstrating exceptional cost-efficiency compared to training from scratch. Extensive evaluations on benchmarks like DPG-Bench and LongText-Bench show that Amber-Image achieves high-fidelity synthesis and superior text rendering, matching much larger models.

