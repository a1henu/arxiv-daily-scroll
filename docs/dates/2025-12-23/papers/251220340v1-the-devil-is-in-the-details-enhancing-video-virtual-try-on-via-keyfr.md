---
layout: default
title: The devil is in the details: Enhancing Video Virtual Try-On via Keyframe-Driven Details Injection
---

# The devil is in the details: Enhancing Video Virtual Try-On via Keyframe-Driven Details Injection
**arXiv**：[2512.20340v1](https://arxiv.org/abs/2512.20340) · [PDF](https://arxiv.org/pdf/2512.20340.pdf)  
**作者**：Qingdong He, Xueqin Chen, Yanjie Pan, Peng Tang, Pengcheng Xu, Zhenye Gan, Chengjie Wang, Xiaobin Hu, Jiangning Zhang, Yabiao Wang  

**一句话要点**：提出KeyTailor框架以解决视频虚拟试穿中细节动态与背景一致性问题

**关键词**：视频虚拟试穿, 扩散变换器, 关键帧驱动, 细节注入, 高分辨率数据集

## 3 点简述
- 现有方法难以捕捉服装细节动态并保持背景完整性，计算成本高且数据集有限
- 采用关键帧驱动细节注入策略，通过关键帧采样和两个模块增强服装细节与背景优化
- 构建ViT-HD数据集，实验显示在动态和静态场景中优于现有方法

## 摘要（原文）

> Although diffusion transformer (DiT)-based video virtual try-on (VVT) has made significant progress in synthesizing realistic videos, existing methods still struggle to capture fine-grained garment dynamics and preserve background integrity across video frames. They also incur high computational costs due to additional interaction modules introduced into DiTs, while the limited scale and quality of existing public datasets also restrict model generalization and effective training. To address these challenges, we propose a novel framework, KeyTailor, along with a large-scale, high-definition dataset, ViT-HD. The core idea of KeyTailor is a keyframe-driven details injection strategy, motivated by the fact that keyframes inherently contain both foreground dynamics and background consistency. Specifically, KeyTailor adopts an instruction-guided keyframe sampling strategy to filter informative frames from the input video. Subsequently,two tailored keyframe-driven modules, the garment details enhancement module and the collaborative background optimization module, are employed to distill garment dynamics into garment-related latents and to optimize the integrity of background latents, both guided by keyframes.These enriched details are then injected into standard DiT blocks together with pose, mask, and noise latents, enabling efficient and realistic try-on video synthesis. This design ensures consistency without explicitly modifying the DiT architecture, while simultaneously avoiding additional complexity. In addition, our dataset ViT-HD comprises 15, 070 high-quality video samples at a resolution of 810*1080, covering diverse garments. Extensive experiments demonstrate that KeyTailor outperforms state-of-the-art baselines in terms of garment fidelity and background integrity across both dynamic and static scenarios.

