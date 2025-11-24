---
layout: default
title: DiffRefiner: Coarse to Fine Trajectory Planning via Diffusion Refinement with Semantic Interaction for End to End Autonomous Driving
---

# DiffRefiner: Coarse to Fine Trajectory Planning via Diffusion Refinement with Semantic Interaction for End to End Autonomous Driving
**arXiv**：[2511.17150v1](https://arxiv.org/abs/2511.17150) · [PDF](https://arxiv.org/pdf/2511.17150.pdf)  
**作者**：Liuhan Yin, Runkun Ju, Guodong Guo, Erkang Cheng  

**一句话要点**：提出DiffRefiner框架，通过扩散精炼提升端到端自动驾驶轨迹规划性能

**关键词**：自动驾驶轨迹规划, 扩散模型, Transformer解码器, 两阶段预测, 场景对齐

## 3 点简述
- 生成式轨迹预测方法依赖噪声或锚点，存在改进空间
- 采用两阶段方法：Transformer生成粗轨迹，扩散模型迭代精炼
- 在NAVSIM v2和Bench2Drive基准上实现SOTA，验证组件有效性

## 摘要（原文）

> Unlike discriminative approaches in autonomous driving that predict a fixed set of candidate trajectories of the ego vehicle, generative methods, such as diffusion models, learn the underlying distribution of future motion, enabling more flexible trajectory prediction. However, since these methods typically rely on denoising human-crafted trajectory anchors or random noise, there remains significant room for improvement. In this paper, we propose DiffRefiner, a novel two-stage trajectory prediction framework. The first stage uses a transformer-based Proposal Decoder to generate coarse trajectory predictions by regressing from sensor inputs using predefined trajectory anchors. The second stage applies a Diffusion Refiner that iteratively denoises and refines these initial predictions. In this way, we enhance the performance of diffusion-based planning by incorporating a discriminative trajectory proposal module, which provides strong guidance for the generative refinement process. Furthermore, we design a fine-grained denoising decoder to enhance scene compliance, enabling more accurate trajectory prediction through enhanced alignment with the surrounding environment. Experimental results demonstrate that DiffRefiner achieves state-of-the-art performance, attaining 87.4 EPDMS on NAVSIM v2, and 87.1 DS along with 71.4 SR on Bench2Drive, thereby setting new records on both public benchmarks. The effectiveness of each component is validated via ablation studies as well.

