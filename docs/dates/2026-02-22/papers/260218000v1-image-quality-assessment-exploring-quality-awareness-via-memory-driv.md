---
layout: default
title: Image Quality Assessment: Exploring Quality Awareness via Memory-driven Distortion Patterns Matching
---

# Image Quality Assessment: Exploring Quality Awareness via Memory-driven Distortion Patterns Matching
**arXiv**：[2602.18000v1](https://arxiv.org/abs/2602.18000) · [PDF](https://arxiv.org/pdf/2602.18000.pdf)  
**作者**：Xuting Lan, Mingliang Zhou, Xuekai Wei, Jielu Yan, Yueting Huang, Huayan Pu, Jun Luo, Weijia Jia  

**一句话要点**：提出记忆驱动质量感知框架以解决图像质量评估中参考图像依赖问题

**关键词**：图像质量评估, 记忆驱动框架, 失真模式匹配, 双模式评估, 无参考评估

## 3 点简述
- 现有全参考图像质量评估方法依赖高质量参考图像，限制了实际应用场景。
- 受人类视觉记忆机制启发，建立记忆库存储失真模式，支持双模式质量评估策略。
- 实验表明，该方法在多个数据集上优于现有方法，适应无参考和全参考任务。

## 摘要（原文）

> Existing full-reference image quality assessment (FR-IQA) methods achieve high-precision evaluation by analysing feature differences between reference and distorted images. However, their performance is constrained by the quality of the reference image, which limits real-world applications where ideal reference sources are unavailable. Notably, the human visual system has the ability to accumulate visual memory, allowing image quality assessment on the basis of long-term memory storage. Inspired by this biological memory mechanism, we propose a memory-driven quality-aware framework (MQAF), which establishes a memory bank for storing distortion patterns and dynamically switches between dual-mode quality assessment strategies to reduce reliance on high-quality reference images. When reference images are available, MQAF obtains reference-guided quality scores by adaptively weighting reference information and comparing the distorted image with stored distortion patterns in the memory bank. When the reference image is absent, the framework relies on distortion patterns in the memory bank to infer image quality, enabling no-reference quality assessment (NR-IQA). The experimental results show that our method outperforms state-of-the-art approaches across multiple datasets while adapting to both no-reference and full-reference tasks.

