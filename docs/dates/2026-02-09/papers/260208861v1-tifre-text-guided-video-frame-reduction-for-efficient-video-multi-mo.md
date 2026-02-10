---
layout: default
title: TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models
---

# TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models
**arXiv**：[2602.08861v1](https://arxiv.org/abs/2602.08861) · [PDF](https://arxiv.org/pdf/2602.08861.pdf)  
**作者**：Xiangtian Zheng, Zishuo Wang, Yuxin Peng  

**一句话要点**：提出TiFRe框架，通过文本引导的视频帧减少，以降低视频多模态大语言模型的计算成本。

**关键词**：视频多模态大语言模型, 帧减少, 文本引导采样, 计算效率, 视频理解

## 3 点简述
- 视频多模态大语言模型因处理大量视频帧导致高计算开销，固定帧率采样易丢失信息。
- TiFRe采用文本引导的帧采样策略，基于用户输入生成提示并选择语义相关帧，结合帧匹配与合并机制保留非关键帧信息。
- 实验表明，TiFRe在减少计算成本的同时，提升了视频-语言任务的性能。

## 摘要（原文）

> With the rapid development of Large Language Models (LLMs), Video Multi-Modal Large Language Models (Video MLLMs) have achieved remarkable performance in video-language tasks such as video understanding and question answering. However, Video MLLMs face high computational costs, particularly in processing numerous video frames as input, which leads to significant attention computation overhead. A straightforward approach to reduce computational costs is to decrease the number of input video frames. However, simply selecting key frames at a fixed frame rate (FPS) often overlooks valuable information in non-key frames, resulting in notable performance degradation. To address this, we propose Text-guided Video Frame Reduction (TiFRe), a framework that reduces input frames while preserving essential video information. TiFRe uses a Text-guided Frame Sampling (TFS) strategy to select key frames based on user input, which is processed by an LLM to generate a CLIP-style prompt. Pre-trained CLIP encoders calculate the semantic similarity between the prompt and each frame, selecting the most relevant frames as key frames. To preserve video semantics, TiFRe employs a Frame Matching and Merging (FMM) mechanism, which integrates non-key frame information into the selected key frames, minimizing information loss. Experiments show that TiFRe effectively reduces computational costs while improving performance on video-language tasks.

