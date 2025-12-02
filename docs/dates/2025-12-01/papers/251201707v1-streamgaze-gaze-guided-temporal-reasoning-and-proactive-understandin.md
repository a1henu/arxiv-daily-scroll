---
layout: default
title: StreamGaze: Gaze-Guided Temporal Reasoning and Proactive Understanding in Streaming Videos
---

# StreamGaze: Gaze-Guided Temporal Reasoning and Proactive Understanding in Streaming Videos
**arXiv**：[2512.01707v1](https://arxiv.org/abs/2512.01707) · [PDF](https://arxiv.org/pdf/2512.01707.pdf)  
**作者**：Daeun Lee, Subhojyoti Mukherjee, Branislav Kveton, Ryan A. Rossi, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Franck Dernoncourt, Mohit Bansal  

**一句话要点**：提出StreamGaze基准以评估多模态大模型在流视频中利用人类注视进行时序和前瞻推理的能力

**关键词**：流视频理解, 注视引导推理, 时序推理, 前瞻预测, 多模态大模型, 基准评估

## 3 点简述
- 核心问题：现有流视频基准缺乏评估多模态大模型如何解释或利用人类注视信号进行时序和前瞻推理
- 方法要点：通过注视提取、区域特定视觉提示和扫描路径构建，开发注视-视频问答生成管道，创建时空基础的问答对
- 实验或效果：在多任务评估中，发现先进多模态大模型与人类性能存在显著差距，揭示了注视使用时序推理和意图建模的局限性

## 摘要（原文）

> Streaming video understanding requires models not only to process temporally incoming frames, but also to anticipate user intention for realistic applications like AR glasses. While prior streaming benchmarks evaluate temporal reasoning, none measure whether MLLMs can interpret or leverage human gaze signals within a streaming setting. To fill this gap, we introduce StreamGaze, the first benchmark designed to evaluate how effectively MLLMs use gaze for temporal and proactive reasoning in streaming videos. StreamGaze introduces gaze-guided past, present, and proactive tasks that comprehensively evaluate streaming video understanding. These tasks assess whether models can use real-time gaze to follow shifting attention and infer user intentions from only past and currently observed frames. To build StreamGaze, we develop a gaze-video QA generation pipeline that aligns egocentric videos with raw gaze trajectories via fixation extraction, region-specific visual prompting, and scanpath construction. This pipeline produces spatio-temporally grounded QA pairs that closely reflect human perceptual dynamics. Across all StreamGaze tasks, we observe substantial performance gaps between state-of-the-art MLLMs and human performance, revealing fundamental limitations in gaze-based temporal reasoning, intention modeling, and proactive prediction. We further provide detailed analyses of gaze-prompting strategies, reasoning behaviors, and task-specific failure modes, offering deeper insight into why current MLLMs struggle and what capabilities future models must develop. All data and code will be publicly released to support continued research in gaze-guided streaming video understanding.

