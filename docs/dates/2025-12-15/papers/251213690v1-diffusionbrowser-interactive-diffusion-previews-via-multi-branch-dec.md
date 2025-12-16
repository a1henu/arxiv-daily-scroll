---
layout: default
title: DiffusionBrowser: Interactive Diffusion Previews via Multi-Branch Decoders
---

# DiffusionBrowser: Interactive Diffusion Previews via Multi-Branch Decoders
**arXiv**：[2512.13690v1](https://arxiv.org/abs/2512.13690) · [PDF](https://arxiv.org/pdf/2512.13690.pdf)  
**作者**：Susung Hong, Chongjian Ge, Zhifei Zhang, Jui-Hsien Wang  

**一句话要点**：提出DiffusionBrowser，通过多分支解码器实现视频扩散模型交互式预览

**关键词**：视频扩散模型, 交互式预览, 多分支解码器, 去噪过程分析, 实时生成, 模态控制

## 3 点简述
- 视频扩散模型生成慢且不透明，用户需长时间等待
- 提出轻量级解码器框架，支持在去噪过程任意点生成RGB和场景内在预览
- 实验显示预览速度超实时4倍，并可通过随机性重注入和模态引导交互控制

## 摘要（原文）

> Video diffusion models have revolutionized generative video synthesis, but they are imprecise, slow, and can be opaque during generation -- keeping users in the dark for a prolonged period. In this work, we propose DiffusionBrowser, a model-agnostic, lightweight decoder framework that allows users to interactively generate previews at any point (timestep or transformer block) during the denoising process. Our model can generate multi-modal preview representations that include RGB and scene intrinsics at more than 4$\times$ real-time speed (less than 1 second for a 4-second video) that convey consistent appearance and motion to the final video. With the trained decoder, we show that it is possible to interactively guide the generation at intermediate noise steps via stochasticity reinjection and modal steering, unlocking a new control capability. Moreover, we systematically probe the model using the learned decoders, revealing how scene, object, and other details are composed and assembled during the otherwise black-box denoising process.

