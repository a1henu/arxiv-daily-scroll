---
layout: default
title: ST4VLA: Spatially Guided Training for Vision-Language-Action Models
---

# ST4VLA: Spatially Guided Training for Vision-Language-Action Models
**arXiv**：[2602.10109v1](https://arxiv.org/abs/2602.10109) · [PDF](https://arxiv.org/pdf/2602.10109.pdf)  
**作者**：Jinhui Ye, Fangjing Wang, Ning Gao, Junqiu Yu, Yangkun Zhu, Bin Wang, Jinyu Zhang, Weiyang Jin, Yanwei Fu, Feng Zheng, Yilun Chen, Jiangmiao Pang  

**一句话要点**：提出ST4VLA框架，通过空间引导训练解决视觉语言模型在具身任务中动作生成不足的问题。

**关键词**：视觉语言动作模型, 空间引导训练, 具身人工智能, 机器人学习, 多模态对齐

## 3 点简述
- 核心问题：大型视觉语言模型在具身任务中难以将指令转化为低级动作。
- 方法要点：采用双阶段训练，包括空间基础预训练和空间引导动作后训练，以对齐空间先验与动作学习。
- 实验或效果：在Google Robot和WidowX Robot上性能显著提升，并展示了对未见对象和长时扰动的强泛化能力。

## 摘要（原文）

> Large vision-language models (VLMs) excel at multimodal understanding but fall short when extended to embodied tasks, where instructions must be transformed into low-level motor actions. We introduce ST4VLA, a dual-system Vision-Language-Action framework that leverages Spatial Guided Training to align action learning with spatial priors in VLMs. ST4VLA includes two stages: (i) spatial grounding pre-training, which equips the VLM with transferable priors via scalable point, box, and trajectory prediction from both web-scale and robot-specific data, and (ii) spatially guided action post-training, which encourages the model to produce richer spatial priors to guide action generation via spatial prompting. This design preserves spatial grounding during policy learning and promotes consistent optimization across spatial and action objectives. Empirically, ST4VLA achieves substantial improvements over vanilla VLA, with performance increasing from 66.1 -> 84.6 on Google Robot and from 54.7 -> 73.2 on WidowX Robot, establishing new state-of-the-art results on SimplerEnv. It also demonstrates stronger generalization to unseen objects and paraphrased instructions, as well as robustness to long-horizon perturbations in real-world settings. These results highlight scalable spatially guided training as a promising direction for robust, generalizable robot learning. Source code, data and models are released at https://internrobotics.github.io/internvla-m1.github.io/

