---
layout: default
title: Plenoptic Video Generation
---

# Plenoptic Video Generation
**arXiv**：[2601.05239v1](https://arxiv.org/abs/2601.05239) · [PDF](https://arxiv.org/pdf/2601.05239.pdf)  
**作者**：Xiao Fu, Shitao Tang, Min Shi, Xian Liu, Jinwei Gu, Ming-Yu Liu, Dahua Lin, Chen-Hsuan Lin  

**一句话要点**：提出PlenopticDreamer框架以解决多视角视频重渲染中的时空一致性问题

**关键词**：多视角视频重渲染, 时空一致性, 自回归生成模型, 相机引导检索, 长视频生成, 机器人操作视角转换

## 3 点简述
- 核心问题：现有单视角视频重渲染方法在多视角场景下难以保持时空一致性，生成区域易出现不一致。
- 方法要点：采用自回归训练多输入单输出视频条件模型，结合相机引导视频检索策略，通过渐进上下文缩放、自条件化和长视频条件机制提升性能。
- 实验或效果：在Basic和Agibot基准测试中实现最先进的视频重渲染，展现优越的视角同步、高保真视觉、准确相机控制和多样视角转换。

## 摘要（原文）

> Camera-controlled generative video re-rendering methods, such as ReCamMaster, have achieved remarkable progress. However, despite their success in single-view setting, these works often struggle to maintain consistency across multi-view scenarios. Ensuring spatio-temporal coherence in hallucinated regions remains challenging due to the inherent stochasticity of generative models. To address it, we introduce PlenopticDreamer, a framework that synchronizes generative hallucinations to maintain spatio-temporal memory. The core idea is to train a multi-in-single-out video-conditioned model in an autoregressive manner, aided by a camera-guided video retrieval strategy that adaptively selects salient videos from previous generations as conditional inputs. In addition, Our training incorporates progressive context-scaling to improve convergence, self-conditioning to enhance robustness against long-range visual degradation caused by error accumulation, and a long-video conditioning mechanism to support extended video generation. Extensive experiments on the Basic and Agibot benchmarks demonstrate that PlenopticDreamer achieves state-of-the-art video re-rendering, delivering superior view synchronization, high-fidelity visuals, accurate camera control, and diverse view transformations (e.g., third-person to third-person, and head-view to gripper-view in robotic manipulation). Project page: https://research.nvidia.com/labs/dir/plenopticdreamer/

