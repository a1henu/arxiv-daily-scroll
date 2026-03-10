---
layout: default
title: WaDi: Weight Direction-aware Distillation for One-step Image Synthesis
---

# WaDi: Weight Direction-aware Distillation for One-step Image Synthesis
**arXiv**：[2603.08258v1](https://arxiv.org/abs/2603.08258) · [PDF](https://arxiv.org/pdf/2603.08258.pdf)  
**作者**：Lei Wang, Yang Cheng, Senmao Li, Ge Wu, Yaxing Wang, Jian Yang  

**一句话要点**：提出WaDi框架，通过权重方向感知蒸馏实现一步图像合成，提升扩散模型推理速度。

**关键词**：一步图像合成, 权重方向蒸馏, 扩散模型加速, 参数高效适配器, 可控生成

## 3 点简述
- 核心问题：扩散模型如Stable Diffusion推理慢，限制实际部署，需加速一步生成。
- 方法要点：分析权重方向变化是关键，设计LoRaD适配器建模方向变化，集成到VSD中形成WaDi框架。
- 实验或效果：在COCO数据集上达到最优FID分数，参数效率高，泛化至可控生成等下游任务。

## 摘要（原文）

> Despite the impressive performance of diffusion models such as Stable Diffusion (SD) in image generation, their slow inference limits practical deployment. Recent works accelerate inference by distilling multi-step diffusion into one-step generators. To better understand the distillation mechanism, we analyze U-Net/DiT weight changes between one-step students and their multi-step teacher counterparts. Our analysis reveals that changes in weight direction significantly exceed those in weight norm, highlighting it as the key factor during distillation. Motivated by this insight, we propose the Low-rank Rotation of weight Direction (LoRaD), a parameter-efficient adapter tailored to one-step diffusion distillation. LoRaD is designed to model these structured directional changes using learnable low-rank rotation matrices. We further integrate LoRaD into Variational Score Distillation (VSD), resulting in Weight Direction-aware Distillation (WaDi)-a novel one-step distillation framework. WaDi achieves state-of-the-art FID scores on COCO 2014 and COCO 2017 while using only approximately 10% of the trainable parameters of the U-Net/DiT. Furthermore, the distilled one-step model demonstrates strong versatility and scalability, generalizing well to various downstream tasks such as controllable generation, relation inversion, and high-resolution synthesis.

