---
layout: default
title: OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving
---

# OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving
**arXiv**：[2512.14044v1](https://arxiv.org/abs/2512.14044) · [PDF](https://arxiv.org/pdf/2512.14044.pdf)  
**作者**：Zhenguo Zhang, Haohan Zhen, Yishen Wang, Le Xu, Tianchen Deng, Xuefeng Chen, Qu Chen, Bo Zhang, Wuxiong Huang  

**一句话要点**：提出OmniDrive-R1，通过强化驱动的交错多模态思维链解决自动驾驶中视觉语言模型的可靠性问题。

**关键词**：自动驾驶, 视觉语言模型, 强化学习, 多模态思维链, 视觉定位, 端到端框架

## 3 点简述
- 核心问题：视觉语言模型在自动驾驶中因依赖无基础的文本思维链导致对象幻觉，可靠性不足。
- 方法要点：采用交错多模态思维链统一感知与推理，结合强化学习实现无标注的视觉定位，提升细粒度分析能力。
- 实验或效果：在DriveLMM-o1数据集上，推理分数从51.77%提升至80.35%，答案准确率从37.81%提升至73.62%。

## 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

