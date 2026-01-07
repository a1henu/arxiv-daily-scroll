---
layout: default
title: Omni2Sound: Towards Unified Video-Text-to-Audio Generation
---

# Omni2Sound: Towards Unified Video-Text-to-Audio Generation
**arXiv**：[2601.02731v1](https://arxiv.org/abs/2601.02731) · [PDF](https://arxiv.org/pdf/2601.02731.pdf)  
**作者**：Yusheng Dai, Zehua Chen, Yuxuan Jiang, Baolong Gao, Qiuhong Ke, Jun Zhu, Jianfei Cai  

**一句话要点**：提出Omni2Sound统一模型解决视频-文本-音频生成中的多模态对齐与任务竞争问题

**关键词**：视频-文本-音频生成, 多模态对齐, 扩散模型, 渐进训练, 音频标注数据集

## 3 点简述
- 核心问题：高质量音频标注稀缺导致多模态条件语义冲突，以及跨任务与任务内竞争
- 方法要点：构建SoundAtlas数据集提升V-A-T对齐，设计三阶段渐进训练缓解模态偏差
- 实验效果：在VGGSound-Omni基准上实现单模型统一SOTA性能，支持灵活输入模态

## 摘要（原文）

> Training a unified model integrating video-to-audio (V2A), text-to-audio (T2A), and joint video-text-to-audio (VT2A) generation offers significant application flexibility, yet faces two unexplored foundational challenges: (1) the scarcity of high-quality audio captions with tight A-V-T alignment, leading to severe semantic conflict between multimodal conditions, and (2) cross-task and intra-task competition, manifesting as an adverse V2A-T2A performance trade-off and modality bias in the VT2A task. First, to address data scarcity, we introduce SoundAtlas, a large-scale dataset (470k pairs) that significantly outperforms existing benchmarks and even human experts in quality. Powered by a novel agentic pipeline, it integrates Vision-to-Language Compression to mitigate visual bias of MLLMs, a Junior-Senior Agent Handoff for a 5 times cost reduction, and rigorous Post-hoc Filtering to ensure fidelity. Consequently, SoundAtlas delivers semantically rich and temporally detailed captions with tight V-A-T alignment. Second, we propose Omni2Sound, a unified VT2A diffusion model supporting flexible input modalities. To resolve the inherent cross-task and intra-task competition, we design a three-stage multi-task progressive training schedule that converts cross-task competition into joint optimization and mitigates modality bias in the VT2A task, maintaining both audio-visual alignment and off-screen audio generation faithfulness. Finally, we construct VGGSound-Omni, a comprehensive benchmark for unified evaluation, including challenging off-screen tracks. With a standard DiT backbone, Omni2Sound achieves unified SOTA performance across all three tasks within a single model, demonstrating strong generalization across benchmarks with heterogeneous input conditions. The project page is at https://swapforward.github.io/Omni2Sound.

