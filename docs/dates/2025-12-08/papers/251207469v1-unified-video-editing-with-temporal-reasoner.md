---
layout: default
title: Unified Video Editing with Temporal Reasoner
---

# Unified Video Editing with Temporal Reasoner
**arXiv**：[2512.07469v1](https://arxiv.org/abs/2512.07469) · [PDF](https://arxiv.org/pdf/2512.07469.pdf)  
**作者**：Xiangpeng Yang, Ji Xie, Yiyuan Yang, Yan Huang, Min Xu, Qiang Wu  

**一句话要点**：提出VideoCoF方法，通过链式帧推理解决视频编辑中精度与统一性的冲突。

**关键词**：视频编辑, 链式帧推理, 扩散模型, 无掩码编辑, 运动对齐, 时长外推

## 3 点简述
- 现有视频编辑方法在专家模型精度与统一模型通用性间存在权衡，缺乏精确指令到区域映射。
- VideoCoF引入链式帧推理，强制模型先预测编辑区域潜在表示，再生成目标视频，实现无掩码精确编辑。
- 仅用5万视频对训练，在VideoCoF-Bench上达到先进性能，并支持运动对齐和时长外推。

## 摘要（原文）

> Existing video editing methods face a critical trade-off: expert models offer precision but rely on task-specific priors like masks, hindering unification; conversely, unified temporal in-context learning models are mask-free but lack explicit spatial cues, leading to weak instruction-to-region mapping and imprecise localization. To resolve this conflict, we propose VideoCoF, a novel Chain-of-Frames approach inspired by Chain-of-Thought reasoning. VideoCoF enforces a ``see, reason, then edit" procedure by compelling the video diffusion model to first predict reasoning tokens (edit-region latents) before generating the target video tokens. This explicit reasoning step removes the need for user-provided masks while achieving precise instruction-to-region alignment and fine-grained video editing. Furthermore, we introduce a RoPE alignment strategy that leverages these reasoning tokens to ensure motion alignment and enable length extrapolation beyond the training duration. We demonstrate that with a minimal data cost of only 50k video pairs, VideoCoF achieves state-of-the-art performance on VideoCoF-Bench, validating the efficiency and effectiveness of our approach. Our code, weight, data are available at https://github.com/knightyxp/VideoCoF.

