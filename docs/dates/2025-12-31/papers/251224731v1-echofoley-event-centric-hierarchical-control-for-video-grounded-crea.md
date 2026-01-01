---
layout: default
title: EchoFoley: Event-Centric Hierarchical Control for Video Grounded Creative Sound Generation
---

# EchoFoley: Event-Centric Hierarchical Control for Video Grounded Creative Sound Generation
**arXiv**：[2512.24731v1](https://arxiv.org/abs/2512.24731) · [PDF](https://arxiv.org/pdf/2512.24731.pdf)  
**作者**：Bingxuan Li, Yiming Cui, Yicheng He, Yiwei Wang, Shu Zhang, Longyin Wen, Yulei Niu  

**一句话要点**：提出EchoFoley任务与EchoVidia框架，以解决视频配乐生成中的视觉主导、细粒度控制不足和指令理解弱问题。

**关键词**：视频配乐生成, 事件级控制, 分层语义控制, 慢快思考策略, 基准数据集

## 3 点简述
- 核心问题：现有视频-文本到音频方法存在视觉主导、细粒度控制定义缺失和指令理解弱等限制。
- 方法要点：引入事件级符号表示和分层控制，构建EchoFoley-6k基准，并提出基于慢快思考策略的EchoVidia生成框架。
- 实验或效果：EchoVidia在可控性上超越现有模型40.7%，感知质量提升12.5%。

## 摘要（原文）

> Sound effects build an essential layer of multimodal storytelling, shaping the emotional atmosphere and the narrative semantics of videos. Despite recent advancement in video-text-to-audio (VT2A), the current formulation faces three key limitations: First, an imbalance between visual and textual conditioning that leads to visual dominance; Second, the absence of a concrete definition for fine-grained controllable generation; Third, weak instruction understanding and following, as existing datasets rely on brief categorical tags. To address these limitations, we introduce EchoFoley, a new task designed for video-grounded sound generation with both event level local control and hierarchical semantic control. Our symbolic representation for sounding events specifies when, what, and how each sound is produced within a video or instruction, enabling fine-grained controls like sound generation, insertion, and editing. To support this task, we construct EchoFoley-6k, a large-scale, expert-curated benchmark containing over 6,000 video-instruction-annotation triplets. Building upon this foundation, we propose EchoVidia a sounding-event-centric agentic generation framework with slow-fast thinking strategy. Experiments show that EchoVidia surpasses recent VT2A models by 40.7% in controllability and 12.5% in perceptual quality.

