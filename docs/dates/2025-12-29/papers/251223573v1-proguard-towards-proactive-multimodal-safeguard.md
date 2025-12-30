---
layout: default
title: ProGuard: Towards Proactive Multimodal Safeguard
---

# ProGuard: Towards Proactive Multimodal Safeguard
**arXiv**：[2512.23573v1](https://arxiv.org/abs/2512.23573) · [PDF](https://arxiv.org/pdf/2512.23573.pdf)  
**作者**：Shaohan Yu, Lijun Li, Chenyang Si, Lu Sheng, Jing Shao  

**一句话要点**：提出ProGuard以解决多模态安全风险，通过主动防护识别和描述分布外风险

**关键词**：多模态安全防护, 分布外风险检测, 强化学习训练, 视觉语言模型, 主动安全防护

## 3 点简述
- 核心问题：生成模型快速发展导致多模态安全风险频发，现有防御方法存在局限性
- 方法要点：构建模态平衡数据集，通过强化学习训练视觉语言基础模型，引入分布外安全类别推断任务
- 实验或效果：在二元安全分类上媲美闭源大模型，在风险分类上超越开源模型，主动防护能力显著提升

## 摘要（原文）

> The rapid evolution of generative models has led to a continuous emergence of multimodal safety risks, exposing the limitations of existing defense methods. To address these challenges, we propose ProGuard, a vision-language proactive guard that identifies and describes out-of-distribution (OOD) safety risks without the need for model adjustments required by traditional reactive approaches. We first construct a modality-balanced dataset of 87K samples, each annotated with both binary safety labels and risk categories under a hierarchical multimodal safety taxonomy, effectively mitigating modality bias and ensuring consistent moderation across text, image, and text-image inputs. Based on this dataset, we train our vision-language base model purely through reinforcement learning (RL) to achieve efficient and concise reasoning. To approximate proactive safety scenarios in a controlled setting, we further introduce an OOD safety category inference task and augment the RL objective with a synonym-bank-based similarity reward that encourages the model to generate concise descriptions for unseen unsafe categories. Experimental results show that ProGuard achieves performance comparable to closed-source large models on binary safety classification, substantially outperforms existing open-source guard models on unsafe content categorization. Most notably, ProGuard delivers a strong proactive moderation ability, improving OOD risk detection by 52.6% and OOD risk description by 64.8%.

