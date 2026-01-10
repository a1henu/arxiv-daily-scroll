---
layout: default
title: CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models
---

# CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models
**arXiv**：[2601.04778v1](https://arxiv.org/abs/2601.04778) · [PDF](https://arxiv.org/pdf/2601.04778.pdf)  
**作者**：Tobia Poppi, Burak Uzkent, Amanmeet Garg, Lucas Porto, Garin Kessler, Yezhou Yang, Marcella Cornia, Lorenzo Baraldi, Rita Cucchiara, Florian Schiffers  

**一句话要点**：提出CounterVid框架以缓解视频语言模型中的动作与时间幻觉问题

**关键词**：视频语言模型, 反事实生成, 幻觉缓解, 直接偏好优化, 多模态学习, 合成数据集

## 3 点简述
- 视频语言模型易因过度依赖语言先验而产生动作和时间幻觉
- 通过多模态LLM和扩散模型生成反事实视频，构建合成数据集CounterVid
- 引入MixDPO方法微调模型，在时间排序等任务上提升性能

## 摘要（原文）

> Video-language models (VLMs) achieve strong multimodal understanding but remain prone to hallucinations, especially when reasoning about actions and temporal order. Existing mitigation strategies, such as textual filtering or random video perturbations, often fail to address the root cause: over-reliance on language priors rather than fine-grained visual dynamics. We propose a scalable framework for counterfactual video generation that synthesizes videos differing only in actions or temporal structure while preserving scene context. Our pipeline combines multimodal LLMs for action proposal and editing guidance with diffusion-based image and video models to generate semantic hard negatives at scale. Using this framework, we build CounterVid, a synthetic dataset of ~26k preference pairs targeting action recognition and temporal reasoning. We further introduce MixDPO, a unified Direct Preference Optimization approach that jointly leverages textual and visual preferences. Fine-tuning Qwen2.5-VL with MixDPO yields consistent improvements, notably in temporal ordering, and transfers effectively to standard video hallucination benchmarks. Code and models will be made publicly available.

