---
layout: default
title: DirectSwap: Mask-Free Cross-Identity Training and Benchmarking for Expression-Consistent Video Head Swapping
---

# DirectSwap: Mask-Free Cross-Identity Training and Benchmarking for Expression-Consistent Video Head Swapping
**arXiv**：[2512.09417v1](https://arxiv.org/abs/2512.09417) · [PDF](https://arxiv.org/pdf/2512.09417.pdf)  
**作者**：Yanan Wang, Shengcai Liao, Panwen Hu, Xin Li, Fan Yang, Xiaodan Liang  

**一句话要点**：提出DirectSwap框架和HeadSwapBench数据集，以解决视频头部交换中身份泄漏和运动表情一致性问题。

**关键词**：视频头部交换, 跨身份训练, 配对数据集, 扩散模型, 运动表情一致性, 无掩码修复

## 3 点简述
- 核心问题：现有方法依赖同人跨帧训练和掩码修复，导致身份泄漏、边界伪影及遮挡信息恢复困难。
- 方法要点：构建跨身份配对数据集HeadSwapBench，并设计无掩码直接交换框架DirectSwap，结合运动模块和MEAR损失增强一致性。
- 实验或效果：在多样真实视频场景中实现最先进的视觉质量、身份保真度及运动表情一致性。

## 摘要（原文）

> Video head swapping aims to replace the entire head of a video subject, including facial identity, head shape, and hairstyle, with that of a reference image, while preserving the target body, background, and motion dynamics. Due to the lack of ground-truth paired swapping data, prior methods typically train on cross-frame pairs of the same person within a video and rely on mask-based inpainting to mitigate identity leakage. Beyond potential boundary artifacts, this paradigm struggles to recover essential cues occluded by the mask, such as facial pose, expressions, and motion dynamics. To address these issues, we prompt a video editing model to synthesize new heads for existing videos as fake swapping inputs, while maintaining frame-synchronized facial poses and expressions. This yields HeadSwapBench, the first cross-identity paired dataset for video head swapping, which supports both training (\TrainNum{} videos) and benchmarking (\TestNum{} videos) with genuine outputs. Leveraging this paired supervision, we propose DirectSwap, a mask-free, direct video head-swapping framework that extends an image U-Net into a video diffusion model with a motion module and conditioning inputs. Furthermore, we introduce the Motion- and Expression-Aware Reconstruction (MEAR) loss, which reweights the diffusion loss per pixel using frame-difference magnitudes and facial-landmark proximity, thereby enhancing cross-frame coherence in motion and expressions. Extensive experiments demonstrate that DirectSwap achieves state-of-the-art visual quality, identity fidelity, and motion and expression consistency across diverse in-the-wild video scenes. We will release the source code and the HeadSwapBench dataset to facilitate future research.

