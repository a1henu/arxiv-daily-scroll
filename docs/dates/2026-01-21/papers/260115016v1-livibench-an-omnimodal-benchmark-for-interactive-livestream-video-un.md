---
layout: default
title: LiViBench: An Omnimodal Benchmark for Interactive Livestream Video Understanding
---

# LiViBench: An Omnimodal Benchmark for Interactive Livestream Video Understanding
**arXiv**：[2601.15016v1](https://arxiv.org/abs/2601.15016) · [PDF](https://arxiv.org/pdf/2601.15016.pdf)  
**作者**：Xiaodong Wang, Langling Huang, Zhirong Wu, Xu Zhao, Teng Xu, Xuhong Xia, Peixi Peng  

**一句话要点**：提出LiViBench基准以评估交互式直播视频理解，并开发LiVi-LLM-7B模型提升性能。

**关键词**：交互式直播视频理解, 多模态基准, 半自动标注, 指令调优, 实时评论检索

## 3 点简述
- 现有视频基准主要针对非交互视频，缺乏对直播视频的评估。
- 设计半自动标注流程和多模态任务，构建包含音频、语音和实时评论的基准。
- 实验显示模型在LiViBench上优于大型开源模型，并在通用基准上表现增强。

## 摘要（原文）

> The development of multimodal large language models (MLLMs) has advanced general video understanding. However, existing video evaluation benchmarks primarily focus on non-interactive videos, such as movies and recordings. To fill this gap, this paper proposes the first omnimodal benchmark for interactive livestream videos, LiViBench. It features a diverse set of 24 tasks, highlighting the perceptual, reasoning, and livestream-specific challenges. To efficiently construct the dataset, we design a standardized semi-automatic annotation workflow that incorporates the human-in-the-loop at multiple stages. The workflow leverages multiple MLLMs to form a multi-agent system for comprehensive video description and uses a seed-question-driven method to construct high-quality annotations. All interactive videos in the benchmark include audio, speech, and real-time comments modalities. To enhance models' understanding of interactive videos, we design tailored two-stage instruction-tuning and propose a Video-to-Comment Retrieval (VCR) module to improve the model's ability to utilize real-time comments. Based on these advancements, we develop LiVi-LLM-7B, an MLLM with enhanced knowledge of interactive livestreams. Experiments show that our model outperforms larger open-source models with up to 72B parameters, narrows the gap with leading proprietary models on LiViBench, and achieves enhanced performance on general video benchmarks, including VideoMME, LongVideoBench, MLVU, and VideoEval-Pro.

