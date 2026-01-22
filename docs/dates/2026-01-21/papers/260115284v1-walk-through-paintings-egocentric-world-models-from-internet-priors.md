---
layout: default
title: Walk through Paintings: Egocentric World Models from Internet Priors
---

# Walk through Paintings: Egocentric World Models from Internet Priors
**arXiv**：[2601.15284v1](https://arxiv.org/abs/2601.15284) · [PDF](https://arxiv.org/pdf/2601.15284.pdf)  
**作者**：Anurag Bagchi, Zhipeng Bao, Homanga Bharadhwaj, Yu-Xiong Wang, Pavel Tokmakov, Martial Hebert  

**一句话要点**：提出EgoWM方法，将预训练视频扩散模型转化为动作条件世界模型，实现可控未来预测。

**关键词**：世界模型, 视频扩散模型, 动作条件预测, 结构一致性, 泛化能力, 轻量微调

## 3 点简述
- 核心问题：如何使视频生成模型准确预测动作驱动的未来，而非仅生成合理未来。
- 方法要点：通过轻量级条件层注入运动命令，利用互联网规模视频模型的先验知识，无需从头训练。
- 实验或效果：在导航和操作任务中产生连贯预测，提升结构一致性分数达80%，泛化至未见环境如画作内部。

## 摘要（原文）

> What if a video generation model could not only imagine a plausible future, but the correct one, accurately reflecting how the world changes with each action? We address this question by presenting the Egocentric World Model (EgoWM), a simple, architecture-agnostic method that transforms any pretrained video diffusion model into an action-conditioned world model, enabling controllable future prediction. Rather than training from scratch, we repurpose the rich world priors of Internet-scale video models and inject motor commands through lightweight conditioning layers. This allows the model to follow actions faithfully while preserving realism and strong generalization. Our approach scales naturally across embodiments and action spaces, ranging from 3-DoF mobile robots to 25-DoF humanoids, where predicting egocentric joint-angle-driven dynamics is substantially more challenging. The model produces coherent rollouts for both navigation and manipulation tasks, requiring only modest fine-tuning. To evaluate physical correctness independently of visual appearance, we introduce the Structural Consistency Score (SCS), which measures whether stable scene elements evolve consistently with the provided actions. EgoWM improves SCS by up to 80 percent over prior state-of-the-art navigation world models, while achieving up to six times lower inference latency and robust generalization to unseen environments, including navigation inside paintings.

