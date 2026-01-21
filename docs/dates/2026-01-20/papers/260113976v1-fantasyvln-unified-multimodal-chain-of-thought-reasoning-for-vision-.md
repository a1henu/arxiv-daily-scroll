---
layout: default
title: FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation
---

# FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation
**arXiv**：[2601.13976v1](https://arxiv.org/abs/2601.13976) · [PDF](https://arxiv.org/pdf/2601.13976.pdf)  
**作者**：Jing Zuo, Lingzhou Mu, Fan Jiang, Chengcheng Ma, Mu Xu, Yonggang Qi  

**一句话要点**：提出FantasyVLN统一隐式推理框架，以解决视觉语言导航中显式思维链推理的时空开销问题。

**关键词**：视觉语言导航, 思维链推理, 多模态学习, 隐式表示, 实时导航, 统一框架

## 3 点简述
- 核心问题：现有思维链推理方法在视觉语言导航中面临空间基础缺失或推理开销过大的挑战。
- 方法要点：通过预训练视觉自回归器将想象视觉编码为紧凑隐空间，实现多模态思维链的统一学习。
- 实验或效果：在LH-VLN数据集上提升导航成功率与效率，推理延迟比显式方法降低一个数量级。

## 摘要（原文）

> Achieving human-level performance in Vision-and-Language Navigation (VLN) requires an embodied agent to jointly understand multimodal instructions and visual-spatial context while reasoning over long action sequences. Recent works, such as NavCoT and NavGPT-2, demonstrate the potential of Chain-of-Thought (CoT) reasoning for improving interpretability and long-horizon planning. Moreover, multimodal extensions like OctoNav-R1 and CoT-VLA further validate CoT as a promising pathway toward human-like navigation reasoning. However, existing approaches face critical drawbacks: purely textual CoTs lack spatial grounding and easily overfit to sparse annotated reasoning steps, while multimodal CoTs incur severe token inflation by generating imagined visual observations, making real-time navigation impractical. In this work, we propose FantasyVLN, a unified implicit reasoning framework that preserves the benefits of CoT reasoning without explicit token overhead. Specifically, imagined visual tokens are encoded into a compact latent space using a pretrained Visual AutoRegressor (VAR) during CoT reasoning training, and the model jointly learns from textual, visual, and multimodal CoT modes under a unified multi-CoT strategy. At inference, our model performs direct instruction-to-action mapping while still enjoying reasoning-aware representations. Extensive experiments on LH-VLN show that our approach achieves reasoning-aware yet real-time navigation, improving success rates and efficiency while reducing inference latency by an order of magnitude compared to explicit CoT methods.

