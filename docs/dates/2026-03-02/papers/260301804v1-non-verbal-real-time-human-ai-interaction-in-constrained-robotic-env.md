---
layout: default
title: Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments
---

# Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments
**arXiv**：[2603.01804v1](https://arxiv.org/abs/2603.01804) · [PDF](https://arxiv.org/pdf/2603.01804.pdf)  
**作者**：Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  

**一句话要点**：提出首个实时2D关键点框架，实现受限环境中人机非语言交互。

**关键词**：非语言交互, 实时生成, 2D关键点, 轻量架构, 时间连贯性, 统计保真度

## 3 点简述
- 研究AI生成与人类生成数据在全身运动非语言交流中的统计保真度差异。
- 采用轻量架构，在NVIDIA Orin Nano上达100 FPS，通过合成序列预训练减少运动误差。
- 评估显示SORA生成剪辑性能下降，VEO降幅较小，表明时间连贯性驱动实际性能。

## 摘要（原文）

> We study the ongoing debate regarding the statistical fidelity of AI-generated data compared to human-generated data in the context of non-verbal communication using full body motion. Concretely, we ask if contemporary generative models move beyond surface mimicry to participate in the silent, but expressive dialogue of body language. We tackle this question by introducing the first framework that generates a natural non-verbal interaction between Human and AI in real-time from 2D body keypoints. Our experiments utilize four lightweight architectures which run at up to 100 FPS on an NVIDIA Orin Nano, effectively closing the perception-action loop needed for natural Human-AI interaction. We trained on 437 human video clips and demonstrated that pretraining on synthetically-generated sequences reduces motion errors significantly, without sacrificing speed. Yet, a measurable reality gap persists. When the best model is evaluated on keypoints extracted from cutting-edge text-to-video systems, such as SORA and VEO, we observe that performance drops on SORA-generated clips. However, it degrades far less on VEO, suggesting that temporal coherence, not image fidelity, drives real-world performance. Our results demonstrate that statistically distinguishable differences persist between Human and AI motion.

