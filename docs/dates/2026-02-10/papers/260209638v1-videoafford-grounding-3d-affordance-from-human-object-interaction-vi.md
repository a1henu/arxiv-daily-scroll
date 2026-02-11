---
layout: default
title: VideoAfford: Grounding 3D Affordance from Human-Object-Interaction Videos via Multimodal Large Language Model
---

# VideoAfford: Grounding 3D Affordance from Human-Object-Interaction Videos via Multimodal Large Language Model
**arXiv**：[2602.09638v1](https://arxiv.org/abs/2602.09638) · [PDF](https://arxiv.org/pdf/2602.09638.pdf)  
**作者**：Hanqing Wang, Mingyu Liu, Xiaoyu Chen, Chengwei MA, Yiming Zhong, Wenti Yin, Yuhao Liu, Zhiqing Cui, Jiahao Yuan, Lu Dai, Zhiyuan Ma, Hui Xiong  

**一句话要点**：提出VideoAfford以通过多模态大语言模型从人-物交互视频中学习3D可操作性，解决动态交互上下文不足问题。

**关键词**：3D可操作性学习, 多模态大语言模型, 人-物交互视频, 潜在动作编码, 空间感知损失, 开放世界泛化

## 3 点简述
- 核心问题：现有方法依赖静态语言和图像线索，缺乏动态交互上下文，难以揭示3D可操作性的时空和因果线索。
- 方法要点：基于VIDA数据集，利用多模态大语言模型增强可操作性分割能力，结合潜在动作编码器提取视频动态先验，并引入空间感知损失函数。
- 实验或效果：模型在实验中显著优于现有方法，展现出强开放世界泛化能力和可操作性推理能力。

## 摘要（原文）

> 3D affordance grounding aims to highlight the actionable regions on 3D objects, which is crucial for robotic manipulation. Previous research primarily focused on learning affordance knowledge from static cues such as language and images, which struggle to provide sufficient dynamic interaction context that can reveal temporal and causal cues. To alleviate this predicament, we collect a comprehensive video-based 3D affordance dataset, \textit{VIDA}, which contains 38K human-object-interaction videos covering 16 affordance types, 38 object categories, and 22K point clouds. Based on \textit{VIDA}, we propose a strong baseline: VideoAfford, which activates multimodal large language models with additional affordance segmentation capabilities, enabling both world knowledge reasoning and fine-grained affordance grounding within a unified framework. To enhance action understanding capability, we leverage a latent action encoder to extract dynamic interaction priors from HOI videos. Moreover, we introduce a \textit{spatial-aware} loss function to enable VideoAfford to obtain comprehensive 3D spatial knowledge. Extensive experimental evaluations demonstrate that our model significantly outperforms well-established methods and exhibits strong open-world generalization with affordance reasoning abilities. All datasets and code will be publicly released to advance research in this area.

