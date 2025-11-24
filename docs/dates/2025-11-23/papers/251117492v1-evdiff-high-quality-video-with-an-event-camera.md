---
layout: default
title: EvDiff: High Quality Video with an Event Camera
---

# EvDiff: High Quality Video with an Event Camera
**arXiv**：[2511.17492v1](https://arxiv.org/abs/2511.17492) · [PDF](https://arxiv.org/pdf/2511.17492.pdf)  
**作者**：Weilun Li, Lei Sun, Ruixi Gao, Qi Jiang, Yuqin Ma, Kaiwei Wang, Ming-Hsuan Yang, Luc Van Gool, Danda Pani Paudel  

**一句话要点**：提出EvDiff扩散模型以从事件相机生成高质量彩色视频

**关键词**：事件相机, 扩散模型, 视频生成, 代理训练, 时间一致性

## 3 点简述
- 事件相机重建强度图像存在绝对亮度模糊的严重不适定问题
- 采用代理训练框架和单步扩散模型，结合时间一致编码器降低计算成本
- 在真实数据集上，像素级和感知指标优于现有方法，平衡保真度与真实感

## 摘要（原文）

> As neuromorphic sensors, event cameras asynchronously record changes in brightness as streams of sparse events with the advantages of high temporal resolution and high dynamic range. Reconstructing intensity images from events is a highly ill-posed task due to the inherent ambiguity of absolute brightness. Early methods generally follow an end-to-end regression paradigm, directly mapping events to intensity frames in a deterministic manner. While effective to some extent, these approaches often yield perceptually inferior results and struggle to scale up in model capacity and training data. In this work, we propose EvDiff, an event-based diffusion model that follows a surrogate training framework to produce high-quality videos. To reduce the heavy computational cost of high-frame-rate video generation, we design an event-based diffusion model that performs only a single forward diffusion step, equipped with a temporally consistent EvEncoder. Furthermore, our novel Surrogate Training Framework eliminates the dependence on paired event-image datasets, allowing the model to leverage large-scale image datasets for higher capacity. The proposed EvDiff is capable of generating high-quality colorful videos solely from monochromatic event streams. Experiments on real-world datasets demonstrate that our method strikes a sweet spot between fidelity and realism, outperforming existing approaches on both pixel-level and perceptual metrics.

