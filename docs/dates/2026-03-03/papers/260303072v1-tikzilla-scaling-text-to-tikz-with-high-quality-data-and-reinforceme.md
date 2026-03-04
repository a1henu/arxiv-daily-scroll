---
layout: default
title: TikZilla: Scaling Text-to-TikZ with High-Quality Data and Reinforcement Learning
---

# TikZilla: Scaling Text-to-TikZ with High-Quality Data and Reinforcement Learning
**arXiv**：[2603.03072v1](https://arxiv.org/abs/2603.03072) · [PDF](https://arxiv.org/pdf/2603.03072.pdf)  
**作者**：Christian Greisinger, Steffen Eger  

**一句话要点**：提出TikZilla模型，通过高质量数据和强化学习提升文本到TikZ的生成质量。

**关键词**：文本到TikZ生成, 强化学习, 高质量数据集, 逆图形训练, 开源模型

## 3 点简述
- 核心问题：现有文本到TikZ数据集小且噪声大，导致文本与渲染图不匹配；监督微调方法易产生循环、无关内容等错误。
- 方法要点：构建更大更高质量的DaTikZ-V4数据集，采用监督微调加强化学习的两阶段训练，利用逆图形训练的编码器提供奖励信号。
- 实验或效果：人类评估显示TikZilla在5分制上比基础模型提升1.5-2分，超越GPT-4o，与GPT-5在图像评估中相当，模型规模更小。

## 摘要（原文）

> Large language models (LLMs) are increasingly used to assist scientists across diverse workflows. A key challenge is generating high-quality figures from textual descriptions, often represented as TikZ programs that can be rendered as scientific images. Prior research has proposed a variety of datasets and modeling approaches for this task. However, existing datasets for Text-to-TikZ are too small and noisy to capture the complexity of TikZ, causing mismatches between text and rendered figures. Moreover, prior approaches rely solely on supervised fine-tuning (SFT), which does not expose the model to the rendered semantics of the figure, often resulting in errors such as looping, irrelevant content, and incorrect spatial relations. To address these issues, we construct DaTikZ-V4, a dataset more than four times larger and substantially higher in quality than DaTikZ-V3, enriched with LLM-generated figure descriptions. Using this dataset, we train TikZilla, a family of small open-source Qwen models (3B and 8B) with a two-stage pipeline of SFT followed by reinforcement learning (RL). For RL, we leverage an image encoder trained via inverse graphics to provide semantically faithful reward signals. Extensive human evaluations with over 1,000 judgments show that TikZilla improves by 1.5-2 points over its base models on a 5-point scale, surpasses GPT-4o by 0.5 points, and matches GPT-5 in the image-based evaluation, while operating at much smaller model sizes. Code, data, and models will be made available.

