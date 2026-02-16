---
layout: default
title: Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening
---

# Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening
**arXiv**：[2602.12679v1](https://arxiv.org/abs/2602.12679) · [PDF](https://arxiv.org/pdf/2602.12679.pdf)  
**作者**：Wooseok Jeon, Seunghyun Shin, Dongmin Shin, Hae-Gon Jeon  

**一句话要点**：提出运动先验蒸馏以解决生成中间帧中的双向路径不匹配问题

**关键词**：生成中间帧, 图像到视频扩散模型, 推理时采样, 运动先验蒸馏, 时间连贯性

## 3 点简述
- 现有推理时采样方法因前向与后向路径运动先验不一致导致时间不连续和视觉伪影
- 通过将前向路径的运动残差蒸馏到后向路径，抑制双向不匹配并提升时间连贯性
- 在标准基准上定量评估并开展用户研究，验证了方法在实际场景中的有效性

## 摘要（原文）

> Recent progress in image-to-video (I2V) diffusion models has significantly advanced the field of generative inbetweening, which aims to generate semantically plausible frames between two keyframes. In particular, inference-time sampling strategies, which leverage the generative priors of large-scale pre-trained I2V models without additional training, have become increasingly popular. However, existing inference-time sampling, either fusing forward and backward paths in parallel or alternating them sequentially, often suffers from temporal discontinuities and undesirable visual artifacts due to the misalignment between the two generated paths. This is because each path follows the motion prior induced by its own conditioning frame. In this work, we propose Motion Prior Distillation (MPD), a simple yet effective inference-time distillation technique that suppresses bidirectional mismatch by distilling the motion residual of the forward path into the backward path. Our method can deliberately avoid denoising the end-conditioned path which causes the ambiguity of the path, and yield more temporally coherent inbetweening results with the forward motion prior. We not only perform quantitative evaluations on standard benchmarks, but also conduct extensive user studies to demonstrate the effectiveness of our approach in practical scenarios.

