---
layout: default
title: Vision Language Models: A Survey of 26K Papers
---

# Vision Language Models: A Survey of 26K Papers
**arXiv**：[2510.09586v1](https://arxiv.org/abs/2510.09586) · [PDF](https://arxiv.org/pdf/2510.09586.pdf)  
**作者**：Fengming Lin  
**一句话要点**：分析26K篇论文以量化计算机视觉与语言模型研究趋势
**关键词**：视觉语言模型, 多模态研究, 生成方法, 3D视频分析, 参数高效适应, 研究趋势分析

## 3 点简述
- 核心问题：量化CVPR、ICLR和NeurIPS会议中视觉语言模型的研究趋势与宏观变化
- 方法要点：使用手工词典对标题和摘要进行标准化与标签分配，挖掘任务、架构等细粒度线索
- 实验或效果：识别多模态、生成方法和3D视频活动的三大宏观转变，并比较不同会议特点

## 摘要（原文）

> We present a transparent, reproducible measurement of research trends across
> 26,104 accepted papers from CVPR, ICLR, and NeurIPS spanning 2023-2025. Titles
> and abstracts are normalized, phrase-protected, and matched against a
> hand-crafted lexicon to assign up to 35 topical labels and mine fine-grained
> cues about tasks, architectures, training regimes, objectives, datasets, and
> co-mentioned modalities. The analysis quantifies three macro shifts: (1) a
> sharp rise of multimodal vision-language-LLM work, which increasingly reframes
> classic perception as instruction following and multi-step reasoning; (2)
> steady expansion of generative methods, with diffusion research consolidating
> around controllability, distillation, and speed; and (3) resilient 3D and video
> activity, with composition moving from NeRFs to Gaussian splatting and a
> growing emphasis on human- and agent-centric understanding. Within VLMs,
> parameter-efficient adaptation like prompting/adapters/LoRA and lightweight
> vision-language bridges dominate; training practice shifts from building
> encoders from scratch to instruction tuning and finetuning strong backbones;
> contrastive objectives recede relative to cross-entropy/ranking and
> distillation. Cross-venue comparisons show CVPR has a stronger 3D footprint and
> ICLR the highest VLM share, while reliability themes such as efficiency or
> robustness diffuse across areas. We release the lexicon and methodology to
> enable auditing and extension. Limitations include lexicon recall and
> abstract-only scope, but the longitudinal signals are consistent across venues
> and years.

