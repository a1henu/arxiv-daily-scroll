---
layout: default
title: Video4Spatial: Towards Visuospatial Intelligence with Context-Guided Video Generation
---

# Video4Spatial: Towards Visuospatial Intelligence with Context-Guided Video Generation
**arXiv**：[2512.03040v1](https://arxiv.org/abs/2512.03040) · [PDF](https://arxiv.org/pdf/2512.03040.pdf)  
**作者**：Zeqi Xiao, Yiwei Zhao, Lingxiao Li, Yushi Lan, Yu Ning, Rahul Garg, Roshni Cooper, Mohammad H. Taghavi, Xingang Pan  

**一句话要点**：提出Video4Spatial框架，利用视频扩散模型实现仅基于视觉数据的复杂空间任务处理。

**关键词**：视频生成模型, 视觉空间智能, 场景导航, 对象定位, 视频扩散模型, 上下文引导

## 3 点简述
- 核心问题：探索视频生成模型是否仅凭视觉数据展现类似人类的视觉空间智能。
- 方法要点：通过视频场景上下文引导的视频扩散模型，执行场景导航和对象定位任务。
- 实验或效果：在导航和定位任务中展示强空间理解能力，并泛化至长上下文和域外环境。

## 摘要（原文）

> We investigate whether video generative models can exhibit visuospatial intelligence, a capability central to human cognition, using only visual data. To this end, we present Video4Spatial, a framework showing that video diffusion models conditioned solely on video-based scene context can perform complex spatial tasks. We validate on two tasks: scene navigation - following camera-pose instructions while remaining consistent with 3D geometry of the scene, and object grounding - which requires semantic localization, instruction following, and planning. Both tasks use video-only inputs, without auxiliary modalities such as depth or poses. With simple yet effective design choices in the framework and data curation, Video4Spatial demonstrates strong spatial understanding from video context: it plans navigation and grounds target objects end-to-end, follows camera-pose instructions while maintaining spatial consistency, and generalizes to long contexts and out-of-domain environments. Taken together, these results advance video generative models toward general visuospatial reasoning.

