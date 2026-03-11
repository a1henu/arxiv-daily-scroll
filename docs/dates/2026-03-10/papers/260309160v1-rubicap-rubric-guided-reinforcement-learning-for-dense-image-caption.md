---
layout: default
title: RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning
---

# RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning
**arXiv**：[2603.09160v1](https://arxiv.org/abs/2603.09160) · [PDF](https://arxiv.org/pdf/2603.09160.pdf)  
**作者**：Tzu-Heng Huang, Sirajul Salekin, Javier Movellan, Frederic Sala, Manjot Bilkhu  

**一句话要点**：提出RubiCap框架，通过LLM编写的评分标准指导强化学习，以解决密集图像描述中奖励信号获取的瓶颈问题。

**关键词**：密集图像描述, 强化学习, 大语言模型, 评分标准指导, 视觉语言预训练, 多面评估

## 3 点简述
- 核心问题：密集图像描述任务中，强化学习因缺乏确定性检查器而难以获取细粒度奖励信号，限制了输出多样性和泛化能力。
- 方法要点：利用LLM编写样本特定的评分标准，将候选描述共识转化为结构化多面评估，替代粗粒度标量奖励。
- 实验或效果：在CapArena上实现最高胜率，在CaptionQA上展示优越的词效率，紧凑模型能生成优于专有模型的预训练视觉语言模型。

## 摘要（原文）

> Dense image captioning is critical for cross-modal alignment in vision-language pretraining and text-to-image generation, but scaling expert-quality annotations is prohibitively expensive. While synthetic captioning via strong vision-language models (VLMs) is a practical alternative, supervised distillation often yields limited output diversity and weak generalization. Reinforcement learning (RL) could overcome these limitations, but its successes have so far been concentrated in verifiable domains that rely on deterministic checkers -- a luxury not available in open-ended captioning. We address this bottleneck with RubiCap, a novel RL framework that derives fine-grained, sample-specific reward signals from LLM-written rubrics. RubiCap first assembles a diverse committee of candidate captions, then employs an LLM rubric writer to extract consensus strengths and diagnose deficiencies in the current policy. These insights are converted into explicit evaluation criteria, enabling an LLM judge to decompose holistic quality assessment and replace coarse scalar rewards with structured, multi-faceted evaluations. Across extensive benchmarks, RubiCap achieves the highest win rates on CapArena, outperforming supervised distillation, prior RL methods, human-expert annotations, and GPT-4V-augmented outputs. On CaptionQA, it demonstrates superior word efficiency: our 7B model matches Qwen2.5-VL-32B-Instruct, and our 3B model surpasses its 7B counterpart. Remarkably, using the compact RubiCap-3B as a captioner produces stronger pretrained VLMs than those trained on captions from proprietary models.

