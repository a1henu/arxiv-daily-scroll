---
layout: default
title: TiViBench: Benchmarking Think-in-Video Reasoning for Video Generative Models
---

# TiViBench: Benchmarking Think-in-Video Reasoning for Video Generative Models
**arXiv**：[2511.13704v1](https://arxiv.org/abs/2511.13704) · [PDF](https://arxiv.org/pdf/2511.13704.pdf)  
**作者**：Harold Haodong Chen, Disen Lan, Wen-Jie Shu, Qingyang Liu, Zihan Wang, Sirui Chen, Wenkai Cheng, Kanghao Chen, Hongfei Zhang, Zixin Zhang, Rongjin Guo, Yu Cheng, Ying-Cong Chen  

**一句话要点**：提出TiViBench基准和VideoTPO策略以评估和提升视频生成模型的推理能力

**关键词**：视频生成模型, 推理能力评估, 基准测试, 测试时优化, 逻辑一致性, 动作规划

## 3 点简述
- 现有基准无法评估视频生成模型的高阶推理能力，如物理合理性和逻辑一致性
- TiViBench从四个维度系统评估推理能力，VideoTPO通过LLM自分析增强推理性能
- 实验显示商业模型推理潜力更强，VideoTPO无需额外训练即可显著提升性能

## 摘要（原文）

> The rapid evolution of video generative models has shifted their focus from producing visually plausible outputs to tackling tasks requiring physical plausibility and logical consistency. However, despite recent breakthroughs such as Veo 3's chain-of-frames reasoning, it remains unclear whether these models can exhibit reasoning capabilities similar to large language models (LLMs). Existing benchmarks predominantly evaluate visual fidelity and temporal coherence, failing to capture higher-order reasoning abilities. To bridge this gap, we propose TiViBench, a hierarchical benchmark specifically designed to evaluate the reasoning capabilities of image-to-video (I2V) generation models. TiViBench systematically assesses reasoning across four dimensions: i) Structural Reasoning & Search, ii) Spatial & Visual Pattern Reasoning, iii) Symbolic & Logical Reasoning, and iv) Action Planning & Task Execution, spanning 24 diverse task scenarios across 3 difficulty levels. Through extensive evaluations, we show that commercial models (e.g., Sora 2, Veo 3.1) demonstrate stronger reasoning potential, while open-source models reveal untapped potential that remains hindered by limited training scale and data diversity. To further unlock this potential, we introduce VideoTPO, a simple yet effective test-time strategy inspired by preference optimization. By performing LLM self-analysis on generated candidates to identify strengths and weaknesses, VideoTPO significantly enhances reasoning performance without requiring additional training, data, or reward models. Together, TiViBench and VideoTPO pave the way for evaluating and advancing reasoning in video generation models, setting a foundation for future research in this emerging field.

