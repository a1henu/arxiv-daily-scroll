---
layout: default
title: CameraMaster: Unified Camera Semantic-Parameter Control for Photography Retouching
---

# CameraMaster: Unified Camera Semantic-Parameter Control for Photography Retouching
**arXiv**：[2511.21024v1](https://arxiv.org/abs/2511.21024) · [PDF](https://arxiv.org/pdf/2511.21024.pdf)  
**作者**：Qirui Yang, Yang Yang, Ying Zeng, Xiaobin Hu, Bo Li, Huanjing Yue, Jingyu Yang, Peng-Tao Jiang  

**一句话要点**：提出CameraMaster统一框架，实现摄影后期处理中的精确相机语义参数控制。

**关键词**：图像编辑, 扩散模型, 相机参数控制, 语义参数对齐, 摄影后期处理

## 3 点简述
- 核心问题：现有方法依赖模糊文本提示或独立参数调整，难以实现物理一致的多参数控制。
- 方法要点：通过解耦相机指令与参数嵌入，并注入内容特征，实现语义与参数的紧密对齐。
- 实验或效果：在78K数据集上验证，支持多参数组合，响应单调线性，性能优于现有方法。

## 摘要（原文）

> Text-guided diffusion models have greatly advanced image editing and generation. However, achieving physically consistent image retouching with precise parameter control (e.g., exposure, white balance, zoom) remains challenging. Existing methods either rely solely on ambiguous and entangled text prompts, which hinders precise camera control, or train separate heads/weights for parameter adjustment, which compromises scalability, multi-parameter composition, and sensitivity to subtle variations. To address these limitations, we propose CameraMaster, a unified camera-aware framework for image retouching. The key idea is to explicitly decouple the camera directive and then coherently integrate two critical information streams: a directive representation that captures the photographer's intent, and a parameter embedding that encodes precise camera settings. CameraMaster first uses the camera parameter embedding to modulate both the camera directive and the content semantics. The modulated directive is then injected into the content features via cross-attention, yielding a strongly camera-sensitive semantic context. In addition, the directive and camera embeddings are injected as conditioning and gating signals into the time embedding, enabling unified, layer-wise modulation throughout the denoising process and enforcing tight semantic-parameter alignment. To train and evaluate CameraMaster, we construct a large-scale dataset of 78K image-prompt pairs annotated with camera parameters. Extensive experiments show that CameraMaster produces monotonic and near-linear responses to parameter variations, supports seamless multi-parameter composition, and significantly outperforms existing methods.

