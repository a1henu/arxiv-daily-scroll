---
layout: default
title: U-Mind: A Unified Framework for Real-Time Multimodal Interaction with Audiovisual Generation
---

# U-Mind: A Unified Framework for Real-Time Multimodal Interaction with Audiovisual Generation
**arXiv**：[2602.23739v1](https://arxiv.org/abs/2602.23739) · [PDF](https://arxiv.org/pdf/2602.23739.pdf)  
**作者**：Xiang Deng, Feng Gao, Yong Zhang, Youxin Pang, Xu Xiaoming, Zhuoliang Kang, Xiaoming Wei, Yebin Liu  

**一句话要点**：提出U-Mind统一框架，实现实时多模态交互与音视频生成，以解决跨模态对齐和推理能力退化问题。

**关键词**：多模态交互, 实时生成, 跨模态对齐, 推理能力, 音视频合成, 统一框架

## 3 点简述
- 核心问题：现有系统在实时多模态交互中存在跨模态对齐差和推理能力退化，阻碍自然动态通信。
- 方法要点：采用统一对齐与推理框架，通过分段对齐策略增强同步，利用排练驱动学习保持推理能力。
- 实验或效果：在问答、指令跟随和动作生成等任务上达到先进性能，支持实时视频渲染和同步反馈。

## 摘要（原文）

> Full-stack multimodal interaction in real-time is a central goal in building intelligent embodied agents capable of natural, dynamic communication. However, existing systems are either limited to unimodal generation or suffer from degraded reasoning and poor cross-modal alignment, preventing coherent and perceptually grounded interactions. In this work, we introduce U-Mind, the first unified system for high-intelligence multimodal dialogue that supports real-time generation and jointly models language, speech, motion, and video synthesis within a single interactive loop. At its core, U-Mind implements a Unified Alignment and Reasoning Framework that addresses two key challenges: enhancing cross-modal synchronization via a segment-wise alignment strategy, and preserving reasoning abilities through Rehearsal-Driven Learning. During inference, U-Mind adopts a text-first decoding pipeline that performs internal chain-of-thought planning followed by temporally synchronized generation across modalities. To close the loop, we implement a real-time video rendering framework conditioned on pose and speech, enabling expressive and synchronized visual feedback. Extensive experiments demonstrate that U-Mind achieves state-of-the-art performance on a range of multimodal interaction tasks, including question answering, instruction following, and motion generation, paving the way toward intelligent, immersive conversational agents.

