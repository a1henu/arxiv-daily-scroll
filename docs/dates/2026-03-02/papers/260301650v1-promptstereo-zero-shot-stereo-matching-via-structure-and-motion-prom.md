---
layout: default
title: PromptStereo: Zero-Shot Stereo Matching via Structure and Motion Prompts
---

# PromptStereo: Zero-Shot Stereo Matching via Structure and Motion Prompts
**arXiv**：[2603.01650v1](https://arxiv.org/abs/2603.01650) · [PDF](https://arxiv.org/pdf/2603.01650.pdf)  
**作者**：Xianqi Wang, Hao Yang, Hangtian Wang, Junda Cheng, Gangwei Xu, Min Lin, Xin Yang  

**一句话要点**：提出PromptStereo，通过结构和运动提示实现零样本立体匹配

**关键词**：零样本立体匹配, 迭代细化, 提示学习, 单目深度先验, 结构运动提示

## 3 点简述
- 现有方法在零样本泛化中迭代细化阶段利用不足，GRU架构难以有效利用单目深度先验
- 提出提示循环单元，将单目结构和立体运动线索作为提示集成到单目深度基础模型解码器中
- 实验显示PromptStereo在多个数据集上实现最先进的零样本泛化性能，推理速度相当或更快

## 摘要（原文）

> Modern stereo matching methods have leveraged monocular depth foundation models to achieve superior zero-shot generalization performance. However, most existing methods primarily focus on extracting robust features for cost volume construction or disparity initialization. At the same time, the iterative refinement stage, which is also crucial for zero-shot generalization, remains underexplored. Some methods treat monocular depth priors as guidance for iteration, but conventional GRU-based architectures struggle to exploit them due to the limited representation capacity. In this paper, we propose Prompt Recurrent Unit (PRU), a novel iterative refinement module based on the decoder of monocular depth foundation models. By integrating monocular structure and stereo motion cues as prompts into the decoder, PRU enriches the latent representations of monocular depth foundation models with absolute stereo-scale information while preserving their inherent monocular depth priors. Experiments demonstrate that our PromptStereo achieves state-of-the-art zero-shot generalization performance across multiple datasets, while maintaining comparable or faster inference speed. Our findings highlight prompt-guided iterative refinement as a promising direction for zero-shot stereo matching.

