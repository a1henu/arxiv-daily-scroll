---
layout: default
title: VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization
---

# VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization
**arXiv**：[2512.16906v1](https://arxiv.org/abs/2512.16906) · [PDF](https://arxiv.org/pdf/2512.16906.pdf)  
**作者**：Xiaoyan Cong, Haotian Yang, Angtian Wang, Yizhi Wang, Yiding Yang, Canyu Zhang, Chongyang Ma  

**一句话要点**：提出VIVA框架，通过VLM引导编码和奖励优化解决指令视频编辑的泛化问题。

**关键词**：指令视频编辑, 视觉语言模型, 奖励优化, 扩散变换器, 数据生成

## 3 点简述
- 核心问题：现有方法基于简单编辑数据训练，难以泛化到复杂真实世界指令。
- 方法要点：使用VLM编码指令和视觉上下文，结合Edit-GRPO奖励优化提升编辑质量。
- 实验或效果：在指令遵循、泛化能力和编辑质量上优于先进方法。

## 摘要（原文）

> Instruction-based video editing aims to modify an input video according to a natural-language instruction while preserving content fidelity and temporal coherence. However, existing diffusion-based approaches are often trained on paired data of simple editing operations, which fundamentally limits their ability to generalize to diverse and complex, real-world instructions. To address this generalization gap, we propose VIVA, a scalable framework for instruction-based video editing that leverages VLM-guided encoding and reward optimization. First, we introduce a VLM-based instructor that encodes the textual instruction, the first frame of the source video, and an optional reference image into visually-grounded instruction representations, providing fine-grained spatial and semantic context for the diffusion transformer backbone. Second, we propose a post-training stage, Edit-GRPO, which adapts Group Relative Policy Optimization to the domain of video editing, directly optimizing the model for instruction-faithful, content-preserving, and aesthetically pleasing edits using relative rewards. Furthermore, we propose a data construction pipeline designed to synthetically generate diverse, high-fidelity paired video-instruction data of basic editing operations. Extensive experiments show that VIVA achieves superior instruction following, generalization, and editing quality over state-of-the-art methods. Website: https://viva-paper.github.io

