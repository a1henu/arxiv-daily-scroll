---
layout: default
title: Atomic Action Slicing: Planner-Aligned Options for Generalist VLA Agents
---

# Atomic Action Slicing: Planner-Aligned Options for Generalist VLA Agents
**arXiv**：[2512.11584v1](https://arxiv.org/abs/2512.11584) · [PDF](https://arxiv.org/pdf/2512.11584.pdf)  
**作者**：Stefan Tabakov, Asen Popov, Dimitar Dimitrov, S. Ensiye Kiyamousavi, Vladimir Hristov, Boris Kraychev  

**一句话要点**：提出原子动作切片方法以提升通用视觉语言动作代理的长时任务泛化能力

**关键词**：原子动作切片, 视觉语言动作模型, 长时任务规划, 动作分解, 泛化能力提升

## 3 点简述
- 当前视觉语言动作模型在技能或对象新组合任务中泛化能力差
- 通过分解长时演示为短类型化原子动作，对齐规划器需求
- 在LIBERO数据集上验证，微调CLIP-RT+模型提升任务成功率

## 摘要（原文）

> Current vision-language-action (VLA) models generalize poorly, particularly when tasks require new compositions of skills or objects. We introduce Atomic Action Slicing (AAS), a planner-aligned approach that decomposes long-horizon demonstrations into short, typed atomic actions that are easier for planners to use and policies to learn. Using LIBERO demonstrations, AAS produces a validated dataset of 2,124 atomic segments labeled with action type, temporal span, and confidence. A stronger segmenter (Gemini 2.5 Pro) closely matches planner-defined plans and remains robust under keyframe jitter, while smaller models perform worse on multi-object tasks. Fine-tuning CLIP-RT+ on our atomic dataset improves task success from 94.2% to 95.3% on LIBERO-Goal and 83.8% to 88.8% on LIBERO-Long. We publicly release the GATE-VLAP dataset on HuggingFace(https://huggingface.co/datasets/gate-institute/GATE-VLAP-datasets)

