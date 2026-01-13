---
layout: default
title: HiVid-Narrator: Hierarchical Video Narrative Generation with Scene-Primed ASR-anchored Compression
---

# HiVid-Narrator: Hierarchical Video Narrative Generation with Scene-Primed ASR-anchored Compression
**arXiv**：[2601.07366v1](https://arxiv.org/abs/2601.07366) · [PDF](https://arxiv.org/pdf/2601.07366.pdf)  
**作者**：Haoxuan Li, Mengyan Li, Junjun Zheng  

**一句话要点**：提出HiVid-Narrator框架，通过分层压缩和阶段化构建解决电商视频结构化叙事生成问题。

**关键词**：视频叙事生成, 多模态压缩, 电商视频理解, 分层表示, 时间对齐

## 3 点简述
- 核心问题：现有方法难以统一感知细粒度视觉细节并组织成连贯高层故事，电商视频节奏快、信息密集。
- 方法要点：引入E-HVC数据集，采用阶段化构建和SPA-Compressor压缩多模态令牌，生成基于事实的时间对齐叙事。
- 实验或效果：相比现有方法，在减少输入令牌的同时实现更优叙事质量，具体指标未知。

## 摘要（原文）

> Generating structured narrations for real-world e-commerce videos requires models to perceive fine-grained visual details and organize them into coherent, high-level stories--capabilities that existing approaches struggle to unify. We introduce the E-commerce Hierarchical Video Captioning (E-HVC) dataset with dual-granularity, temporally grounded annotations: a Temporal Chain-of-Thought that anchors event-level observations and Chapter Summary that compose them into concise, story-centric summaries. Rather than directly prompting chapters, we adopt a staged construction that first gathers reliable linguistic and visual evidence via curated ASR and frame-level descriptions, then refines coarse annotations into precise chapter boundaries and titles conditioned on the Temporal Chain-of-Thought, yielding fact-grounded, time-aligned narratives. We also observe that e-commerce videos are fast-paced and information-dense, with visual tokens dominating the input sequence. To enable efficient training while reducing input tokens, we propose the Scene-Primed ASR-anchored Compressor (SPA-Compressor), which compresses multimodal tokens into hierarchical scene and event representations guided by ASR semantic cues. Built upon these designs, our HiVid-Narrator framework achieves superior narrative quality with fewer input tokens compared to existing methods.

