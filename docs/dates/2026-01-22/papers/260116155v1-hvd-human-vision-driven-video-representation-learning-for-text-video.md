---
layout: default
title: HVD: Human Vision-Driven Video Representation Learning for Text-Video Retrieval
---

# HVD: Human Vision-Driven Video Representation Learning for Text-Video Retrieval
**arXiv**：[2601.16155v1](https://arxiv.org/abs/2601.16155) · [PDF](https://arxiv.org/pdf/2601.16155.pdf)  
**作者**：Zequn Xie, Xin Liu, Boyun Zhang, Yuxiao Lin, Sihang Cai, Tao Jin  

**一句话要点**：提出HVD模型以解决文本-视频检索中特征交互盲目性问题，通过模仿人类视觉认知实现精准匹配。

**关键词**：文本-视频检索, 人类视觉驱动, 粗到细对齐, 关键帧选择, 补丁特征压缩, 注意力机制

## 3 点简述
- 核心问题：现有方法因文本查询稀疏性导致特征交互盲目，难以区分关键视觉信息与背景噪声。
- 方法要点：引入粗到细对齐机制，包括关键帧选择模块和补丁特征压缩模块，模拟人类宏观与微观感知。
- 实验或效果：在五个基准测试中实现最先进性能，验证了模型能捕捉类人视觉焦点。

## 摘要（原文）

> The success of CLIP has driven substantial progress in text-video retrieval. However, current methods often suffer from "blind" feature interaction, where the model struggles to discern key visual information from background noise due to the sparsity of textual queries. To bridge this gap, we draw inspiration from human cognitive behavior and propose the Human Vision-Driven (HVD) model. Our framework establishes a coarse-to-fine alignment mechanism comprising two key components: the Frame Features Selection Module (FFSM) and the Patch Features Compression Module (PFCM). FFSM mimics the human macro-perception ability by selecting key frames to eliminate temporal redundancy. Subsequently, PFCM simulates micro-perception by aggregating patch features into salient visual entities through an advanced attention mechanism, enabling precise entity-level matching. Extensive experiments on five benchmarks demonstrate that HVD not only captures human-like visual focus but also achieves state-of-the-art performance.

