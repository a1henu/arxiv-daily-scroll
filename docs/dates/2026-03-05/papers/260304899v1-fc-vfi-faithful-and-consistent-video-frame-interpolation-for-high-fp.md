---
layout: default
title: FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation
---

# FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation
**arXiv**：[2603.04899v1](https://arxiv.org/abs/2603.04899) · [PDF](https://arxiv.org/pdf/2603.04899.pdf)  
**作者**：Ganggui Ding, Hao Chen, Xiaogang Xu  

**一句话要点**：提出FC-VFI以解决视频帧插值中保真度与运动一致性问题，支持高分辨率慢动作生成。

**关键词**：视频帧插值, 慢动作生成, 时序一致性, 语义匹配, 高分辨率视频, 扩散模型

## 3 点简述
- 核心问题：现有方法依赖生成先验或易错光流，导致插值帧保真度低和运动不一致。
- 方法要点：引入潜在序列时序建模继承首尾帧保真线索，利用语义匹配线进行结构感知运动引导。
- 实验或效果：在多种场景下实现高保真和结构完整性，支持4倍和8倍插值提升帧率至120/240 FPS。

## 摘要（原文）

> Large pre-trained video diffusion models excel in video frame interpolation but struggle to generate high fidelity frames due to reliance on intrinsic generative priors, limiting detail preservation from start and end frames. Existing methods often depend on motion control for temporal consistency, yet dense optical flow is error-prone, and sparse points lack structural context. In this paper, we propose FC-VFI for faithful and consistent video frame interpolation, supporting \(4\times\)x and \(8\times\) interpolation, boosting frame rates from 30 FPS to 120 and 240 FPS at \(2560\times 1440\)resolution while preserving visual fidelity and motion consistency. We introduce a temporal modeling strategy on the latent sequences to inherit fidelity cues from start and end frames and leverage semantic matching lines for structure-aware motion guidance, improving motion consistency. Furthermore, we propose a temporal difference loss to mitigate temporal inconsistencies. Extensive experiments show FC-VFI achieves high performance and structural integrity across diverse scenarios.

